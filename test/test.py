import requests
import httpx
import os
from fastapi import HTTPException

def download_video(video_url, local_path):
    try:
        response = requests.get(video_url)
        with open(local_path, 'wb') as f:
            f.write(response.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


def get_vimeo_oembed_data(video_url):
    api_endpoint = "https://vimeo.com/api/oembed.json"
    params = {'url': video_url}

    response = requests.get(api_endpoint, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "메타데이터 수신 실패"}

video_url = 'https://vimeo.com/1006101658'  # 실제 비디오 URL로 변경
oembed_data = get_vimeo_oembed_data(video_url)

print(oembed_data)


# download_video("https://vimeo.com/1006101658", "C:/Users/NEULET/Desktop/tharm_ai/test/video.avi")