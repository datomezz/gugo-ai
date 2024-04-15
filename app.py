# IDEAS
# 1) AI should always run or delay 1 second.
# 2) It analize the whole situation on the screen 


# I should teach AI how to 
# I should teach AI how to 
# I should teach AI how to resize width
# I should teach AI how to resize height
# 

# STEPS
# First Task is asked (TASKS should be pre-defined categories and you just have to pick your option)
# APP takes screen of entire screen

# I should give GPT only few type of actions, so it would be in boundries. All AI actions would be proceed by these actions.
# First I take a screenshot o

import pyautogui

mouseInitPosition = 0, 0

screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position() 
pyautogui.moveTo(mouseInitPosition)
print('hello world', currentMouseX, currentMouseY)
# pyautogui.click('test1.png')
im1 = pyautogui.screenshot()
im2 = pyautogui.screenshot('my_screenshot.png')