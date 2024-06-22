import pyperclip
import subprocess
import webbrowser
import pyautogui as auto
import time
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
webbrowser.get('chrome').open('mail.google.com/mail/u/0/#inbox?compose=new')
time.sleep(1)
auto.hotkey('alt', 'tab')
print("a: AAAAAAAAAAAAAAAA\nb: BBBBBBBBBBBBBBBBB\nc: CCCCCCCCCCCCCCCCCCCC\nd: DDDDDDDDDDDDDDDDDDDDDDD\ne: EEEEEEEEEEEEEEEEEEEEEEE")
choice = input("choose option: ")
if choice.lower() == 'a':
    file_path = "C:/Users/Gage/Desktop/python_shit/textdocs/test.txt"
elif choice.lower() == 'b':
    file_path = "C:/Users/Gage/Desktop/python_shit/textdocs/test2.txt"
elif choice.lower() == 'c':
    file_path = "C:/Users/Gage/Desktop/python_shit/textdocs/test3.txt"
elif choice.lower() == 'd':
    file_path = "C:/Users/Gage/Desktop/python_shit/textdocs/test4.txt"
elif choice.lower() == 'e':
    file_path = "C:/Users/Gage/Desktop/python_shit/textdocs/test5.txt"
with open(file_path, 'r') as file:
    contents = file.read()
pyperclip.copy(contents)

print("contents copied")
auto.hotkey('alt', 'tab')
time.sleep(1)
for i in range(2):
    auto.hotkey('tab')
auto.hotkey('ctrl', 'v')