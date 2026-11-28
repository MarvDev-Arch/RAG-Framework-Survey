# RAG Framework Survey

## A Six-Day Practical Study and Comparison of LlamaIndex, Haystack, LangChain and LlamaStack

| Project detail | Information |
|---|---|
| **Author** | Ifeanyi Marvelous Akpati |
| **GitHub** | MarvDev-Arch |
| **Start date** | 25 November 2026 |
| **Expected completion** | 30 November 2026 |
| **Duration** | 6 days |
| **Category** | DevOps / AI Engineering |
| **Current status** | **Days 1, 2 and 3 completed** |

---

## 1. Project Overview

This project is a six-day technical survey of four leading Retrieval-Augmented Generation (RAG) frameworks: LlamaIndex, Haystack, LangChain and LlamaStack.

The objective is to research, understand, implement and compare these frameworks based on their document-ingestion pipelines, retrieval abstractions, agent and tool support, observability, and production readiness.

### Project Scope and Progress

| Day | Activities | Expected deliverable | Status |
|---|---|---|---|
| Day 1 | RAG fundamentals, AI, LLMs, embeddings, vector databases and RAG architecture | Fundamentals documentation | **Completed** |
| Day 2 | LlamaIndex and Haystack research, architecture, ingestion and retrieval | Framework research and practical exercises | **Completed** |
| Day 3 | LangChain and LlamaStack research, APIs, agents and tool integration | Framework research and practical exercises | **Completed** |
| Day 4 | Implement four minimal RAG pipelines using the same 10-page document corpus | Four working RAG implementations | Upcoming |
| Day 5 | Compare ingestion, retrieval, agents/tools, observability and production readiness | Feature matrix and testing results | Upcoming |
| Day 6 | Complete evaluation, decision guide, recommendations and final documentation | Final Markdown research report | Upcoming |

**Scope boundary:** Day 1 covers RAG fundamentals and development-environment preparation. Days 2 and 3 focus on individual framework research. Day 4 covers practical implementation. Day 5 is dedicated to framework comparison and evaluation. Day 6 completes the decision guide and final report.

The complete survey is planned for six working days.

## 2. Project Objective

To understand and compare four RAG frameworks and evaluate how they support the development of AI applications that retrieve information from external knowledge sources.

The survey examines:

- Document-ingestion pipelines.
- Retrieval abstractions.
- Agent and tool support.
- Observability and monitoring.
- Production readiness.
- Practical implementation and evaluation.

## 3. Understanding RAG

RAG stands for **Retrieval-Augmented Generation**. It is an AI technique that enables a Large Language Model (LLM) to retrieve relevant information from external knowledge sources before generating an answer.

For example, an AI application can search company PDF documents to answer employee questions about IT policies.

### RAG Architecture

```text
                 DOCUMENT INGESTION
                         |
                         v
                  +-------------+
                  |  Documents  |
                  +-------------+
                         |
                         v
                  +-------------+
                  | Document    |
                  | Loader      |
                  +-------------+
                         |
                         v
                  +-------------+
                  | Text        |
                  | Chunking    |
                  +-------------+
                         |
                         v
                  +-------------+
                  | Embeddings  |
                  +-------------+
                         |
                         v
                  +-------------+
                  | Vector      |
                  | Database    |
                  +-------------+
                         ^
                         |
                  Stored vectors
                         |
USER QUESTION -----------+
       |
       v
+------------------+
| Question         |
| Embedding        |
+------------------+
       |
       v
+------------------+       +------------------+
| Similarity       |------>| Relevant Context |
| Search           |       +------------------+
+------------------+                |
                                     v
                              +-------------+
                              | LLM Model   |
                              +-------------+
                                     |
                                     v
                              +-------------+
                              | Generated   |
                              | Answer      |
                              +-------------+
```

### How RAG Works

**Document ingestion**

1. Load documents.
2. Extract text.
3. Divide large documents into smaller chunks.
4. Generate embeddings.
5. Store embeddings in a vector database.

**Retrieval and generation**

1. Receive a user question.
2. Convert the question into an embedding.
3. Search the vector database.
4. Retrieve relevant information.
5. Send the retrieved context to an LLM.
6. Generate an answer.

