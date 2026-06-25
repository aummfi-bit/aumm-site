import { readFileSync } from "node:fs";
import { join } from "node:path";
import type { VercelRequest, VercelResponse } from "@vercel/node";
import { retrieve } from "../ask/lib/retriever.js";
import { synthesize } from "../ask/lib/synthesizer.js";
import type { AskIndex } from "../ask/lib/types.js";

let cachedIndex: AskIndex | null = null;

function loadIndex(): AskIndex {
  if (cachedIndex) {
    return cachedIndex;
  }
  const path = join(process.cwd(), "ask", "index.json");
  cachedIndex = JSON.parse(readFileSync(path, "utf-8")) as AskIndex;
  return cachedIndex;
}

function routedFile(req: VercelRequest): string | undefined {
  const fromQuery = req.query.file;
  if (typeof fromQuery === "string" && fromQuery.endsWith(".md")) {
    return fromQuery;
  }
  const original = req.headers["x-vercel-original-path"];
  if (typeof original === "string" && original.endsWith(".md")) {
    return original.replace(/^\//, "");
  }
  return undefined;
}

export default async function handler(req: VercelRequest, res: VercelResponse) {
  if (req.method !== "GET") {
    res.setHeader("Allow", "GET");
    return res.status(405).json({ error: "Method not allowed" });
  }

  const ask = typeof req.query.ask === "string" ? req.query.ask.trim() : "";
  const goal =
    typeof req.query.goal === "string" ? req.query.goal.trim() : undefined;

  if (!ask) {
    return res.status(400).json({
      error: "Missing required query parameter: ask",
      example:
        "GET /04_tokenomics.md?ask=What+is+the+AuMM+max+supply",
    });
  }

  const anthropicKey = process.env.ANTHROPIC_API_KEY;
  if (!anthropicKey) {
    return res.status(503).json({
      error: "Ask endpoint is not configured (missing ANTHROPIC_API_KEY).",
    });
  }

  try {
    const index = loadIndex();
    const file = routedFile(req);
    const queryText = goal ? `${goal} ${ask}` : ask;
    const chunks = retrieve(index, queryText, file);
    const response = await synthesize(
      ask,
      goal,
      chunks,
      index.canon_sha,
      anthropicKey,
      process.env.ASK_MODEL,
    );

    res.setHeader("Content-Type", "application/json; charset=utf-8");
    res.setHeader("Cache-Control", "no-store");
    res.setHeader("Access-Control-Allow-Origin", "*");
    return res.status(200).json(response);
  } catch (err) {
    console.error("ask handler error:", err);
    return res.status(500).json({
      error: "Ask query failed.",
      detail: err instanceof Error ? err.message : String(err),
    });
  }
}
