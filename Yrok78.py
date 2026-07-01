import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("❌⭕ Хрестики-Нолики")
        self.root.geometry("420x550")
        self.root.config(bg="#8B008B")
        
        self.current_player = "X"
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.buttons = []
        
        self._build_ui()
    
    def _build_ui(self):
        # ─── Заголовок з рахунком ───
        self.score_label = tk.Label(
            self.root,
            text=self._score_text(),
            font=("Arial", 16, "bold"),
            bg="#2c3e50", fg="white", pady=10,
        )
        self.score_label.pack()
        
        # ─── Чий хід ───
        self.turn_label = tk.Label(
            self.root,
            text="Хід: X",
            font=("Arial", 14),
            bg="#2c3e50", fg="#e74c3c", pady=5,
        )
        self.turn_label.pack()
        
        # ─── Поле 3×3 ───
        board_frame = tk.Frame(self.root, bg="#2c3e50")
        board_frame.pack(pady=10)
        
        for i in range(9):
            btn = tk.Button(
                board_frame,
                text="",
                font=("Arial", 40, "bold"),
                width=4, height=2,
                bg="#ecf0f1",
                command=lambda idx=i: self.click(idx),
            )
            btn.grid(row=i // 3, column=i % 3, padx=3, pady=3)
            self.buttons.append(btn)
        
        # ─── Кнопка рестарту ───
        reset_btn = tk.Button(
            self.root,
            text="🔄 Нова гра",
            font=("Arial", 14, "bold"),
            bg="#27ae60", fg="white",
            command=self.reset_board,
            padx=20, pady=10,
        )
        reset_btn.pack(pady=15)
        
        # ─── Скинути рахунок ───
        clear_btn = tk.Button(
            self.root,
            text="Скинути рахунок",
            font=("Arial", 10),
            bg="#7f8c8d", fg="white",
            command=self.reset_scores,
        )
        clear_btn.pack()
    
    def _score_text(self):
        return (
            f"X: {self.scores['X']}    "
            f"O: {self.scores['O']}    "
            f"Нічиї: {self.scores['Draws']}"
        )
    
    def click(self, index):
        if self.buttons[index]["text"] != "":
            return                           # клітинка зайнята
        
        # Поставити символ:
        self.buttons[index]["text"] = self.current_player
        self.buttons[index]["fg"] = "#e74c3c" if self.current_player == "X" else "#3498db"
        
        # Перевірка перемоги:
        winning_line = self._check_winner()
        if winning_line:
            self._highlight_winner(winning_line)
            self.scores[self.current_player] += 1
            self.score_label["text"] = self._score_text()
            self.root.after(1500, lambda: self._show_result(f"🎉 {self.current_player} переміг!"))
            return
        
        # Нічия:
        if self._is_board_full():
            self.scores["Draws"] += 1
            self.score_label["text"] = self._score_text()
            self.root.after(500, lambda: self._show_result("🤝 Нічия!"))
            return
        
        # Зміна гравця:
        self.current_player = "O" if self.current_player == "X" else "X"
        self.turn_label["text"] = f"Хід: {self.current_player}"
        self.turn_label["fg"] = "#e74c3c" if self.current_player == "X" else "#3498db"
    
    def _check_winner(self):
        """Повертає лінію перемоги (список з 3 індексів) або None."""
        win_combos = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],   # рядки
            [0, 3, 6], [1, 4, 7], [2, 5, 8],   # колонки
            [0, 4, 8], [2, 4, 6],              # діагоналі
        ]
        for combo in win_combos:
            a, b, c = combo
            if (self.buttons[a]["text"] == self.buttons[b]["text"] ==
                    self.buttons[c]["text"] != ""):
                return combo
        return None
    
    def _is_board_full(self):
        return all(btn["text"] != "" for btn in self.buttons)
    
    def _highlight_winner(self, combo):
        """Підсвічує переможну лінію."""
        for idx in combo:
            self.buttons[idx]["bg"] = "#f1c40f"      # жовтий
    
    def _show_result(self, message):
        messagebox.showinfo("Результат", message)
        self.reset_board()
    
    def reset_board(self):
        for btn in self.buttons:
            btn["text"] = ""
            btn["bg"] = "#ecf0f1"
        self.current_player = "X"
        self.turn_label["text"] = "Хід: X"
        self.turn_label["fg"] = "#e74c3c"
    
    def reset_scores(self):
        self.scores = {"X": 0, "O": 0, "Draws": 0}
        self.score_label["text"] = self._score_text()
        self.reset_board()


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
