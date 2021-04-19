import pyautogui, time 

time.sleep(2);

f = open ("text.txt", "r")
for palabra in f:
    pyautogui.typewrite(palabra) 
    pyautogui.press("enter")

