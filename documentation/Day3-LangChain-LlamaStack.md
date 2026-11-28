&#x20;Day 3 – LangChain and LlamaStack



Date: 27 November 2026  

Status:Completed – Core Implementation and Testing



&#x20;1. Overview



Today, I explored and implemented practical RAG workflows using LangChain and LlamaStack. The focus was on understanding document ingestion, text splitting, embeddings, vector databases, semantic retrieval, framework configuration and tool integration.



I successfully implemented document retrieval with both frameworks using the same sample document and the `all-MiniLM-L6-v2` embedding model.



&#x20;2. LangChain Implementation



I completed the following tasks:



\- Installed LangChain and its required integrations in a separate Python 3.14 virtual environment (`day3-venv`).

\- Loaded `corpus/rag-introduction.txt` using `TextLoader`.

\- Split the document using `RecursiveCharacterTextSplitter`.

\- Configured a chunk size of 500 characters and an overlap of 50 characters.

\- Generated embeddings using `sentence-transformers/all-MiniLM-L6-v2`.

\- Created a FAISS vector store.

\- Tested semantic retrieval using the question: "What are embeddings?"

\- Implemented and tested a calculator tool using LangChain.



Practical Results:



\- Successfully loaded one document.

\- Created three text chunks.

\- Generated embeddings and created the FAISS vector store.

\- Retrieved two relevant results for the test question.

\- Successfully tested the calculator tool, which returned `100` for `25 \* 4`.



3\. LlamaStack Implementation



I completed the following tasks:



\- Installed LlamaStack 0.7.3 and LlamaStack Client 0.7.5.

\- Explored LlamaStack CLI commands, distributions and available APIs.

\- Inspected the Starter configuration and provider settings.

\- Installed missing dependencies required for server startup, including MCP 1.30.0, Together, Anthropic, chardet and pypdf.

\- Configured the `all-MiniLM-L6-v2` embedding model.

\- Registered the embedding model with a dimension of 384.

\- Configured FAISS as the vector database provider.

\- Created a vector store named `rag-survey-store`.

\- Uploaded `corpus/rag-introduction.txt` to LlamaStack.

\- Attached the document to the vector store.

\- Tested semantic retrieval through the LlamaStack API.



Practical Results:



\- LlamaStack server started successfully on port 8321.

\- API health check returned HTTP 200 OK.

\- The MiniLM embedding model was successfully registered.

\- The FAISS vector store was created successfully.

\- Document upload and attachment returned HTTP 200 OK.

\- Document processing completed successfully.

\- Retrieval returned relevant content from `rag-introduction.txt`.



The retrieval test used the question:



"What are embeddings?"



The result returned a similarity score of approximately 0.8185.



&#x20;4. Challenges and Solutions



| Challenge | Solution |

|---|---|

| Missing Python dependencies | Installed the required missing packages. |

| MCP compatibility issue | Installed MCP 1.30.0. |

| Embedding model registration issue | Updated the Starter configuration to register MiniLM with 384 dimensions. |

| Port 8321 already in use | Identified and stopped the previous server process before restarting. |

| Unsupported CLI commands | Inspected the installed CLI and used supported Python SDK methods. |

| LangChain agent missing OpenAI credentials | Tested the calculator tool independently without requiring an API key. |

| Vector store model identification | Used the fully qualified registered model ID. |



5\. What I Learned



\- How to load and prepare documents for RAG applications.

\- How text chunking improves document retrieval.

\- How Hugging Face embedding models convert text into numerical vectors.

\- How FAISS stores embeddings and supports similarity search.

\- How LangChain connects document loaders, splitters, embeddings and vector stores.

\- How to implement and test tools using LangChain.

\- How LlamaStack uses distributions, providers, APIs and configuration files.

\- How to register embedding models and create vector stores in LlamaStack.

\- How to upload documents and perform semantic retrieval through APIs.



6\. Screenshots and Practical Evidence



All Day 3 screenshots are saved in `diagrams/day3/`.



| Screenshot file | Description |

llama-cli-and-version-check.png` | Llama CLI and version checks |

llama-cli-help.png` | LlamaStack CLI commands and help |

llamastack-api-health.png` | Successful LlamaStack API health check |

llamastack-api-list.png` | Available LlamaStack APIs |

llamastack-configuration.png` | LlamaStack Starter configuration |

llamastack-dependency-installation.png` | Installation of required dependencies |

llamastack-distributions.png` | Available LlamaStack distributions |

llamastack-document-upload-and-retrieval.png` | Document upload and retrieval evidence |

llamastack-embedding-model-registration.png` | MiniLM embedding model registration |

llamastack-installation.png` | LlamaStack installation evidence |

llamastack-provider-list.png` | Available LlamaStack providers |

llamastack-server-start.png` | Successful LlamaStack server startup |



Additional LangChain evidence:



langchain/test\_agent.py` – Calculator tool implementation and test.

\-langchain/app.py` – LangChain retrieval implementation.



7\. Framework Comparison



| Feature | LangChain | LlamaStack |



| Installation | Successful | Successful |

| Document ingestion | Successful | Successful |

| Embedding model | all-MiniLM-L6-v2 | all-MiniLM-L6-v2 |

| Embedding dimension | 384 | 384 |

| FAISS vector store | Successful | Successful |

| Semantic retrieval | Successful | Successful |

| Tool testing | Calculator tool tested | Tool execution not completed |

| Full LLM answer generation | Not tested | Not tested |



&#x20;8. Scope Limitations



The practical implementation focused on document ingestion, embedding generation, vector storage, semantic retrieval and basic tool testing.



Full LLM answer generation was not implemented during this phase. LlamaStack tool execution was also not completed.



The LangChain calculator test verified tool execution independently; it did not establish successful autonomous agent execution.



&#x20;9. Day 3 Outcome



Day 3 provided practical experience with two important RAG frameworks: LangChain and LlamaStack.



I successfully implemented document retrieval using the same sample document and embedding model in both frameworks. I also tested LangChain calculator tool integration and configured LlamaStack with FAISS for document ingestion and retrieval.



The practical results, troubleshooting steps and screenshots have been documented for future reference and comparison.



Day 3 Completed Successfully – Core Implementation and Testing.

