Tugas Akhir Percobaan 3

Judul Program : Sistem Pencarian Kode Barang Minimarket (Searching)

Program ini adalah aplikasi Command Line Interface (CLI) yang mendemonstrasikan implementasi algoritma pencarian (searching) dalam struktur data array (list). Pencarian merupakan operasi krusial untuk menemukan posisi sekumpulan data tertentu secara efisien. Dalam program ini, diterapkan dua jenis algoritma pencarian. Pertama, algoritma Sequential Search yang menggunakan metode brute force untuk memeriksa setiap elemen satu per satu dari awal hingga akhir, yang sangat cocok untuk kondisi data yang masih acak. Kedua, algoritma Binary Search yang menggunakan pendekatan divide and conquer (membagi dua ruang pencarian pada setiap iterasi) yang berjalan jauh lebih cepat (kompleksitas logaritmik), namun mensyaratkan data harus diurutkan terlebih dahulu sebelum dicari. 

Source Code :

<img width="3456" height="6400" alt="Snippet (1)" src="https://github.com/user-attachments/assets/6cf865f2-982f-4870-ac60-582fc55723d3" />


1. Mendefinisikan fungsi seq_search dengan parameter arr (array) dan target (nilai yang dicari).
2. Memulai perulangan for dari indeks 0 hingga batas panjang array (len(arr)).
3. Melakukan pengecekan apakah elemen array pada indeks ke-i sama dengan nilai target.
4. Jika sama, kembalikan nilai i (indeks di mana target ditemukan) dan hentikan fungsi.
5. Jika perulangan selesai dan target tidak ditemukan, kembalikan nilai -1 sebagai tanda gagal.
6. 
7. Mendefinisikan fungsi bin_search dengan parameter arr dan target.
8. Menetapkan variabel low dengan nilai 0 (indeks awal pencarian).
9. Menetapkan variabel high dengan nilai panjang array dikurangi 1 (indeks akhir pencarian).
10. Memulai perulangan while yang berjalan selama batas low tidak melewati batas high (low <= high).
11. Menghitung nilai tengah (mid) dengan menjumlahkan low dan high lalu dibagi 2 (pembagian bulat).
12. Mengecek apakah nilai elemen pada indeks mid sama dengan target.
13. Jika sama, kembalikan indeks mid karena data berhasil ditemukan.
14. Jika nilai elemen di indeks mid lebih kecil dari target, geser batas low ke mid + 1 (buang sisi kiri).
15. Kondisi else jika nilai elemen di indeks mid lebih besar dari target.
16. Geser batas high ke mid - 1 (buang sisi kanan).
17. Jika perulangan while habis dan target tidak ditemukan, kembalikan nilai -1.
18. 
19. Mendefinisikan fungsi menu untuk menampilkan antarmuka pilihan ke terminal.
20. Mencetak judul menu sistem.
21. Mencetak opsi 1 (Input).
22. Mencetak opsi 2 (Sequential Search).
23. Mencetak opsi 3 (Binary Search).
24. Mencetak opsi 0 (Keluar).
25. 
26. Mendefinisikan fungsi utama (main) tempat berjalannya logika sistem.
27. Mendeklarasikan list kosong bernama data untuk menampung input kode barang.
28. Membuat variabel running bernilai True sebagai pengontrol jalannya perulangan utama.
29. Memulai perulangan while selama nilai running adalah True.
30. Memanggil fungsi menu() agar tampil di layar.
31. Meminta input pilihan menu dari user.
32. 
33. Mengecek jika user memilih menu '1'.
34. Meminta user menginputkan jumlah barang yang akan dimasukkan.
35. Memulai perulangan for sebanyak jumlah barang tersebut.
36. Meminta user menginputkan kode barang satu per satu.
37. Memasukkan nilai kode tersebut ke dalam list data menggunakan fungsi append().
38. 
39. Mengecek jika user memilih menu '2'.
40. Meminta input kode yang ingin dicari secara Sequential.
41. Memanggil fungsi seq_search, mengirimkan list data dan nilai cari, lalu menyimpan hasilnya di variabel idx.
42. Mengecek apakah nilai idx bukan -1 (artinya ditemukan).
43. Mencetak pesan berhasil beserta letak indeks dari kode tersebut.
44. Kondisi else jika idx bernilai -1.
45. Mencetak pesan bahwa kode tidak ditemukan.
46. 
47. Mengecek jika user memilih menu '3'.
48. Memanggil fungsi .sort() bawaan Python untuk mengurutkan list data secara otomatis, karena Binary Search mewajibkan data terurut.
49. Mencetak kondisi data yang sudah berhasil diurutkan ke layar agar user dapat melihat perubahannya.
50. Meminta input kode yang ingin dicari secara Binary.
51. Memanggil fungsi bin_search dan menyimpan hasil indeksnya di variabel idx.
52. Mengecek apakah nilai idx bukan -1 (artinya ditemukan).
53. Mencetak pesan berhasil beserta letak indeks dari kode tersebut pada data yang sudah diurutkan.
54. Kondisi else jika idx bernilai -1.
55. Mencetak pesan bahwa kode tidak ditemukan.
56. 
57. Mengecek jika user memilih menu '0'.
58. Mengubah nilai running menjadi False agar perulangan while berhenti.
59. Mencetak pesan penutup bahwa sistem ditutup.
60. 
61. Kondisi else untuk menangani input menu yang tidak sesuai (misal: huruf atau angka di luar 0-3).
62. Mencetak pesan error "Menu tidak valid".
63. 
64. Mengecek apakah file Python ini dieksekusi sebagai program utama.
65. Memanggil fungsi main() untuk mengeksekusi program.

Output :

Menu 1 (Input Kode Barang)
--- SISTEM PENCARIAN KODE BARANG ---
1. Input Data Kode
2. Sequential Search (Data Acak)
3. Binary Search (Auto-Sort)
0. Keluar
Pilih menu: 1
Jumlah barang: 5
Kode ke-1: 405
Kode ke-2: 102
Kode ke-3: 305
Kode ke-4: 100
Kode ke-5: 130

<img width="356" height="271" alt="image" src="https://github.com/user-attachments/assets/ab63a350-e22f-483a-917c-6da3bf2aecd3" />


Menu 2 (Sequential Search)
Pilih menu: 2
Cari kode (Sequential): 100
Sukses! Kode 301 ditemukan pada indeks ke-3

<img width="479" height="188" alt="image" src="https://github.com/user-attachments/assets/1883cc40-080a-4986-8a4d-1abaf46ff50b" />


Menu 3 (Binary Search)
Pilih menu: 3
Data diurutkan terlebih dahulu: [100, 102, 130, 305, 405]
Cari kode (Binary): 405
Sukses! Kode 509 ditemukan pada indeks ke-4.

<img width="532" height="214" alt="image" src="https://github.com/user-attachments/assets/ce7aea82-fb98-434b-b431-9916e14a8151" />


Menu 0 (Keluar)
<img width="353" height="193" alt="image" src="https://github.com/user-attachments/assets/4bf21788-980b-4115-a5a2-db92ea7efb18" />


Link : [https://youtu.be/[MASUKKAN LINK YOUTUBEMU DI SINI]](https://youtu.be/4wQqVYaMomw)
