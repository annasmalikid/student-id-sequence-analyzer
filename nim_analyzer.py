def proses_nim():
    print("=== NIM ANALYZER TOOL ===\n")

    raw_input = input("Masukkan NIM Anda (contoh: 312310520): ")
    
    if not raw_input.isdigit():
        print("Error: Harap masukkan hanya angka!")
        return

    nim_list = [int(x) for x in raw_input]
    
    print(f"\nData List Asli: {nim_list}")
    print("-" * 40)

   try:
        print(f"1. Digit ke-4 (Index 3)      : {nim_list[3]}")
        print(f"2. Digit ke-2 s/d Terakhir   : {nim_list[1:]}")
        print(f"3. Digit Terakhir (Index -1) : {nim_list[-1]}")
    except IndexError:
        print("Error: NIM terlalu pendek untuk operasi ini.")
        return

    print("\n--- Manipulasi Data ---")
    nim_list[3] = 0 
    print(f"4. Setelah Index 3 diubah ke 0 : {nim_list}")

    total_angka = sum(nim_list)
    print(f"5. Jumlah total digit (Sum)    : {total_angka}")

    nim_sorted = sorted(nim_list)
    print(f"6. Digit diurutkan (Ascending) : {nim_sorted}")

    nim_reversed = nim_list[::-1]
    print(f"7. Digit dibalik (Reverse)     : {nim_reversed}")

    nim_string_baru = "".join(map(str, nim_list))
    print(f"\nNIM Baru (String Format)       : {nim_string_baru}")

if __name__ == "__main__":
    proses_nim()
