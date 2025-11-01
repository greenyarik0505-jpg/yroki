# =========== PyautoGUI ваш помічник ===========

# pip install pyautogui 

# import pyautogui

# # дізнаємось розмір свого екрану
# screenWidth,screenHeight = pyautogui.size() # отримує розміри нашого екрану 
# print(f"Розмір нашого екрану {screenWidth}*{screenHeight} пікселів")

# лівий верхній кут це 0,0

# import pyautogui
# import time 

# screenWidth,screenHeight = pyautogui.size() # отримує розміри нашого екрану 

# Переміщуємо курсор в центр (плавно за 1 секунду)
# pyautogui.moveTo(screenWidth/2,screenHeight/2,duration=1)
# pyautogui.moveTo(0,screenHeight/2,duration=1)
# pyautogui.moveTo(screenWidth/2,0,duration=1)
# pyautogui.moveTo(screenWidth/2,screenHeight/2,duration=1)
# pyautogui.moveTo(screenWidth,screenHeight,duration=1)
# pyautogui.moveTo(0,0,duration=1)
# print("курсор в центрі")

# import pyautogui
# import time
# screenWidth,screenHeight = pyautogui.size() # отримує розміри нашого екрану 
# pyautogui.click()

# pyautogui.moveTo(100,200,duration=1)
# pyautogui.click()
# pyautogui.rightClick()
# pyautogui.moveTo(100,750,duration=1)
# pyautogui.doubleClick()
# pyautogui.moveTo(screenWidth/2,screenHeight/2,duration=1)
# pyautogui.doubleClick()
# print("Я клікнув в точці 100,200 ")

# import pyautogui
# import time

# time.sleep(3)

# distance = 200
# pyautogui.mouseDown() # Затиснути клавішу мишки
# pyautogui.moveRel(distance,0,duration=0.5) # рухає мишку відносно місця де ми її залишили
# pyautogui.moveRel(0,distance,duration=0.5)
# pyautogui.moveRel(-distance,0,duration=0.5)
# pyautogui.moveRel(0,-distance,duration=0.5)
# pyautogui.mouseUp()


# import pyautogui
# import time

# time.sleep(2)

# pyautogui.write("""Pryvit,svit Ya robot 3000 terminator
# Pryvit,svit Ya robot 3000 terminator
# """,interval=0.01)

# # Pryvit,svit Ya robot 3000 terminator

# import pyautogui
# import time
# time.sleep(3)

# pyautogui.hotkey("ctrl","a")
# time.sleep(1)
# pyautogui.hotkey("ctrl","c")
# pyautogui.hotkey("alt","F4")
# pyautogui.hotkey("ctrl","v")

# import pyautogui
# import time
# time.sleep(3)
# pyautogui.hotkey("ctrl","t")
# time.sleep(1)

# pyautogui.write("google.com",interval=0.5)
# pyautogui.press("enter")

# pyautogui.hotkey("alt","F4")


# import pyautogui
# pyautogui.alert("Urok завершено")
# vidpovid = pyautogui.confirm("Тобі сподобалось?",buttons=["так","Ні"])
# if vidpovid == "Tak":
#     pyautogui.alert("SUPERRRRR")
# else:
#     pyautogui.alert("Windows delete")
# im = pyautogui.screenshot("screen1.png")
# print("Скріншот у вас в папці ")

# Відкриває Paint.
# Малює щось просте (наприклад, смайлик або будиночок).
# Робить скріншот свого малюнка.
# Показує повідомлення про завершення.
import pyautogui
import time

time.sleep(3)

pyautogui.moveTo(300, 300)
pyautogui.click()
pyautogui.dragRel(100, 0, duration=0.5)
pyautogui.dragRel(0, 100, duration=0.5)
pyautogui.dragRel(-100, 0, duration=0.5)
pyautogui.dragRel(0, -100, duration=0.5)
pyautogui.moveTo(330, 330)
pyautogui.click()
pyautogui.dragRel(10, 0, duration=0.2)
pyautogui.moveTo(360, 330)
pyautogui.click()
pyautogui.dragRel(10, 0, duration=0.2)

pyautogui.moveTo(325, 360)
pyautogui.dragRel(60, 0, duration=0.5)
pyautogui.dragRel(-60, 10, duration=0.5)

time.sleep(2)
screenshot = pyautogui.screenshot()
screenshot.save("screenshot.png")

print("Малюнок завершено! Скриншот збережено як 'screenshot.png'.")