import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import yt_dlp
import qrcode
from gtts import gTTS
import os
import threading

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Мій Супер Комбайн")
        self.geometry("650x550")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        self.add_tab(ImageTab(self.notebook), "🖼 Картинка")
        self.add_tab(YouTubeTab(self.notebook), "📺 YouTube")
        self.add_tab(QRTab(self.notebook), "📱 QR Код")
        self.add_tab(TTSTab(self.notebook), "🔊 Озвучка")
        
    def add_tab(self, frame, text):
        self.notebook.add(frame, text=text)

class ImageTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Перегляд зображень", font=("Arial", 14, "bold")).pack(pady=10)
        
        self.image_label = tk.Label(self, text="Натисніть кнопку, щоб вибрати файл", bg="#f0f0f0", width=40, height=10)
        self.image_label.pack(pady=10, expand=True)
        
        tk.Button(self, text="📂 Відкрити файл", command=self.load_image, bg="#e1e1e1").pack(pady=10)
        
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Images", "*.jpg *.png *.jpeg *.bmp")])
        if file_path:
            try:
                image = Image.open(file_path)
                image.thumbnail((400, 300))
                photo = ImageTk.PhotoImage(image)
                
                self.image_label.config(image=photo, text="", width=0, height=0)
                self.image_label.image = photo
            except Exception as e:
                messagebox.showerror("Помилка", f"Не вдалося відкрити:\n{e}")

class YouTubeTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Завантаження з YouTube", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self, text="Вставте посилання:").pack()
        self.url_entry = tk.Entry(self, width=50)
        self.url_entry.pack(pady=5)
        
        self.status_label = tk.Label(self, text="Готовий до роботи", fg="gray")
        self.status_label.pack(pady=10)
        
        tk.Button(self, text="📥 Завантажити", command=self.start_download, bg="#ffcccc").pack(pady=5)
        
    def start_download(self):
        url = self.url_entry.get().strip()
        if not url:
            messagebox.showwarning("Увага", "Введіть посилання!")
            return
            
        self.status_label.config(text="⏳ Завантаження... (зачекайте)", fg="orange")
        threading.Thread(target=self.download, args=(url,), daemon=True).start()
        
    def download(self, url):
        try:
            options = {"format": "best", "outtmpl": "downloads/%(title)s.%(ext)s"}
            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([url])
            self.status_label.config(text="✓ Успішно завантажено в папку downloads!", fg="green")
        except Exception as e:
            self.status_label.config(text="✗ Помилка завантаження", fg="red")
            print(e)


class QRTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Генератор QR кодів", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self, text="Введіть текст або посилання:").pack()
        self.qr_entry = tk.Entry(self, width=50)
        self.qr_entry.pack(pady=5)
        
        self.qr_image_label = tk.Label(self)
        self.qr_image_label.pack(pady=10)
        
        tk.Button(self, text="📱 Генерувати QR", command=self.generate_qr, bg="#ccffcc").pack(pady=5)
        
    def generate_qr(self):
        data = self.qr_entry.get().strip()
        if not data:
            messagebox.showwarning("Увага", "Введіть текст!")
            return
            
        qr = qrcode.QRCode(box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        img = img.resize((250, 250))
        photo = ImageTk.PhotoImage(img)
        
        self.qr_image_label.config(image=photo)
        self.qr_image_label.image = photo

class TTSTab(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        tk.Label(self, text="Озвучка тексту (Google)", font=("Arial", 14, "bold")).pack(pady=10)
        
        tk.Label(self, text="Введіть текст (українською):").pack()
        self.text_input = tk.Text(self, height=5, width=50)
        self.text_input.pack(pady=10)
        
        self.status_label = tk.Label(self, text="", fg="blue")
        self.status_label.pack(pady=5)
        
        tk.Button(self, text="🔊 Озвучити", command=self.speak, bg="#ccccff").pack(pady=5)
        
    def speak(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Увага", "Введіть текст!")
            return
            
        self.status_label.config(text="⏳ Генерація аудіо...", fg="orange")
        self.update()
        
        try:
            tts = gTTS(text=text, lang='uk')
            filename = "speech.mp3"
            tts.save(filename)
            self.status_label.config(text="▶️ Відтворення...", fg="green")
            os.startfile(filename)
        except Exception as e:
            self.status_label.config(text=f"Помилка: {e}", fg="red")

if __name__ == "__main__":
    app = App()
    app.mainloop()
