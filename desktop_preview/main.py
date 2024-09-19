import cv2
import time
import keyboard
import pywintypes
import numpy as np
import tkinter as tk
import customtkinter as ctk
import win32clipboard as wcb

from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def ImageButton_Generator(img_path, target_size, target_frame, w, h, active_bg, bg):
    source = Image.open(img_path)
    source = source.resize(target_size)
    img = ImageTk.PhotoImage(source)
    btn = tk.Button(target_frame, image=img, relief='flat', width=w, height=h, activebackground=active_bg, bg=bg)
    btn.image = img
    return btn

def change_label(target_label):
    texts = ctk.StringVar()
    texts = get_clipboard_data()
    target_label.configure(text=texts)

def get_clipboard_data():
    retry_attempts = 5
    for attempt in range(retry_attempts):
        try:
            wcb.OpenClipboard()
            texts = wcb.GetClipboardData()
            wcb.CloseClipboard()
            return texts
        except pywintypes.error as e:
            if attempt < retry_attempts - 1:
                time.sleep(0.1)  # 100ms 대기 후 재시도
            else:
                return "클립보드에 접근할 수 없습니다."
def keyboard_event_handler():
    keyboard.add_hotkey('ctrl+c', lambda: change_label(detected_label))
    root.after(1000, keyboard_event_handler)

# App Main
root = ctk.CTk()
root.title("Deep Signer")
root.resizable(False, False)
ctk.set_appearance_mode('dark')
        
# Frames
button_frame = ctk.CTkFrame(root)
button_frame.pack(side='left', expand=False, padx=20, pady=20)
frame = ctk.CTkFrame(root, corner_radius=5, width=150, height=200)
frame.pack(side='left', expand=False, padx=10, pady=20)

# Left Toolbar Button group
home_btn = ImageButton_Generator('desktop_preview/assets/home.png', (35, 35), button_frame, 35, 35, '#2b2b2b', '#2b2b2b')
home_btn.grid(row=0, column=0, padx=15, pady=40)
ttsl_btn = ImageButton_Generator('desktop_preview/assets/sign-language.png', (35, 35), button_frame, 35, 35, '#2b2b2b', '#2b2b2b')
ttsl_btn.grid(row=1, column=0, padx=15, pady=40)
setting_btn = ImageButton_Generator('desktop_preview/assets/settings.png', (35, 35), button_frame, 35, 35, '#2b2b2b', '#2b2b2b')
setting_btn.grid(row=2, column=0, padx=15, pady=40)

# sub panel
detected_label = ctk.CTkLabel(frame, text="입력된 텍스트")
detected_label.grid(row=0, column=0, padx=100, pady=240)
detected_label.configure(wraplength=250)  # 250px을 넘어가는 텍스트는 줄바꿈
                                                                                                                                                         
# canvas areas
show_canvas = ctk.CTkCanvas(root, width=400, height=630)
show_canvas.pack(side='left')

keyboard_event_handler()
root.mainloop()