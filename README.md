# Adventurer's Inventory
`Daffa Mohamad Fathoni 2206824161
PBP E`

## Tautan Aplikasi
[Link to Adventurer's Inventory](https://adventurers-inventory.adaptable.app/main)

## Tugas 2
>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).

 - [x] Membuat sebuah proyek Django baru.

Saya membuat direktori lokal dan repo baru di Github bernama ***Adventurer's Inventory***. Saya inisiasi git dilanjut dengan menghubungkan kedua hal tersebut (direktori lokal dan repo di Github). Setelah itu, saya mengaktifkan *Virtual Environment* untuk menanmbahkan dan mengisolasi *dependencies* serta membuat projek Django yang baru dengan command `django-admin startproject adventurers-inventory .` Terakhir saya tidak lupa membuat file `.gitignore` untuk menghindari dan mengantisipasi file-file yang harus diabaikan oleh *version control* git ketika melakukan `add`, `commit`, dan `push`.

 - [x]  Membuat aplikasi dengan nama `main` pada proyek tersebut.

Pada proyek ***Adventurer's Inventory*** ini terdapat suatu aplikasi bernama `main` yang memiliki model, tampilan, dan URL khusus dengan rute `/main`. Inisiasi aplikasi `main` saya lakukan dengan perintah `python manage.py startapp main` hingga terbentuk direktori baru pada projek/direktori utama. Tak lupa saya daftarkan aplikasi ini ke `INSTALLED APPS` di `settings.py` seperti berikut,

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main'
    ]
```
Maka, aplikasi `main` sudah terbuat dan terdaftar pada projek ***Adventurer's Inventory***.

 - [x] Melakukan *routing* pada proyek agar dapat menjalankan aplikasi `main`.

Pada dasarnya, *routing* dilakukan agar aplikasi `main` dapat diakses melalui projek hingga aplikasi dan juga pada peramban web. Pada URL tingkat proyek (direktori proyek `adventurers_inventory`) terdapat file `urls.py` yang berisi:

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', include('main.urls'))
]
```
Pada import path yang terdapat `include` akan mengimpor rute URL aplikasi lain ke dalam `urls.py` tingkat proyek. Lalu pada variabel `urlpatterns` terdapat path URL `main/` yang mendefinisikan rute ke file `urls.py` pada aplikasi `main`.

 - [x] Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib sebagai berikut.
    + `name` sebagai nama *item* dengan tipe `CharField`.
    + `amount` sebagai jumlah *item* dengan tipe `IntegerField`.
    + `description` sebagai deskripsi *item* dengan tipe `TextField`.

Pada direktori `main` terdapat file `models.py` sebagai format data yang akan kita simpan dalam aplikasi ini. Data-data ini dapat kita buat, akses, perbarui, dan hapus dengan perintah-perintah SQL (istilahnya CRUD). Models ini pada umumnya berada pada belakang tampilan untuk mengatur dan mengelola struktur data dan logika aplikasi tersebut. File `models.py` ini berisi:
```
from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    item_level = models.IntegerField()
    use = models.TextField()
```
Tambahan selain pada tugas, data tersebut memiliki atribut lain berupa `price` untuk harga suatu `Item`, `item_level` untuk nilai kelangkaan (*rarity*) `Item` tersebut, dan `use` untuk kegunaan `Item` tersebut ketika dipakai.

