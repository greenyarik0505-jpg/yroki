import customtkinter as ctk
import threading
import time
import keyboard
import random
import pyautogui

# ------------- Глобальные переменные -------------
key_running = False
click_running = False
afk_running = False
afk_timer_seconds = 0

selected_key = "space"
current_language = "ENG"  # "ENG", "RUS", "UKR"

# ------------- Тексты -------------
texts = {
    "ENG": {
        "auto_press":"Auto Key Press","auto_click":"Auto Clicker","anti_afk":"Anti-AFK Roblox","settings":"Settings",
        "interval":"Interval:","minutes":"Minutes:","seconds":"Seconds:","key_selected":"Selected key: ",
        "choose_key":"Choose key","start":"Start","stop":"Stop",
        "anti_afk_desc":"Anti-AFK for Roblox\nPresses Space for 1 second every 18–19 minutes",
        "theme":"Theme:","language":"Language:","next_press":"Next press in: ",
        "status":"Status: ","running":"Running","stopped":"Stopped","current":"Current: "
    },
    "RUS": {
        "auto_press":"Автонажатие","auto_click":"Автокликер","anti_afk":"Anti-AFK Roblox","settings":"Настройки",
        "interval":"Интервал:","minutes":"Минуты:","seconds":"Секунды:","key_selected":"Выбранная клавиша: ",
        "choose_key":"Выбрать клавишу","start":"Старт","stop":"Стоп",
        "anti_afk_desc":"Anti-AFK для Roblox\nНажимает пробел на 1 секунду каждые 18–19 минут",
        "theme":"Тема:","language":"Язык:","next_press":"Следующее нажатие через: ",
        "status":"Статус: ","running":"Работает","stopped":"Остановлено","current":"Текущий: "
    },
    "UKR": {
        "auto_press":"Автонажаття","auto_click":"Автоклікер","anti_afk":"Anti-AFK Roblox","settings":"Налаштування",
        "interval":"Інтервал:","minutes":"Хвилини:","seconds":"Секунди:","key_selected":"Вибрана клавіша: ",
        "choose_key":"Вибрати клавішу","start":"Старт","stop":"Стоп",
        "anti_afk_desc":"Anti-AFK для Roblox\nНатискає пробіл на 1 секунду кожні 18–19 хвилин",
        "theme":"Тема:","language":"Мова:","next_press":"Наступне натискання через: ",
        "status":"Статус: ","running":"Працює","stopped":"Зупинено","current":"Поточна: "
    }
}

tab_titles = {
    "ENG": ["Auto Key Press","Auto Clicker","Anti-AFK Roblox","Settings"],
    "RUS": ["Автонажатие","Автокликер","Anti-AFK Roblox","Настройки"],
    "UKR": ["Автонажаття","Автоклікер","Anti-AFK Roblox","Налаштування"]
}

# ------------- Функции логики -------------
def run_key(delay, key_name):
    global key_running
    while key_running:
        try:
            keyboard.press(key_name)
            time.sleep(1)   # держим 1 секунду
            keyboard.release(key_name)
        except Exception:
            pass
        for _ in range(int(delay)):
            if not key_running:
                break
            time.sleep(1)
        if not key_running:
            break

def start_key(minutes, seconds, key_name):
    global key_running
    if not key_running:
        key_running = True
        delay = minutes*60 + seconds
        threading.Thread(target=run_key, args=(delay, key_name), daemon=True).start()
        update_status_labels()

def stop_key():
    global key_running
    key_running = False
    update_status_labels()

def run_clicker(delay):
    global click_running
    while click_running:
        try:
            pyautogui.click()   # реальное кликанье мыши
        except Exception:
            # если pyautogui не доступен — молча пропускаем
            pass
        for _ in range(int(delay)):
            if not click_running:
                break
            time.sleep(1)
        if not click_running:
            break

def start_clicker(minutes, seconds):
    global click_running
    if not click_running:
        click_running = True
        delay = minutes*60 + seconds
        threading.Thread(target=run_clicker, args=(delay,), daemon=True).start()
        update_status_labels()

def stop_clicker():
    global click_running
    click_running = False
    update_status_labels()

def run_roblox_afk():
    global afk_running, afk_timer_seconds
    while afk_running:
        delay = random.randint(1080, 1140)  # 18–19 минут
        afk_timer_seconds = delay
        for _ in range(delay):
            if not afk_running:
                break
            time.sleep(1)
            afk_timer_seconds -= 1
        if not afk_running:
            break
        try:
            keyboard.press('space')
            time.sleep(1)
            keyboard.release('space')
        except Exception:
            pass

def start_roblox_afk():
    global afk_running
    if not afk_running:
        afk_running = True
        threading.Thread(target=run_roblox_afk, daemon=True).start()
        update_status_labels()

