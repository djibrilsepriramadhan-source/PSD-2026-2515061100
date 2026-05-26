Tugas Akhir Percobaan 5

Judul Program : Sistem Manajemen ID Produk Gudang (Binary Search Tree)

Program ini adalah aplikasi Command Line Interface (CLI) yang mengimplementasikan struktur data Binary Search Tree (BST) untuk mengelola data barang di gudang. BST merupakan struktur data pohon berakar yang memiliki aturan khusus: setiap simpul (node) memiliki nilai (ID Produk) yang lebih besar dari semua simpul di subpohon kirinya, dan lebih kecil dari semua simpul di subpohon kanannya. 

Melalui implementasi ini, pencarian (Search) ID Produk dapat berjalan sangat efisien karena beroperasi menyerupai pencarian biner, di mana ruang pencarian dibagi dua pada setiap cabangnya (kompleksitas O(log n) pada kasus rata-rata). Selain itu, program memanfaatkan algoritma penelusuran Inorder Traversal, yang secara otomatis akan membaca sisi kiri (terkecil), akar, lalu sisi kanan (terbesar). Hal ini membuat fungsi tampilan daftar produk selalu tercetak rapi secara ascending (terurut dari ID terkecil ke terbesar) tanpa perlu menjalankan algoritma sorting terpisah.

Source Code :

[MASUKKAN SCREENSHOT FULL KODINGAN PYTHON KAMU DI SINI]

1. Mendefinisikan class Node sebagai representasi simpul dalam pohon.
2. Mendefinisikan fungsi inisialisasi (__init__) untuk setiap Node baru dengan parameter id_produk dan nama_produk.
3. Menyimpan nilai argumen id_produk ke dalam atribut self.id_produk.
4. Menyimpan nilai argumen nama_produk ke dalam atribut self.nama_produk.
5. Menginisialisasi pointer anak kiri (self.left) dengan nilai None.
6. Menginisialisasi pointer anak kanan (self.right) dengan nilai None.
7. 
8. Mendefinisikan class BST_Gudang yang bertindak sebagai pengelola keseluruhan struktur pohon biner.
9. Mendefinisikan fungsi inisialisasi untuk BST.
10. Menginisialisasi atribut self.root dengan None, menandakan bahwa pohon pada awalnya masih kosong.
11. 
12. Mendefinisikan fungsi rekursif insert_data untuk menambahkan Node baru berdasarkan id_produk.
13. Mengecek jika root saat ini adalah None (titik kosong tempat node baru harus disisipkan).
14. Mengembalikan objek Node baru yang berisi id_produk dan nama_produk sebagai daun/akar.
15. 
16. Mengecek jika id_produk yang dimasukkan lebih kecil dari nilai id_produk pada root saat ini.
17. Melakukan pemanggilan rekursif ke subpohon kiri (root.left) untuk mencari tempat sisipan di sebelah kiri.
18. Mengecek kondisi sebaliknya (elif), jika id_produk lebih besar dari id_produk pada root saat ini.
19. Melakukan pemanggilan rekursif ke subpohon kanan (root.right) untuk menyisipkan data di sebelah kanan.
20. 
21. Mengembalikan nilai root saat ini agar pohon tetap terhubung dengan benar setelah proses rekursi.
22. 
23. Mendefinisikan fungsi rekursif search_data untuk mencari data produk berdasarkan ID-nya.
24. Mengecek kondisi basis (base case): jika root mencapai None (data tidak ada).
25. Mengembalikan nilai None yang menandakan data tidak ditemukan.
26. 
27. Mengecek kondisi jika id_produk pada root saat ini sama persis dengan target_id.
28. Mengembalikan objek root tersebut karena data berhasil ditemukan.
29. 
30. Mengecek jika target_id lebih kecil dari id_produk pada root.
31. Melakukan pencarian rekursif hanya ke subpohon kiri (root.left), mengabaikan bagian kanan.
32. Kondisi else jika target_id lebih besar dari id_produk root.
33. Melakukan pencarian rekursif hanya ke subpohon kanan (root.right), mengabaikan bagian kiri.
34. 
35. Mendefinisikan fungsi inorder_traversal untuk menelusuri dan mencetak isi pohon secara rekursif.
36. Mengecek agar proses traversal hanya berjalan jika root tidak bernilai None.
37. Memanggil dirinya sendiri (rekursi) menelusuri ujung terdalam subpohon kiri (nilai terkecil).
38. Mencetak data id_produk dan nama_produk dari simpul saat ini.
39. Memanggil dirinya sendiri menelusuri subpohon kanan. Hasil akhirnya adalah data tercetak terurut.
40. 
41. Mendefinisikan fungsi menu() untuk menampilkan daftar fitur aplikasi.
42. (Baris 42-46) Mencetak teks menu interaktif: 1. Tambah, 2. Cari, 3. Tampilkan Urut, dan 0. Keluar.
43. 
44. Mendefinisikan fungsi utama main() untuk eksekusi logika.
45. Membuat objek/instance bernama bst dari class BST_Gudang().
46. Mengatur variabel running = True untuk mengontrol perulangan program utama.
47. 
48. Memulai perulangan while selama nilai running adalah True.
49. Memanggil fungsi menu().
50. Menerima input pilihan pengguna ke dalam variabel pilih.
51. 
52. Mengecek jika pengguna memilih menu 1.
53. Meminta input ID produk bertipe data integer.
54. Meminta input nama produk.
55. Memanggil bst.insert_data untuk menyisipkan data ke dalam BST dan memperbarui bst.root.
56. Mencetak pesan bahwa penambahan produk telah sukses.
57. 
58. Mengecek jika pengguna memilih menu 2.
59. Meminta input target ID produk yang ingin dicari di gudang.
60. Memanggil fungsi bst.search_data() dan menyimpan return value-nya di variabel hasil.
61. Mengecek jika variabel hasil tidak bernilai None (data ditemukan).
62. Mencetak pesan keberhasilan lengkap dengan nama produk yang dicari.
63. Kondisi else (jika hasil adalah None).
64. Mencetak pesan bahwa produk dengan ID tersebut tidak ditemukan di dalam pohon.
65. 
66. Mengecek jika pengguna memilih menu 3.
67. Mengecek apakah BST masih kosong dengan melihat bst.root bernilai None.
68. Mencetak pesan peringatan jika gudang masih kosong.
69. Kondisi else jika pohon memiliki data.
70. Mencetak header daftar produk.
71. Memanggil metode inorder_traversal() dari simpul bst.root untuk mencetak data secara ascending (terurut dari ID terkecil).
72. 
73. Mengecek jika pengguna memilih menu 0.
74. Mengubah running menjadi False untuk menghentikan program.
75. Mencetak kalimat penutup program.
76. 
77. Kondisi catch-all (else) jika pengguna memasukkan angka/menu yang tidak ada di pilihan.
78. Mencetak peringatan "Menu tidak valid".
79. 
80. Memeriksa apakah file ini dijalankan sebagai main program.
81. Mengeksekusi fungsi main().


