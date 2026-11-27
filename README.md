RAG Framework Survey: A Six-Day Practical Study and Comparison of LlamaIndex, Haystack, LangChain and LlamaStack

Author: Ifeanyi Marvelous Akpati
GitHub: MarvDev-Arch
Project Start Date: 25 November 2026
Expected Completion: 30 November 2026
Duration: 6 Days
Category: DevOps / AI Engineering
Difficulty: Intermediate
Current Status: Days 1, 2 and 3 Completed

1. Project Scope and Boundary
This project is a six-day technical survey of four leading Retrieval-Augmented Generation (RAG) frameworks: LlamaIndex, Haystack, LangChain and LlamaStack.

The objective is to research, understand, implement and compare these frameworks based on their ingestion pipelines, retrieval abstractions, agent/tool support, observability and production readiness.

Scope by Day
Day	Activities	Expected Deliverable	Status
Day 1	RAG fundamentals, AI, LLMs, embeddings, vector databases and RAG architecture.	Fundamentals documentation.	Completed
Day 2	LlamaIndex and Haystack research, architecture, ingestion and retrieval.	Framework research and practical exercises.	Completed
Day 3	LangChain and LlamaStack research, APIs, agents and tool integration.	Framework research and practical exercises.	Completed
Day 4	Implement four minimal RAG pipelines using the same 10-page document corpus.	Four working RAG implementations.	Upcoming
Day 5	Compare ingestion, retrieval, agents/tools, observability and production readiness.	Feature matrix and testing results.	Upcoming
Day 6	Complete evaluation, decision guide, recommendations and final documentation.	Final Markdown research report.	Upcoming


Scope Boundary: Day 1 covers RAG fundamentals and development environment preparation. Days 2 and 3 focus on individual framework research. Day 4 covers practical implementation. Day 5 is dedicated to framework comparison and evaluation. Day 6 completes the decision guide and final report.

The complete survey is planned for six working days.
2. Project Objective
To understand and compare four RAG frameworks and evaluate how they support the development of AI applications that retrieve information from external knowledge sources.

The survey will examine:
- Document ingestion pipelines.
- Retrieval abstractions.
- Agent and tool support.
- Observability and monitoring.
- Production readiness.
- Practical implementation and evaluation.
3. Understanding RAG
RAG stands for Retrieval-Augmented Generation

It is an AI technique that enables Large Language Models to retrieve relevant information from external knowledge sources before generating an answer.

For example, an AI application can search company PDF documents to answer employee questions about IT policies.

 RAG Architecture
   DOCUMENTS
       |
       v
DOCUMENT LOADER
       |
       v
  TEXT CHUNKING
       |
       v
    EMBEDDINGS
       |
       v
 VECTOR DATABASE

  USER QUESTION
       |
       v
    RETRIEVAL
       |
       v
RELEVANT CONTEXT
       |
       v
    LLM MODEL
       |
       v
 GENERATED ANSWER
 How RAG Works

Document Ingestion:
1. Load documents.
2. Extract text.
3. Divide text into smaller chunks.
4. Generate embeddings.
5. Store embeddings in a vector database.
Retrieval and Generation:
1. Receive a user question.
2. Convert the question into an embedding.
3. Search the vector database.
4. Retrieve relevant information.
5. Send retrieved context to an LLM.
6. Generate an answer.
7. Technical Glossary
Term	Simple Explanation
AI	Technology that enables machines to perform intelligent tasks.
LLM	Large Language Model used to understand and generate text.
RAG	Retrieval-Augmented Generation.
Embeddings	Numerical representations of information.
Vector Database	Database used to store and search vector representations.
Chunking	Dividing large documents into smaller sections.
Retrieval	Finding relevant information from stored documents.
Generation	Producing an answer using an AI model.
Ingestion	Collecting and preparing data for an application.
Semantic Search	Finding information based on meaning rather than exact keywords.


