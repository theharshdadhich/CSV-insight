from fastapi import FastAPI
from routes import upload, ask, plot

app = FastAPI(title="CSV Insight API")

# Include different routers
app.include_router(upload.router)
app.include_router(ask.router)
app.include_router(plot.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)