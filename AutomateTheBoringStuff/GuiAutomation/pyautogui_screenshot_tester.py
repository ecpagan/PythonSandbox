import os
import pyautogui

#example with windows calculator, screenshot a key and cut only one key in an image
os.system('calc.exe')
pyautogui.screenshot('screenshot_example.png')
key_to_press = pyautogui.locateCenterOnScreen('7_key_win_calc.png')
pyautogui.moveTo(key_to_press, duration=1)
pyautogui.click(key_to_press)