5. Daily Research Documentation
This section provides direct access to the research completed each day.
Day	Documentation	Status
Day 1	[RAG Fundamentals](documentation/Day1-RAG-Fundamentals.md)	Completed
Day 2	[LlamaIndex and Haystack](documentation/Day2-LlamaIndex-Haystack.md)	Completed
Day 3	[LangChain and LlamaStack](documentation/Day3-LangChain-LlamaStack.md)	Completed
Day 4	[Practical Implementation](documentation/Day4-Practical-Implementation.md)	Upcoming
Day 5	[Testing and Comparison](documentation/Day5-Testing-and-Comparison.md)	Upcoming
Day 6	[Final Report](documentation/Day6-Final-Report.md)	Upcoming


6. Frameworks Under Investigation
LlamaIndex
A framework for connecting LLMs to external data sources through document ingestion, indexing and retrieval.

Haystack
A framework for developing AI search applications, question-answering systems and structured RAG pipelines.

LangChain
A framework for building LLM applications using integrations, retrievers, agents and external tools.

LlamaStack
An open-source framework that provides standardized APIs and configurable services for building generative AI applications.
7. Development Environment
Technology	Purpose
Python	Main programming language.
Visual Studio Code	Development environment.
PowerShell	Command-line operations.
Git	Version control.
GitHub	Source code hosting and collaboration.
Docker	Application containerization where applicable.


8. Project Structure
RAG-FRAMEWORK-SURVEY/
├── corpus/
│   └── rag-introduction.txt
├── diagrams/
├── documentation/
├── haystack/
├── langchain/
├── llamaindex/
├── llamastack/
├── results/
├── .gitignore
└── README.md
The venv/ folder is the local Python virtual environment and should remain excluded from Git using .gitignore.
9. Expected Final Deliverables
At the end of the six-day survey, this repository will contain:
- A comprehensive Markdown research report.
- A feature comparison matrix.
- Four minimal working RAG pipelines.
- A shared 10-page document corpus.
- Practical testing and evaluation results.
- A decision guide explaining when to choose each framework.
- Final technical recommendations.
- Implementation screenshots and supporting evidence.
10. Official Documentation
    - LlamaIndex Documentation
    - Haystack Documentation
    - LangChain Documentation
    - LlamaStack Documentation
11. Day 2 – LlamaIndex and Haystack
Date:26 November 2026
Status:Completed

On Day 2, I worked with LlamaIndex and Haystack to understand how both frameworks handle document loading, embeddings, indexing and information retrieval.

I installed the frameworks, configured my Python virtual environment and used the same sample document to test their retrieval capabilities.

LlamaIndex Implementation

I started with LlamaIndex and completed the following tasks:
- Installed LlamaIndex in my Python virtual environment.
- Installed the HuggingFace embedding integration.
- Created rag-introduction.txt as my sample knowledge document.
- Configured the all-MiniLM-L6-v2 local embedding model.
- Loaded the document using SimpleDirectoryReader.
- Created a vector index using VectorStoreIndex.
- Configured a retriever to find relevant information.
- Tested questions directly from the VS Code terminal.
Practical Result:

LlamaIndex successfully loaded my document and retrieved relevant information when I asked questions such as "What does RAG mean?"

 Haystack Implementation

After completing the LlamaIndex exercise, I moved to Haystack and carried out the following tasks:
- Installed Haystack and its Sentence Transformers integration.
- Created a separate Haystack application.
- Loaded the same rag-introduction.txt document.
- Created an InMemoryDocumentStore.
- Generated document embeddings.
- Configured the text embedder.
- Connected the retriever to the Haystack pipeline.
- Tested document retrieval using questions from the terminal.
Practical Result:

Haystack successfully loaded the document, created the retrieval pipeline and returned relevant information based on my questions.

Framework Comparison
Feature	LlamaIndex	Haystack
Document Loading	SimpleDirectoryReader	Document components
Embedding Model	HuggingFace	Sentence Transformers
Indexing and Storage	VectorStoreIndex	InMemoryDocumentStore
Retrieval	Index Retriever	InMemoryEmbeddingRetriever
Workflow	Index and retrieval	Connected pipeline
Practical Test	Successful	Successful


Challenges I Resolved

