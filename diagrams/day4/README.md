# Day 4 Screenshot Evidence

Screenshots are arranged in execution order.

| No. | Screenshot | Evidence |
|---|---|---|
| 1 | `01-shared-document-corpus.png` | Shared RAG document used by all four frameworks |
| 2 | `02-common-test-questions.png` | Three common questions used for retrieval tests |
| 3 | `03-langchain-retrieval-test.png` | LangChain retrieval run |
| 4 | `04-haystack-retrieval-test.png` | Haystack retrieval run |
| 5 | `05-llamaindex-retrieval-test.png` | LlamaIndex retrieval run |
| 6 | `06-llamastack-retrieval-test.png` | LlamaStack API retrieval run; requests returned HTTP 200 |

All four frameworks were tested against `corpus/rag-introduction.txt` using
`corpus/test-questions.txt` and the `all-MiniLM-L6-v2` embedding model where
configured in their implementations.

Note: LlamaStack reports provider-specific similarity scores. Do not compare
its scores directly with scores from the other frameworks.
