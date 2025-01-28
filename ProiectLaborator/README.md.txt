# Simulator de Aruncare a Zarurilor

Aceasta este o aplicație simplă în Python care simulează aruncarea zarurilor folosind `tkinter` pentru interfața grafică și `Pillow` pentru gestionarea imaginilor. Utilizatorii pot introduce numărul de zaruri pe care doresc să le arunce (între 1 și 5), iar aplicația va afișa fețele zarurilor aruncate pe ecran. Aplicația calculează, de asemenea, suma totală a zarurilor aruncate și afișează rezultatul.

## Funcționalități
- **Simulare Aruncare Zaruri**: Utilizatorii pot arunca până la 5 zaruri deodată.
- **Fețe de Zar Aleatorii**: Fețele zarurilor sunt afișate folosind imagini (`face1.jpg`, `face2.jpg`, etc.).
- **Calculul Sumei**: Aplicația calculează suma valorilor zarurilor și afișează rezultatul.
- **Imagine de Fundal**: Se poate seta o imagine de fundal pentru fereastră.
- **Interfață Interactivă**: Butoanele își schimbă culoarea la trecerea cursorului și la clic pentru o experiență mai interactivă.

## Cerințe
- Python 3.x
- Biblioteci:
  - `tkinter` (pentru GUI)
  - `random` (pentru generarea valorilor aleatorii ale zarurilor)
  - `Pillow` (pentru gestionarea fișierelor de imagine)

### Instalare Biblioteci Necesare
Puteți instala `Pillow` folosind pip:
```
pip install pillow
```

## Cum să Rulați Aplicația

1. Clonați sau descărcați repository-ul care conține scriptul.
2. Asigurați-vă că aveți următoarele imagini în aceeași directoare cu scriptul:
    - `face1.jpg`, `face2.jpg`, `face3.jpg`, `face4.jpg`, `face5.jpg`, `face6.jpg` (fețele zarurilor)
    - `background.jpg` (imaginea de fundal pentru fereastră)
3. Rulați scriptul:
    ```bash
    python dice_rolling_simulator.py
    ```

4. Introduceți numărul de zaruri pe care doriți să le aruncați (între 1 și 5) și apăsați pe butonul "Aruncă zarurile" pentru a vedea rezultatele.

## Cum Funcționează
1. Utilizatorul introduce numărul de zaruri pe care dorește să le arunce.
2. Programul generează aruncări aleatorii de zaruri între 1 și 6 pentru fiecare zar.
3. Imaginile corespunzătoare fiecărei fețe de zar sunt afișate în fereastră.
4. Suma totală a zarurilor aruncate este calculată și afișată în partea de jos.
5. Utilizatorul poate apăsa pe butonul "Aruncă zarurile" pentru a arunca din nou zarurile.

## Exemplu de Fețe de Zar
Asigurați-vă că imaginile pentru fețele zarurilor (`face1.jpg`, `face2.jpg`, etc.) sunt disponibile în directorul de lucru. Aceste imagini vor reprezenta fețele zarurilor (fiecare imagine corespunzând unei valori a zarului, de exemplu, `face1.jpg` pentru un zar care arată 1).

## Personalizare
- **Schimbarea Imaginilor de Fundal**: Înlocuiți `background.jpg` cu imaginea de fundal dorită.
- **Fețele Zarurilor**: Modificați imaginile fețelor de zar pentru a se potrivi preferințelor dvs. Asigurați-vă că acestea sunt numite `face1.jpg`, `face2.jpg`, etc., pentru fiecare valoare între 1 și 6.

## Licență
Acest proiect este licențiat sub Licența MIT - consultați fișierul [LICENSE](LICENSE) pentru detalii.

---

### Rezolvarea Problemelor
- Dacă imaginea de fundal sau imaginile zarurilor nu se încarcă, asigurați-vă că acestea se află în directorul corect și că calea fișierului este corectă.
- Dacă aplicația nu încarcă imaginile, verificați dacă `Pillow` este instalat corect. Puteți face acest lucru rulând:
  ```bash
  pip install pillow
  ```

---
