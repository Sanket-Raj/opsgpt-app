# OpsGPT: GitOps-Powered LLM Inference Pipeline

**OpsGPT** is an end-to-end DevOps project that demonstrates the deployment of a lightweight Large Language Model (LLM) using modern GitOps principles. It serves a Hugging Face model via a FastAPI interface, containerized with Docker, and deployed to Kubernetes using ArgoCD for continuous delivery.

## 🚀 Project Overview

The goal of this project was to build a robust "Machine Learning Operations" (MLOps) workflow that bridges the gap between application development and Kubernetes operations.

It utilizes a **Split-Repository Strategy** to separate application source code from infrastructure manifests:
* **Application Repo:** Contains the FastAPI code, model inference logic, and Dockerfile.
* **GitOps Repo:** Contains the Kubernetes manifests (Helm/Kustomize) monitored by ArgoCD.

## 🛠️ Tech Stack

* **Language:** Python 3.9+
* **Framework:** FastAPI (for serving the API)
* **AI/ML:** Hugging Face `transformers` (Model: `SmolLM-135M` / `distilgpt2`)
* **Containerization:** Docker
* **Orchestration:** Kubernetes (K8s)
* **CI/CD:** GitHub Actions (CI) + ArgoCD (CD)
* **Version Control:** Git

## 🏗️ Architecture

The pipeline follows this workflow:
1.  **Code Push:** Code changes are pushed to the main branch of this repository.
2.  **CI Pipeline:** GitHub Actions builds the Docker image and pushes it to Docker Hub/GHCR.
3.  **Manifest Update:** The CI pipeline automatically updates the image tag in the separate *GitOps repository*.
4.  **Sync:** ArgoCD detects the change in the GitOps repo and syncs the Kubernetes cluster to the new state.

## ⚙️ Installation & Local Run

To run the inference API locally without Kubernetes:

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/opsgpt-app.git](https://github.com/YOUR_USERNAME/opsgpt-app.git)
cd opsgpt-app

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload
