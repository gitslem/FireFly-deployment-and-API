import gradio as gr
import requests

BASE_URL = "http://127.0.0.1:5000/api/v1/namespaces/default/apis/todo_contract"

def create_task(description):
    data = {
        "method": "createTask",
        "params": {"_description": description}
    }
    res = requests.post(f"{BASE_URL}/invoke", json=data)
    return res.json()

def toggle_task(task_id):
    data = {
        "method": "toggleTask",
        "params": {"_id": int(task_id)}
    }
    res = requests.post(f"{BASE_URL}/invoke", json=data)
    return res.json()

def get_task(task_id):
    res = requests.post(f"{BASE_URL}/query", json={
        "method": "getTask",
        "params": {"_id": int(task_id)}
    })
    return res.json()

with gr.Blocks() as demo:
    with gr.Row():
        desc = gr.Textbox(label="New Task Description")
        gr.Button("Create").click(create_task, inputs=[desc], outputs="textbox")

    with gr.Row():
        task_id = gr.Number(label="Task ID")
        gr.Button("Toggle Complete").click(toggle_task, inputs=[task_id], outputs="textbox")

    with gr.Row():
        task_id2 = gr.Number(label="Task ID to Fetch")
        gr.Button("Get Task").click(get_task, inputs=[task_id2], outputs="textbox")

demo.launch()
