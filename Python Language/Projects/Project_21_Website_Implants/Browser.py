import webbrowser
import pyautogui
import time

chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
webbrowser.get(chrome_path).open("https://pyautogui.readthedocs.io/en/latest/quickstart.html")

for i in range(5):
    time.sleep(1)
    pyautogui.scroll(-100) #For Scroll Down

