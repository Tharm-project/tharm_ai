from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random
import uuid

app = FastAPI()

# 비디오 메타데이터 모델 정의
class VideoMetadata(BaseModel):
    url: str
    title: str
    total_time: float
    width: int
    height: int
    fps: int

# 요청 데이터 모델 정의
class TextRequest(BaseModel):
    text: str

# 비디오 메타데이터 생성 함수
def generate_video_metadata(text: str) -> VideoMetadata:
    # 예시로 텍스트 길이에 따라 비디오 메타데이터를 생성
    random_width = random.randint(480, 1920)
    random_height = random.randint(320, 1080)
    random_fps = random.choice([24, 30, 60])
    random_total_time = random.uniform(10.0, 300.0)  # 10초에서 300초 사이의 비디오 길이

    return VideoMetadata(
        url=f"http://example.com/videos/{uuid.uuid4()}.mp4",  # 랜덤한 비디오 URL 생성
        title=f"Video for {text[:10]}",  # 텍스트의 앞부분을 제목으로 사용
        total_time=random_total_time,
        width=random_width,
        height=random_height,
        fps=random_fps
    )

@app.post("/")
async def receive_text(text_request: TextRequest):
    try:
        # 클라이언트로부터 받은 텍스트
        text = text_request.text
        print(f"Received text: {text}")

        # 비디오 메타데이터 생성
        video_metadata = generate_video_metadata(text)

        # 응답으로 비디오 메타데이터 반환
        return video_metadata
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))