During the practical exercises, I encountered a few issues and worked through them:
- Configured pip correctly within my Python environment.
- Fixed the document directory path in my LlamaIndex application.
- Resolved a Haystack import error by installing the separate Sentence Transformers integration.
- Completed the HuggingFace embedding model download despite Windows caching warnings.
 What I Learned

From the exercises, I gained practical experience with:
- Installing and configuring RAG frameworks.
- Loading external documents into applications.
- Generating local text embeddings.
- Creating vector indexes and document stores.
- Configuring retrieval components.
- Building a modular retrieval pipeline.
- Testing and comparing different RAG frameworks.
 Screenshots and Practical Evidence

I saved screenshots of the installation, application setup and terminal tests in the diagrams/day2/ folder.
Figure	Screenshot Description
1	LlamaIndex installation
2	LlamaIndex project and application setup
3	LlamaIndex document retrieval test
4	Haystack installation
5	Haystack pipeline execution


Screenshot Files:
- diagrams/day2/01-llamaindex-installation.png
- diagrams/day2/02-llamaindex-project-and-app.png
- diagrams/day2/03-llamaindex-retrieval-test.png
- diagrams/day2/04-haystack-installation.png
- diagrams/day2/05-haystack-pipeline-execution.png
Day 2 Outcome

I successfully installed and tested LlamaIndex and Haystack using the same sample document and local embedding model.

Both frameworks retrieved relevant information from my document. Through this exercise, I understood the difference between LlamaIndex's indexing approach and Haystack's component-based pipeline.

The applications currently demonstrate document retrieval. Full LLM-based answer generation will be covered in the next implementation stages.

Day 2 Completed Successfully.
12. Day 3 – LangChain and LlamaStack
Date: 27 November 2026
Status: Completed

On Day 3, I explored LangChain and LlamaStack, focusing on document loading, text splitting, embeddings, vector storage, retrieval and framework configuration.

LangChain Implementation
- Installed LangChain and its integrations in a separate Python 3.14 virtual environment (day3-venv).
- Loaded corpus/rag-introduction.txt using TextLoader.
- Split the document into chunks using RecursiveCharacterTextSplitter with a 500-character chunk size and 50-character overlap.
- Generated embeddings using sentence-transformers/all-MiniLM-L6-v2.
- Created a FAISS vector store.
- Tested semantic retrieval with the question: "What are embeddings?"
Practical Result:

LangChain successfully loaded one document, created three chunks, built a FAISS vector store and retrieved two relevant results.

LlamaStack Implementation
- Installed LlamaStack 0.7.3 and LlamaStack Client 0.7.5.
- Explored the CLI, Starter distribution, available providers and configuration files.
- Resolved an MCP compatibility issue by installing MCP 1.30.0.
- Investigated missing optional provider dependencies, including Together and Anthropic.
Practical Result:

LlamaStack installation and CLI checks were successful. Starter server startup and API testing remain outstanding because provider dependencies and configuration still need to be resolved.

Challenges
- Resolved missing Python dependencies.
- Fixed an MCP compatibility issue.
- Investigated optional provider dependencies and Starter configuration.
What I Learned
- Document loading and text chunking.
- Hugging Face embeddings and FAISS vector storage.
- Semantic similarity search with LangChain.
- LlamaStack distributions, providers, CLI commands and configuration.
Screenshots and Practical Evidence

Day 3 screenshots are saved in diagrams/day3/:
- 01-langchain-application-code.png – LangChain application code.
- 02-llamastack-starter-configuration.png – Starter configuration output.
- 03-llamastack-provider-configuration.png – Provider configuration inspection.
Day 3 Outcome

LangChain document retrieval was successfully implemented. LlamaStack was installed and explored, but server startup and API verification are still pending.

Day 3 Completed Successfully.
13. Conclusion
This survey aims to develop a practical understanding of modern RAG frameworks and their application in AI-powered knowledge retrieval systems.

The research will progress from foundational concepts to framework-specific implementations, comparative testing and final technical recommendations.

This repository serves as the central record of the six-day research and implementation process.