import type { AskResponse, Citation } from "./types.js";
import { type RetrievedChunk } from "./retriever.js";

const DEFAULT_MODEL = "claude-sonnet-4-6";

const SYSTEM_PROMPT = `You answer questions about Project Aureum (AuMM) strictly from the provided documentation excerpts. The grounding rules are non-negotiable and match the aumm-skill Claude skill:

- Answer ONLY from the supplied excerpts. Never use outside knowledge or fill gaps from memory.
- Quote canonical language verbatim where precision matters (formulas, parameter values, fee bands, immutable bounds).
- Cite the section identifier for every claim (e.g. §xxix, F-11, x-a) drawn from the excerpt headings/text.
- Apply interpretive rules: AuMM issuance ≠ BTC mining; CCC ≠ CCB; Miliarium pools cannot be gauge-challenged; four governance actions not two; script.md is non-authoritative.
- If the excerpts do not contain the answer, say so explicitly and set answered_from_corpus=false. Do NOT fabricate parameters, formulas, governance mechanics, or pool details.
- Do not present anything as investment advice.

Return ONLY a JSON object, no prose, no markdown fences, with exactly this shape:
{
  "answer": "<concise natural-language answer grounded in the excerpts>",
  "citations": [ { "section_id": "<e.g. §xxix or F-11>", "file": "<source .md filename>", "excerpt": "<short verbatim snippet, <25 words>" } ],
  "answered_from_corpus": <true|false>
}`;

interface AnthropicMessage {
  content: Array<{ type: string; text?: string }>;
}

interface ModelPayload {
  answer?: string;
  citations?: Citation[];
  answered_from_corpus?: boolean;
}

function parseModelJson(text: string): ModelPayload {
  const clean = text.replace(/^```(?:json)?/i, "").replace(/```$/, "").trim();
  return JSON.parse(clean) as ModelPayload;
}

export async function synthesize(
  ask: string,
  goal: string | undefined,
  chunks: RetrievedChunk[],
  canonSha: string,
  apiKey: string,
  model?: string,
): Promise<AskResponse> {
  if (chunks.length === 0) {
    return {
      answer:
        "That isn't covered in the Aureum documentation corpus. See https://aumm.fi for the full specification.",
      citations: [],
      canon_sha: canonSha,
      answered_from_corpus: false,
    };
  }

  const context = chunks
    .map(
      (c) =>
        `### FILE: ${c.file}  SECTION: ${c.section_id || c.heading}\n${c.text}`,
    )
    .join("\n\n---\n\n");

  const userContent =
    `QUESTION: ${ask}\n` +
    (goal ? `GOAL: ${goal}\n` : "") +
    `\nDOCUMENTATION EXCERPTS:\n\n${context}`;

  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": apiKey,
      "anthropic-version": "2023-06-01",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: model ?? process.env.ASK_MODEL ?? DEFAULT_MODEL,
      max_tokens: 1024,
      system: SYSTEM_PROMPT,
      messages: [{ role: "user", content: userContent }],
    }),
  });

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Anthropic API failed (${res.status}): ${body}`);
  }

  const data = (await res.json()) as AnthropicMessage;
  const text =
    data.content.find((b) => b.type === "text")?.text?.trim() ??
    "No answer generated.";

  try {
    const parsed = parseModelJson(text);
    return {
      answer: parsed.answer ?? text,
      citations: Array.isArray(parsed.citations) ? parsed.citations : [],
      canon_sha: canonSha,
      answered_from_corpus: parsed.answered_from_corpus !== false,
    };
  } catch {
    return {
      answer: text,
      citations: [],
      canon_sha: canonSha,
      answered_from_corpus: true,
    };
  }
}
