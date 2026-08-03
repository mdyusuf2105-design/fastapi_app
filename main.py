from fastapi import FastAPI

app = FastAPI(
    title="FastAPI Backend",
    version="1.0.0"
)


@app.get("/health")
def health():
    return {
        "status": "Healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "1.0.0"
    }
