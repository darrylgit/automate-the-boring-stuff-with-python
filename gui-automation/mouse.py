import pyautogui

width, height = pyautogui.size()

# Move mouse to position
# pyautogui.moveTo(400, 500, duration=5)

# Move mouse up 100px
# pyautogui.moveRel(0, -100)

# Get mouse position
print(pyautogui.position())

pyautogui.click(584, 99)
