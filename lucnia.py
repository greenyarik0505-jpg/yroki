import pyautogui 
import time
pyautogui.alert("Привет ето спамер для тг и тд")
while(True):
    d = pyautogui.prompt("Напишить текст (Подерживается только англ мова)").lower()
    s = pyautogui.prompt("Напишить скільки раз повторять: ").lower()
    pyautogui.alert("Нажмите enter или кнопку ok чтоби начать")
    for a in range(int(s)):
        time.sleep(1)
        pyautogui.write(d)
        pyautogui.press("Enter")