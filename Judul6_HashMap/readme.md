Tugas Akhir Percobaan 6

Judul Program : Sistem Buku Telepon Digital 

[cite_start]Program ini adalah aplikasi Command Line Interface (CLI) yang mengimplementasikan struktur data Hash Map untuk membuat sebuah sistem Buku Telepon. Hash Map adalah struktur data asosiatif yang menyimpan data dalam bentuk pasangan kunci-nilai (key-value pairs)[cite: 1998, 1999]. Pada program ini, "Nama" bertindak sebagai Kunci (Key) yang unik, dan "Nomor" bertindak sebagai Nilai (Value). [cite_start]Program memanfaatkan fungsi hash untuk menjumlahkan nilai ASCII dari karakter nama, kemudian di-modulo dengan ukuran tabel untuk menghasilkan indeks penyimpanan[cite: 2026].

Untuk menangani masalah tabrakan (Collision) di mana dua nama berbeda mungkin menghasilkan indeks yang sama, program ini menggunakan metode Separate Chaining. [cite_start]Separate chaining adalah metode penanganan tabrakan dengan cara menempatkan struktur data tambahan, yaitu Linked List, di setiap slot tabel[cite: 2045, 2046]. Hal ini memungkinkan satu indeks menyimpan lebih dari satu kontak tanpa saling menimpa, sehingga efisiensi pencarian dengan kompleksitas O(1) tetap terjaga.

Source Code :

<img width="1432" height="4396" alt="code" src="https://github.com/user-attachments/assets/b8262b0c-fc26-4d1e-9912-ac54e5d85f44" />


1. Mendefinisikan class Node untuk membuat cetak biru simpul Linked List.
2. Mendefinisikan fungsi inisialisasi (__init__) dengan parameter nama dan nomor.
3. Menyimpan argumen nama ke atribut self.nama.
4. Menyimpan argumen nomor ke atribut self.nomor.
5. Menginisialisasi pointer self.next menjadi None.
6. 
7. Mendefinisikan class BukuTelepon sebagai pengelola Hash Map.
8. Mendefinisikan fungsi inisialisasi dengan parameter ukuran default 5 (sengaja kecil agar tabrakan/collision mudah terjadi dan bisa didemonstrasikan).
9. Menyimpan ukuran tabel ke atribut self.size.
10. Membuat list kosong (tabel hash) berisi nilai None sebanyak ukuran size.
11. 
12. Mendefinisikan fungsi hash_function untuk mengonversi string nama menjadi indeks angka.
13. Menginisialisasi variabel total_ascii dengan angka 0.
14. Memulai perulangan for untuk setiap karakter di dalam string nama.
15. Menjumlahkan nilai desimal ASCII dari setiap karakter menggunakan fungsi bawaan ord().
16. Mengembalikan sisa bagi (modulo) dari total_ascii dengan ukuran tabel untuk memastikan indeks tidak melewati batas (out of bounds).
17. 
18. Mendefinisikan fungsi insert untuk menambah atau memperbarui kontak.
19. Memanggil hash_function untuk mendapatkan letak indeks dari nama.
20. Mengatur current pada tabel di indeks tersebut.
21. 
22. Memulai perulangan untuk menelusuri Linked List di slot tersebut (mengecek jika ada data lama).
23. Jika nama pada node saat ini sama dengan nama yang diinputkan (artinya kontak sudah ada).
24. Perbarui atribut nomor dengan nomor yang baru.
25. Hentikan fungsi menggunakan return.
26. Geser current ke node selanjutnya.
27. 
28. Jika nama belum ada di dalam rantai, buat objek new_node.
29. Sambungkan pointer next node baru ke head (simpul pertama) di indeks saat ini.
30. Jadikan node baru tersebut sebagai head baru (menyisipkan di awal Linked List).
31. 
32. Mendefinisikan fungsi search untuk mencari nomor telepon berdasarkan nama.
33. Mendapatkan letak indeks dari fungsi hash.
34. Mengatur current untuk menelusuri rantai di indeks tersebut.
35. 
36. Melakukan perulangan selama current tidak None.
37. Mengecek apakah kunci nama cocok.
38. Jika cocok, kembalikan nilai nomor teleponnya.
39. Geser current ke node selanjutnya jika belum cocok.
40. Mengembalikan None jika perulangan habis dan nama tidak ditemukan.
41. 
42. Mendefinisikan fungsi hapus untuk membuang kontak dari tabel.
43. Mendapatkan indeks dari fungsi hash.
44. Mengatur pointer current dan prev (awalnya None) untuk penelusuran.
45. 
46. Memulai perulangan while untuk menelusuri rantai.
47. Mengecek kecocokan nama.
48. Jika cocok, cek apakah node yang dihapus ada di paling depan (prev is None).
49. Jika ya, ubah head tabel tersebut menjadi node selanjutnya.
50. Jika tidak, sambungkan node sebelumnya (prev) langsung ke node setelahnya (melompati node target).
51. Mengembalikan True sebagai tanda sukses menghapus.
52. Memperbarui prev dengan current.
53. Menggeser current ke posisi selanjutnya.
54. Mengembalikan False jika data gagal ditemukan.
55. 
56. Mendefinisikan fungsi display untuk mencetak isi tabel hash ke layar terminal.
57. (Baris 57-64) Menelusuri setiap indeks dari 0 hingga size-1, lalu menelusuri Linked List di masing-masing indeks untuk mencetak format [Nama : Nomor] -> None.
58. 
59. Mendefinisikan fungsi utama main() untuk eksekusi CLI.
60. Membuat instance objek buku berukuran 5.
61. Mengatur variabel running = True untuk loop utama.
62. (Baris 70-76) Mencetak menu antarmuka dan meminta input pilihan.
63. 
64. Mengecek pilihan menu 1 (Insert). Meminta input lalu memanggil buku.insert().
65. Mengecek pilihan menu 2 (Search). Meminta input lalu memanggil buku.search() dan mencetak hasilnya.
66. Mengecek pilihan menu 3 (Delete). Meminta input lalu memanggil buku.hapus().
67. Mengecek pilihan menu 4 (Display). Memanggil buku.display().
68. Mengecek pilihan menu 0 (Keluar). Menghentikan loop dengan merubah running menjadi False.
69. Kondisi else jika input menu tidak sesuai.
70. Memeriksa apakah file dieksekusi sebagai main program lalu memanggil fungsi main().

