import { buildSystemPrompt, buildUserPrompt } from "./prompts.js";
import type { AskResponse, Citation } from "./types.js";
import { excerpt, type RetrievedChunk } from "./retriever.js";

const MODEL = "claude-sonnet-4-20250514";

interface AnthropicMessage {
  content: Array<{ type: string; text?: string }>;
}

export async function synthesize(
  ask: string,
  goal: string | undefined,
  chunks: RetrievedChunk[],
  canonSha: string,
  apiKey: string,
): Promise<AskResponse> {
  if (chunks.length === 0) {
    return {
      answer:
        "The retrieved corpus does not contain material relevant to this question. Check https://aumm.fi directly or consult a human for content that may post-date this canon snapshot.",
      citations: [],
      canon_sha: canonSha,
      answered_from_corpus: false,
    };
  }

  const res = await fetch("https://api.anthropic.com/v1/messages", {
    method: "POST",
    headers: {
      "x-api-key": apiKey,
      "anthropic-version": "2023-06-01",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      model: MODEL,
      max_tokens: 2048,
      system: buildSystemPrompt(canonSha),
      messages: [
        {
          role: "user",
          content: buildUserPrompt(
            ask,
            goal,
            chunks.map((c) => ({
              section_id: c.section_id,
              file: c.file,
              text: c.text,
            })),
          ),
        },
      ],
    }),
  });

  if (!res.ok) {
    const body = await res.text();
    throw new Error(`Anthropic API failed (${res.status}): ${body}`);
  }

  const data = (await res.json()) as AnthropicMessage;
  const answer =
    data.content.find((b) => b.type === "text")?.text?.trim() ??
    "No answer generated.";

  const citations: Citation[] = chunks.map((c) => ({
    section_id: c.section_id,
    file: c.file,
    excerpt: excerpt(c.text),
  }));

  const insufficient =
    /not specified|does not contain|cannot be answered|no relevant/i.test(
      answer,
    );

  return {
    answer,
    citations,
    canon_sha: canonSha,
    answered_from_corpus: !insufficient,
  };
}
