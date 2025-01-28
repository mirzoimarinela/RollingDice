import random


def number_guessing_game():
    # Generează un număr aleator între 1 și 20
    secret_number = random.randint(1, 20)
    attempts = 5

    print("Am ales un număr între 1 și 20. Poți să-l ghicești în 5 încercări?")

    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Încercarea {attempt}/{attempts}: Introdu numărul: "))

            if guess < 1 or guess > 20:
                print("Te rog să introduci un număr între 1 și 20.")
                continue

            if guess < secret_number:
                print("Prea mic!")
            elif guess > secret_number:
                print("Prea mare!")
            else:
                print(f"Felicitări! Ai ghicit numărul {secret_number} în {attempt} încercări!")
                break
        except ValueError:
            print("Te rog să introduci un număr valid.")

    else:
        print(f"Ai rămas fără încercări. Numărul secret era {secret_number}.")


if _name_ == "_main_":
    number_guessing_game()