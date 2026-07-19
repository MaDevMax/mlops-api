import pickle
from fastapi import FastAPI

app = FastAPI()

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def root():
    return {"message": "MLOps API with pickle model", "model_loaded": True}

@app.get("/predict")
def predict(x: float):
    result = model.predict(x)
    return {"x": x, "prediction": result, "model_source": "model.pkl"}

@app.get("/health")
def health():
    return {"status": "ok"}
