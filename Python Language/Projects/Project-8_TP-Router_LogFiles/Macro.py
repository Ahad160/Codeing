import pyautogui
import time
import subprocess

# Specify the full path to the Chrome executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

# Open Google Chrome
subprocess.Popen([chrome_path])

# Give some time for Chrome to open
time.sleep(5)

# Simulate pressing Alt+D to focus on the address bar
pyautogui.hotkey("alt", "d")

# Type the URL
pyautogui.typewrite("192.168.0.1")

# Press Enter
pyautogui.press("enter")

# Give some time for the page to load
time.sleep(4)
# Type "admin"
pyautogui.typewrite("admin")

# Press Enter
pyautogui.press("enter")

time.sleep(3)

pyautogui.hotkey("Esc")

# Simulate pressing "System Tool" in the menu➖➖➖➖➖➖➖➖➖➖➖➖
for i in range(0, 18):
    pyautogui.press("tab")
time.sleep(5)

pyautogui.press("enter")

# Simulate pressing "System Log"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
for i in range(0, 9):
    pyautogui.press("tab")

pyautogui.press("enter")

for i in range(0, 7):
    pyautogui.press("tab")
time.sleep(3)
# Simulate pressing To save "System Log" files
pyautogui.press("enter")
time.sleep(2)
pyautogui.typewrite("Router_Logfile.txt")  # log File Name
time.sleep(2)
pyautogui.hotkey("alt", "d")
pyautogui.typewrite("E:/")  # log File Path
pyautogui.hotkey("Esc")
pyautogui.press("enter")
pyautogui.press("enter")


# Simulate pressing "Log Out"➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖
time.sleep(5)
pyautogui.hotkey("Esc")
for i in range(0, 39):
    pyautogui.press("tab")

pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.press("enter")

# Simulate pressing "Closeing Chrome"
pyautogui.hotkey("ctrl", "w")


print("Successfully Router Logfile Download")


