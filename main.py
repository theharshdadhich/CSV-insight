from fastapi import FastAPI, File, UploadFile, HTTPException, Form
from fastapi.responses import JSONResponse
import polars as pl  # Use Polars instead of Pandas
import ollama
from pydantic import BaseModel
import matplotlib.pyplot as plt
import io
import base64
import plotly.express as px
import json
app = FastAPI()

# Pydantic model for query input
class Query(BaseModel):
    question: str

# Global variable to store the uploaded CSV data
df = None

@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...)):
    global df
    try:
        # Read CSV file using Polars
        df = pl.read_csv(file.file)
        return JSONResponse(content={"message": "File uploaded successfully"})
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error processing CSV file: {str(e)}")

@app.post("/ask/")
async def ask_question(query: Query):
    global df
    if df is None:
        raise HTTPException(status_code=400, detail="No CSV file uploaded")
    
    try:
        # Use Ollama to generate a response
        response = ollama.generate(model='llama3.2', prompt = f"Answer the question based on this data:\n{df.head(5).to_pandas().to_string()}\nQuestion: {query.question}")
        answer = response['response']
        
        return JSONResponse(content={"answer": answer})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {str(e)}")

@app.post("/plot/")
async def generate_graph(column: str = Form(...), plot_type: str = Form(...)):    
    global df
    if df is None:
        raise HTTPException(status_code=400, detail="No CSV file uploaded.")
    if column not in df.columns:  
         raise HTTPException(status_code=400, detail=f"Invalid column name: {column}")
    # Convert Polars column to Pandas for Plotly compatibility
    df = df.to_pandas()
    # Select Graph Type
    if plot_type == "bar":       
        fig = px.bar(df, x=column, title=f"Bar Chart for {column}")
    elif plot_type == "line":    
        fig = px.line(df, y=column, title=f"Line Graph for {column}")
    elif plot_type == "scatter":     
        fig = px.scatter(df, x=column, y=df.columns[1], title=f"Scatter Plot for {column}")
    elif plot_type == "histogram":       
        fig = px.histogram(df, x=column, title=f"Histogram for {column}")
    else:       
        raise HTTPException(status_code=400, detail="Unsupported graph type.")
    # Convert Plotly figure to JSON
    return json.loads(fig.to_json())

@app.get("/columns/")
async def get_columns():
    global df
    if df is None:
        raise HTTPException(status_code=400, detail="No CSV file uploaded.")
    return {"columns":df.columns}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)