def stop_roblox_afk():
    global afk_running, afk_timer_seconds
    afk_running = False
    afk_timer_seconds = 0
    update_status_labels()

# ------------- GUI -------------
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔥 AutoMaster 3000 🔥")
app.geometry("720x580")
app.resizable(False, False)

# глобальные ссылки на динамические виджеты
tabview = None
afk_timer_label = None
status_key_label = None
status_click_label = None
status_afk_label = None
label_key = None
current_lang_label = None
language_optionmenu = None
theme_optionmenu = None

def update_status_labels():
    """Обновляет метки статусов и текущий язык."""
    try:
        lang = texts[current_language]
        if status_key_label is not None:
            status_key_label.configure(text=f"{lang['status']}{lang['running'] if key_running else lang['stopped']}")
        if status_click_label is not None:
            status_click_label.configure(text=f"{lang['status']}{lang['running'] if click_running else lang['stopped']}")
        if status_afk_label is not None:
            status_afk_label.configure(text=f"{lang['status']}{lang['running'] if afk_running else lang['stopped']}")
        if current_lang_label is not None:
            current_lang_label.configure(text=f"{texts[current_language]['current']}{current_language}")
        # OptionMenu визуально установить текущее значение
        if language_optionmenu is not None:
            try:
                language_optionmenu.set(current_language)
            except Exception:
                pass
        if theme_optionmenu is not None:
            try:
                theme_optionmenu.set(ctk.get_appearance_mode().capitalize())
            except Exception:
                pass
    except Exception:
        pass

# функция выбора клавиши (в отдельном потоке, чтобы UI не блокировался)
def choose_key_threaded(label_widget):
    def _worker():
        try:
            # подсказка
            app.after(0, lambda: label_widget.configure(text="Press any key..."))
            key = keyboard.read_key()  # блокирует поток, но не UI
            # keyboard.read_key() иногда возвращает 'space'/'shift' — OK
            global selected_key
            selected_key = key
            app.after(0, lambda: label_widget.configure(text=f"{texts[current_language]['key_selected']}{selected_key}"))
            app.after(0, update_status_labels)
        except Exception:
            app.after(0, lambda: label_widget.configure(text=f"{texts[current_language]['key_selected']}{selected_key}"))
    threading.Thread(target=_worker, daemon=True).start()

