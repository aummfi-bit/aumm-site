export interface IndexChunk {
  file: string;
  section_id: string;
  heading: string;
  text: string;
}

export interface AskIndex {
  canon_sha: string;
  chunk_count?: number;
  chunks: IndexChunk[];
}

export interface Citation {
  section_id: string;
  file: string;
  excerpt: string;
}

export interface AskResponse {
  answer: string;
  citations: Citation[];
  canon_sha: string;
  answered_from_corpus: boolean;
}