## 4. Technical Glossary

| Term | Simple explanation |
|---|---|
| AI | Technology that enables machines to perform intelligent tasks. |
| LLM | Large Language Model used to understand and generate text. |
| RAG | Retrieval-Augmented Generation. |
| Embeddings | Numerical representations of information. |
| Vector database | A database used to store and search vector representations. |
| Chunking | Dividing large documents into smaller sections. |
| Retrieval | Finding relevant information from stored documents. |
| Generation | Producing an answer using an AI model. |
| Ingestion | Collecting and preparing data for an application. |
| Semantic search | Finding information based on meaning rather than exact keywords. |

## 5. Daily Research Documentation

| Day | Documentation | Status |
|---|---|---|
| Day 1 | RAG Fundamentals | Completed |
| Day 2 | LlamaIndex and Haystack | Completed |
| Day 3 | LangChain and LlamaStack | Completed |
| Day 4 | Practical Implementation | Upcoming |
| Day 5 | Testing and Comparison | Upcoming |
| Day 6 | Final Report | Upcoming |

## 6. Frameworks Under Investigation

### LlamaIndex

A framework for connecting LLMs to external data sources through document ingestion, indexing and retrieval.

### Haystack

A framework for developing AI search applications, question-answering systems and structured RAG pipelines.

### LangChain

A framework for building LLM applications using integrations, retrievers, agents and external tools.

### LlamaStack

An open-source framework that provides standardized APIs and configurable services for building generative AI applications.

## 7. Development Environment

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Visual Studio Code | Development environment |
| PowerShell | Command-line operations |
| Git | Version control |
| GitHub | Source-code hosting and collaboration |
| Docker | Application containerization where applicable |

## 8. Project Structure

```text
RAG-FRAMEWORK-SURVEY/
|
+-- corpus/
|   +-- rag-introduction.txt
|
+-- diagrams/
|   +-- day2/
|   +-- day3/
|
+-- documentation/
|   +-- Day1-RAG-Fundamentals.md
|   +-- Day2-LlamaIndex-Haystack.md
|   +-- Day3-LangChain-LlamaStack.md
|   +-- Day4-Practical-Implementation.md
|   +-- Day5-Testing-and-Comparison.md
|   +-- Day6-Final-Report.md
|
+-- haystack/
+-- langchain/
+-- llamaindex/
+-- llamastack/
+-- results/
|
+-- .gitignore
+-- README.md
```

The local `venv/` and `day3-venv/` folders are Python virtual environments and should remain excluded from Git using `.gitignore`.

## 9. Expected Final Deliverables

At the end of the six-day survey, this repository will contain:

- A comprehensive Markdown research report.
- A feature comparison matrix.
- Four minimal working RAG pipelines.
- A shared 10-page document corpus.
- Practical testing and evaluation results.
- A decision guide explaining when to choose each framework.
- Final technical recommendations.
- Implementation screenshots and supporting evidence.

## 10. Official Documentation

