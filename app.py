from fastapi import FastAPI
from pydantic import BaseModel
from model import get_embedding

app = FastAPI()

class EmbeddingRequest(BaseModel):
    text: str

@app.post("/embed")
def embed(req: EmbeddingRequest):
    embedding = get_embedding(req.text)
    return {"embedding": embedding}