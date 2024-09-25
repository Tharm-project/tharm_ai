import uuid
import random
from pydantic import BaseModel
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException
from firebase_controller import Controller

app = FastAPI()

class VideoMetadata(BaseModel):
    url: str

class TextRequest(BaseModel):
    text: str


@app.post("/")
async def receive_text(text_request: TextRequest):
    try:
        text = text_request.text
        print(f"Received text: {text}")
        local_file_path = "./video_handler/1m_demo.mp4"  # Example local video file path
        storage_file_name = f"videos/{uuid.uuid4()}.mp4"  # Unique filename for Firebase
        uploaded_url = Controller.upload_video(local_file_path, storage_file_name)
        return {"video_url": uploaded_url}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))