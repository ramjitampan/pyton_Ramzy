def konversi_dari_detik():
    total_detik = int(input("Input jumlah detik: "))

    sisa_waktu = total_detik
    total_hari = sisa_waktu // 86400
    sisa_waktu = sisa_waktu % 86400

    total_jam = sisa_waktu // 3600
    sisa_waktu %= 3600

    total_menit = sisa_waktu // 60
    sisa_waktu %= 60

    print("\n--- Hasil Konversi ---")
    if total_detik >= 86400:
        print(f"{total_hari} hari, {total_jam} jam, {total_menit} menit, {sisa_waktu} detik")
    elif total_detik >= 3600:
        print(f"{total_jam} jam, {total_menit} menit, {sisa_waktu} detik")
    elif total_detik >= 60:
        print(f"{total_menit} menit, {sisa_waktu} detik")
    else:
        print(f"{total_detik} detik")

konversi_dari_detik()
