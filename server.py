from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI(debug=True)

@app.get("/")
def home():
    print("hmmm")
    with open("template/home.html", "r") as file:
        content = file.read().strip()
    return HTMLResponse(content, 200)

@app.websocket("/ws")
async def ws_chat(websocket: WebSocket):
    await websocket.accept()
    print("Connected")

    # while True:
    #     print("Connected.")
    #     data = await websocket.receive_text()
    #     await websocket.send_text(data)
