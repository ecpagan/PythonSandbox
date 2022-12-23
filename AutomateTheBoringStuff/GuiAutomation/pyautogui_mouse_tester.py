import pyautogui

width, height = pyautogui.size()
actual_cursor_position = pyautogui.position()
pyautogui.moveTo(10, 10, duration=1.5)
pyautogui.moveRel(200, 0, duration=2)
pyautogui.moveRel(0, -100, duration=1)
pyautogui.click(339, 38)
pyautogui.doubleClick(339, 38)
pyautogui.rightClick(339, 38)
pyautogui.click()

# to get positions easier open cmd and execute this
# import pyautogui
# pyautogui.displayMousePosition()
