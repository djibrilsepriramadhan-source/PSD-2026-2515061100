Tugas Akhir Percobaan 2

Judul Program : Sistem Pengurutan Harga Barang Minimarket (Sorting)

Program ini adalah aplikasi Command Line Interface (CLI) yang berfungsi untuk memasukkan dan mengurutkan data harga barang. Dalam sistem kasir atau inventaris, kemampuan mengurutkan harga sangat krusial untuk fitur seperti "filter termurah" atau "filter termahal". Program ini mendemonstrasikan dua algoritma pengurutan (sorting) yang berbeda. Pertama, Insertion Sort digunakan untuk mengurutkan harga secara Ascending (termurah ke termahal) dengan cara menyisipkan elemen ke posisi yang tepat pada bagian array yang sudah terurut. Kedua, Exchange Sort digunakan untuk mengurutkan harga secara Descending (termahal ke termurah) dengan cara menjadikan satu elemen sebagai pivot dan membandingkannya langsung dengan seluruh elemen sisa, lalu menukarnya jika ditemukan nilai yang lebih besar.

Source Code :

[MASUKKAN SCREENSHOT FULL KODINGAN PYTHON KAMU DI SINI]

1. Mendefinisikan fungsi insertion_sort_asc untuk mengurutkan harga dari kecil ke besar.
2. Menyimpan jumlah elemen array ke dalam variabel n.
3. Memulai perulangan dari indeks ke-1 (elemen kedua) hingga akhir array.
4. Menyimpan nilai elemen saat ini ke dalam variabel sementara (temp).
5. Menginisialisasi variabel j untuk menunjuk ke indeks tepat sebelum i.
6. Memulai perulangan while selama j belum melewati batas (>= 0) dan nilai array[j] lebih besar dari temp.
7. Menggeser nilai array[j] ke kanan (ke indeks j+1) untuk memberi ruang bagi temp.
8. Mengurangi nilai j untuk mengecek elemen sebelumnya lagi.
9. Menempatkan nilai temp ke posisi yang sudah kosong (j+1).
10. 
11. Mendefinisikan fungsi exchange_sort_desc untuk mengurutkan harga dari besar ke kecil.
12. Menyimpan jumlah elemen array ke dalam variabel n.
13. Memulai perulangan luar yang berfungsi sebagai penentu indeks acuan (pivot).
14. Memulai perulangan dalam untuk membandingkan pivot dengan semua elemen di sebelah kanannya.
15. Memeriksa apakah nilai pivot saat ini (arr[i]) lebih kecil dari elemen pembanding (arr[j]).
16. Jika iya, simpan nilai arr[i] ke variabel temp.
17. Timpa nilai arr[i] dengan nilai arr[j] yang lebih besar.
18. Masukkan nilai temp ke arr[j] (proses pertukaran selesai).
19. 
20. Mendefinisikan fungsi menu() untuk menampilkan antarmuka.
21. Mencetak judul header sistem pengurutan.
22. Mencetak 4 pilihan aksi: Input, Urut Termurah, Urut Termahal, dan Keluar.
23. 
24. Mendefinisikan fungsi utama main() tempat logika dieksekusi.
25. Membuat list kosong bernama 'harga' untuk menampung data input.
26. Membuat variabel running = True sebagai pengontrol perulangan program utama.
27. Memulai perulangan while selama running bernilai True.
28. Memanggil fungsi menu() untuk ditampilkan ke layar terminal.
29. Meminta input pilihan menu dari pengguna.
30. Memeriksa jika pengguna memilih menu '1'.
31. Meminta input jumlah barang yang akan didata (integer).
32. Melakukan perulangan for sebanyak jumlah barang tersebut.
33. Meminta input harga untuk masing-masing barang satu per satu.
34. Memasukkan harga yang diinput ke dalam list 'harga' menggunakan append().
35. Memeriksa jika pengguna memilih menu '2'.
36. Memanggil fungsi insertion_sort_asc() untuk mengurutkan list harga.
37. Mencetak hasil list yang sudah terurut dari termurah ke termahal.
38. Memeriksa jika pengguna memilih menu '3'.
39. Memanggil fungsi exchange_sort_desc() untuk mengurutkan list harga.
40. Mencetak hasil list yang sudah terurut dari termahal ke termurah.
41. Memeriksa jika pengguna memilih menu '0'.
42. Mengubah status running menjadi False untuk menghentikan loop utama.
43. Mencetak pesan "Sistem ditutup. Terima kasih!".
44. Kondisi else jika user memasukkan angka selain 1, 2, 3, atau 0.
45. Mencetak peringatan "Menu tidak valid.".
46. 
47. Mengecek apakah file Python ini dieksekusi langsung sebagai program utama.
48. Menjalankan fungsi main().

Output :

Menu 1 (Input Harga)
--- SISTEM PENGURUTAN HARGA BARANG ---
1. Input Harga
2. Urutkan Termurah (Asc)
3. Urutkan Termahal (Desc)
0. Keluar
Pilih menu: 1
Jumlah barang: 5
Harga barang ke-1: Rp 15000
Harga barang ke-2: Rp 5000
Harga barang ke-3: Rp 25000
Harga barang ke-4: Rp 12000
Harga barang ke-5: Rp 8000

[MASUKKAN SCREENSHOT SAAT KAMU MENGINPUTKAN DATA DI MENU 1]

Menu 2 (Urutkan Termurah - Insertion Sort)
Pilih menu: 2
Harga Termurah -> Termahal: [5000, 8000, 12000, 15000, 25000]

[MASUKKAN SCREENSHOT SAAT KAMU MEMILIH MENU 2]

Menu 3 (Urutkan Termahal - Exchange Sort)
Pilih menu: 3
Harga Termahal -> Termurah: [25000, 15000, 12000, 8000, 5000]

[MASUKKAN SCREENSHOT SAAT KAMU MEMILIH MENU 3]

Menu 0 (Keluar)
[MASUKKAN SCREENSHOT SAAT KAMU KETIK 0]

Link : https://youtu.be/[MASUKKAN LINK YOUTUBEMU DI SINI]
