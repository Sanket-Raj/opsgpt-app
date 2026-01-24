# OpsGPT: GitOps-Driven MLOps Inference Engine

OpsGPT is a production-grade inference engine designed to serve Hugging Face LLMs (DistilGPT-2/SmolLM) with high availability and automated delivery. 

I built this project to demonstrate a **Split-Repository GitOps Strategy**, separating application source code from configuration manifests to ensure security, auditability, and clean release cycles.
# OpsGPT: GitOps MLOps Pipeline

[ Badges here: CI Status | Python 3.10 | Docker ]

## 🚀 Overview
OpsGPT is a production-ready LLM inference engine deployed via Kubernetes.

## 🛠️ Local Development
1. Install dependencies: `pip install -r requirements.txt`
2. Run server: `uvicorn app.main:app --reload`

## 🔮 Future Roadmap
- [ ] Add Redis Caching
- [ ] Implement Model Quantization

## 🏗 Architecture

```mermaid
graph LR
    A[Developer] -->|Push Code| B(opsgpt-app Repo)
    B -->|GitHub Action| C{CI Pipeline}
    C -->|Build & Test| D[Docker Registry]
    C -->|Update Tag| E(opsgpt-gitops Repo)
    E -->|Sync| F[ArgoCD]
    F -->|Deploy| G[Kubernetes Cluster]
    G -->|Scale| H[HPA]
