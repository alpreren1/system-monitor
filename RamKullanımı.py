import psutil
import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Sistem Monitörü")
root.geometry("300x180")



root.resizable(False, False)


ram_label = tk.Label(root, text="", width=5, anchor="w", height=5, borderwidth=3, relief="solid")
ram_label.pack(fill="both", expand=True)


cpu_label = tk.Label(root, text="", width=5, anchor="w", height=5, borderwidth=3, relief="solid")
cpu_label.pack(fill="both", expand=True)




def update_ram_label():
    ram_percent = psutil.virtual_memory().percent
    ram_label.config(text=f"RAM Kullanımı: {ram_percent}%")
    root.after(1000, update_ram_label)

update_ram_label()


def update_cpu_label():
    cpu_percent = psutil.cpu_percent()
    cpu_label.config(text=f"CPU Kullanımı: {cpu_percent}%")
    root.after(1000, update_cpu_label)

update_cpu_label()



root.mainloop()
