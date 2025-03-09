import gradio as gr
import requests
import json
import plotly.graph_objects as go

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
    
def generate_graph(column, plot_type):
    payload = {"column": column, "plot_type": plot_type}
    response = requests.post(f"{BACKEND_URL}/plot/", data=payload)

    if response.status_code != 200:
        return "Error generating graph"

    # Convert JSON response to Plotly Figure
    fig_data = json.loads(response.text)
    fig = go.Figure(fig_data)

    return fig

def get_column_names():
    response = requests.get(f"{BACKEND_URL}/columns/")
    if response.status_code == 200:
        return response.json().get("columns", [])
    return []

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
        column_input = gr.Dropdown(choices=get_column_names(), label="Select Column for Graph")
        plot_type_input = gr.Radio(["bar", "line", "scatter", "histogram"], label="Select Graph Type")
        graph_button = gr.Button("Generate Graph")
        graph_output = gr.Plot(label="Generated Graph")

        
    upload_button.click(upload_csv, inputs=file_input, outputs=upload_output)
    ask_button.click(ask_question, inputs=question_input, outputs=answer_output)
    graph_button.click(generate_graph, inputs=[column_input, plot_type_input], outputs=graph_output)
        

demo.launch()