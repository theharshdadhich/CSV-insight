from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import polars as pl  # Use Polars instead of Pandas
import ollama
from pydantic import BaseModel
import matplotlib.pyplot as plt
import io
import base64

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
async def plot_graph():
    global df
    if df is None:
        raise HTTPException(status_code=400, detail="No CSV file uploaded")
    
    try:
        # Example: Plot the first numerical column
        plt.figure()
        first_column = df.columns[0]
        plt.bar(df[first_column].to_list(), df[first_column].to_list())  # Convert Polars Series to list for plotting
        plt.title("Sample Plot")
        
        # Save plot to a bytes buffer
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        
        # Encode the plot image to base64
        image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8')
        return JSONResponse(content={"image": image_base64})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating plot: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)