def build_ui():
    """(Re)build the whole tabview UI according to current_language"""
    global tabview, afk_timer_label, status_key_label, status_click_label, status_afk_label
    global label_key, current_lang_label, language_optionmenu, theme_optionmenu

    # удалить старый tabview
    try:
        if tabview is not None:
            tabview.destroy()
    except Exception:
        pass

    tabview = ctk.CTkTabview(app, width=700, height=520)
    tabview.pack(padx=10, pady=10)

    titles = tab_titles[current_language]
    tabview.add(titles[0])
    tabview.add(titles[1])
    tabview.add(titles[2])
    tabview.add(titles[3])

    # --- Auto Key ---
    parent = tabview.tab(titles[0])
    ctk.CTkLabel(parent, text=texts[current_language]["interval"]).pack(pady=6)
    frame_inputs = ctk.CTkFrame(parent); frame_inputs.pack(pady=6)
    ctk.CTkLabel(frame_inputs, text=texts[current_language]["minutes"]).grid(row=0,column=0,padx=5,pady=5)
    min_entry = ctk.CTkEntry(frame_inputs, width=80); min_entry.insert(0,"0"); min_entry.grid(row=0,column=1,padx=5,pady=5)
    ctk.CTkLabel(frame_inputs, text=texts[current_language]["seconds"]).grid(row=0,column=2,padx=5,pady=5)
    sec_entry = ctk.CTkEntry(frame_inputs, width=80); sec_entry.insert(0,"30"); sec_entry.grid(row=0,column=3,padx=5,pady=5)

    label_key = ctk.CTkLabel(parent, text=f"{texts[current_language]['key_selected']}{selected_key}")
    label_key.pack(pady=8)
    choose_key_btn = ctk.CTkButton(parent, text=texts[current_language]['choose_key'],
                                   command=lambda: choose_key_threaded(label_key))
    choose_key_btn.pack(pady=4)

    status_key_label = ctk.CTkLabel(parent, text=""); status_key_label.pack(pady=4)
    start_btn = ctk.CTkButton(parent, text=texts[current_language]['start'],
                              command=lambda: start_key(int(min_entry.get() or 0), int(sec_entry.get() or 0), selected_key))
    start_btn.pack(pady=6)
    stop_btn = ctk.CTkButton(parent, text=texts[current_language]['stop'], command=stop_key)
    stop_btn.pack(pady=6)

    # --- Auto Clicker ---
    parent = tabview.tab(titles[1])
    ctk.CTkLabel(parent, text=texts[current_language]["interval"]).pack(pady=6)
    frame_inputs2 = ctk.CTkFrame(parent); frame_inputs2.pack(pady=6)
    ctk.CTkLabel(frame_inputs2, text=texts[current_language]["minutes"]).grid(row=0,column=0,padx=5,pady=5)
    min_entry_c = ctk.CTkEntry(frame_inputs2, width=80); min_entry_c.insert(0,"0"); min_entry_c.grid(row=0,column=1,padx=5,pady=5)
    ctk.CTkLabel(frame_inputs2, text=texts[current_language]["seconds"]).grid(row=0,column=2,padx=5,pady=5)
    sec_entry_c = ctk.CTkEntry(frame_inputs2, width=80); sec_entry_c.insert(0,"1"); sec_entry_c.grid(row=0,column=3,padx=5,pady=5)

    status_click_label = ctk.CTkLabel(parent, text=""); status_click_label.pack(pady=4)
    start_click_btn = ctk.CTkButton(parent, text=texts[current_language]['start'],
                                    command=lambda: start_clicker(int(min_entry_c.get() or 0), int(sec_entry_c.get() or 0)))
    start_click_btn.pack(pady=6)
    stop_click_btn = ctk.CTkButton(parent, text=texts[current_language]['stop'], command=stop_clicker)
    stop_click_btn.pack(pady=6)

    # --- Anti-AFK ---
    parent = tabview.tab(titles[2])
    ctk.CTkLabel(parent, text=texts[current_language]["anti_afk_desc"], justify="center").pack(pady=8)
    afk_timer_label = ctk.CTkLabel(parent, text=""); afk_timer_label.pack(pady=6)
    status_afk_label = ctk.CTkLabel(parent, text=""); status_afk_label.pack(pady=4)
    start_afk_btn = ctk.CTkButton(parent, text=texts[current_language]['start'], command=start_roblox_afk)
    start_afk_btn.pack(pady=6)
    stop_afk_btn = ctk.CTkButton(parent, text=texts[current_language]['stop'], command=stop_roblox_afk)
    stop_afk_btn.pack(pady=6)

    # --- Settings ---
    parent = tabview.tab(titles[3])
    theme_label = ctk.CTkLabel(parent, text=texts[current_language]['theme']); theme_label.pack(pady=6)
    theme_optionmenu = ctk.CTkOptionMenu(parent, values=["Light","Dark"],
                                         command=lambda v: change_theme(v))
    theme_optionmenu.pack(pady=5)
    # выставим текущую тему
    try:
        theme_optionmenu.set(ctk.get_appearance_mode().capitalize())
    except Exception:
        pass

    language_label = ctk.CTkLabel(parent, text=texts[current_language]['language']); language_label.pack(pady=6)
    current_lang_label = ctk.CTkLabel(parent, text=f"{texts[current_language]['current']}{current_language}"); current_lang_label.pack(pady=4)
    language_optionmenu = ctk.CTkOptionMenu(parent, values=["ENG","RUS","UKR"], command=lambda v: change_language(v))
    language_optionmenu.pack(pady=5)
    # выставим текущий язык отображаемым в меню
    try:
        language_optionmenu.set(current_language)
    except Exception:
        pass

    # сохраняем widgets в globals, чтобы другие потоки могли их обновлять
    globals().update({
        "tabview": tabview,
        "afk_timer_label": afk_timer_label,
        "status_key_label": status_key_label,
        "status_click_label": status_click_label,
        "status_afk_label": status_afk_label,
        "label_key": label_key,
        "current_lang_label": current_lang_label,
        "language_optionmenu": language_optionmenu,
        "theme_optionmenu": theme_optionmenu
    })

    # обновим статусы сразу
    update_status_labels()

def change_language(lang):
    global current_language
    current_language = lang
    # пересобираем UI для корректного перевода заголовков вкладок и надписей
    build_ui()

def change_theme(mode):
    # ожидание: mode == "Light" или "Dark"
    try:
        ctk.set_appearance_mode(mode)
    except Exception:
        pass

# ------------- Обновление метки AFK -------------
def update_afk_timer_label_loop():
    while True:
        try:
            if afk_running and afk_timer_seconds and afk_timer_seconds > 0 and afk_timer_label is not None:
                minutes = afk_timer_seconds // 60
                seconds = afk_timer_seconds % 60
                afk_timer_label.configure(text=f"{texts[current_language]['next_press']}{minutes:02d}:{seconds:02d}")
            else:
                if afk_timer_label is not None:
                    afk_timer_label.configure(text="")
            update_status_labels()
        except Exception:
            pass
        time.sleep(1)

# ------------- Запуск UI и фонового таймера -------------
build_ui()
threading.Thread(target=update_afk_timer_label_loop, daemon=True).start()
app.mainloop()