- [LlamaIndex Documentation](https://docs.llamaindex.ai/)
- [Haystack Documentation](https://docs.haystack.deepset.ai/)
- [LangChain Documentation](https://python.langchain.com/docs/)
- [LlamaStack Documentation](https://llama-stack.readthedocs.io/)

---

# Daily Progress and Practical Work

## 11. Day 1 – RAG Fundamentals

**Status:** Completed

Day 1 focused on understanding the core concepts behind Retrieval-Augmented Generation and preparing the development environment.

### Topics Covered

- Artificial Intelligence and Large Language Models.
- Retrieval-Augmented Generation.
- Embeddings and vector databases.
- Document chunking and retrieval.
- The basic RAG architecture.

The purpose of this foundation was to understand how an application can retrieve relevant information from external documents before generating a response.

## 12. Day 2 – LlamaIndex and Haystack

**Date:** 26 November 2026  
**Status:** Completed

On Day 2, I worked with LlamaIndex and Haystack to understand how both frameworks handle document loading, embeddings, indexing and information retrieval.

I installed the frameworks, configured my Python virtual environment and used the same sample document to test their retrieval capabilities.

### LlamaIndex Implementation

Tasks completed:

1. Installed LlamaIndex in my Python virtual environment.
2. Installed the Hugging Face embedding integration.
3. Created `rag-introduction.txt` as my sample knowledge document.
4. Configured the `all-MiniLM-L6-v2` local embedding model.
5. Loaded the document using `SimpleDirectoryReader`.
6. Created a vector index using `VectorStoreIndex`.
7. Configured a retriever to find relevant information.
8. Tested questions directly from the VS Code terminal.

**Practical result:** LlamaIndex successfully loaded my document and retrieved relevant information when I asked questions such as "What does RAG mean?"

### Haystack Implementation

Tasks completed:

1. Installed Haystack and its Sentence Transformers integration.
2. Created a separate Haystack application.
3. Loaded the same `rag-introduction.txt` document.
4. Created an `InMemoryDocumentStore`.
5. Generated document embeddings.
6. Configured the text embedder.
7. Connected the retriever to the Haystack pipeline.
8. Tested document retrieval using questions from the terminal.

**Practical result:** Haystack successfully loaded the document, created the retrieval pipeline and returned relevant information based on my questions.

### Framework Comparison

| Feature | LlamaIndex | Haystack |
|---|---|---|
| Document loading | `SimpleDirectoryReader` | Document components |
| Embedding model | Hugging Face | Sentence Transformers |
| Indexing and storage | `VectorStoreIndex` | `InMemoryDocumentStore` |
| Retrieval | Index retriever | `InMemoryEmbeddingRetriever` |
| Workflow | Index and retrieval | Connected pipeline |
| Practical test | Successful | Successful |

### Challenges Resolved

- Configured pip correctly within my Python environment.
- Fixed the document directory path in my LlamaIndex application.
- Resolved a Haystack import error by installing the separate Sentence Transformers integration.
- Completed the Hugging Face embedding model download despite Windows caching warnings.

### What I Learned

- Installing and configuring RAG frameworks.
- Loading external documents into applications.
- Generating local text embeddings.
- Creating vector indexes and document stores.
- Configuring retrieval components.
- Building a modular retrieval pipeline.
- Testing and comparing different RAG frameworks.

### Screenshots and Practical Evidence

Screenshots of the installation, application setup and terminal tests are saved in `diagrams/day2/`.

| Screenshot file | Description |
|---|---|
| `01-llamaindex-installation.png` | LlamaIndex installation |
| `02-llamaindex-project-and-app.png` | LlamaIndex project and application setup |
| `03-llamaindex-retrieval-test.png` | LlamaIndex document retrieval test |
| `04-haystack-installation.png` | Haystack installation |
| `05-haystack-pipeline-execution.png` | Haystack pipeline execution |

### Day 2 Outcome

I successfully installed and tested LlamaIndex and Haystack using the same sample document and local embedding model.

Both frameworks retrieved relevant information from my document. Through this exercise, I understood the difference between LlamaIndex's indexing approach and Haystack's component-based pipeline.

The applications currently demonstrate document retrieval. Full LLM-based answer generation will be covered in the next implementation stages.

**Day 2 completed successfully.**

## 13. Day 3 – LangChain and LlamaStack

**Date:** 27 November 2026  
**Status:** Completed

On Day 3, I explored LangChain and LlamaStack, focusing on document loading, text splitting, embeddings, vector storage, retrieval and framework configuration.

### LangChain Implementation

Tasks completed:

1. Installed LangChain and its integrations in a separate Python 3.14 virtual environment (`day3-venv`).
2. Loaded `corpus/rag-introduction.txt` using `TextLoader`.
3. Split the document using `RecursiveCharacterTextSplitter` with a 500-character chunk size and 50-character overlap.
4. Generated embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
5. Created a FAISS vector store.
6. Tested semantic retrieval with the question: "What are embeddings?"

**Practical result:** LangChain successfully loaded one document, created three chunks, built a FAISS vector store and retrieved two relevant results.

### LlamaStack Implementation

Tasks completed:

1. Installed LlamaStack 0.7.3 and LlamaStack Client 0.7.5.
2. Explored the CLI, Starter distribution, available providers and configuration files.
3. Resolved an MCP compatibility issue by installing MCP 1.30.0.
4. Investigated missing optional provider dependencies, including Together and Anthropic.

**Practical result:** LlamaStack installation and CLI checks were successful. Starter server startup and API testing remain outstanding because provider dependencies and configuration still need to be resolved.

### Challenges

- Resolved missing Python dependencies.
- Fixed an MCP compatibility issue.
- Investigated optional provider dependencies and Starter configuration.

### What I Learned

- Document loading and text chunking.
- Hugging Face embeddings and FAISS vector storage.
- Semantic similarity search with LangChain.
- LlamaStack distributions, providers, CLI commands and configuration.



## Screenshots and Practical Evidence

Day 3 practical screenshots are saved in `diagrams/day3/`. They provide evidence of the LangChain and LlamaStack installation, configuration, API inspection, document ingestion and retrieval processes.

| Screenshot file | Description |
|---|---|
| `01-langchain-application-code.png` | LangChain application code |
| `02-llamastack-starter-configuration.png` | LlamaStack starter configuration |
| `03-llamastack-provider-configuration.png` | LlamaStack provider configuration inspection |
| `llama-cli-and-version-check.png` | Llama CLI and version checks |
| `llama-cli-help.png` | LlamaStack CLI help and available commands |
| `llamastack-api-health.png` | Successful LlamaStack API health check |
| `llamastack-api-list.png` | Available LlamaStack APIs |
| `llamastack-configuration.png` | LlamaStack configuration details |
| `llamastack-dependency-installation.png` | Installation of missing dependencies |
| `llamastack-distributions.png` | Available LlamaStack distributions |
| `llamastack-document-upload-and-retrieval.png` | Document upload and retrieval test |
| `llamastack-embedding-model-registration.png` | Registration of all-MiniLM-L6-v2 embedding model |
| `llamastack-installation.png` | LlamaStack installation evidence |
| `llamastack-provider-list.png` | Available LlamaStack providers |
| `llamastack-server-start.png` | Successful LlamaStack server startup |

### Practical Test Results

- LangChain successfully loaded and retrieved content from the sample document.
- LangChain calculator tool returned the correct result: `100`.
- LlamaStack server health check returned `OK`.
- all-MiniLM-L6-v2 was registered with 384 embedding dimensions.
- FAISS vector store was created successfully.
- `rag-introduction.txt` was uploaded and processed successfully.
- LlamaStack successfully retrieved relevant document content with a similarity score of approximately `0.8185`.


## Day 3: LangChain and LlamaStack

### Practical Implementation

**LangChain**
- Installed and configured LangChain.
- Loaded the RAG sample document.
- Split the document into smaller chunks.
- Generated embeddings using all-MiniLM-L6-v2.
- Created a FAISS vector store.
- Successfully retrieved relevant document content.
- Tested a calculator tool using LangChain.

**LlamaStack**
- Installed and configured LlamaStack 0.7.3.
- Started the LlamaStack server successfully.
- Registered all-MiniLM-L6-v2 with 384 embedding dimensions.
- Created a FAISS vector store.
- Uploaded rag-introduction.txt.
- Successfully retrieved relevant document content.
- Confirmed successful API responses.

### Troubleshooting
- Resolved missing Python dependencies.
- Corrected embedding model registration.
- Resolved port 8321 conflicts.
- Worked around unsupported CLI and SDK methods.

### Comparison

| Feature | LangChain | LlamaStack |
|---|---|---|
| Installation | Successful | Successful |
| Document ingestion | Successful | Successful |
| Embeddings | MiniLM | MiniLM |
| FAISS | Successful | Successful |
| Retrieval | Successful | Successful |
| Tool testing | Calculator | Not completed |
| Full answer generation | Not tested | Not tested |



## 14. Conclusion

This survey aims to develop a practical understanding of modern RAG frameworks and their application in AI-powered knowledge retrieval systems.

The research progresses from foundational concepts to framework-specific implementations, comparative testing and final technical recommendations.

This repository serves as the central record of the six-day research and implementation process.