Setiap perubahan pada `models`, dilakukan perintah `python manage.py makemigrations` untuk menciptakan berkas migrasi, lalu `python manage.py migrate` untuk mengaplikasikan perubahan model dari dalam berkas migrasi ke basis data.

 - [x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah *template* HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

`views.py` yang dimaksud berada pada direktori `main`, fungsi pada file ini akan bertugas untuk mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai pada variabel tersebut sehingga dapat me-*render* tampilan HTML menggunakan data yang diberikan. Pada `views.py` berisi kode berikut:
```
from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': 'Adventurer\'s Inventory',
        'name': 'Daffa Mohamad Fathoni',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
```
Pada kode di atas, fungsi `show_main` mengembalikan dengan `render` dari parameter `request` yang berupa objek permintaan HTTP, `"main.html"` berupa template yang dituju, dan `context` yaitu berisi data-data yang akan ditampilkan.
```
<h1>{{app_name}}</h1>

<h5>Nama: </h5>
<p>{{ name }}</p>
<h5>Kelas: </h5>
<p>{{ class }} </p>
```
Isi `main.html` di atas akan menampilkan bentuk format template dan terdapat kurung kurawal yang berfungsi untuk menyesuaikan tampilan dengan data pada `views.py`.

 - [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

Pada direktori `main` dibuat file `urls.py` dengan isi berikut:
```
from django.urls import path, include
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main')
]
```
Kode berikut akan mengatur dan mendefinisikan URL pada aplikasi `main`, lalu menampilkan bentuk *template* dengan `show_main` yang ada di `views.py` ketika URL tersebut diakses. 

 - [x] Melakukan *deployment* ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

Pada PBP sekarang, kepentingan *deployment* bertujuan untuk menampilkan secara langsung atau *live* hasil dari aplikasi dari proyek yang kita buat. Dalam hal ini, digunakan Adaptable.io sebagai wadah untuk *deployment*. *Deployment* pada Adaptable cukup menghubungkan akun Github dan repo proyek yang kita buat. *Template Deployment* yang dipakai adalah `Python App Template`, dan basis data yang dipakai adalah `PostgreSQL`. `Start Command` menggunakan perintah `python manage.py migrate && gunicorn adventurers-inventory.wsgi`.

Terakhir, aplikasi yang saya buat memiliki *domain* bernama `https://adventurers-inventory.adaptable.app/main`.


>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.

![bagan]("C:\Users\Daffa Fathoni\Documents\Universitas Indonesia\Ilmu Komputer\Semester 3\Pemrograman Berbasis Platform\Tugas\baganrequest.png")

Saat pengguna mengirimkan permintaan HTTP aplikasi main melalui web browser, urls.py melakukan pemetaan URL untuk meneruskan permintaan HTTP ke views.py sesuai dengan URL yang diminta. Kemudian, view menghasilkan response HTTP berupa halaman HTML. Dalam proses ini, views.py mengambil data yang diperlukan melalui models.py dan menampilkan data tersebut menggunakan template main.html.

>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Virtual environment digunakan untuk mengisolasi *dependencies* dan modul Python yang dipakai untuk kebutuhan proyek Anda masing-masing sehingga tidak akan bertabrakan dan terpengaruh oleh modul atau konfigurasi proyek yang lain. Hal ini akan menghindari instalasi paket atau modul secara global karena semisal paket atau modul tersebut hanya untuk proyek tertentu.

Semisal Proyek A menggunakan Django 4.0 dan Proyek B menggunakan Django 4.1, dengan *virtual environment* akan memudahkan dalam mengelola konsistensi dari *dependencies* masing-masing proyek tersebut untuk menghindari adanya konflik.

Virtual environment dibuat dengan perintah `python -m venv env`, dan diaktifkan dengan perintah `env\Scripts\activate.bat`.

Membuat aplikasi tanpa *virtual environment* tetap dapat dijalankan namun lebih dianjurkan mengimplementasikan *virtual environment* karena hal ini dapat memudahkan untuk pengelolaan konsistensi dari masing-masing *dependencies* proyek sehingga menjadikannya sebuah *good practice* 

>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

| MVC         | MVT         | MVVM          |
| :---        |    ----   |          --- |
| Model-View-Controller      | Model-View-Template     | Model-View-View-Model   |
| Model: Menyimpan dan mengimplementasikan pengelolaan logika data   | Model: Menyimpan dan mengimplementasikan pengelolaan logika data        | Model: Menyimpan dan mengimplementasikan pengelolaan logika data    |
| View: Bertanggung jawab sebagai pengelola antarmuka pengguna dan menampilkan data yang diberikan model lalu mengirim input ke Controller | View: Visualisasi dan menampilkan data ke pengguna tetapi dalam Framework Python Django| View: Menginformasi ke ViewModel terkait interaksi pengguna, dan hanya menampilkan data yang disediakan oleh ViewModel |
| Controller: Menjembatani hubungan antara View dan Model dan sebagai inti logika dan alur aplikasi dengan menginformasi interaksi user ke Model | Template: Mengambil data dari model dan menampilkannya, berupa HTML  | ViewModel: Perantara antara Model dan View, mengubah data dari Model menjadi format sesuai dengan tampilan |
|![mvc](https://media.geeksforgeeks.org/wp-content/uploads/20201002214740/MVCSchema.png) |![mvp](https://media.geeksforgeeks.org/wp-content/uploads/20201024233154/MVPSchema.png) |![mvvm](https://media.geeksforgeeks.org/wp-content/uploads/20201002215007/MVVMSchema.png) |
|MVC adalah pola yang umum digunakan dalam pengembangan aplikasi berbasis desktop dan web tradisional. Ini memisahkan tiga komponen utama aplikasi untuk meningkatkan pemeliharaan dan pengembangan kode. |MVT adalah pola yang spesifik untuk kerangka kerja Django, yang dirancang khusus untuk pengembangan aplikasi web dengan Python. Ini menggantikan View dalam MVC dengan Template, yang memungkinkan pemisahan yang lebih jelas antara tampilan dan pemrosesan HTTP. |MVVM adalah pola desain yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama pada platform seperti WPF (Windows Presentation Foundation). Ini fokus pada pemisahan antara tampilan dan logika bisnis, dengan menggunakan ViewModel sebagai perantara. |