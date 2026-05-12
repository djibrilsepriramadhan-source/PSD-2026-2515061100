def seq_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def bin_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def menu():
    print("\n--- SISTEM PENCARIAN KODE BARANG ---")
    print("1. Input Data Kode")
    print("2. Sequential Search (Data Acak)")
    print("3. Binary Search (Auto-Sort)")
    print("0. Keluar")

def main():
    data = []
    running = True
    while running:
        menu()
        pilih = input("Pilih menu: ")
        
        if pilih == '1':
            jum = int(input("Jumlah barang: "))
            for i in range(jum):
                val = int(input(f"Kode ke-{i+1}: "))
                data.append(val)
                
        elif pilih == '2':
            cari = int(input("Cari kode (Sequential): "))
            idx = seq_search(data, cari)
            if idx != -1:
                print(f"Sukses! Kode {cari} ditemukan pada indeks ke-{idx}.")
            else:
                print("Gagal! Kode tidak ditemukan.")
                
        elif pilih == '3':
            data.sort()
            print(f"Data diurutkan terlebih dahulu: {data}")
            cari = int(input("Cari kode (Binary): "))
            idx = bin_search(data, cari)
            if idx != -1:
                print(f"Sukses! Kode {cari} ditemukan pada indeks ke-{idx}.")
            else:
                print("Gagal! Kode tidak ditemukan.")
                
        elif pilih == '0':
            running = False
            print("Sistem ditutup. Terima kasih!")
            
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()
