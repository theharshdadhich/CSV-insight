import gradio as gr # type: ignore
import requests# type: ignore
import json
import plotly.io as pio# type: ignore
import plotly.graph_objects as go# type: ignore
# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000"

# Function to upload CSV
def upload_csv(file):
    if file is None:
        return "No file uploaded"

    # Open the file in binary mode
    with open(file.name, "rb") as f:
        files = {"file": (file.name, f, "text/csv")}  # ✅ Ensure correct content type
        response = requests.post(f"{BACKEND_URL}/upload/", files=files)

    return response.json().get("message", "Error uploading file")
# Function to ask a question
def ask_question(question):
    response = requests.post(f"{BACKEND_URL}/ask/", json={"question": question})
    return response.json().get("answer", "Error getting answer")


def generate_graph(x_column, y_column, plot_type):
    payload = {
        "x_column": x_column,
        "y_column": y_column,
        "plot_type": plot_type
    }

    response = requests.post(f"{BACKEND_URL}/plot/", json=payload)

    if response.status_code != 200:
        fig = go.Figure()
        fig.add_annotation(text=f"Error: {response.text}",  
                           x=0.5, y=0.5, showarrow=False, font=dict(size=20))
        return fig

    # Convert JSON response to Plotly Figure
    fig_data = response.json()
    return pio.from_json(json.dumps(fig_data))


# Gradio interface
with gr.Blocks() as demo:
    gr.Markdown("# CSV Question Answering and Visualization")
    
    # Upload CSV Tab
    with gr.Tab("Upload CSV"):
        file_input = gr.File(label="Upload CSV File")
        upload_button = gr.Button("Upload")
        upload_output = gr.Textbox(label="Upload Status")
        upload_button.click(upload_csv, inputs=file_input, outputs=upload_output)
    
    # Ask Question Tab
    with gr.Tab("Ask Question"):
        question_input = gr.Textbox(label="Enter your question")
        ask_button = gr.Button("Ask")
        answer_output = gr.Textbox(label="Answer")
        ask_button.click(ask_question, inputs=question_input, outputs=answer_output)

   # Plot Graph Tab
    with gr.Tab("Plot Graph"):
        x_column_input = gr.Textbox(label="Enter X-Axis Column Name")
        y_column_input = gr.Textbox(label="Enter Y-Axis Column Name")
        plot_type_input = gr.Radio(["bar", "line", "scatter", "histogram"], label="Select Graph Type")
        graph_button = gr.Button("Generate Graph")
        graph_output = gr.Plot(label="Generated Graph")

        graph_button.click(generate_graph, inputs=[x_column_input, y_column_input, plot_type_input], outputs=graph_output)


# Launch Gradio app
demo.launch()