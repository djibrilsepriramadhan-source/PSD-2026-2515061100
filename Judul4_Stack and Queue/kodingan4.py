class AntreanQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, nama):
        self.items.append(nama)
        print(f"[Info] Pelanggan '{nama}' masuk ke antrean.")

    def dequeue(self):
        if self.is_empty():
            print("[Error] Antrean masih kosong.")
            return None
        return self.items.pop(0)

    def display(self):
        if self.is_empty():
            print("Status: Antrean kosong.")
        else:
            print(f"Antrean saat ini (Depan -> Belakang): {self.items}")

class RiwayatStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, nama):
        self.items.append(nama)

    def display(self):
        if self.is_empty():
            print("Status: Riwayat panggilan kosong.")
        else:
            print("Riwayat Panggilan (Terbaru di atas):")
            for i in range(len(self.items)-1, -1, -1):
                print(f"-> {self.items[i]}")

def menu():
    print("\n=== SISTEM LAYANAN PELANGGAN ===")
    print("1. Tambah Antrean (Enqueue)")
    print("2. Panggil Pelanggan (Dequeue -> Push)")
    print("3. Lihat Antrean (Queue)")
    print("4. Lihat Riwayat (Stack)")
    print("0. Keluar")

def main():
    antrean = AntreanQueue()
    riwayat = RiwayatStack()
    running = True

    while running:
        menu()
        pilih = input("Pilih menu (0-4): ")
        
        if pilih == '1':
            nama = input("Masukkan nama pelanggan: ")
            antrean.enqueue(nama)
            
        elif pilih == '2':
            dipanggil = antrean.dequeue()
            if dipanggil is not None:
                print(f"[Panggilan] Harap menuju loket: '{dipanggil}'")
                riwayat.push(dipanggil)
                
        elif pilih == '3':
            antrean.display()
            
        elif pilih == '4':
            riwayat.display()
            
        elif pilih == '0':
            running = False
            print("Sistem layanan ditutup. Terima kasih!")
            
        else:
            print("Menu tidak valid, silakan coba lagi.")

if __name__ == "__main__":
    main()