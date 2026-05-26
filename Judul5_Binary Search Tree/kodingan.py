class Node:
    def __init__(self, id_produk, nama_produk):
        self.id_produk = id_produk
        self.nama_produk = nama_produk
        self.left = None
        self.right = None

class BST_Gudang:
    def __init__(self):
        self.root = None

    def insert_data(self, root, id_produk, nama_produk):
        if root is None:
            return Node(id_produk, nama_produk)
        
        if id_produk < root.id_produk:
            root.left = self.insert_data(root.left, id_produk, nama_produk)
        elif id_produk > root.id_produk:
            root.right = self.insert_data(root.right, id_produk, nama_produk)
        
        return root

    def search_data(self, root, target_id):
        if root is None:
            return None
        
        if root.id_produk == target_id:
            return root
        
        if target_id < root.id_produk:
            return self.search_data(root.left, target_id)
        else:
            return self.search_data(root.right, target_id)

    def inorder_traversal(self, root):
        if root is not None:
            self.inorder_traversal(root.left)
            print(f"ID: {root.id_produk} | Nama: {root.nama_produk}")
            self.inorder_traversal(root.right)

def menu():
    print("\n=== SISTEM MANAJEMEN ID PRODUK (BST) ===")
    print("1. Tambah Produk")
    print("2. Cari Produk")
    print("3. Tampilkan Semua Urut")
    print("0. Keluar")

def main():
    bst = BST_Gudang()
    running = True

    while running:
        menu()
        pilih = input("Pilih menu (0-3): ")
        
        if pilih == '1':
            id_prod = int(input("Masukkan ID Produk (Angka): "))
            nama = input("Masukkan Nama Produk: ")
            bst.root = bst.insert_data(bst.root, id_prod, nama)
            print(f"[Sukses] Produk '{nama}' dengan ID {id_prod} ditambahkan.")
            
        elif pilih == '2':
            target = int(input("Masukkan ID Produk yang dicari: "))
            hasil = bst.search_data(bst.root, target)
            if hasil is not None:
                print(f"[Ditemukan] Produk ID {target} adalah '{hasil.nama_produk}'.")
            else:
                print(f"[Gagal] Produk dengan ID {target} tidak ditemukan.")
                
        elif pilih == '3':
            if bst.root is None:
                print("Gudang masih kosong.")
            else:
                print("\n--- DAFTAR PRODUK (Diurutkan dari ID terkecil) ---")
                bst.inorder_traversal(bst.root)
                
        elif pilih == '0':
            running = False
            print("Sistem ditutup. Terima kasih!")
            
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()