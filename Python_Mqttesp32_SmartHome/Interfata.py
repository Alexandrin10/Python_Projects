import subprocess
import threading
import tkinter as tk
import sys

# Creare interfață grafică
root = tk.Tk()
root.title("Control Lumina")
root.geometry("300x200")  # Dimensiuni mai mari pentru fereastra

# Etichetă
label = tk.Label(root, text="Selectează modul de control al luminii:")
label.pack()

# Variabilă de tip flag pentru controlul rulării controlului vocal
continue_vocal_control = threading.Event()

# Funcție pentru controlul luminii prin gesturi
def gesturi_callback():
    subprocess_run("Gest.py")
    hide_buttons()

# Funcție pentru controlul luminii prin voce
def voce_callback():
    global continue_vocal_control
    continue_vocal_control.set()
    threading.Thread(target=subprocess_run, args=("Vocal.py",)).start()
    hide_buttons()

# Funcție pentru revenirea la alegerea modului de control
def return_callback():
    global continue_vocal_control
    continue_vocal_control.clear()
    button_gesturi.pack()
    button_voce.pack()
    button_return.pack_forget()

# Funcție pentru ieșirea din aplicație
def exit_callback():
    root.destroy()

def hide_buttons():
    button_gesturi.pack_forget()
    button_voce.pack_forget()
    button_return.pack(side=tk.LEFT)

def subprocess_run(script_name):
    # Obține calea către interpretorul Python curent
    python_path = sys.executable

    # Rulează scriptul specificat cu interpretorul Python curent
    subprocess.run([python_path, script_name])

# Stil pentru butoane
button_style = {"font": "bold", "bg": "#1e3d59", "fg": "#a0a0a0"}

# Buton pentru controlul luminii prin gesturi
button_gesturi = tk.Button(root, text="Control prin gesturi", command=gesturi_callback, **button_style)
button_gesturi.pack(pady=10)  # Adăugăm puțin spațiu între butoane

# Buton pentru controlul luminii prin voce
button_voce = tk.Button(root, text="Control prin voce", command=voce_callback, **button_style)
button_voce.pack(pady=10)  # Adăugăm puțin spațiu între butoane

# Buton pentru revenirea la alegerea modului de control
button_return = tk.Button(root, text="Return", command=return_callback, **button_style)

# Buton pentru ieșirea din aplicație
button_exit = tk.Button(root, text="Ieșire", command=exit_callback, **button_style)
button_exit.place(relx=0.5, rely=0.9, anchor=tk.CENTER)  # Poziționăm butonul în partea de jos, în centrul ferestrei

# Execuția buclei principale a interfeței grafice
root.mainloop()
