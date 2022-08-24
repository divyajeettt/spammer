import pyautogui
import time


start: int = int(input("Enter the starting countdown: "))
interval: int = int(input("Enter the interval between each word: "))

# The program starts after start seconds, to switch to another app
time.sleep(start)

with open("spamtext.txt") as f:
    text: str = f.read().split()

for word in text:
    pyautogui.typewrite(word)
    pyautogui.press("enter", interval=0) # interval between each word