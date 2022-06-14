import pyautogui as pyautogui
import uuid
import time
import pandas as pd

list=pd.read_csv('list.csv')['links'].tolist()
#%%
def skip_2_next():
    for _ in range(20):
        pyautogui.press('tab')

# time.sleep(5)
# skip_2_next()

#%%
time.sleep(5)

pyautogui.press('tab')

pyautogui.press('right')
for x in list:
    pyautogui.write(' '+str(x))
    skip_2_next()
    pyautogui.press('right')






