def insertion_sort_asc(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def exchange_sort_desc(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp

def menu():
    print("\n SISTEM PENGURUTAN HARGA BARANG")
    print("1. Input Harga\n2. Urutkan Termurah (Asc)\n3. Urutkan Termahal (Desc)\n0. Keluar")

def main():
    harga = []
    running = True
    while running:
        menu()
        pilih = input("Pilih menu: ")
        if pilih == '1':
            jum = int(input("Jumlah barang: "))
            for i in range(jum):
                val = int(input(f"Harga barang ke-{i+1}: Rp "))
                harga.append(val)
        elif pilih == '2':
            insertion_sort_asc(harga)
            print(f"Harga Termurah -> Termahal: {harga}")
        elif pilih == '3':
            exchange_sort_desc(harga)
            print(f"Harga Termahal -> Termurah: {harga}")
        elif pilih == '0':
            running = False
            print("Sistem ditutup. Terima kasih!")
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()