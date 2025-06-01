def number_analysis():
    numbers = []
    for i in range(20):
        num = float(input(f"Masukkan angka ke-{i+1}: "))
        numbers.append(num)

    print("Nilai terkecil:", min(numbers))
    print("Nilai terbesar:", max(numbers))
    print("Total semua angka:", sum(numbers))
    print("Rata-rata:", sum(numbers) / len(numbers))

number_analysis()
