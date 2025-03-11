import ollama
import state  # ✅ Import global df

def query_llm(question):
    if state.df is None:
        raise ValueError("No CSV file uploaded.")
    
    prompt = f"Answer based on this data:\n{state.df.head(100).to_pandas().to_string()}\nQuestion: {question}"
    response = ollama.generate(model='llama3.2', prompt=prompt)
    
    return response['response']