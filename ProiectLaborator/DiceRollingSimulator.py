import tkinter as tk  # Importăm Tkinter pentru crearea interfeței grafice
from random import randint  # Importăm randint pentru a genera numere aleatorii pentru zaruri
from PIL import Image, ImageTk  # Importăm PIL pentru manipularea imaginilor
import pygame  # Importăm pygame pentru a reda sunetul

# Inițializăm pygame pentru redarea sunetului
pygame.mixer.init()  # Pregătim mixer-ul Pygame pentru a reda fișiere audio

# Funcția care simulează aruncarea zarurilor
def roll_dice():
    try:
        # Obținem numărul de zaruri introdus de utilizator
        num_dice = int(dice_entry.get())  # Convertim valoarea din câmpul de input într-un număr întreg

        # Verificăm dacă numărul de zaruri este valid
        if num_dice <= 0:
            result_label.config(text="Introduceți un număr valid de zaruri!", fg="red", bg="black")
            return
        if num_dice > 5:
            result_label.config(text="Numărul maxim de zaruri este 5!", fg="red", bg="black")
            return
    except ValueError:  # Dacă inputul nu este un număr valid
        result_label.config(text="Vă rugăm să introduceți un număr valid!", fg="red", bg="black")
        return

    # Redăm sunetul de zaruri care se rostogolesc
    pygame.mixer.music.load("dice-sound.mp3")  # Încarcă fișierul audio
    pygame.mixer.music.play()  # Redă sunetul

    # Simulăm aruncarea zarurilor
    dice_results = [randint(1, 6) for _ in range(num_dice)]  # Generăm un număr aleatoriu între 1 și 6 pentru fiecare zar

    # Ștergem rezultatele anterioare (imaginile de zaruri)
    for img in dice_images:
        canvas.delete(img)

    dice_images.clear()  # Resetează lista de imagini de zaruri

    # Calculăm lățimea totală a zarurilor pe ecran pentru a le poziționa corect
    total_width = num_dice * 100 + (num_dice - 1) * 20

    # Calculăm offset-ul pentru a centra zarurile pe canvas
    x_offset = (700 - total_width) // 2  # 700 este lățimea canvas-ului

    # Afișăm fiecare imagine a zarului pe canvas
    for i, result in enumerate(dice_results):
        dice_image = Image.open(f"photo/face{result}.jpg")  # Deschidem imaginea corespunzătoare valorii zarului
        dice_image = dice_image.resize((100, 100), Image.Resampling.LANCZOS)  # Redimensionăm imaginea
        dice_photo = ImageTk.PhotoImage(dice_image)  # Converim imaginea într-un format utilizabil în Tkinter

        # Adăugăm imaginea pe canvas
        dice_img = canvas.create_image(x_offset + i * 120, 400, image=dice_photo)
        dice_images.append(dice_photo)  # Păstrăm referința la imagine pentru a evita eliberarea acesteia
        canvas.image = dice_photo  # Menținem referința pentru a preveni eliberarea imaginii din memorie

    total = sum(dice_results)  # Calculăm suma totală a valorilor zarurilor

    # Construim textul de rezultat pentru a-l afișa în etichetă
    result_text = f"Ați aruncat zarurile: {', '.join(map(str, dice_results))}\n"
    result_text += f"Suma totală: {total}"

    # Actualizăm textul etichetei pentru a arăta rezultatele
    result_label.config(text=result_text, fg="gold", bg="gray")


# Crearea ferestrei principale
root = tk.Tk()  # Creăm fereastra principală
root.title("Dice Rolling Simulator")  # Setăm titlul ferestrei
root.geometry("600x550")  # Setăm dimensiunea ferestrei

# Setăm un canvas pentru fundal și interfața grafică
canvas = tk.Canvas(root, width=600, height=550)  # Creăm un canvas cu dimensiunile specificate
canvas.pack(fill="both", expand=True)  # Adăugăm canvas-ul în fereastra principală

# Încercăm să încărcăm imaginea de fundal
try:
    bg_image = Image.open("photo/background.jpg")  # Încercăm să deschidem imaginea de fundal
    bg_image = bg_image.resize((600, 550), Image.Resampling.LANCZOS)  # Redimensionăm imaginea pentru a se potrivi cu dimensiunile ferestrei
    bg_photo = ImageTk.PhotoImage(bg_image)  # Converim imaginea într-un format compatibil cu Tkinter
    # Setăm imaginea de fundal pe canvas
    canvas.create_image(0, 0, image=bg_photo, anchor="nw")
except Exception as e:  # Dacă apare o eroare la încărcarea imaginii
    print(f"Eroare la încărcarea imaginii de fundal: {e}")
    result_label.config(text="Nu s-a putut încărca imaginea de fundal.", fg="red", bg="black")

# Eticheta pentru titlul aplicației
title_label = tk.Label(root, text="Dice Rolling Simulator", font=("Comic Sans Ms", 25, "bold"), fg="black", bg="#FFD700", relief="ridge")
canvas.create_window(300, 50, window=title_label)  # Adăugăm eticheta pe canvas

# Eticheta pentru a solicita numărul de zaruri
dice_label = tk.Label(root, text="Număr de zaruri (1-5):", font=("Courier New", 22, "bold"), fg="gold", bg="#000000", relief="groove")
canvas.create_window(300, 140, window=dice_label)  # Adăugăm eticheta pe canvas

# Câmpul de input pentru numărul de zaruri
dice_entry = tk.Entry(root, font=("Arial", 22), relief="solid")
canvas.create_window(300, 225, window=dice_entry)  # Adăugăm câmpul de input pe canvas

# Funcțiile pentru efectele de hover și apăsare pe buton
def on_enter(event):  # Schimbă culoarea butonului când cursorul este deasupra
    roll_button.config(bg="white")

def on_leave(event):  # Revine la culoarea originală când cursorul părăsește butonul
    roll_button.config(bg="gray")

def on_press(event):  # Schimbă stilul butonului când este apăsat
    roll_button.config(relief="sunken", font=("Courier New", 20, "bold"), bg="#16A085")

def on_release(event):  # Revine la stilul original când este eliberat
    roll_button.config(relief="raised", font=("Courier New", 20, "bold"), bg="#F1C40F")

# Crearea butonului pentru a arunca zarurile
roll_button = tk.Button(root, text="Aruncă zarurile", font=("Courier New", 20, "bold"), command=roll_dice, bg="#F1C40F", fg="black", relief="raised")
roll_button.bind("<Enter>", on_enter)  # Legăm funcțiile de efectele de hover
roll_button.bind("<Leave>", on_leave)
roll_button.bind("<ButtonPress-1>", on_press)  # Legăm funcțiile de apăsare
roll_button.bind("<ButtonRelease-1>", on_release)
canvas.create_window(300, 300, window=roll_button)  # Adăugăm butonul pe canvas

# Eticheta pentru a arăta rezultatul aruncării zarurilor
result_label = tk.Label(root, text="Introduceți numărul de zaruri și apăsați pe buton!", font=("Courier New", 12), fg="gold", bg="#000000", relief="raised", padx=10, pady=10)
canvas.create_window(300, 490, window=result_label)  # Adăugăm eticheta pe canvas

# Lista pentru a păstra imaginile zarurilor
dice_images = []  # Lista va conține referințele la imaginile zarurilor afișate pe canvas

# Rulăm aplicația
root.mainloop()  # Începe bucla principală Tkinter pentru a rula aplicația
