from fastapi import WebSocket, APIRouter
from fastapi.responses import HTMLResponse

from messenger.chat.html_stub_dev import html

chat_ws_router = APIRouter()


@chat_ws_router.get("/")
async def get():
    return HTMLResponse(html)


@chat_ws_router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
