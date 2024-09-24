import uuid
import random
from pydantic import BaseModel
from datetime import datetime, timezone
from fastapi import FastAPI, HTTPException

app = FastAPI()

class VideoMetadata(BaseModel):
    url: str
    title: str
    total_time: float
    width: int
    height: int
    fps: int
    created_at: datetime

class TextRequest(BaseModel):
    text: str

def dummy_metadata(text: str) -> VideoMetadata:
    random_width = random.randint(480, 1920)
    random_height = random.randint(320, 1080)
    random_fps = random.choice([24, 30, 60])
    total_time = random.uniform(1.0, 300.0)
    create_time = datetime.now(timezone.utc)

    return VideoMetadata(
        url=f"http://example.com/videos/{uuid.uuid4()}.mp4",  
        title=f"Video for {text[:10]}",
        total_time=total_time,  
        width=random_width,
        height=random_height,
        fps=random_fps,  
        created_at=create_time
    )

@app.post("/")
async def receive_text(text_request: TextRequest):
    try:
        text = text_request.text
        print(f"Received text: {text}")
        video_metadata = dummy_metadata(text)

        return video_metadata.dict()  
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
