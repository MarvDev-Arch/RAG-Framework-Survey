Day 3 – LangChain and LlamaStack
Date: 27 November 2026
Status: Completed

1. Overview
Today, I explored LangChain and LlamaStack to understand how they support RAG and AI application development. I completed a LangChain retrieval practical and explored LlamaStack installation, CLI commands, distributions and provider configuration.
2. LangChain Implementation
I completed the following tasks:
- Installed LangChain and its required integrations in a separate Python 3.14 virtual environment (day3-venv).
- Loaded corpus/rag-introduction.txt using TextLoader.
- Split the document with RecursiveCharacterTextSplitter.
- Set the chunk size to 500 characters and overlap to 50 characters.
- Generated embeddings using sentence-transformers/all-MiniLM-L6-v2.
- Created a FAISS vector store.
- Tested semantic retrieval with the question: “What are embeddings?”
Practical result: The application loaded one document, created three chunks, built the FAISS vector store and returned two relevant results.
3. LlamaStack Exploration
I completed the following tasks:
- Installed LlamaStack 0.7.3 and LlamaStack Client 0.7.5.
- Explored the LlamaStack CLI and its available commands.
- Reviewed the built-in distributions, including Starter.
- Inspected the Starter configuration and provider settings.
- Resolved an MCP compatibility issue by installing MCP 1.30.0.
- Investigated missing optional provider dependencies, including Together and Anthropic.
Practical result: LlamaStack installation and CLI checks were successful. The Starter server encountered missing optional provider dependencies, which I investigated by reviewing its dependency list and configuration.
4. Challenges and Solutions
- Missing Python packages: Investigated the missing provider dependencies reported during Starter startup.
- MCP compatibility: Installed MCP 1.30.0 to resolve the CLI compatibility issue.
- Provider configuration: Inspected the Starter configuration to understand its inference, embedding, vector storage and other providers.
5. What I Learned
- How to load and split documents for retrieval.
- How Hugging Face embeddings represent text numerically.
- How FAISS stores vectors and supports similarity search.
- How LangChain connects loaders, splitters, embeddings and vector stores.
- How LlamaStack uses distributions, providers, CLI commands and configuration files.
6. Screenshots and Evidence
The Day 3 screenshots are stored in diagrams/day3/:
Screenshot	Description
01-langchain-application-code.png	LangChain application code
02-llamastack-starter-configuration.png	LlamaStack Starter configuration
03-llamastack-provider-configuration.png	LlamaStack provider configuration


7. Day 3 Outcome
I successfully implemented and tested document retrieval with LangChain using Hugging Face embeddings and FAISS. I also installed LlamaStack, verified its CLI and explored its distributions, dependencies and provider configuration.

Day 3 Completed Successfully.