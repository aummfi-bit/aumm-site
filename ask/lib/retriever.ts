import type { AskIndex, IndexChunk } from "./types.js";

export const TOP_K = 12;
export const MAX_CONTEXT_CHARS = 60_000;
export const ROUTED_PAGE_BOOST = 1.4;
const BM25_K1 = 1.5;
const BM25_B = 0.75;

export interface RetrievedChunk extends IndexChunk {
  score: number;
}

function tokenize(s: string): string[] {
  return (s.toLowerCase().match(/[a-z0-9§-]+/g) ?? []).filter((t) => t.length > 1);
}

export function excerpt(text: string, maxLen = 480): string {
  const normalized = text.replace(/\s+/g, " ").trim();
  if (normalized.length <= maxLen) {
    return normalized;
  }
  return normalized.slice(0, maxLen - 1) + "…";
}

export function retrieve(
  index: AskIndex,
  query: string,
  routedFile?: string,
): RetrievedChunk[] {
  const chunks = index.chunks;
  const qTerms = tokenize(query);
  if (qTerms.length === 0 || chunks.length === 0) {
    return [];
  }

  const docs = chunks.map((c) =>
    tokenize(`${c.text} ${c.heading} ${c.section_id}`),
  );

  const df = new Map<string, number>();
  for (const d of docs) {
    for (const t of new Set(d)) {
      df.set(t, (df.get(t) ?? 0) + 1);
    }
  }

  const n = chunks.length;
  const avgdl = docs.reduce((s, d) => s + d.length, 0) / n;

  const scored = chunks.map((c, i) => {
    const d = docs[i];
    const tf = new Map<string, number>();
    for (const t of d) {
      tf.set(t, (tf.get(t) ?? 0) + 1);
    }
    const dl = d.length;
    let score = 0;
    for (const qt of qTerms) {
      const f = tf.get(qt) ?? 0;
      if (!f) continue;
      const docFreq = df.get(qt) ?? 0;
      const idf = Math.log(1 + (n - docFreq + 0.5) / (docFreq + 0.5));
      score +=
        (idf * (f * (BM25_K1 + 1))) /
        (f + BM25_K1 * (1 - BM25_B + (BM25_B * dl) / avgdl));
    }
    if (routedFile && c.file === routedFile) {
      score *= ROUTED_PAGE_BOOST;
    }
    return { ...c, score };
  });

  scored.sort((a, b) => b.score - a.score);

  const out: RetrievedChunk[] = [];
  let budget = MAX_CONTEXT_CHARS;
  for (const row of scored) {
    if (row.score <= 0) break;
    if (row.text.length > budget) continue;
    out.push(row);
    budget -= row.text.length;
    if (out.length >= TOP_K) break;
  }

  return out;
}
