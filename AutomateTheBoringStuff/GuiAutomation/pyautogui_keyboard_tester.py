import pyautogui

pyautogui.click(300, 200)  # to focus
pyautogui.typewrite('#Hello world!', interval=0.2)
pyautogui.typewrite(['a', 'b', 'left', 'left', 'X', 'Y'], interval=1)

# list of all keys available:
# pyautogui.KEYBOARD_KEYS

# to press a single key
pyautogui.press('f1')
pyautogui.hotkey('ctrl', 'o')  # Ctrl + o
