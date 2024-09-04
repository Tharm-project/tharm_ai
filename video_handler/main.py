import vimeo

class Handler:
    def __init__(self):
        self.vimeo_client = vimeo.VimeoClient(token='', 
                                         key='', 
                                         secret='')

    def Upload_video(self):
        videoPath = "C:/Users/NEULET/Downloads/1m_video.mp4" # 영상 source 경로
        response = self.vimeo_client.upload(videoPath) 
        uri = response
        
        videoTitle = "1분 영상"
        self.vimeo_client.patch(uri, data={"name": videoTitle})  # 영상 제목 설정
        
        video_url = f"https://tharm.src.com{uri}"
        print("Uploaded Video URL: ", video_url)

if __name__ == "__main__":
    controller = Handler()
    controller.Upload_video()