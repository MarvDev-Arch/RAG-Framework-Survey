# Day 4: Practical RAG Framework Implementation

**Project:** RAG Framework Survey – LlamaIndex, Haystack, LangChain and LlamaStack  
**Author:** Ifeanyi Marvelous Akpati  
**Date:** 28 November 2026  
**Status:** Completed  
**Category:** DevOps / AI Engineering

## 1. Introduction

Day 4 focused on the practical implementation and testing of four RAG frameworks: LlamaIndex, Haystack, LangChain and LlamaStack.

The goal was to build and test a basic document retrieval pipeline with each framework using the same document, questions and local embedding model.

## 2. Project Objectives

- Implement retrieval pipelines using four RAG frameworks.
- Use a common document corpus for testing.
- Use the same embedding model across the frameworks.
- Execute the same questions against each framework.
- Observe and compare the retrieval results.
- Capture screenshots as practical evidence.

## 3. Shared Document and Test Questions

The document used for all four implementations was:

`corpus/rag-introduction.txt`

The common test questions were stored in:

`corpus/test-questions.txt`

Questions:

1. What is Retrieval-Augmented Generation (RAG)?
2. What are embeddings?
3. What is the purpose of a vector database?

**Embedding model:**

`sentence-transformers/all-MiniLM-L6-v2`

This model was used to maintain consistency across the practical tests.

## 4. Framework Implementation

### 4.1 LangChain

LangChain was implemented using the following components:

- TextLoader – loads the document.
- RecursiveCharacterTextSplitter – divides the document into smaller chunks.
- HuggingFaceEmbeddings – generates document embeddings.
- FAISS – stores vectors and supports similarity search.

**Testing results:**
- Successfully loaded the document.
- Created 3 text chunks.
- Created a FAISS vector store.
- Retrieved 2 relevant results for each test question.

**Outcome:** Successful.

### 4.2 Haystack

Haystack was implemented using:

- InMemoryDocumentStore – stores documents and embeddings.
- SentenceTransformersDocumentEmbedder – generates document embeddings.
- SentenceTransformersTextEmbedder – generates query embeddings.
- InMemoryEmbeddingRetriever – retrieves relevant documents.

**Testing results:**
- Successfully loaded the shared document.
- Generated document embeddings.
- Created the retrieval pipeline.
- Successfully retrieved relevant content for all three questions.

**Outcome:** Successful.

### 4.3 LlamaIndex

LlamaIndex was implemented using:

- SimpleDirectoryReader – loads the document.
- HuggingFaceEmbedding – generates embeddings.
- VectorStoreIndex – creates the searchable vector index.
- Retriever – retrieves relevant document sections.

**Testing results:**
- Successfully loaded the document.
- Created the vector index.
- Executed all three test questions.
- Retrieved relevant document content.

**Outcome:** Successful.

### 4.4 LlamaStack

LlamaStack was implemented using its client API and configured FAISS vector store.

The implementation involved:

- Connecting to the local LlamaStack server.
- Using the registered all-MiniLM-L6-v2 embedding model.
- Creating and using a FAISS vector store.
- Uploading the shared document.
- Attaching the document to the vector store.
- Executing retrieval requests through the LlamaStack API.

**Testing results:**

All three questions were submitted successfully. The API returned relevant document content.

Observed similarity scores:

| Test Question | Returned Score |
|---|---:|
| What is RAG? | 1.5647 |
| What are embeddings? | 0.8185 |
| What is a vector database? | 0.9999 |

Note: These scores are provider-specific retrieval values. They should not be treated as probabilities or directly compared with scores from other frameworks.

**Outcome:** Successful.

## 5. Practical Comparison

| Feature | LangChain | Haystack | LlamaIndex | LlamaStack |
|---|---|---|---|---|
| Document loading | Successful | Successful | Successful | Successful |
| Embedding generation | Successful | Successful | Successful | Configured |
| Vector storage | FAISS | In-memory store | Vector index | FAISS |
| Retrieval testing | Successful | Successful | Successful | Successful |
| Common questions | 3 | 3 | 3 | 3 |

All four frameworks successfully completed the retrieval tests.

## 6. Challenges Encountered

| Challenge | Resolution |
|---|---|
| Missing Python packages | Installed the required dependencies. |
| Import errors | Corrected the package imports. |
| Missing framework dependencies | Installed the required framework integrations. |
| Undefined variables | Updated the application scripts. |
| File path issues | Used project-relative paths. |
| LlamaStack configuration | Updated the embedding model and vector store configuration. |

## 7. Lessons Learned

During Day 4, I learned:

- How different RAG frameworks load and process documents.
- How embedding models convert text into numerical representations.
- How vector stores support document retrieval.
- How similarity search retrieves relevant information.
- How to test multiple frameworks using a common dataset.
- How to troubleshoot package, import and configuration issues.

## 8. Screenshot Evidence

Practical screenshots are stored in:

`diagrams/day4/`

| Screenshot | Description |
|---|---|
| 01-shared-document-corpus.png | Shared document used for testing |
| 02-common-test-questions.png | Common questions used across frameworks |
| 03-langchain-retrieval-test.png | LangChain retrieval results |
| 04-haystack-retrieval-test.png | Haystack retrieval results |
| 05-llamaindex-retrieval-test.png | LlamaIndex retrieval results |
| 06-llamastack-retrieval-test.png | LlamaStack retrieval results |

## 9. Day 4 Conclusion

Day 4 was successfully completed. I implemented and tested retrieval pipelines using LangChain, Haystack, LlamaIndex and LlamaStack.

Using the same document, embedding model and test questions helped maintain a consistent testing approach.

The practical results will be used for the framework comparison on Day 5 and the final project report on Day 6.

**Next:** Day 5 – Framework Comparison and Analysis.
