from fastapi import FastAPI, Request
from transformers import pipeline
import torch
import time

app = FastAPI()

# Initialize the model (SmolLM-135M is very lightweight)
# It will run on CPU in your local Minikube environment
print("Loading model...")
generator = pipeline("text-generation", model="HuggingFaceTB/SmolLM-135M", device=-1)
print("Model loaded!")

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/generate")
async def generate(data: dict):
    prompt = data.get("prompt", "What is DevOps?")
    start_time = time.time()
    
    result = generator(prompt, max_new_tokens=50, do_sample=True)
    
    duration = time.time() - start_time
    return {
        "response": result[0]['generated_text'],
        "latency_seconds": round(duration, 4)
    }