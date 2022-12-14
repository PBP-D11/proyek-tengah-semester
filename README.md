# 🤖 EV-ryday 🤖

Selamat datang ke repositori kelompok D11, yaitu aplikasi yang bernama EV-ryday!

> Proyek ini dibuat untuk memenuhi tugas Proyek Tengah Semester (PTS)
> pada mata kuliah Pemrograman Berbasis Platform (CSGE602022) yang
> diselenggarakan oleh Fakultas Ilmu Komputer, Universitas Indonesia
> pada Semester Gasal, Tahun Ajaran 2022/2023.

[![Test and Deploy][actions-badge]][commits-gh]

## 🧑🏻‍💻 Pengembang Aplikasi : Kelompok - D11👩🏻‍💻

- [Muhammad Hafizha Dhiyaulhaq (Hafizh)](https://github.com/hafizhdh) (2106750723)
- [Fernando Nathaniel Sutanto (Nando)](https://github.com/nandonathaniel) (2106629995)
- [Nadhif Rahman Alfan (Nadhif)](https://github.com/nadhifralfan) (2106751783)
- [Michael Baptiswa Marully Pangaribuan (Michael)](https://github.com//Whosmichael) (2106752054)
- [Fitria Dwi Cahya (Fitria)](https://github.com/fitriadc) (2106751410)
- [Moreno Rassya Wibisana (Moreno)](https://github.com/morenoraw) (106752003)

## 🚘 Tautan Aplikasi Heroku 🚘

Proyek ini dapat diakses di [ev-ryday.herokuapp.com](https://ev-ryday.up.railway.app)

## 📃 Cerita aplikasi yang diajukan serta manfaatnya 📃

### Latar Belakang

Transportasi merupakan salah satu aspek terpenting dalam kehidupan manusia. Di era modern ini, hampir semua orang membutuhkan transportasi, mulai dari transportasi umum hingga transportasi pribadi demi memenuhi kebutuhan mobilitas yang yang cepat. Seiring berjalannya waktu, tingkat kepemilikan kendaraan pribadi semakin tinggi, yang secara tidak langsung meningkatkan penggunaan bahan bakar. Tingginya penggunaan bahan bakar minyak memberikan banyak dampak buruk bagi dunia, mulai dari melambungnya harga minyak bumi hingga emisi gas rumah kaca yang telah menjadi concern masyarakat dunia hingga hari ini. Akibat permasalahan tersebut, produsen-produsen mobil ternama mulai mengembangkan mobil bertenaga listrik. Mobil listrik dinilai akan menjadi solusi yang dapat memecahkan masalah-masalah di atas.

Walau menjadi solusi, mobil listrik juga memiliki banyak hambatan dan kekurangan. Mulai dari harganya yang relatif lebih mahal karena harga baterai ion lithium yang masih cukup tinggi. Faktor lain yang menghambat adalah, jumlah stasiun pengisian daya yang masih tergolong sedikit. Stasiun pengisian daya baterai untuk mobil listrik merupakan fasilitas terpenting yang harus disediakan, untuk menyokong penggunaan mobil listrik secara meluas. Minimnya instalasi pengisian daya tersebut menyebabkan, lokasi stasiunnya masih sangat tersebar dan cukup sulit diketahui, hal ini juga menjadi salah satu _bottleneck_ dalam penggunaan mobil listrik.

EV-ryday hadir untuk memberikan solusi bagi masalah tersebut. EV-ryday merupakan sebuah platform multifungsi bagi para pengguna mobil listrik. EV-ryday menyediakan berbagai fitur yang dapat membantu para pengguna mobil listrik, mulai dari informasi lokasi pengisian daya baterai terdekat, forum bagi para pengguna, informasi tempat servis mobil listrik, hingga katalog mobil listrik.Dengan dikembangkannya EV-ryday, diharapkan penggunaan mobil listrik dapat lebih meluas sehingga dapat menciptakan lingkungan yang _sustainable_.

### Tujuan dan Manfaat

Aplikasi EV-ryday memiliki tujuan yakni menjadi sarana masyarakat untuk beralih kepada moda transportasi dengan sumber daya energi yang berkelanjutan dan lebih terbarukan pada masa yang akan datang.

Manfaat dari aplikasi EV-ryday adalah sebagai berikut:
1. Membantu pemilik kendaraan listrik lebih mudah dalam melakukan hal-hal yang berhubungan dengan pemeliharaan dan perawatan.
2. Memberikan wawasan kepada masyarakat yang masih belum atau ragu-ragu mengenai pemeliharaan kendaraan listrik tersebut.
3. Menjadikan aplikasi EV-ryday untuk menjadi wadah bertukar informasi mengenai kendaraan listrik dari segi kebutuhan hingga jasa pemeliharaan.

## 👩🏻‍💻 Persona 👩🏻‍💻

1. Bukan pengguna mobil listrik

- Goals :
  1. Mencari informasi seputar kendaraan listrik
  2. Bertanya seputar kendaraan listrik pada forum yang tersedia
  3. Mencari mobill listrik impian
- Permasalahan : 
  1. Ingin membeli mobil listrik tetapi masih awam mengenai mobil listrik
  2. Bingung untuk bertanya seputar mobil listrik

2. Pengguna Baru mobil listrik

- Goals : 
  1. Mencari informasi mengenai tips merawat mobil listrik
  2. Mencari informasi mengenai charging station di sekitar tempat tinggalnya
  3. Bergabung dengan komunitas mobil listrik untuk menambah relasi dan informasi
- Permasalahan : 
  1. Baru membeli mobil listrik dan tidak mengerti cara merawat mobil listrik dengan baik
  2. Belum mempunyai home charging dan harus mencari charging station yang paling dekat dengan rumahnya
  3. Tidak memiliki relasi sesama pengguna mobil listrik

3. Pengguna Antusias Mobil Listrik

- Goals : 
  1. Membantu pengguna yang masih baru dalam dunia mobil listrik dengan aktif menjawab pada forum
  2. Menambahkan charging station yang belum tercover oleh website
- Permasalahan : 
  1. Mencari tempat untuk sharing seputar mobil listrik
  2. Menemukan charging station baru dan ingin sharing kepada komunitas
  
  *test


## 📝 Modul dan Pembagiannya 📝

| No  | Modul         | Deskripsi                                                                                 | PJ Modul |
| --- | ------------- | ----------------------------------------------------------------------------------------- | -------- |
| 1   | User          | Mengisi dan update profile                                                                | Nadhif   |
|     |               | Autentikasi (login, logout user)                                                          |          |
|     |               | Mapping models, views, dan integrasi                                                      |          |
| 2   | Find Charge   | Ada list untuk tempat mengecas mobil listrik                                              | Hafizh   |
|     |               | Formulir untuk melapor adanya tempat pengecasan                                           |          |
|     |               | History bila pernah mengecas di tempat yang telah digunakan                               |          |
| 3   | EVorums       | Ada dasbor seperti forum diskusi SCELE                                                    | Michael  |
|     |               | User bisa bertanya, menjawab, atau menghapus keduanya                                     |          |
| 4   | EVices        | Terdapat informasi mengenai tempat servis mobil listrik terdekat                          | Nando    |
|     | (EV Services) | User bisa mendapatkan kontak lengkap mengenai tempat servis tersebut                      |          |
| 5   | EVishlist     | Catalog mobil elektronik untuk mengenal pengguna mengenai mobil listrik                   | Fitria   |
|     | (EV Wishlist) | User dapat menandai mobil yang disuka untuk disimpan sebagai wishlist                     |          |
| 6   | EV News       | User dapat melihat news sekitar EV, dan bisa filtering sesuai source news yang dilihat    | Moreno   |
