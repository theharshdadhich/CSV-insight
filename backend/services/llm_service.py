from models.response import Response
import ollama
import state  
from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai import Agent
from pydantic_ai.providers.openai import OpenAIProvider


async def query_llm(question):
    if state.df is None:
        raise ValueError("No CSV file uploaded.")
    
    prompt = f"Answer based on this data:\n{state.df.head(100).to_pandas().to_string()}\nQuestion: {question}"
    # response = ollama.generate(model='llama3.2', prompt=prompt)
    ollama_model = OpenAIModel(model_name = "llama3.2", provider=OpenAIProvider(base_url='http://localhost:11434/v1'))
    agent = Agent(ollama_model,result_type = Response)
    response = await agent.run(prompt)
    return response["answer"]