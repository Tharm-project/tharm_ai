import vimeo

class Handler:
    def __init__(self):
        self.vimeo_client = vimeo.VimeoClient(token='B5D004318199D43D961CCE24315804DB', 
                                              key='36a09be1adc1d074a9672dfa1b7a0d8945aebc68', 
                                              secret='Pc7xMrCGoJL68FMUz5A1smVjg2id76G1YXLVFyuhsE3XsHcx/08DZZxPYw60ds0NphC6pi8Rv4vZoIegOaKORBCU3r6nKCWzZttZB9jo19Jos5fQgKOko2uge/qUylls')

    def Upload_video(self):
        videoPath = "C:/Users/NEULET/Downloads/1m_video.mp4"  # 영상 source 경로
        response = self.vimeo_client.upload(videoPath) 
        uri = response
        
        videoTitle = "1분 영상"
        self.vimeo_client.patch(uri, data={"name": videoTitle})  # 영상 제목 설정
        
        video_url = f"https://vimeo.com{uri}"
        print("영상 업로드 완료. Video URL: ", video_url)
        
    def Delete_video(self, target_uri):
        response = self.vimeo_client.delete(target_uri)

        if response.status_code == 204:
            print(f"{target_uri} - 영상 삭제 완료")
        else:
            print(f"영상 삭제 실패. Status code: {response.status_code}")
    
    def GET_Video_info(self, uri):
        video_info = self.vimeo_client.get(uri)  # 업로드 영상 정보 가져오기

        if video_info.status_code != 200:
            print(f"Error fetching video info. Status code: {video_info.status_code}")
            return

        data = video_info.json()

        print("====== Video Metadata ======")
        print("Title:", data.get('name'))
        print("Duration (seconds):", data.get('duration'))
        print("Link:", data.get('link'))
        print("Width:", data.get('width'))
        print("Height:", data.get('height'))
        print("FPS:", data.get('fps'))
        print("Plays:", data.get('stats', {}).get('plays'))

# if __name__ == "__main__":
#     controller = Handler()
#     controller.GET_Video_info("https://vimeo.com/1006101658")
