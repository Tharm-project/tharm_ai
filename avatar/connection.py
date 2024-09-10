import socket
import numpy as np

def send_message(data, server_ip, server_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = (server_ip, server_port)
    
    try:
        sock.sendto(data, server_address)
        print(f"Sent message: {data}")
    finally:
        sock.close()

if __name__ == "__main__":
    server_ip = '127.0.0.1'  # Unity 서버의 IP 주소
    server_port = 2000       # Unity 서버와 동일한 포트 번호
    
    keypoints = np.load("C:/Users/NEULET/Desktop/Tharm/data/local/pose/KETI_SL_0000000001_pose.npy")

    for i in keypoints:
        print(i.shape)
        send_message(i, server_ip, server_port)

