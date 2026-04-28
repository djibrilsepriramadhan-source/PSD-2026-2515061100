Tugas Akhir Percobaan 1

Judul Program : Sistem Manajemen Daftar Bacaan Buku

Program ini berfungsi sebagai sistem manajemen data yang dirancang untuk memudahkan pengguna dalam melakukan pencatatan dan pemantauan daftar bacaan buku secara terstruktur. Dengan menyediakan fitur utama seperti input data buku, penghapusan buku yang telah selesai dibaca, serta tampilan laporan daftar bacaan, program ini membantu meningkatkan efisiensi pendataan. Algoritma dan struktur data yang diterapkan dalam program ini adalah Doubly Linked List, di mana setiap node merepresentasikan satu data buku dan memiliki dua pointer (prev dan next) yang memungkinkan penelusuran secara dua arah. Implementasi ini menggunakan teknik manipulasi pointer untuk menyisipkan dan menghapus data tanpa perlu menggeser elemen lain di dalam memori, yang kemudian dikombinasikan dengan mekanisme perulangan (looping) untuk menyajikan data dalam format antrean yang sistematis dan mudah dibaca.

Source Code :

[MASUKKAN SCREENSHOT FULL KODINGAN PYTHON KAMU DI SINI]

1. Mndefinisikan class bernama Node sebagai cetak biru untuk membuat simpul data
2. Mndefinisikan fungsi inisialisasi (__init__) untuk class Node dengan parameter judul dan penulis
3. Menyimpan argumen judul ke dalam atribut self.judul
4. Menyimpan argumen penulis ke dalam atribut self.penulis
5. Mengatur pointer prev (sebelumnya) menjadi none
6. Mengatur pointer next (selanjutnya) menjadi None
7. 
8. Mendefinisikan class DaftarBacaanDLL untuk mengelola struktur Doubly Linked List.
9. Mendefinisikan fungsi inisialisasi (__init__) untuk senarai.
10. Mengatur pointer head (kepala/awal) menjadi None karena list masih kosong.
11. Mengatur pointer tail (ekor/akhir) menjadi None.
12. 
13. Mendefinisikan fungsi tambah_akhir untuk memasukkan buku di akhir antrean.
14. Membuat instance node baru dari class Node.
15. Mengecek apakah list masih kosong (head adalah None).
16. Jika ya, head diatur menunjuk ke node baru.
17. Dan tail juga diatur menunjuk ke node baru.
18. Jika list tidak kosong (else).
19. Pointer prev dari node baru dihubungkan ke tail yang lama.
20. Pointer next dari tail lama dihubungkan ke node baru.
21. Menggeser pointer tail agar menunjuk ke node baru sebagai akhir senarai.
22. Mencetak pesan bahwa buku berhasil ditambahkan.
23. 
24. Mendefinisikan fungsi hapus_buku berdasarkan judul yang dicari.
25. Mengatur variabel current dimulai dari head untuk penelusuran.
26. Memulai perulangan selama current tidak bernilai None.
27. Mengecek apakah judul pada current sama dengan judul yang dicari (mengabaikan huruf besar/kecil).
28. Mengecek apakah node yang akan dihapus berada di posisi head.
29. Jika ya, geser head ke node selanjutnya.
30. Jika head baru ada isinya, putus pointer prev-nya menjadi None.
31. Jika head baru kosong (list habis), atur tail menjadi None juga.
32. Mengecek apakah node yang akan dihapus berada di posisi tail.
33. Jika ya, geser tail ke node sebelumnya.
34. Putus pointer next pada tail yang baru menjadi None.
35. Jika node yang akan dihapus berada di tengah (bukan head dan tail).
36. Sambungkan pointer next dari node sebelumnya ke node sesudahnya (melompati node target).
37. Sambungkan pointer prev dari node sesudahnya ke node sebelumnya.
38. Mencetak pesan bahwa buku telah sukses dihapus.
39. Menghentikan fungsi dengan return.
40. Menggeser current ke node selanjutnya untuk iterasi perulangan.
41. Mencetak pesan bahwa buku tidak ditemukan jika perulangan selesai tanpa hasil.
42. 
43. Mendefinisikan fungsi tampilkan_maju untuk mencetak daftar buku dari awal ke akhir.
44. Mencetak header pembatas daftar bacaan.
45. Mengatur variabel current dimulai dari head.
46. Mengatur variabel urutan dimulai dari angka 1.
47. Memulai perulangan selama current tidak bernilai None.
48. Mencetak nomor urut, judul buku, dan penulisnya menggunakan format string.
49. Menggeser current ke node selanjutnya.
50. Menambah nilai urutan sebanyak 1.
51. 
52. Mendefinisikan fungsi bernama menu untuk menampilkan daftar pilihan ke layar.
53. Mencetak daftar opsi 1 (Tambah), 2 (Hapus), 3 (Lihat), dan 0 (Keluar).
54. 
55. Mendefinisikan fungsi utama (main) tempat seluruh logika inti berjalan.
56. Membuat objek/instance dari class DaftarBacaanDLL.
57. Membuat variabel running = True untuk menjaga agar perulangan program tetap berjalan.
58. Memulai perulangan utama selama variabel running bernilai True.
59. Memanggil fungsi menu yang sudah didefinisikan sebelumnya.
60. Mengambil input pilihan menu dari user.
61. Mengecek jika user memilih menu nomor 1.
62. Meminta input judul buku dari user.
63. Meminta input nama penulis dari user.
64. Memanggil fungsi tambah_akhir dengan argumen judul dan penulis.
65. Mengecek jika user memilih menu nomor 2.
66. Meminta input judul buku yang ingin dihapus.
67. Memanggil fungsi hapus_buku.
68. Mengecek jika user memilih menu nomor 3.
69. Memanggil fungsi tampilkan_maju.
70. Mengecek jika user memilih menu nomor 0.
71. Mengubah running menjadi False agar perulangan utama berhenti.
72. Mencetak pesan Program ditutup. See you next time!
73. Jika user memasukkan angka yang tidak ada di menu.
74. Mencetak pesan bahwa pilihan tidak tersedia.
75. 
76. Baris standar Python untuk memastikan fungsi main() hanya berjalan jika file ini dieksekusi langsung.
77. Memanggil fungsi utama untuk menjalankan seluruh program.


Output : Tampilan Menu
<img width="302" height="89" alt="image" src="https://github.com/user-attachments/assets/a47e6577-eb64-4d77-adc4-94765a3d4d62" />


Menu 1 (Input Data)
Pilih menu : 1
Judul Buku: Petualangan don quixote
Penulis: Miguel
Buku 'Petualangan don quixote' berhasil ditambahkan.

<img width="482" height="92" alt="image" src="https://github.com/user-attachments/assets/f0726ff2-4c18-4b3b-9d07-aa3148c1ddc4" />


Menu 3 (Lihat Daftar Bacaan)
<img width="550" height="142" alt="image" src="https://github.com/user-attachments/assets/8a0265ca-6a86-4b42-9108-ec0144d0417a" />


Menu 2 (Hapus Buku)
Pilih menu : 2
Masukkan Judul yang dihapus: bumi manusia
Buku 'bumi manusia' telah dihapus.

<img width="414" height="75" alt="image" src="https://github.com/user-attachments/assets/38dcf9c8-3255-4afb-be59-e8d2f6c57950" />


Menu 0 (Keluar)
<img width="169" height="41" alt="image" src="https://github.com/user-attachments/assets/a1bf1d2b-5033-4d2c-87dc-4a9cf0768d9a" />


Link : https://youtu.be/[MASUKKAN LINK YOUTUBEMU DI SINI]