Output :
<img width="339" height="221" alt="image" src="https://github.com/user-attachments/assets/738c5339-d7d2-4692-9644-d8386869ab0e" />


Menu 1 (Tambah Kontak)
=== BUKU TELEPON (HASH MAP) ===
1. Tambah/Update Kontak
2. Cari Kontak
3. Hapus Kontak
4. Lihat Semua Kontak
0. Keluar
Pilih menu: 1
Masukkan Nama: Cheisya
Masukkan Nomor: 08123456
Kontak 'Cheisya' berhasil disimpan.

<img width="397" height="161" alt="image" src="https://github.com/user-attachments/assets/f25beb30-1b25-4b3a-b92f-a80deaef56cc" />


Menu 4 
Pilih menu: 4
--- ISI HASH MAP BUKU TELEPON ---
Indeks 0: [Cheisya : 08123456] -> None
Indeks 1: [siti : 08888] ->  None
Indeks 2: None
Indeks 3: [Budi : 082288] -> None
Indeks 4: None

<img width="351" height="211" alt="image" src="https://github.com/user-attachments/assets/850e58bb-00ab-4d4f-aab8-b0b3fa6dce6e" />


Menu 2 (Cari Kontak)
Pilih menu: 2
Nama yang dicari: cheisya
Ditemukan! Nomor Yaya: 08123456

<img width="304" height="215" alt="image" src="https://github.com/user-attachments/assets/6957fe75-01e8-45b2-8c17-bf2a249b84fa" />


Menu 0 (Keluar)
<img width="315" height="173" alt="image" src="https://github.com/user-attachments/assets/b203bd22-2ba0-49d7-ba43-e9ec4af0f676" />


Link : https://youtu.be/[MASUKKAN LINK YOUTUBEMU DI SINI]