Output :

Menu 1 (Tambah Produk - Insert)
=== SISTEM MANAJEMEN ID PRODUK (BST) ===
1. Tambah Produk (Insert)
2. Cari Produk (Search)
3. Tampilkan Semua Urut (Inorder)
0. Keluar
Pilih menu (0-3): 1
Masukkan ID Produk (Angka): 10
Masukkan Nama Produk: Laptop
[Sukses] Produk 'Laptop' dengan ID 10 ditambahkan.

[MASUKKAN SCREENSHOT SAAT KAMU MENGINPUTKAN BEBERAPA DATA ACAK DI MENU 1, misal masukkan ID: 105, 50, 200, 25]

Menu 3 (Tampilkan Semua Urut - Inorder Traversal)
Pilih menu (0-3): 3
--- DAFTAR PRODUK (Diurutkan dari ID terkecil) ---
ID: 10 | Nama: laptop
ID: 27 | Nama: mouse
ID: 30 | Nama: keyboard
ID: 26 | Nama: Monitor

[MASUKKAN SCREENSHOT SAAT MEMILIH MENU 3, BUKTIKAN BAHWA DATA MUNCUL TERURUT PADAHAL INPUTNYA ACAK]

Menu 2 (Cari Produk - Search)
Pilih menu (0-3): 2
Masukkan ID Produk yang dicari: 50
[Ditemukan] Produk ID 50 adalah 'mouse'.

[MASUKKAN SCREENSHOT SAAT MENCARI DATA MENGGUNAKAN MENU 2]

Menu 0 (Keluar)
[MASUKKAN SCREENSHOT SAAT KETIK 0 LALU PROGRAM TERTUTUP]

Link : https://youtu.be/[MASUKKAN LINK YOUTUBEMU DI SINI]
