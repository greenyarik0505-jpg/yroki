# import pyautogui
# x , y = pyautogui.size()
# print(f"Розмір нашого екрану {x} на {y} пікселів ")
# pyautogui.moveTo(x,y,duration=1) # перейти на позицію x,y за duration часу 
# pyautogui.moveRel(x,y,duration=1) # переміститись від точки на якій вже мишка 
# pyautogui.dragRel(x,y,duration=1) # перетягнути від місця до точки
# pyautogui.mouseDown() # опустити мишку (почати перетягувати)
# pyautogui.mouseUp() # підняти мишку і перестати перетягувати

# # Клавіатурі

# pyautogui.write("Пишемо текст",interval=1) # пишемо текст з інтервалом між кожним символом 1 секунда 

# pyautogui.press("enter") # нажати клавішу

# pyautogui.hotkey("win","r") # Зажимання хоткеїв (гарячих клавіш)

# pyautogui.alert("Увага увага дякую за увагу") # просто увага 

# pyautogui.screenshot("screen.png") # зберегти скріншот у папку з кодом

import pyautogui
import time
# ПЛАН ЗАВДАННЯ
# прінти для користувача
print("Ласкаво просимо в нашу розумну програму Tun tun Programun")
while True:
    print("=======================ОБЕРІТЬ ДІЮ============================= \n 1. Відкрити YouTube \n 2. Відкрити браузер \n 3. Відкрити Блокнот \n 4. Відкрити калькулятор \n 5. Відкрити Telegram \n 6. Відкрити Visual Studio Code \n 7. Відкрити Roblox \n 8. Відкрити Viber \n 9. Відкрити Microsoft Store \n 10. Відкрити Захист Windows \n 11. Дізнатися погоду \n 12. Відкрити Провідник \n 13. Відкрити Диспетчер завдань \n 14. Відкрити Paint \n 15. Відкрити Корзину\n 16. Відкрити сайт \n 17. Зробити знімок екрану \n 18. Відкрити Календар\n 19. Відкрити Командний рядок\n 20. Відкрити Налаштування Windows")
    a =pyautogui.prompt("Обирайте дію: ").lower()  
    pyautogui.alert("Увага зараз програма почне працювати йдіть попийте чай ")
    if a == "1":
        yoteber = pyautogui.prompt("Введіть ютубера: (Якщо хочете открить просто ютуб просто нажміть enter)")
        if yoteber:
            print(f"Шукаю ютубера {yoteber}...")
            time.sleep(2)
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge", interval=0.10)
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write(f"https://www.youtube.com/@{yoteber}", interval=0.10)
            pyautogui.press("enter")
        else:
            
            pyautogui.alert("Ви не ввели ютубера! откривается просто ютуб або що у тебе в пошуку")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge", interval=0.10)
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write("https://www.youtube.com", interval=0.10)
            pyautogui.press("enter")

    if a == "2":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"msedge", interval=0.10)
        pyautogui.press("enter")
    if a == "3":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"notepad", interval=0.10)
        pyautogui.press("enter")
    if a == "4":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"calc", interval=0.10)
        pyautogui.press("enter")
    if a == "5":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"D:\Telegram Desktop\Telegram.exe", interval=0.10)
        pyautogui.press("enter")
    if a == "6":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"D:\Microsoft VS Code\Code.exe", interval=0.10)
        pyautogui.press("enter")
    if a == "7":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"roblox-player:1", interval=0.10)
        pyautogui.press("enter")
    if a == "8":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"C:\Users\%USERNAME%\AppData\Local\Viber\Viber.exe", interval=0.10)
        pyautogui.press("enter")
    if a == "9":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"ms-windows-store:", interval=0.10)
        pyautogui.press("enter")
    if a == "10":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"ms-settings:windowsdefender", interval=0.10)
        pyautogui.press("enter")
    if a == "11":
        Caut = pyautogui.prompt("Введіть назву міста, в якому хочете дізнатись погоду: (Якщо хочете щоб знайшло у вашому місті просто нажміть enter)")
        if Caut:
            print(f"Шукаю погоду в місті {Caut}...")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge")
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write(f"Weather in {Caut}", interval=0.10)
            pyautogui.press("enter")
        else:
            pyautogui.alert("Ви не ввели назву міста! Шукаю погоду у вашому місті")
            pyautogui.hotkey("win", "r")
            pyautogui.write("msedge")
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write("Weather" , interval=0.10)
            pyautogui.press("enter")
    if a == "12":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"explore", interval=0.10)
        pyautogui.press("enter")
    if a == "13":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"taskmgr", interval=0.10)
        pyautogui.press("enter")
    if a == "14":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"mspaint", interval=0.10)
        pyautogui.press("enter")
    if a == "15" :
        pyautogui.hotkey("win","r")
        pyautogui.write(r"explorer.exe shell:RecycleBinFolder", interval=0.10)
        pyautogui.press("enter")
    if a == "16" :
        Caut = pyautogui.prompt("Введіть назву сайту який хочете открить:")
        if Caut:
            print(f"Шукаю сайт {Caut}...")
            pyautogui.hotkey("win", "r")
            time.sleep(1)
            pyautogui.write("msedge")
            pyautogui.press("enter")
            time.sleep(6)
            pyautogui.write(f"https://www.{Caut}", interval=0.10)
            pyautogui.press("enter")
        else:
            pyautogui.alert("Ви не ввели сайт команда отменена!")
    if a == "17" :
        time.sleep(2)
        pyautogui.screenshot("screen.png")
    if a == "18":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"outlookcal:", interval=0.10)
        pyautogui.press("enter")
    if a == "19":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"cmd", interval=0.10)
        pyautogui.press("enter")
    if a == "20":
        pyautogui.hotkey("win","r")
        pyautogui.write(r"ms-settings:", interval=0.10)
        pyautogui.press("enter")