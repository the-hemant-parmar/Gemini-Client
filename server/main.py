from model import query
from fastapi import FastAPI, Form
import uvicorn
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:4173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping")
async def ping():
    return "Hloooo, Duniya (from FastAPI)"


@app.get("/predict")
async def predict(question: str = "Hello"):
    print(question)
    result = query(question)
    return {"answer": result}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
