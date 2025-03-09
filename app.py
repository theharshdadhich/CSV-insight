import gradio as gr
import requests

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000"

def upload_csv(file):
    response = requests.post(f"{BACKEND_URL}/upload/", files={"file": file})
    return response.json().get("message", "Error uploading file")

def ask_question(question):
    response = requests.post(f"{BACKEND_URL}/ask/", json={"question": question})
    return response.json().get("answer", "Error getting answer")

def plot_graph():
    response = requests.post(f"{BACKEND_URL}/plot/")
    if response.status_code == 200:
        return response.json().get("image", "Error getting plot")
    else:
        return "Error generating plot"

# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# CSV Question Answering and Visualization")
    
    with gr.Tab("Upload CSV"):
        file_input = gr.File(label="Upload CSV File")
        upload_button = gr.Button("Upload")
        upload_output = gr.Textbox(label="Upload Status")
    
    with gr.Tab("Ask Question"):
        question_input = gr.Textbox(label="Enter your question")
        ask_button = gr.Button("Ask")
        answer_output = gr.Textbox(label="Answer")
    
    with gr.Tab("Plot Graph"):
        plot_button = gr.Button("Generate Plot")
        plot_output = gr.Image(label="Plot")
    
    upload_button.click(upload_csv, inputs=file_input, outputs=upload_output)
    ask_button.click(ask_question, inputs=question_input, outputs=answer_output)
    plot_button.click(plot_graph, outputs=plot_output)

demo.launch()