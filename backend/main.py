from fastapi import FastAPI

app = FastAPI(title="NEXUS")


@app.get("/")
def home():
    return {
        "project": "NEXUS",
        "status": "running"
    }