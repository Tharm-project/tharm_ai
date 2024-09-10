import requests

class VideoDataSender:
    def __init__(self, target_ip_port):
        self.host = f"http://{target_ip_port}/videos/ai/"
    
    def post_data(self, video_url, title, duration, width, height, fps):
        json_data = {
            "url": video_url,
            "title": title,
            "total_time": duration, 
            "width": width,
            "height": height,
            "fps": fps
        }

        try:
            response = requests.post(self.host, json=json_data)
            response.raise_for_status()  # HTTP 오류 발생 시 예외 처리
            print(response.json())
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # HTTP Error 
        except requests.exceptions.ConnectionError as conn_err:
            print(f"Connection error occurred: {conn_err}")  # connection Error
        except requests.exceptions.Timeout as timeout_err:
            print(f"Timeout error occurred: {timeout_err}")  # timeout Error

# if __name__ == "__main__":
#     uploader = VideoDataSender("114.201.19.101:44783")
#     response = uploader.post_data(
#         video_url="http://example.com/video.mp4",
#         title="Sample Video",
#         duration="5:34",
#         width="1920",
#         height="1080",
#         fps="30"
#     )
#     print(response)