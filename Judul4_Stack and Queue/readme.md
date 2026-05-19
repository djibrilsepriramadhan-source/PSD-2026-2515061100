Tugas Akhir Percobaan 4

Judul Program : Sistem Layanan Pelanggan (Implementasi Stack dan Queue)

[cite_start]Program ini adalah aplikasi Command Line Interface (CLI) yang mendemonstrasikan penggunaan dua struktur data linier secara bersamaan, yaitu Queue (Antrean) dan Stack (Tumpukan)[cite: 1201, 1249]. Program ini menyimulasikan sistem pada loket layanan pelanggan (Customer Service). 

[cite_start]Konsep Queue diterapkan pada fitur "Tambah Antrean", di mana data pelanggan dimasukkan ke posisi belakang (Enqueue) dan dipanggil dari posisi paling depan (Dequeue) menggunakan prinsip First In First Out (FIFO). Sementara itu, konsep Stack diterapkan pada "Riwayat Panggilan". Setiap kali seorang pelanggan selesai dipanggil dari antrean, data mereka akan di-Push ke dalam Stack riwayat. [cite_start]Dengan menggunakan prinsip Last In First Out (LIFO), sistem dapat menampilkan daftar pelanggan yang baru saja dilayani, di mana pelanggan terakhir akan berada di posisi paling atas (Top) pada tampilan riwayat.

Source Code :

<img width="1418" height="3446" alt="code" src="https://github.com/user-attachments/assets/54819dda-60b0-46fa-a9a1-6b661768e9de" />


1. Mendefinisikan class AntreanQueue untuk mengelola struktur data Queue.
2. Mendefinisikan fungsi inisialisasi (__init__) untuk class AntreanQueue.
3. Membuat list kosong bernama items untuk menampung data antrean.
4. Mendefinisikan fungsi is_empty untuk mengecek apakah antrean kosong.
5. Mengembalikan nilai True jika panjang list items adalah 0.
6. Mendefinisikan fungsi enqueue dengan parameter nama untuk menambah antrean.
7. Menambahkan data nama ke posisi paling akhir list menggunakan fungsi append().
8. Mencetak pesan konfirmasi bahwa pelanggan berhasil masuk ke antrean.
9. Mendefinisikan fungsi dequeue untuk mengeluarkan data dari depan antrean.
10. Mengecek apakah antrean dalam kondisi kosong dengan memanggil is_empty().
11. Jika kosong, cetak pesan error.
12. Kembalikan nilai None karena tidak ada data yang bisa dikeluarkan.
13. Jika tidak kosong, keluarkan (pop) dan kembalikan elemen pada indeks ke-0 (paling depan).
14. Mendefinisikan fungsi display untuk mencetak isi Queue.
15. Mengecek apakah antrean kosong, jika ya cetak "Antrean kosong".
16. Jika tidak, cetak keseluruhan isi list dari depan ke belakang.
17. 
18. Mendefinisikan class RiwayatStack untuk mengelola struktur data Stack.
19. Mendefinisikan fungsi inisialisasi list kosong untuk items.
20. (Sama)
21. Mendefinisikan fungsi is_empty untuk Stack.
22. (Sama)
23. Mendefinisikan fungsi push dengan parameter nama untuk menambah data ke Stack.
24. Menambahkan data nama ke posisi paling atas (akhir list) menggunakan append().
25. Mendefinisikan fungsi display khusus untuk Stack.
26. Mengecek apakah Stack kosong, jika ya cetak "Riwayat kosong".
27. Jika tidak kosong, cetak header riwayat panggilan.
28. Memulai perulangan mundur (dari indeks terakhir hingga indeks ke-0) agar data terbaru tampil di atas.
29. Mencetak elemen list satu per satu dari atas ke bawah.
30. 
31. Mendefinisikan fungsi menu() untuk mencetak antarmuka CLI.
32. (Baris 32-38) Mencetak daftar opsi: Enqueue, Dequeue->Push, Lihat Queue, Lihat Stack, dan Keluar.
33. 
34. Mendefinisikan fungsi utama main() tempat logika program berjalan.
35. Membuat objek/instance antrean dari class AntreanQueue.
36. Membuat objek/instance riwayat dari class RiwayatStack.
37. Membuat variabel running = True untuk menjaga perulangan utama.
38. Memulai perulangan while selama running bernilai True.
39. Memanggil fungsi menu() ke layar.
40. Meminta input pilihan menu dari user.
41. 
42. Mengecek jika user memilih menu 1.
43. Meminta input nama pelanggan.
44. Memanggil metode enqueue() pada objek antrean dengan argumen nama tersebut.
45. 
46. Mengecek jika user memilih menu 2.
47. Memanggil metode dequeue() pada antrean dan menyimpan hasilnya di variabel dipanggil.
48. Mengecek apakah nilai dipanggil tidak sama dengan None (berhasil dikeluarkan).
49. Mencetak instruksi panggilan ke loket untuk pelanggan tersebut.
50. Memanggil metode push() pada objek riwayat untuk merekam nama pelanggan ke dalam Stack.
51. 
52. Mengecek jika user memilih menu 3.
53. Memanggil metode display() pada objek antrean.
54. 
55. Mengecek jika user memilih menu 4.
56. Memanggil metode display() pada objek riwayat.
57. 
58. Mengecek jika user memilih menu 0.
59. Mengubah running menjadi False untuk menghentikan program.
60. Mencetak pesan penutup.
61. Kondisi else jika input menu tidak sesuai, akan mencetak "Menu tidak valid".
62. 
63. Baris standar untuk menjalankan fungsi main() jika file dieksekusi langsung.

Output :

Menu 1 (Tambah Antrean / Enqueue)
=== SISTEM LAYANAN PELANGGAN ===
1. Tambah Antrean (Enqueue)
2. Panggil Pelanggan (Dequeue -> Push)
3. Lihat Antrean (Queue)
4. Lihat Riwayat (Stack)
0. Keluar
Pilih menu (0-4): 1
Masukkan nama pelanggan: Djibril
[Info] Pelanggan 'Djibril' masuk ke antrean.

<img width="424" height="186" alt="image" src="https://github.com/user-attachments/assets/5e8e8417-99d2-460c-b5a5-bbb47fd02c79" />


Menu 3 (Lihat Antrean / Queue)
Pilih menu (0-4): 3
Antrean saat ini (Depan -> Belakang): ['Cheisya', 'Aqila']

<img width="593" height="192" alt="image" src="https://github.com/user-attachments/assets/81b93cf2-d94b-4f2e-aff6-1a09c272e838" />


Menu 2 & 4 (Panggil Pelanggan & Lihat Riwayat Stack)
Pilih menu (0-4): 2
[Panggilan] Harap menuju loket: 'Djibril'

Pilih menu (0-4): 4
Riwayat Panggilan (Terbaru di atas):
-> Djibril

<img width="376" height="211" alt="image" src="https://github.com/user-attachments/assets/4debc1f7-3e25-4ef8-9f0d-eb6d2e07d056" />


Menu 0 (Keluar)
<img width="377" height="186" alt="image" src="https://github.com/user-attachments/assets/78a0eb8b-33bc-4f9f-90fe-bba191ddb3f8" />


Link : https://youtu.be/BEbmwdbo4II
