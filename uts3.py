import random

def main_game():
    opsi = ["batu", "kertas", "gunting"]

    while True:
        user = input("Pilih salah satu (batu/kertas/gunting): ").lower()
        cpu = random.choice(opsi)

        if user not in opsi:
            print("Pilihan tidak dikenali. Ulangi ya.")
            continue

        print(f"Komputer memilih: {cpu}")

        if user == cpu:
            print("Hasilnya seri. Ayo coba lagi!")
            continue

        menang = (
            (user == "batu" and cpu == "gunting") or
            (user == "gunting" and cpu == "kertas") or
            (user == "kertas" and cpu == "batu")
        )

        if menang:
            print("TCH Hoki kamu!")
        else:
            print("owkdaodka isue, bot kah!")
        break

main_game()
