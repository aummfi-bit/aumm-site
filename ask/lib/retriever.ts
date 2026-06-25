import type { AskIndex, IndexChunk } from "./types.js";

const DEFAULT_TOP_K = 8;
const MIN_SCORE = 0.25;

function cosineSimilarity(a: number[], b: number[]): number {
  let dot = 0;
  let normA = 0;
  let normB = 0;
  for (let i = 0; i < a.length; i++) {
    dot += a[i] * b[i];
    normA += a[i] * a[i];
    normB += b[i] * b[i];
  }
  const denom = Math.sqrt(normA) * Math.sqrt(normB);
  return denom === 0 ? 0 : dot / denom;
}

export interface RetrievedChunk extends IndexChunk {
  score: number;
}

export function retrieve(
  index: AskIndex,
  queryEmbedding: number[],
  topK = DEFAULT_TOP_K,
): RetrievedChunk[] {
  const scored = index.chunks.map((chunk) => ({
    ...chunk,
    score: cosineSimilarity(queryEmbedding, chunk.embedding),
  }));

  scored.sort((a, b) => b.score - a.score);
  const top = scored.slice(0, topK);
  return top.filter((c) => c.score >= MIN_SCORE);
}

export function excerpt(text: string, maxLen = 480): string {
  const normalized = text.replace(/\s+/g, " ").trim();
  if (normalized.length <= maxLen) {
    return normalized;
  }
  return normalized.slice(0, maxLen - 1) + "…";
}
