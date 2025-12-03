import tkinter as tk
from tkinter import messagebox
import threading
import time

class AlarmIstirahat:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Waktu Istirahat")
        self.root.geometry("450x220")
        self.root.resizable(False, False)
        self.root.configure(bg="#890AB3")


        self.running = False
        self.detik_sisa = 0

        # Label Judul
        tk.Label(root, text="Alarm Waktu Bekerja/Waktu Istirahat", 
                 font=("Century", 14, "bold")).pack(pady=5)

        # Input menit
        frame_input = tk.Frame(root)
        frame_input.pack(pady=5)

        tk.Label(frame_input, text="Durasi (menit): ", font=("Century", 12)).pack(side="left")
        self.entry_menit = tk.Entry(frame_input, width=5, font=("Century", 12))
        self.entry_menit.pack(side="left")

        # Label countdown
        self.label_countdown = tk.Label(root, text="Timer: 00:00",
                                        font=("Arial", 16), fg="red")
        self.label_countdown.pack(pady=10)

        # Tombol
        frame_button = tk.Frame(root)
        frame_button.pack(pady=10)

        tk.Button(frame_button, text="Start", width=10,
                  command=self.start_alarm).pack(side="left", padx=5)

        tk.Button(frame_button, text="Stop", width=10,
                  command=self.stop_alarm).pack(side="left", padx=5)

    def start_alarm(self):
        if self.running:
            return

        try:
            menit = int(self.entry_menit.get())
            self.detik_sisa = menit * 60
        except:
            messagebox.showwarning("Input Salah", "Masukkan angka menit yang valid!")
            return

        self.running = True
        thread = threading.Thread(target=self.countdown)
        thread.daemon = True
        thread.start()

    def stop_alarm(self):
        self.running = False
        self.label_countdown.config(text="Timer: 00:00")

    def countdown(self):
        while self.running and self.detik_sisa > 0:
            menit = self.detik_sisa // 60
            detik = self.detik_sisa % 60
            self.label_countdown.config(text=f"Timer: {menit:02d}:{detik:02d}")
            time.sleep(1)
            self.detik_sisa -= 1

        if self.running:
            self.running = False
            self.alarm_selesai()

    def alarm_selesai(self):
        # bunyi beep 5x
        for _ in range(5):
            print('\a')
            time.sleep(0.3)

        messagebox.showinfo("Waktunya Istirahat",
                            "⏰ Alarm selesai!\nSaatnya ambil waktu istirahat.")

        self.label_countdown.config(text="Timer: 00:00")


# Jalankan aplikasi
root = tk.Tk()
app = AlarmIstirahat(root)
root.mainloop()
