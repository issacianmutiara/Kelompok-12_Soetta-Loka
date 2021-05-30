
[Soetta-Loka]
Tugas Besar Praktikum Program Komputer 2021 Kelas [B] Kelompok [12]
Program ini dibuat untuk [memudahkan pembelian tiket pesawat secara online]


Repository

Berkas ['Kelompok 12_Flowchart']
        Merupakan lampiran berupa diagram alir yang menjelaskan cara kerja program

Berkas ['ACC_12_Abyan_TUBES TAHAP 1]
        Merupakan laporan berisi usulan ide yang digunakan sebagai acuan pembuatan program

Berkas ['data_maskapai']
        Merupakan berkas pendukung program/database yang berisi nama pesawat, rute penerbangan, dan harga

Berkas ['dom_nondom']
        Merupakan berkas pendukung program/database yang berisi jenis penerbangan domestik dan non domestik

Berkas ['hotel']
        Merupakan berkas pendukung program/database yang berisi nama nama hotel pada tujuan domestik dan non domestik beserta harga

Berkas ['kelas_maskapai']
        Merupakan berkas pendukung program/database yang berisi kelas penerbangan yaitu ekonomi, bisnis, dan eksekutif beserta bobot harga tiap kelas

Berkas ['waktu_penerbangan']
        Merupakan berkas pendukung program/database yang berisi waktu penerbangan tiap tujuan, baik waktu take off maupun waktu landing

Berkas ['logo soettaloka black resize']
        Merupakan berkas pendukung yang berisi gambar logo Soetta-Loka backgorund hitam pada tampilan pertama / main page

Berkas ['logo soettaloka']
        Merupakan gambar logo Soetta-Loka backgorund putih

Berkas ['main_windows]
        Merupakan main file untuk menjalankan/running program Soetta-Loka

Berkas 'README.md'
        Merupakan penjelasan singkat isi dari repository

System Requirement

Beberapa syarat yang diperlukan untuk running program :
1. Pada komputer sudah terinstal Tkinter, untuk memastikan bisa terlebih dahulu membuka interpreter Python lalu ketik import_tkinter
2. Pada komputer sudah terinstal PIL, jika belum maka buka command prompt lalu ketik pip install pillow
3. Agar program dapat berjalan, maka download/miliki semua database yang sudah ter-upload di github dengan cara download ZIP, kemudian ekstrak file lalu buka file main_windows

Cara memakai program :
1. Setelah memenuhi persyaratan diatas, maka langkah selanjutnya adalah membuka file main_windows
2. Running, kemudian pada tampilan pertama terdapat tombol 'pesan tiket' kemudian klik
3. Maka pengguna akan diteruskan pada tampilan kedua yaitu On-booking. Pada halaman ini pengguna diminta untuk memilih jenis tujuan penerbangan (domestik/non domestik), tujuan, waktu penerbangan, kelas penerbangan
4. Jika sudah diisi semua, lalu klik next, maka program akan menampilkan halaman identitas penumpang. di mana pengguna diminta untuk mengisi identitas dirinya yang terdiri dari nama, tempat tanggal lahir, nomor KTP, dan alamat
5. Klik cek data, hal ini bertujuan untuk mengurangi kesalahan data yang di input
6. Pada tampilan selanjutnya, hot deals page, di mana pengguna diberi penawaran spesial. Jika berminat maka memilih penginapan yang diinginkan, jika tidak klik lewati
7. halaman selanjutnya berisi pilihan metode pembayaran, pengguna dapat memilih menggunakan metode apa
8. Jika proses transaksi sudah berhasil, pengguna dapat mencetak tiket