Day 2: LlamaIndex and Haystack

Author: Ifeanyi Marvelous Akpati  
Project: RAG Framework Survey  
Date:26 November 2026

1. Objective

The focus of Day 2 was to understand and test LlamaIndex and Haystack. Both frameworks were installed and tested using the same sample document and local embedding model.

 2. Environment Setup

- Operating System: Windows 11
- Code Editor: Visual Studio Code
- Python: 3.15.2
- Environment: Python Virtual Environment
- Sample Document: rag-introduction.txt
- Embedding Model: all-MiniLM-L6-v2

 3. LlamaIndex

LlamaIndex is a framework used to connect language models to external data sources such as documents, databases and websites.

Main components:

- Data Connectors: Load information from external sources.
- Documents: Hold the loaded information.
- Nodes: Divide documents into smaller sections.
- Embeddings: Convert text into numerical vectors.
- Vector Index: Organises information for searching.
- Retriever: Finds relevant information.
- Query Engine: Handles information retrieval and response generation.
- Agents: Allow applications to interact with external tools.

Practical Implementation

Installed LlamaIndex using:

powershell
python -m pip install llama-index


Installed the local embedding integration:

powershell
python -m pip install llama-index-embeddings-huggingface sentence-transformers


The practical exercise involved:

1. Creating a sample RAG document.
2. Configuring a local embedding model.
3. Loading the document using SimpleDirectoryReader.
4. Creating a vector index using VectorStoreIndex.
5. Configuring a retriever.
6. Testing questions against the document.

Result: LlamaIndex successfully loaded the document and retrieved relevant information when asked what RAG means.

 Screenshots

Figure 1: LlamaIndex installation  
`diagrams/day2/01-llamaindex-installation.png`

Figure 2: LlamaIndex application in VS Code  
`diagrams/day2/02-llamaindex-project-and-app.png`

Figure 3: LlamaIndex retrieval test  
`diagrams/day2/03-llamaindex-retrieval-test.png`

4. Haystack

Haystack is a framework used to build AI-powered search, question-answering and RAG applications. It uses components connected through pipelines.

Main components:

- Document Store: Stores documents and embeddings.
- Document Embedder: Converts documents into numerical vectors.
- Text Embedder: Converts user questions into vectors.
- Retriever: Searches for relevant documents.
- Pipeline: Connects different components.
- Prompt Builder: Prepares prompts for language models.
- Generator: Generates responses using an LLM.
- Agents: Interact with external tools.
 Practical Implementation

Installed Haystack using:

powershell
python -m pip install haystack-ai sentence-transformers


Installed the Sentence Transformers integration:

powershell


The practical exercise involved:

1. Creating a Haystack application.
2. Loading the same RAG sample document.
3. Creating an InMemoryDocumentStore.
4. Generating document embeddings.
5. Configuring the text embedder.
6. Connecting the retriever to the pipeline.
7. Testing questions and retrieving relevant information.

**Result:** Haystack successfully loaded the document, created its retrieval pipeline and returned relevant information when asked what RAG means.

 Screenshots

Figure 4: Haystack installation  
`diagrams/day2/04-haystack-installation.png`

Figure 5: Haystack pipeline execution  
`diagrams/day2/05-haystack-pipeline-execution.png`
5. Framework Comparison

| Feature | LlamaIndex | Haystack |
|---|---|---|
| Main purpose | Connecting LLMs to external data | Building search and RAG pipelines |
| Document loading | SimpleDirectoryReader | Document components |
| Embeddings | HuggingFace integration | Sentence Transformers |
| Indexing and storage | VectorStoreIndex | InMemoryDocumentStore |
| Retrieval | Index Retriever | InMemoryEmbeddingRetriever |
| Workflow | Query engines and workflows | Connected pipelines |
| Agent support | Yes | Yes |
| Local models | Supported | Supported |

6. Challenges Encountered

**Python Environment:** Configured the virtual environment and resolved the pip command issue.

**LlamaIndex Document Path:** Corrected the document directory path using Python pathlib.

**Haystack Import Error:** Resolved the Sentence Transformers import issue by installing the separate Haystack integration package.

**HuggingFace Warnings:** Encountered download authentication and Windows symlink-cache warnings. The model downloaded and worked successfully.

 7. What I Learned

- How to install and configure LlamaIndex and Haystack.
- How documents are loaded and processed.
- How embeddings represent text numerically.
- How vector indexing and document stores work.
- How retrievers find relevant information.
- How Haystack components are connected through pipelines.
- How the two frameworks approach document retrieval.

 8. Conclusion

Day 2 provided practical experience with LlamaIndex and Haystack. Both frameworks were successfully installed and tested using the same document and local embedding model.

The exercises demonstrated document loading, embedding generation, indexing, storage and information retrieval.

Both applications currently perform retrieval rather than complete LLM-based answer generation.

9. References

- LlamaIndex: https://developers.llamaindex.ai/
- LlamaIndex Ingestion Pipeline: https://developers.llamaindex.ai/python/framework/module_guides/loading/ingestion_pipeline/
- Haystack: https://docs.haystack.deepset.ai/docs/intro
- Haystack Pipelines: https://docs.haystack.deepset.ai/docs/pipelines
- Sentence Transformers: https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2