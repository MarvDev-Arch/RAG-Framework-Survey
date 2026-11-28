# Day 3 Screenshot Evidence

Place this folder at `diagrams/day3/` in the RAG-FRAMEWORK-SURVEY project.

| File | Evidence |
|---|---|
| `llamastack-installation.png` | LlamaStack package installation |
| `llamastack-dependency-installation.png` | Dependency troubleshooting and installation |
| `llama-cli-help.png` | Llama CLI help output |
| `llama-cli-and-version-check.png` | CLI command and version-check evidence |
| `llamastack-distributions.png` | Available LlamaStack distributions |
| `llamastack-api-list.png` | APIs exposed by the Starter distribution |
| `llamastack-provider-list.png` | Available provider implementations |
| `llamastack-configuration.png` | Starter configuration inspection |
| `llamastack-embedding-model-registration.png` | all-MiniLM-L6-v2 registration/configuration |
| `llamastack-server-start.png` | LlamaStack server running on port 8321 |
| `llamastack-api-health.png` | Health endpoint returns `OK` |
| `llamastack-document-upload-and-retrieval.png` | Document upload, vector-store attachment, and retrieval test |

The configuration copy is in `llamastack/config.yaml`. It registers `all-MiniLM-L6-v2` as a 384-dimensional embedding model and sets it as the default vector-store embedding model. Review it against the installed LlamaStack version before using it outside this project environment.
