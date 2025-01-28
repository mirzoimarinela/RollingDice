import tkinter as tk
from random import randint
from PIL import Image, ImageTk

# Functia pentru a arunca zarurile
def roll_dice():
    try:
        num_dice = int(dice_entry.get())  # Obținem numărul de zaruri din câmpul de input
        if num_dice <= 0:
            result_label.config(text="Introduceți un număr valid de zaruri!", fg="red", bg="black")
            return
    except ValueError:
        result_label.config(text="Vă rugăm să introduceți un număr valid!", fg="red", bg="black")
        return

    dice_results = [randint(1, 6) for _ in range(num_dice)]  # Aruncăm zarurile
    total = sum(dice_results)  # Calculăm suma valorilor zarurilor

    # Construim textul de rezultat
    result_text = f"Ați aruncat zarurile: {', '.join(map(str, dice_results))}\n"
    result_text += f"Suma totală: {total}"

    # Actualizăm eticheta cu rezultatul
    result_label.config(text=result_text, fg="gold", bg="gray")


# Crearea ferestrei principale
root = tk.Tk()
root.title("Dice Rolling Simulator")
root.geometry("600x550")  # Setăm dimensiunea ferestrei

# Setăm o imagine de fundal
canvas = tk.Canvas(root, width=400, height=350)
canvas.pack(fill="both", expand=True)

# Încărcăm imaginea de fundal
bg_image = Image.open("../ProiectLaborator/photo/background.jpg")  # Înlocuiește cu calea către imaginea ta
bg_image = bg_image.resize((600, 550), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality downsampling
bg_photo = ImageTk.PhotoImage(bg_image)

# Setăm imaginea de fundal pe canvas
canvas.create_image(0, 0, image=bg_photo, anchor="nw")

# Eticheta titlu
title_label = tk.Label(root, text="Dice Rolling Simulator", font=("Comic Sans Ms", 25, "bold"), fg="black", bg="#FFD700", relief="ridge")
title_label_canvas = canvas.create_window(300, 50, window=title_label)

# Eticheta pentru inputul numărului de zaruri
dice_label = tk.Label(root, text=" Număr de zaruri:", font=("Courier New", 22,"bold"), fg="gold", bg="#000000", relief="groove")
dice_label_canvas = canvas.create_window(300, 140, window=dice_label)

# Câmp de input pentru numărul de zaruri
dice_entry = tk.Entry(root, font=("Arial", 22), relief="solid")
dice_entry_canvas = canvas.create_window(300, 225, window=dice_entry)

# Funcțiile pentru efectele de hover și apăsare

def on_enter(event):
    roll_button.config(bg="white")  # Culoare când mouse-ul intră pe buton

def on_leave(event):
    roll_button.config(bg="gray")  # Culoare de bază când mouse-ul părăsește butonul

def on_press(event):
    roll_button.config(relief="sunken", font=("Courier New", 20, "bold"), bg="#16A085")  # Efect de apăsare

def on_release(event):
    roll_button.config(relief="raised", font=("Courier New", 20, "bold"), bg="#F1C40F")  # Butonul revine la starea normală

# Crearea butonului pentru a arunca zarurile
roll_button = tk.Button(root, text="Aruncă zarurile", font=("Courier New", 20, "bold"), command=roll_dice, bg="#F1C40F", fg="black", relief="raised")

# Legătura cu evenimentele de hover și apăsare
roll_button.bind("<Enter>", on_enter)  # Când mouse-ul intră pe buton
roll_button.bind("<Leave>", on_leave)  # Când mouse-ul părăsește butonul
roll_button.bind("<ButtonPress-1>", on_press)  # Când butonul este apăsat
roll_button.bind("<ButtonRelease-1>", on_release)  # Când butonul este eliberat

# Adăugarea butonului pe canvas
roll_button_canvas = canvas.create_window(300, 300, window=roll_button)


# Eticheta pentru afișarea rezultatului
result_label = tk.Label(root, text="Introduceți numărul de zaruri și apăsați pe buton!", font=("Courier New", 12), fg="gold", bg="#000000", relief="raised", padx=10, pady=10)
result_label_canvas = canvas.create_window(300, 440, window=result_label)

# Rulăm aplicația
root.mainloop()
