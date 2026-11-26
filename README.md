RAG Framework Survey
LlamaIndex | Haystack | LangChain | LlamaStack

Author: Ifeanyi Marvelous Akpati  
GitHub: MarvDev-Arch  
Project Start Date: 25 November 2026  
Expected Completion: 30 November 2026  
Duration: 6 Days  
Category: DevOps / AI Engineering  
Difficulty: Intermediate  
Current Status: Day 1 Documentation Completed



 1. Project Scope and Boundary

This project is a six-day technical survey of four leading Retrieval-Augmented Generation (RAG) frameworks: LlamaIndex, Haystack, LangChain and LlamaStack.

The objective is to research, understand, implement and compare these frameworks based on their ingestion pipelines, retrieval abstractions, agent/tool support, observability and production readiness.

 Scope by Day

| Day | Activities | Expected Deliverable |
|---|---|---|
| Day 1 | RAG fundamentals, AI, LLMs, embeddings, vector databases and RAG architecture. | Fundamentals documentation. |
| Day 2 | LlamaIndex and Haystack research, architecture, ingestion and retrieval. | Framework research and practical exercises. |
| Day 3 | LangChain and LlamaStack research, APIs, agents and tool integration. | Framework research and practical exercises. |
| Day 4 | Implement four minimal RAG pipelines using the same 10-page document corpus. | Four working RAG implementations. |
| Day 5 | Compare ingestion, retrieval, agents/tools, observability and production readiness. | Feature matrix and testing results. |
| Day 6 | Complete evaluation, decision guide, recommendations and final documentation. | Final Markdown research report. |

Scope Boundary:Day 1 covers RAG fundamentals and development environment preparation. Days 2 and 3 focus on individual framework research. Day 4 covers practical implementation. Day 5 is dedicated to framework comparison and evaluation. Day 6 completes the decision guide and final report.

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

RAG stands for Retrieval-Augmented Generation.

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
           |
           |
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



4. Technical Glossary

| Term | Simple Explanation |
|---|---|
| AI | Technology that enables machines to perform intelligent tasks. |
| LLM | Large Language Model used to understand and generate text. |
| RAG | Retrieval-Augmented Generation. |
| Embeddings | Numerical representations of information. |
| Vector Database | Database used to store and search vector representations. |
| Chunking | Dividing large documents into smaller sections. |
| Retrieval | Finding relevant information from stored documents. |
| Generation | Producing an answer using an AI model. |
| Ingestion | Collecting and preparing data for an application. |
| Semantic Search | Finding information based on meaning rather than exact keywords. |



 5. Daily Research Documentation

This section provides direct access to the research completed each day.

| Day | Documentation | Status |
|---|---|---|
| Day 1 | [RAG Fundamentals](documentation/Day1-RAG-Fundamentals.md) | Completed |
| Day 2 | [LlamaIndex and Haystack](documentation/Day2-LlamaIndex-Haystack.md) | Upcoming |
| Day 3 | [LangChain and LlamaStack](documentation/Day3-LangChain-LlamaStack.md) | Upcoming |
| Day 4 | [Practical Implementation](documentation/Day4-Practical-Implementation.md) | Upcoming |
| Day 5 | [Testing and Comparison](documentation/Day5-Testing-and-Comparison.md) | Upcoming |
| Day 6 | [Final Report](documentation/Day6-Final-Report.md) | Upcoming |



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

| Technology | Purpose |
|---|---|
| Python | Main programming language. |
| Visual Studio Code | Development environment. |
| PowerShell | Command-line operations. |
| Git | Version control. |
| GitHub | Source code hosting and collaboration. |
| Docker | Application containerization where applicable. |



8. Project Structure

  
RAG-FRAMEWORK-SURVEY/
├── corpus/
├── documentation/
├── llamaindex/
├── haystack/
├── langchain/
├── llamastack/
├── results/
├── diagrams/
├── .gitignore
└── README.md




 9. Expected Final Deliverables

At the end of the six-day survey, this repository will contain:

1. A comprehensive Markdown research report.
2. A feature comparison matrix.
3. Four minimal working RAG pipelines.
4. A shared 10-page document corpus.
5. Practical testing and evaluation results.
6. A decision guide explaining when to choose each framework.
7. Final technical recommendations.
8. Implementation screenshots and supporting evidence.



 10. Official Documentation

- [LlamaIndex Documentation](https://developers.llamaindex.ai/)
- [Haystack Documentation](https://docs.haystack.deepset.ai/)
- [LangChain Documentation](https://docs.langchain.com/)
- [LlamaStack Documentation](https://llama-stack.readthedocs.io/)



11. Conclusion

This survey aims to develop a practical understanding of modern RAG frameworks and their application in AI-powered knowledge retrieval systems.

The research will progress from foundational concepts to framework-specific implementations, comparative testing and final technical recommendations.

This repository serves as the central record of the six-day research and implementation process.