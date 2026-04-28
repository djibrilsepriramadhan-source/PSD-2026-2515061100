class Node:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
        self.prev = None
        self.next = None

class DaftarBacaanDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah_akhir(self, judul, penulis):
        new_node = Node(judul, penulis)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        print(f"Buku '{judul}' berhasil ditambahkan.")

    def hapus_buku(self, judul_dicari):
        current = self.head
        while current is not None:
            if current.judul.lower() == judul_dicari.lower():
                if current == self.head:
                    self.head = current.next
                    if self.head: self.head.prev = None
                    else: self.tail = None
                elif current == self.tail:
                    self.tail = current.prev
                    self.tail.next = None
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                print(f"Buku '{current.judul}' telah dihapus.")
                return
            current = current.next
        print("Buku tidak ditemukan.")

    def tampilkan_maju(self):
        print("DAFTAR BACAAN")
        current = self.head
        urutan = 1
        while current is not None:
            print(f"{urutan}. {current.judul} (Penulis: {current.penulis})")
            current = current.next
            urutan += 1

def menu():
    print("\n1. Tambah Buku\n2. Hapus Buku\n3. Lihat Daftar\n0. Keluar")

def main():
    dll = DaftarBacaanDLL()
    running = True
    while running:
        menu()
        pilihan = input("Pilih menu : ")
        if pilihan == '1':
            judul = input("Judul Buku: ")
            penulis = input("Penulis: ")
            dll.tambah_akhir(judul, penulis)
        elif pilihan == '2':
            judul = input("Masukkan Judul yang dihapus: ")
            dll.hapus_buku(judul)
        elif pilihan == '3':
            dll.tampilkan_maju()
        elif pilihan == '0':
            running = False
            print("Seleaiii")
        else:
            print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    main()