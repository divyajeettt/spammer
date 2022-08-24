import pyautogui
import time


def read() -> str:
    """reads and returns contents of the file"""
    
    with open("spamtext.txt") as f:
        text: str = f.read().split()
    return text


def main() -> None:
    """__main__ function"""
    
    start: int = int(input("Enter the starting countdown: "))
    interval: int = int(input("Enter the interval between each word: "))

    # The program starts after start seconds, to switch to another app
    time.sleep(start)

    for word in text:
        pyautogui.typewrite(word)
        pyautogui.press("enter", interval=0) # interval between each word


if __name__ == "__main__":
    main()
