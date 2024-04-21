import tkinter as tk
from tkinter import messagebox
from plyer import notification
import time


class ReminderApp:
    def __init__(self, master):
        self.master = master
        master.title("Lembrete para Beber Água")

        self.label = tk.Label(master, text="Intervalo de tempo (minutos):")
        self.label.pack()

        self.entry = tk.Entry(master)
        self.entry.pack()

        self.button = tk.Button(master, text="Começar", command=self.start_reminder)
        self.button.pack()

    def start_reminder(self):
        intervalo = int(self.entry.get())
        self.reminder_loop(intervalo)

    def reminder_loop(self, intervalo):
        while True:
            notification.notify(
                title="Hora de Beber Água!",
                message="Não se esqueça de beber água.",
                timeout=10
            )
            time.sleep(intervalo * 60)  # Convertendo para segundos


def main():
    root = tk.Tk()
    app = ReminderApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
