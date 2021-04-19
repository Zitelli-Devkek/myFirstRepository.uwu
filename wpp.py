import pyautogui, time 


z = 1
while z<=40:
    time.sleep (4)
    pyautogui.typewrite("Por que llorabas?")
    pyautogui.press("enter")
    z= (z+1)

