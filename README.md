# :school_satchel: Adventurer's Inventory :tent:
`Daffa Mohamad Fathoni 2206824161
PBP E`

## Tautan Aplikasi
[Link to Adventurer's Inventory](https://daffa-mohamad-tugas.pbp.cs.ui.ac.id/)


# Tugas 2

<details>
<summary>1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

 - [x] Membuat sebuah proyek Django baru.

Saya membuat direktori lokal dan repo baru di Github bernama ***Adventurer's Inventory***. Saya inisiasi git dilanjut dengan menghubungkan kedua hal tersebut (direktori lokal dan repo di Github). Setelah itu, saya mengaktifkan *Virtual Environment* untuk menanmbahkan dan mengisolasi *dependencies* serta membuat projek Django yang baru dengan command `django-admin startproject adventurers-inventory .` Terakhir saya tidak lupa membuat file `.gitignore` untuk menghindari dan mengantisipasi file-file yang harus diabaikan oleh *version control* git ketika melakukan `add`, `commit`, dan `push`.

 - [x]  Membuat aplikasi dengan nama `main` pada proyek tersebut.

Pada proyek ***Adventurer's Inventory*** ini terdapat suatu aplikasi bernama `main` yang memiliki model, tampilan, dan URL khusus dengan rute `/main`. Inisiasi aplikasi `main` saya lakukan dengan perintah `python manage.py startapp main` hingga terbentuk direktori baru pada projek/direktori utama. Tak lupa saya daftarkan aplikasi ini ke `INSTALLED APPS` di `settings.py` seperti berikut,

```python
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

```python
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
```python
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
```python
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
```python
<h1>{{app_name}}</h1>

<h5>Nama: </h5>
<p>{{ name }}</p>
<h5>Kelas: </h5>
<p>{{ class }} </p>
```
Isi `main.html` di atas akan menampilkan bentuk format template dan terdapat kurung kurawal yang berfungsi untuk menyesuaikan tampilan dengan data pada `views.py`.

 - [x] Membuat sebuah *routing* pada `urls.py` aplikasi `main` untuk memetakan fungsi yang telah dibuat pada `views.py`.

Pada direktori `main` dibuat file `urls.py` dengan isi berikut:
```python
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

</details>

<details>
<summary>2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.</summary>

![bagan](https://github.com/fathonidf/adventurers-inventory/assets/105644250/9cb5536b-83d7-45ea-ae2b-a8abde7cde9e)

Saat pengguna mengirimkan permintaan HTTP aplikasi main melalui web browser, urls.py melakukan pemetaan URL untuk meneruskan permintaan HTTP ke views.py sesuai dengan URL yang diminta. Kemudian, view menghasilkan response HTTP berupa halaman HTML. Dalam proses ini, views.py mengambil data yang diperlukan melalui models.py dan menampilkan data tersebut menggunakan template main.html.
</details>

<details>
<summary>3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?</summary>

Virtual environment digunakan untuk mengisolasi *dependencies* dan modul Python yang dipakai untuk kebutuhan proyek Anda masing-masing sehingga tidak akan bertabrakan dan terpengaruh oleh modul atau konfigurasi proyek yang lain. Hal ini akan menghindari instalasi paket atau modul secara global karena semisal paket atau modul tersebut hanya untuk proyek tertentu.

Semisal Proyek A menggunakan Django 4.0 dan Proyek B menggunakan Django 4.1, dengan *virtual environment* akan memudahkan dalam mengelola konsistensi dari *dependencies* masing-masing proyek tersebut untuk menghindari adanya konflik.

Virtual environment dibuat dengan perintah `python -m venv env`, dan diaktifkan dengan perintah `env\Scripts\activate.bat`.

Membuat aplikasi tanpa *virtual environment* tetap dapat dijalankan namun lebih dianjurkan mengimplementasikan *virtual environment* karena hal ini dapat memudahkan untuk pengelolaan konsistensi dari masing-masing *dependencies* proyek sehingga menjadikannya sebuah *good practice* 
</details>

<details>
<summary>4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.</summary>

| MVC         | MVT         | MVVM          |
| ---        |    ----   |          --- |
| Model-View-Controller      | Model-View-Template     | Model-View-View-Model   |
| Model: Menyimpan dan mengimplementasikan pengelolaan logika data   | Model: Menyimpan dan mengimplementasikan pengelolaan logika data        | Model: Menyimpan dan mengimplementasikan pengelolaan logika data    |
| View: Bertanggung jawab sebagai pengelola antarmuka pengguna dan menampilkan data yang diberikan model lalu mengirim input ke Controller | View: Visualisasi dan menampilkan data ke pengguna tetapi dalam Framework Python Django| View: Menginformasi ke ViewModel terkait interaksi pengguna, dan hanya menampilkan data yang disediakan oleh ViewModel |
| Controller: Menjembatani hubungan antara View dan Model dan sebagai inti logika dan alur aplikasi dengan menginformasi interaksi user ke Model | Template: Mengambil data dari model dan menampilkannya, berupa HTML  | ViewModel: Perantara antara Model dan View, mengubah data dari Model menjadi format sesuai dengan tampilan |
|![mvc](https://media.geeksforgeeks.org/wp-content/uploads/20201002214740/MVCSchema.png) |![mvp](https://media.geeksforgeeks.org/wp-content/uploads/20201024233154/MVPSchema.png) |![mvvm](https://media.geeksforgeeks.org/wp-content/uploads/20201002215007/MVVMSchema.png) |
|MVC adalah pola yang umum digunakan dalam pengembangan aplikasi berbasis desktop dan web tradisional. Ini memisahkan tiga komponen utama aplikasi untuk meningkatkan pemeliharaan dan pengembangan kode. |MVT adalah pola yang spesifik untuk kerangka kerja Django, yang dirancang khusus untuk pengembangan aplikasi web dengan Python. Ini menggantikan View dalam MVC dengan Template, yang memungkinkan pemisahan yang lebih jelas antara tampilan dan pemrosesan HTTP. |MVVM adalah pola desain yang sering digunakan dalam pengembangan aplikasi berbasis antarmuka pengguna (UI), terutama pada platform seperti WPF (Windows Presentation Foundation). Ini fokus pada pemisahan antara tampilan dan logika bisnis, dengan menggunakan ViewModel sebagai perantara. |

</details>

---

# Tugas 3

<details>
<summary>1. Apa perbedaan antara form POST dan form GET dalam Django?</summary>

* GET dan POST merupakan sebuah form HTTP Requests, yaitu sebuah jalur komunikasi antar client dan web server di World Wide Web

| `GET`   | `POST`  |
| ---   | ---   |
| Meminta untuk menerima data dari web server| Meminta untuk mengirimkan data ke web server|
| Mengembalikan kode status HTTP 200 jika data sukses diterima | Mengembalikan kode status HTTP 201 jika sukses *created*|
| Dikirimkan melalui URL sebagai bagian dari query string | Dikirimkan dalam body request HTTP secara tersembunyi |
| Tidak cocok untuk data yang bersifat sensitif | Ideal untuk data yang rahasia |
| Terbatas pada panjang URL| Tidak ada batasan dari panjang data yang dikirim |


* Contoh pemakaian form `GET`
```html
<form action="/search/" method="GET">
        <input type="text" id="query">
        <input type="submit" value="Search">
    </form>
```

* Contoh pemakaian form `FORM`
```html
<form action="/submit-post/" method="POST">
        <input type="text" id="name">
        <input type="submit" value="Submit">
    </form>
```

</details>

<details>
<summary>2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?</summary>

* Data Delivery pada suatu platform dibutuhkan untuk komunikasi antar klien dengan server. Bentuk atau format data bisa dalam bentuk `HTML`, `XML`, atau `JSON`.
* HTML lebih menekankan fungsinya berguna sebagai mendeskripsikan bagaimana data ditampilkan, mendefinisikan struktur dan tampilan web.

| XML   | JSON  | 
| ---   | ---  | 
|Extensible Markup Language | JavaScript Object Notation | 
|Berdasarkan SGML |Berdasarkan JavaScript |
| Menggunakan tag (`</>`) untuk merepresentasikan data | Menggunakan kurung kurawal (`{}`), kurung siku(`[]`), dan berbentuk `key:value` |
| Struktur data yang kuat dan kompleks | Sintaks yang ebih ringkas dan mudah dibaca manusia (*Human Readable*)|
|Dapat mewakili berbagai jenis data dan menyertakan dokumentasi yang jelas |Pemrosesan yang lebih cepat dan mudah, juga kompatibel dengan JavaScript |

* Contoh sintaks `HTML`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contoh HTML</title>
</head>
<body>
    <h1>Selamat datang di contoh HTML!</h1>
    <p>Ini adalah halaman web sederhana.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
</body>
</html>
```

* Contoh sintaks `XML`:
```xml
<person>
    <name>John Doe</name>
    <age>30</age>
    <city>New York</city>
</person>
```

* Contoh sintaks `JSON`:
```json
{
    "person": {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    }
}
```


</details>

<details>
<summary>3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?</summary>

### Beberapa kelebihan JSON yang mendukung hingga sering digunakan untuk transfer data antar klien dan server ada pada poin-poin berikut:

1. ### Mudah dibaca 
Format yang ringkas dan mudah dibaca manusia menjadikannya ideal untuk mengirim dan menerima data pada server. Hal ini menjadikannya lebih efisien dan mudah dipahami

2. ### Kompatibilitas dengan JavaScript
Merupakan subset dari JavaScript maka mudah digunakan dan diproses pada bahasa pemrograman Javascript. Data-data JSON dapat di-*parse* hingga menjadi objek JavaScript dan sebaliknya.

3. ### Struktur Hierarki
Mendukung representasi data dengan pasangan `key:value` yang memungkinkan penyusunan data lebih kompleks dan efektif.

4. ### Didukung oleh Banyak Bahasa Pemrograman
Sebagian besar bahasa Pemrograman kompatibel dengan JSON sehingga memudahkan pertukaran data antar klien dan server.

5. ### Format Data dalam RESTful API
JSON adalah format data yang umum digunakan dalam RESTful API. Hal tersebut sering duganakan dalam pengembangan web sehingga menjadikannya pilihan yang cocok untuk berkomunikasi dengan API.

</details>

<details>
<summary>4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

- [x] Membuat input form untuk menambahkan objek model pada app sebelumnya.

1. `forms.py` dibuat untuk menghandle ketika ada input `item` baru dari sisi pengguna. 
```python
from django.forms import ModelForm
from main.models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "amount", "description", "price", "item_level", "use"]
```

Pada baris paling atas tidak lupa untuk mengimpor library `ModelForm` dan `Item` yang ada pada `models.py`. `models = Item` untuk merujuk model yang akan disimpan pada *form*. `fields = []` berguna untuk menunjukkan attribute apa saja yang akan diinput untuk objek `Item` tersebut.

2. Untuk menerima parameter `request`, dibuat fungsi `create_item` untuk menghasilkan formulir yang menambahkan data produk ketika di-submit oada `views.py`.
```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

Potongan kode berikut pada dasarnya memvalidasi (`form.is_valid()`) dan menyimpan data input *form* (`form.save()`) lalu *redirect* ke halaman semula setelah berhasil disimpan (`return HttpResponseRedirect(reverse('main:show_main'))`).

3. Pada `show_main` dimodifikasi agar pada halaman utama ditampilkan object-object yang disimpan pada *database*.

```python
def show_main(request):
    items = Item.objects.all()
    total_items = items.count()

    context = {
        'app_name': 'Adventurer\'s Inventory',
        'name': 'Daffa Mohamad Fathoni',
        'class': 'PBP E',
        'total_items': total_items,
        'items': items
    }

    return render(request, "main.html", context)
```

`items = Item.objects.all()` mengakses objek-objek tersebut, lalu pada `context = {}` ditambahkan `key` berupa `items` untuk nantinya akan ditampilkan di `main.html`. `total_items = items.count()` berguna untuk menghitung banyaknya objek pada *database*, lalu dimasukkan ke dalam variabel `context` untuk nantinya ditampilkan pada `main.html`.

4. Pada `urls.py` ditambahkan *import* fungsi `create_item` lalu menambahkan *path url* ke variable `urlpatterns`.

```python
from django.urls import path, include
from main.views import show_main, create_item

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item')
]
```

5. Untuk tampilan halaman ketika ingin menambahkan/menginput objek baru, dibuat `create_item.html` pada `main/templates` dengan isi kode sebagai berikut.

```html
{% extends 'base.html' %} 

{% block content %}
<h1>Add New Item</h1>

<form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td>
                <input type="submit" value="Add Item"/>
            </td>
        </tr>
    </table>
</form>

{% endblock %}
```

Pada kode `<form method="POST">`, metode *form* yang dipakai adalah `POST` untuk nantinya input data tersebut akan dikirimkan ke server. `{{ form.as_table }}` akan menampilkan *fields form* yang dibuat pada `forms.py`.

6. Terakhir, agar isi data item yang telah diinput dapat ditampilkan, isi `main.html` dapat ditambahkan sintaks `for loop` untuk mengiterasikan tiap item yang terdapat di *database*. 
```html
<h3>Total items in your inventory : {{total_items}}</h3>

<table>
    <tr>
        <th>Name</th>
        <th>Amount</th>
        <th>Description</th>
        <th>Price</th>
        <th>iLvl</th>
        <th>Use</th>
    </tr>

    {% comment %} Berikut cara memperlihatkan data item di bawah baris ini {% endcomment %}

    {% for item in items %}
        <tr>
            <td>{{item.name}}</td>
            <td>{{item.amount}}</td>
            <td>{{item.description}}</td>
            <td>{{item.price}}</td>
            <td>{{item.item_level}}</td>
            <td>{{item.use}}</td>
        </tr>
    {% endfor %}
</table>
```

Pada potongan kode `<h3>Total items in your inventory : {{total_items}}</h3>` akan menampilkan banyaknya `item` yang sudah diinput.  `{% for item in items %}` mengiterasikan tiap item dalam *database*. Kedua sintaks tersebut mengacu pada isi dari `context` pada fungsi `show_main` yang ada di `views.py`.

- [x] Tambahkan 5 fungsi views untuk melihat objek yang sudah ditambahkan dalam format HTML, XML, JSON, XML by ID, dan JSON by ID.

1. Pada `views.py` ditambahkan *import* `HttpResponse` dan `Serializer` untuk nantinya berturut-turut akan berguna untuk berisi parameter data hasil *query* dan *translate* objek model menjadi format yang sesuai.

```python
from django.http import HttpResponse
from django.core import serializers
```

Lalu ditambahkan fungsi pada `views.py` yang akan menampilkan objek dalam format sesuai poin 2

```python
def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```


- [x] Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 2.

1. Untuk memulai *routing* tiap format *views* dapat mengimport fungsi yang dibuat pada `urls.py`.
```python
from django.urls import path, include
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id 
```

2. Lalu menambahkan tiap *path url* ke variabel `urlpatterns` untuk mengakses fungsi-fungsi tersebut.

```python
urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id')
]
```

</details>

<details>
<summary>Screenshot Postman</summary>

### 1. HTML
![html](https://github.com/fathonidf/adventurers-inventory/assets/105644250/9d38de29-6d19-4570-8719-cee4cad2169b)
### 2. XML
![xml](https://github.com/fathonidf/adventurers-inventory/assets/105644250/1ecb41f7-4c34-460d-b298-c0c032e7882c)
### 3. JSON
![json](https://github.com/fathonidf/adventurers-inventory/assets/105644250/dcb68295-0363-48e6-b0bf-8de82149b611)
### 4. XML by ID
![xmlbyid](https://github.com/fathonidf/adventurers-inventory/assets/105644250/aa784e40-bd99-4176-8ce8-a08b4b93ab5e)
### 5. JSON by ID
![jsonbyid](https://github.com/fathonidf/adventurers-inventory/assets/105644250/9ae03290-57ea-4acc-9d1c-e012056b60ca)
</details>

---

# Tugas 4

<details>
<summary>1. Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?</summary>

Django `UserCreationForm` merupakan suatu modul build-in dari Django yang mewarisi class `ModelForm`. Modul ini digunakan untuk meng-*handle* ketika pengguna (*user*) akan membuat akun baru atau biasa disebut *user* baru pada aplikasi web. UserCreationForm memungkinkan *developer* untuk membuat formulir pendaftaran pengguna dengan cepat tanpa harus menulis banyak kode kustom.

### Kelebihan:
1. Kemudahan Penggunaan

Modul ini menyederhanakan proses pembuatan formulir pendaftaran pengguna baru.

2. Validasi Bawaan

Mencakup validasi bawaan untuk berbagai input seperti *username* dan *password*.

3. Integrasi dengan Model User Bawaan Django

Terhubung dengan model `user` bawaan Django yang memungkinkan data dapat dimasukkan dan disimpan dalam tabel `user` secara otomatis.

4. Fleksibilitas

Selain mudah digunakan, kita dapat memodifikasinya sesuai dengan kebutuhan proyek dan aplikasi masing-masing. Seperti menambahkan atau mengubah proses validasi, tampilan, dan lainnya.

5. Kode yang lebih Rapi

Meminimalisir adanya duplikasi kode karena mengikuti prinsip DRY (*Don't Repeat Yourself*) sehingga menjadikannya lebih rapi dan mudah diatur.

### Kekurangan:
1. Modifikasi yang Terbatas

Walaupun dapat memodifikasi untuk menyesuaikan kebutuhan proyek, modul ini akan terbatas ketika dibutuhkan bentuk yang lebih bervariasi. Hal tersebut memungkinkan untuk membuat formulir khusus sendiri.

2. Tidak Cocok untuk Otorisasi lebih Kompleks

`UserCreationForm` ini ditujukan untuk proses pendaftaran `user` secara mendasar. Tetapi, tidak mendukung untuk otorisasi atau profil pengguna yang lebih kompleks.

3. *Bahasa yang Terbatas*

`UserCreationForm` disesuaikan untuk bahasa tertentu khususnya bahasa inggris. Tetapi tidak mendukung ketika digunakan untuk aplikasi multibahasa.



</details>

<details>
<summary>2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?</summary>

|**Autentikasi** | **Otorisasi** |
| --- | --- |
|Memverifikasi klaim dan identitas seorang user| Menentukan hal-hal yang diperbolehkan seorang user akses dan lakukan|
|Bekerja melalui *password*, PIN, biometrik, dan informasi user lainnya| Bekerja melalui pengaturan yang telah diimplementasi dan diatur oleh organisasi tersebut|
|Langkah untuk proses manajemen identitas dan akses yang baik | Dilakukan setelah autentikasi|
| Terlihat dan dapat diatur sebagian oleh user | Tidak terlihat dan tidak diberikan akses pengaturan kepada user |

Contoh potongan kode autentikasi sesuai dengan *library* Django:
 
```python
from django.contrib.auth import authenticate

user = authenticate(username="john", password="secret")
if user is not None:
    # A backend authenticated the credentials
    ...
else:
    # No backend authenticated the credentials
    ...
```

* **Kesimpulan**: Dapat disimpulkan, autentikasi digunakan untuk verifikasi identitas seorang  user. Setelah terautentikasi, otorisasi dilakukan untuk memberikan izin hak dan akses kepada seorang user dalam mengakses informasi-informasi, menjalankan suatu fitur, dan lainnya dengan bergantung pada aturan yang ditetapkan untuk berbagai jenis pengguna.

</details>

<details>
<summary>3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?</summary>

* Cookies adalah sepotong informasi kecil yang disetor dan disimpan di browser klien. Hal ini berguna untuk menyimpan data user di suatu file selama rentang waktu tertentu. Sebuah Cookie mempunyai tanggal kadaluarsa sehingga akan menghapus data atau cookie tersebut secara otomatis ketika mencapai batas waktunya. Django menyediakan *method-method* built-in untuk membuat cookie.

* Sintaks untuk membuat dan mengakses cookie adalah `set_cookie()` dan `get()` atau `request.COOKIES['key]` (dalam bentuk array).

* Contoh sepotong kodingan Django Cookie dalam `views.py` dan `urls.py`:

```python
from django.shortcuts import render  #views.py
from django.http import HttpResponse  
  
def setcookie(request):  
    response = HttpResponse("Cookie Set")  
    response.set_cookie('java-tutorial', 'javatpoint.com')  
    return response  
def getcookie(request):  
    tutorial  = request.COOKIES['java-tutorial']  
    return HttpResponse("java tutorials @: "+  tutorial);  
```

```python
from django.contrib import admin #urls.py
from django.urls import path  
from myapp import views  
urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('index/', views.index),  
    path('scookie',views.setcookie),  
    path('gcookie',views.getcookie)  
]  
```

</details>

<details>
<summary>4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?</summary>

Secara umum, bukan merupakan ancaman terkait privasi dan keamanan web karena tidak menyimpan data pribadi dan tidak bisa mengirim virus. Namun, terdapat beberapa risiko yang harus diwaspadai seperti:

1. **Disalahgunakan oleh pihak ketiga yang tidak berwenang untuk melacak aktivitas online pengguna, mengumpulkan data pribadi.**

2. **Dicuri peretas untuk mengakses informasi sensitif seperti data, token, kredensial dengan tujuan pencurian, pembajakan, atau penipuan.**

3. **Dapat menimbulkan masalah privasi dan keamanan jika tidak dikelola dengan baik oleh pengembang web, seperti tidak menghapus cookie yang sudah tidak diperlukan atau tidak mengenkripsi cookie yang berisi data penting.**

Beberapa hal yang bisa dijadikan sebagai *Best Practice* untuk diikuti seperti:

1. **Menggunakan cookie pihak pertama untuk situs web sendiri**

2. **Cookie hanya berlaku selama pengguna **sedang** menjelajah situs web**

3. **Menggunakan cookie untuk data yang benar-benar diperlukan untuk fungsionalitas web**

4. **Hanya dapat diakses melalui protokol HTTPS yang aman.**

</details>

<details>
<summary>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

- [x] Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.

### Registrasi

1. Pertama, pada `views.py` diimport fungsi-fungsi berikut:

```python
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
```
`UserCreationForm` merupakan modul yang menyediakan template formulir pendaftaran pengguna baru.

2. Membuat fungsi `register` yang akan menghasilkan formulir registrasi dan mendaftarkan akun pengguna ketika di-*submit* dengan potongan kode berikut:

```python
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)
```

`form = UserCreationForm(request.POST)` akan membuat form baru berdasarkan import `UserCreationForm`dengan memasukkan input dari user pada `request.POST`. `form.is_valid()` untuk memvalidasi isi input, `form.save()` untuk menyimpan data dari form. `return redirect('main:login')` mengembalikan halaman ke semula ketika berhasil menyimpan form.

3. Menambahkan file baru dengan `register.html` untuk halaman register dengan kode berikut yang sudah ditambahkan beberapa styling css

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Register</title>
{% endblock meta %}

{% block content %}  

<div class = "container">

    <div class = "title">
        <h1>Register</h1>  
    </div>

    <div class = "register_form">
        <form method="POST" >  
            {% csrf_token %}  
            <table>  
                {{ form.as_table }}  
                <tr>  
                    <td></td>
                    <td><input class="daftar_btn"type="submit" name="submit" value="Daftar"/></td>  
                </tr>  
            </table>  
        </form>
    </div>

    {% if messages %}  
        <ul>   
            {% for message in messages %}  
                <li>{{ message }}</li>  
                {% endfor %}  
        </ul>   
    {% endif %}

</div>  

{% endblock content %}
```

Pada kode di atas, form akan ditampilkan pada bagian `{{ form.as_table }}`.

4. Setelah menambahkan fungsi register, maka kita melakukan *routing* pada `urls.py` dengan mengimport fungsi tersebut dan menambahkan path url ke `urlpatterns`.

```python
from main.views import register

urlpatterns = [
    ...
    path('register/', register, name='register'),
    ...
]
```
### Login

1. Sesuai dengan alur pembuatan form registrasi sebelumnya, membuat fungsi dan form login dimulai di `views.py` untuk mengimport library dan membuat fungsinya dengan kode berikut:

```python
from django.contrib.auth import authenticate, login
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)
```

`authenticate` dan `login` diimpor untuk melakukan autentikasi dan login jika berhasil. Lalu pada fungsi `login_user` tersebut, autentikasi dilakukan pada potongan kode `user = authenticate(request, username=username, password=password)`, menyesuaikan username dan password yang diterima.

Pada kode di atas juga sudah ditambahkan informasi *cookie* yang akan menampilkan kapan pengguna terakhir kali login, kode ini terdapat pada `response.set_cookie('last_login', str(datetime.datetime.now()))`. Kode itu akan membuat cookie `last_login` dan menambahkannya ke dalam response ketika nantinya di `return`.

Agar pada halaman utama ditampilkan waktu terakhir login, maka ditambahkan potongan kode berikut pada `show_main` di dalam dictionary `context` seperti berikut

```python
context = {
        'app_name': 'Adventurer\'s Inventory',
        'name': request.user.username,
        'class': 'PBP E',
        'total_items': total_items,
        'items': items,
        'last_login': request.COOKIES.get("last_login")
    }
```

2. Membuat halaman baru dengan file `login.html` dengan kode berikut:

```html
{% extends 'base.html' %}

{% block meta %}
    <title>Login</title>
{% endblock meta %}

{% block content %}

<div class = "login">

    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
            <tr>
                <td>Username: </td>
                <td><input type="text" name="username" placeholder="Username" class="form-control"></td>
            </tr>
                    
            <tr>
                <td>Password: </td>
                <td><input type="password" name="password" placeholder="Password" class="form-control"></td>
            </tr>

            <tr>
                <td></td>
                <td><input class="btn login_btn" type="submit" value="Login"></td>
            </tr>
        </table>
    </form>

    <h5>Sesi terakhir login: {{ last_login }}</h5>


    {% if messages %}
        <ul>
            {% for message in messages %}
                <li>{{ message }}</li>
            {% endfor %}
        </ul>
    {% endif %}     
        
    Don't have an account yet? <a href="{% url 'main:register' %}">Register Now</a>

</div>

{% endblock content %}
```

pengisian form login ada pada tag `<form></form>`, lalu pada `messages` merupakan modul bawaan dari Django yang akan menampilkan informasi ketika login tidak berhasil.

Terakhir, adalah melakukan *routing* pada `urls.py` dengan kode berikut:

```python
from main.views import login_user

urlpatterns = [
    ...
path('login/', login_user, name='login'),
...
]
```


### Logout

1. Terakhir adalah fungsi dan halaman logout, pada `views.py` kita mengimport library logout dan menambahkan fungsi `logout_user` sebagai berikut:

```python
from django.contrib.auth import logout

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

Pada kode di atas, kita mengimport library `logout` yang akan dipakai pada fungsi `logout_user`, pada fungsi tersebut menerima parameter `request` dan lalu menghapus sesi pengguna tersebut dengan `logout(request)`, dilanjutkan dengan mengarahkan pengguna ke halaman login. `response.delete_cookie('last_login')` akan menghapus informasi *cookie* yang tersimpan saat pengguna melakukan logout.

2. Selanjutnya adalah button logout yang akan ditambahkan pada `main.html` dengan kode berikut:

```html
...
<a href="{% url 'main:logout' %}">
    <button>
        Logout
    </button>
</a>
...
```

3. Terakhir melakukan *routing* pada `urls.py` agar bisa menampilkan dan memberi akses keseluruhan fungsi yang telah terbuat.

```python
from main.views import logout_user, ...

urlpatterns = [
    ...
path('logout/', logout_user, name='logout'),
...
]
```

### Merestriksi Halaman Main

Agar halaman `main.html` hanya bisa diakses ketika login sukses, maka diimport library `login_required` pada `views.py`

```python
from django.contrib.auth.decorators import login_required

...
@login_required(login_url='/login')
def show_main(request):
...
```

Pada kode diatas, pengguna diharuskan login dulu, lalu bisa mengakses `main` ketika sudah tervalidasi/terautentikasi username dan passwordnya pada `@login_requires(login_url='/login')`

- [x] Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.

Akun 1:
![akun1](https://media.discordapp.net/attachments/894158439008305192/1156445662645342238/image.png?ex=6514ff73&is=6513adf3&hm=7acbc38cada213622e7a64dba4cabc8c90a622f625ad451fd3f1be58b04845c0&=&width=972&height=662)

Akun 2:
![akun2](https://media.discordapp.net/attachments/894158439008305192/1156445725312417842/image.png?ex=6514ff82&is=6513ae02&hm=ff9ec3d52f251cb07d0c7ca6b2d3ab59e7a07501f591628d032bfa7cabd8a538&=&width=981&height=662)

- [x] Menghubungkan model Item dengan User.

1. Untuk menghubungkan Model `Item` dengan `User`, maka kita akan menambahkan library `User` pada `models.py` dan mengasosiasikan suatu `Item` dengan user tertentu sesuai dengan kode berikut:

```python
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    description = models.TextField()
    price = models.IntegerField()
    item_level = models.IntegerField()
    use = models.TextField()
```

Pada penambahan `user = models.ForeignKey(User, on_delete=models.CASCADE)`, kode tersebut akan mengimplementasikan *many-to-one* relationship, dimana seorang User dapat memiliki banyak Item pada konteks ini, tapi suatu Item hanya dapat dimiliki oleh satu User.

2. Selanjutnya mengubah potongan kode `create_product` menjadi seperti berikut:

```python
def create_item(request):
    form = ItemForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_item.html", context)
```

Pada `commit=False` mencegah untuk penyimpanan objek secara otomatis sehingga kita dapat mengatur/memodifikasinya terlebih dahulu sebelum disimpan di database.

3. Mengubah `show_main` untuk menampilkan objek `Item` sesuai dengan kepemilikan User yang sedang login.

```python
def show_main(request):
    items = Item.objects.filter(user=request.user)
    total_items = items.count()

    context = {
        'app_name': 'Adventurer\'s Inventory',
        'name': request.user.username,
        ...
    }
```

`items = Item.objects.filter(user=request.user)` tersebut akan menyaring objek `Item` sesuai dengan kepemilikan pengguna yang sedang login. `'name': request.user.username,` akan menampilkan user yang sedang login tersebut.

4. Terakhir, jangan lupa untuk melakukan migrasi model setiap melakukan perubahan pada `models.py`

`python manage.py makemigrations` dan `python manage.py migrate` pada Command Terminal akan mengaplikasikan migrasi tersebut.


- [x] Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.

Pada kode login, logout di atas sudah terasosiasikan dengan cookie untuk menyimpan informasi kapan User terakhir login. Pada dasarnya dilakukan langkah sebagai berikut:

1. Mengimport library pada `views.py` sebagai berikut:

```python
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
```

2. Lalu menambahkan kode pada fungsi `login_user` sebagai berikut:
```python
if user is not None:
    login(request, user)
    response = HttpResponseRedirect(reverse("main:show_main")) 
    response.set_cookie('last_login', str(datetime.datetime.now()))
    return response
```

Hal tersebut akan membuat cookie `last_login` dan mengembalikannya pada response.

3. Menambahkan informasi `last_login` pada `show_main` di variabel `context` untuk menampilkan informasi login terakhir seorang user tersebut

```python
context = {
    'app_name': 'Adventurer\'s Inventory',
    'name': request.user.username,
    'class': 'PBP E',
    'total_items': total_items,
    'items': items,
    'last_login': request.COOKIES.get("last_login")
    }
```
4. Mengubah fungsi `logout_user` yang akan menghapus cookie ketika pengguna melakukan logout

```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```

5. Terakhir, kita menyambungkan `'last_login'` pada `context` dengan tampilan pada `main.html` dengan potongan kode berikut:

```html
...
<h5>Sesi terakhir login: {{ last_login }}</h5>
...
```

Maka pada halaman tersebut akan menampilkan informasi terakhir seorang pengguna melakukan login di halaman utama (`main.html`).

</details>

---

# Tugas 5

<details>
<summary>1. Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.</summary>

### Element selector CSS adalah pola yang digunakan untuk memilih elemen HTML yang ingin diberi gaya. Ada beberapa jenis element selector CSS, antara lain:

* **Selektor tag** adalah selektor yang memilih elemen berdasarkan nama tag. Contohnya, `p { color: blue; }` akan memilih semua elemen `<p>` dan memberi warna teks biru. Selektor tag berguna untuk memberi gaya secara umum kepada elemen yang sama.

* **Selektor class** adalah selektor yang memilih elemen berdasarkan nama class yang diberikan. Selektor class dibuat dengan tanda titik di depannya. Contohnya, `.intro { font-size: 18px; }` akan memilih semua elemen yang memiliki atribut `class="intro"` dan memberi ukuran font `18px`. Selektor class berguna untuk memberi gaya khusus kepada elemen yang memiliki ciri tertentu.

* **Selektor ID** adalah selektor yang memilih elemen berdasarkan nama ID yang diberikan. Selektor ID dibuat dengan tanda pagar `(#)` di depannya. Contohnya, `#header { background: teal; }` akan memilih elemen yang memiliki atribut `id="header"` dan memberi warna latar belakang teal. Selektor ID berguna untuk memberi gaya unik kepada elemen yang hanya ada satu di halaman web.

* **Selektor atribut** adalah selektor yang memilih elemen berdasarkan atribut tertentu. Selektor atribut dibuat dengan tanda kurung siku `[ ]`. Contohnya, `input[type="text"] { border: 1px solid black; }` akan memilih semua elemen `<input>` yang memiliki atribut `type="text"` dan memberi garis tepi hitam. Selektor atribut berguna untuk memberi gaya spesifik kepada elemen yang memiliki nilai atribut tertentu.

* **Selektor universal** adalah selektor yang memilih semua elemen pada jangkauan (scope) tertentu. Selektor universal dibuat dengan tanda bintang `*`. Contohnya, `* { margin: 0; }` akan memilih semua elemen dan memberi margin nol. Selektor universal berguna untuk me-reset gaya bawaan dari browser atau memberi gaya dasar kepada semua elemen.

* **Selektor pseudo** adalah selektor yang memilih elemen berdasarkan keadaan atau posisi tertentu. Selektor pseudo dibuat dengan tanda titik dua `:`. Contohnya, `a:hover { color: red; }` akan memilih semua elemen `<a>` saat kursor mouse berada di atasnya dan memberi warna teks merah. Selektor pseudo berguna untuk memberi gaya dinamis kepada elemen sesuai dengan interaksi pengguna atau struktur dokumen.

Link Referensi
</details>

<details>
<summary>2. Jelaskan HTML5 Tag yang kamu ketahui.</summary>

### HTML5 tag adalah tag yang digunakan untuk membuat dokumen HTML versi 5, yang merupakan standar terbaru untuk web. HTML5 tag memiliki beberapa fitur baru dan perbaikan dari versi sebelumnya, seperti:

* **Tag semantik** adalah tag yang memberikan makna lebih kepada elemen HTML, sehingga memudahkan mesin pencari dan browser untuk memahami struktur dan konten web. Contohnya, tag `<header>`, `<footer>`, `<nav>`, `<article>`, `<section>`, `<aside>`, dan lain-lain.

* **Tag multimedia** adalah tag yang memungkinkan untuk menyisipkan konten audio dan video tanpa perlu plugin tambahan. Contohnya, tag `<audio>` dan `<video>`.

* **Tag grafis** adalah tag yang memungkinkan untuk menggambar grafis 2D dan 3D secara dinamis dengan menggunakan JavaScript. Contohnya, tag `<canvas>` dan `<svg>`.

* **Tag form** adalah tag yang menambahkan beberapa jenis input baru dan atribut baru untuk elemen form. Contohnya, tag `<datalist>`, `<output>`, `<progress>`, `<meter>`, dan lain-lain.

* **Tag struktur** adalah tag yang menentukan tipe dokumen HTML dan bahasa yang digunakan. Contohnya, tag `<!DOCTYPE html>` dan `<html lang="id">`.

</details>

<details>
<summary>3. Jelaskan perbedaan antara margin dan padding.</summary>

### Margin dan padding adalah dua properti CSS yang sering digunakan untuk mengatur jarak antara elemen HTML. Kedua hal ini merupakan bagian dari Box Model pada CSS dengan gambar berikut:

![boxModel](https://hackmd.io/_uploads/B1QiTx9ya.png)

### Berikut adalah beberapa perbedaan antara margin dan padding:

| Margin | Padding |
| --- | --- |
| Jarak antara batas (border) elemen dengan elemen lain di sekitarnya | Jarak antara batas (border) elemen dengan konten (content) elemen itu sendiri|
| Tidak termasuk dalam ukuran elemen | Termasuk dalam ukuran elemen |
| Tidak terpengaruh oleh warna latar belakang (background color) atau gambar latar belakang (background image) elemen| Terpengaruh oleh background color dan background image|
| Tidak memengaruhi ukuran elemen itu sendiri | Memengaruhi ukuran elemen hingga dapat memperluas elemen dan meningkatkan ukurannya jika menambahkan padding tersebut. |


</details>

<details>
<summary>4. Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?</summary>

### *Bootstrap* adalah framework front-end yang menyediakan sekumpulan komponen HTML, CSS, dan JavaScript yang telah dibuat sebelumnya.

Komponen-komponen ini dapat digunakan untuk membuat antarmuka pengguna yang responsif dan mobile-friendly dengan cepat dan mudah12. Bootstrap memiliki desain yang terstruktur dan konsisten, tetapi mungkin kurang fleksibel untuk membuat desain yang unik dan kreatif.

### *Tailwind* adalah framework front-end baru yang tidak menyediakan komponen siap pakai, tetapi terdapat utilitas yang dapat digabungkan untuk desain sesuai kebutuhan.

Tailwind memberikan kebebasan kreatif yang lebih besar, tetapi mungkin memerlukan waktu dan usaha yang lebih banyak untuk membuat antarmuka pengguna yang responsif dan mobile-friendly.

Beberapa perbedaan yang signifikan pada Tailwind dan Bootstrap dapat dilihat pada tabel berikut:

| Tailwind | Bootstrap |
| --- | --- |
|file CSS yang lebih kecil karena hanya memuat kelas-kelas utilitas yang ada| file CSS yang lebih besar karena banyak komponen yang telah didefinisikan |
| Memiliki fleksibilitas dan adaptibilitas tinggi terhadap proyek | Seringkali menghasilkan tampilan yang konsisten |
| Memerlukan pemahaman terhadap kelas-kelas utilitas yang tersedia dan bagaimana memodifikasinya sesuai dengan keinginan masing-masing | Beginner-friendly, memiliki pembelajaran yang cepat untuk pemula karena dapat mulai dengan komponen yang telah tersedia |

</details>

<details>
<summary>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

- [x] Kustomisasi desain pada templat HTML yang telah dibuat pada Tugas 4 dengan menggunakan CSS atau CSS framework (seperti Bootstrap, Tailwind, Bulma) dengan ketentuan sebagai berikut
    - [x] Kustomisasi halaman login, register, dan tambah inventori semenarik mungkin.

    1. Pertama saya kustomisasi halaman login dengan melingkupi keseluruhan halaman dalam satu tag `<div class="container">`. Keseluruhan class `container` ini saya atur dengan CSS yang embed dengan codingan pada tag `<style></style>` berikut
    ```css
    .container{
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        justify-content: center;
        align-items: center;
    }
    ```
    class `container` ini menerapkan tampilan secara flex dan menampilkan elemen secara kolom atau menurun. Serta menengahkan elemen-elemen tersebut.

    Selanjutnya, saya mengubah keseluruhan font dari halaman dengan menggunakan font `font-family = "Andy Bold V2"` dengan sebelumnya mengimport font tersebut dari suatu url dan menaruhnya seperti berikut
    ```css
    @font-face {
        font-family: "Andy Bold V2";
        src: url("https://db.onlinewebfonts.com/t/775c3814e9c1f228d495333e07580d59.eot");
        src: url("https://db.onlinewebfonts.com/t/775c3814e9c1f228d495333e07580d59.eot?#iefix")format("embedded-opentype"),
        url("https://db.onlinewebfonts.com/t/775c3814e9c1f228d495333e07580d59.woff2")format("woff2"),
        url("https://db.onlinewebfonts.com/t/775c3814e9c1f228d495333e07580d59.woff")format("woff"),
        url("https://db.onlinewebfonts.com/t/775c3814e9c1f228d495333e07580d59.ttf")format("truetype"),
        url("https://db.onlinewebfonts.com/t/775c3814e9c1f228d495333e07580d59.svg#Andy Bold V2")format("svg");
    }

    * {
        font-family:"Andy Bold V2";
    }
    ```

    Lalu, saya memisahkan tiap elemen judul pada class `title`, input login pada class `login`, messages dari modul Django pada class `messages`, dan terakhir link yang redirect ke halaman registrasi dengan class `registration box`. Adapun struktur HTML nya sebagai berikut

    ```html
    <div class = "container">
        ...
        <div class = "title">
            ...
        </div>
        ...
        <div class = "login">
            ...
        </div>
        ...
        <div class = "messages_box">
            ...
        </div>
        ...
        <div class = "register_box">
            ...
        </div>
    </div>
    ```



    Pada `login` dan `registration box` saya membuat properti box-shadow untuk mengcontain elemen tersebut dengan styling berikut `style="background-color: rgba(52, 48, 92, 0.8); padding: 10px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);"`. Lalu tiap input text dan password menyesuaikan agar mendapatkan tema background dan font yang sama.

    Agar memiliki background yang menarik, saya menaruh url pada background-image `background-image: url('https://forums.terraria.org/index.php?attachments/n-2-png.31584/');` dan mengatur agar gambar tersebut menutup keseluruhan halaman dengan `background-size: cover;`.

    Pada button dan link saya mengkustomisasi agar button atau link tersebut membesar ketika cursor menghovernya dengan kode berikut

    ```css
    .login_btn{
        background-color: transparent;
        color: #fff;
        border: none;
        cursor: pointer;
        text-shadow: 0px 0px 5px #000000;
        font-size: large;
    }
    .login_btn:hover{
        transform: scale(1.65);
        color:#fed405;
    }
    ```

    2. Pada halaman register, saya banyak mengadaptasi berdasarkan halaman login seperti container flex secara kolom dan wrap, serta menengahkan keseluruhan elemen.

    Halaman ini memiliki 2 class yaitu `register_form` sebagai input user untuk registrasi akun baru dan `login_box` untuk mengarahkan halaman kembali ke halaman login.

    Register form memiliki styling CSS sebagai berikut

    ```css
    .register_form{
        background: rgba(52, 48, 92, 0.8); 
        padding: 30px; 
        border-radius: 10px; 
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
    }
    .submit_btn{
        background-color: transparent;
        border: none;
        cursor: pointer;
        color:white;
        text-shadow: 0px 0px 5px #000000;
        font-family: "Andy Bold V2";
        font-size: 24px;
    }
    .submit_btn:hover{
        transform: scale(1.65);
        color:#fed405;
    }
    ```

    Pada button submit tersebut saya menyamakan tema utamanya agar ketika dihover, button atau link tersebut akan memperbesar scalenya.

    Pada `login_box` saya juga menerapkan yang sama agar memiliki container box shadow yang sama dengan styling secara inline `style="background-color: rgba(52, 48, 92, 0.8); padding: 10px; border-radius: 10px; box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);"`.

    Dan tambahan styling css berikut

    ```css
    a{
        color:white;
        font-family: "Andy Bold V2";
        text-shadow: 0px 0px 5px #000000;      
    }
    .login_link:hover{
        color:#fed405;
        font-size: 1.2rem;
    }
    .login_box{
        margin: 10px 0px 0px 0px;
    }
    ```

    3. Begitu pun juga untuk halaman menambahkan inventori atau `create_item.html`, saya menerapkan styling yang kurang lebih sama namun akan diubah ke depannya agar mendapatkan styling yang tidak monoton pada setiap halaman

    - [x] Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan **Card**.

    Pada halaman daftar inventory ataupun `main.html`, saya masih menampilkan item-item secara tabel, tetapi menambahkan navbar pada posisi paling atas dengan posisinya yang fix tidak berpindah.

    Untuk keseluruhan elemen pada halaman ini masih sama dicontain oleh suatu class `container` yang memiliki styling yang sama seperti berikut

    ```css
    .container{
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        justify-content: center;
    }

    * {
        font-family: "Andy Bold V2";
    }
    ```

    Selanjutnya saya menambahkan elemen navbar sebagai wadah untuk menavigasi (saat ini hanya navigasi ke halaman login dengan cara logout). Struktur HTMLnya dan styling CSSnya adalah sebagai berikut

    ```html
    <nav class="navbar">
            <ul>
                <li><a>{{ name }}</a></li>
                <li><a href="{% url 'main:logout' %}">
                    <button>
                    Logout
                    </button>
                </a></li>
            </ul>
        </nav>
    ```

    ```css
    .navbar {
        position: fixed; /* Membuat navbar tetap di atas halaman */
        top: 0;
        left: 0;
        width: 100%; /* Mengisi seluruh lebar halaman */
        background-color: rgba(54, 53, 131, 0.8);
        font-size: large;
        z-index: 1000; /* Untuk menempatkan navbar di atas konten lainnya */
    }

    .navbar ul {
        list-style-type: none;
        margin: 0;
        padding: 0;
        overflow: hidden;
    }

    .navbar li {
        float: left;
    }

    .navbar li a {
        display: block;
        color: white;
        text-align: center;
        padding: 14px 16px;
        text-decoration: none;
    }
    ```

    Untuk sementara pada table, saya menyesuaikan background color serta fontnya sesuai dengan styling berikut

    ```css
    table, th, td {
        border: 1px solid white;
    }

    th, td {
        padding: 8px;
        text-align: left;
        color: white;
        text-shadow: 0px 0px 5px #000000;
    }

    .judul_table {
        background-color: rgba(54, 53, 131, 1);
    }
    ```

    Serta karena saya sudah menambahkan button untuk menghapus sebuah item, button tersebut saya modifikasi agar memiliki gambar png daripada sebuah label button. Hal ini saya optimisasi dengan cara berikut:

    ```html
    <td>
        <form method="post" action="{% url 'main:trash_item' item.id %}">
            {% csrf_token %}
            <button type="submit"><img src="https://static.wikia.nocookie.net/terraria_gamepedia/images/b/b1/Trash_Slot.png/revision/latest?cb=20171214025354&format=original" /></button>
        </form>
    </td>
    ```

- [x] `add`-`commit`-`push` ke GitHub.

</details>

---

# Tugas 6

<details>
<summary>1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.</summary>

#### Asynchronous programming dan synchronous programming adalah dua model pemrograman yang berbeda. Berikut adalah tiga perbedaan antara keduanya:

| Asynchronous programming | Synchronous programming |
| --- | --- |
|Asynchronous programming memungkinkan beberapa tugas berjalan secara bersamaan atau mandiri tanpa harus menunggu tugas lain selesai | Synchronous programming mengharuskan setiap tugas berjalan secara berurutan dan menunggu tugas sebelumnya selesai |
| Asynchronous programming cocok untuk komputasi terdistribusi, di mana beberapa proses dapat berkomunikasi dan berkolaborasi secara jaringan | Synchronous programming lebih sesuai untuk sistem reaktif, di mana setiap proses harus memberikan respons yang cepat dan konsisten |
|Asynchronous programming memiliki kurva belajar yang lebih tinggi daripada synchronous programming. Asynchronous programming bisa lebih sulit dimengerti karena memerlukan pengetahuan tentang callback, promise, async/await, dan konsep lainnya |Synchronous programming mudah dipahami karena mengikuti alur eksekusi yang jelas dan linier |

</details>

<details>
<summary>2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.</summary>

#### Paradigma event-driven programming adalah paradigma pemrograman di mana alur program ditentukan oleh kejadian-kejadian (events) yang terjadi, seperti aksi pengguna dari mouse, keyboard, touchpad, dan layar sentuh. Kejadian-kejadian ini dipantau oleh kode yang disebut event listener. Jika event listener mendeteksi bahwa event yang ditugaskan telah terjadi, maka ia akan menjalankan event handler (fungsi atau metode yang dipanggil ketika event terjadi).

#### Salah satu contoh penerapan paradigma event-driven programming pada tugas ini adalah ketika kita menggunakan AJAX untuk mengirim permintaan ke server tanpa harus memuat ulang halaman web. AJAX menggunakan objek XMLHttpRequest untuk membuat permintaan asinkron ke server. Objek ini memiliki properti onreadystatechange yang merupakan sebuah event listener. Properti ini menetapkan sebuah fungsi yang akan dijalankan ketika status permintaan berubah. Fungsi ini adalah event handler yang dapat memproses respons dari server dan memperbarui halaman web sesuai dengan respons tersebut.

contoh implementasinya:
```js
async function refreshCards() {
        document.getElementById("item_cards").innerHTML = ""
        const items = await getItems()
        let htmlString = ""
        items.forEach((item) => {
            htmlString += `
            <div class="card">
                <div class="card-body">
                    <h2>${item.fields.name}</h2>
                    <p><img src="${item.fields.link_image}" alt="{ item.name }"></p>
                    <div class="item-description">
                        <p>Description: ${ item.fields.description }</p>
                        <p>Amount: ${ item.fields.price }</p>
                        <p>Type: ${ item.fields.item_level }</p>
                        <p>Amount: ${ item.fields.amount }</p>
                        </div>
                    <a><button onclick="trashItem(${item.pk})" type="submit"><img src="https://static.wikia.nocookie.net/terraria_gamepedia/images/b/b1/Trash_Slot.png/revision/latest?cb=20171214025354&format=original" /></button></a>
                </div>
            </div>` 
        })
        
        document.getElementById("item_cards").innerHTML = htmlString
    }
    function addItem() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItems)
        .then(refreshCards)

        document.getElementById("form").reset()
        return false
    }
    document.getElementById("button_add").onclick = addItem
```


</details>

<details>
<summary>
3. Jelaskan penerapan asynchronous programming pada AJAX.</summary>

#### Asynchronous programming adalah pemrograman yang memungkinkan beberapa tugas berjalan secara bersamaan atau mandiri tanpa harus menunggu tugas lain selesai. AJAX adalah singkatan dari Asynchronous JavaScript and XML, yang merupakan teknik untuk membuat permintaan asinkron ke server web menggunakan JavaScript dan XML.

Penerapan asynchronous programming pada AJAX adalah sebagai berikut:

* AJAX menggunakan objek XMLHttpRequest untuk membuat permintaan asinkron ke server web. Objek ini memiliki properti onreadystatechange yang merupakan sebuah event listener. Properti ini menetapkan sebuah fungsi yang akan dijalankan ketika status permintaan berubah. Fungsi ini adalah event handler yang dapat memproses respons dari server dan memperbarui halaman web sesuai dengan respons tersebut.

* AJAX memungkinkan halaman web untuk mengirim dan menerima data dari server web tanpa harus memuat ulang halaman web. Hal ini meningkatkan performa dan pengalaman pengguna, karena mereka tidak perlu menunggu halaman web selesai dimuat untuk melihat hasil permintaan mereka.

* AJAX juga memungkinkan halaman web untuk mengirim dan menerima data dari server web secara selektif, hanya mengambil data yang dibutuhkan dan tidak perlu mengambil seluruh halaman web. Hal ini menghemat bandwidth dan sumber daya, karena hanya data yang relevan yang dikirim dan diterima.

</details>

<details>
<summary>
4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.</summary>

#### Penerapan AJAX dengan menggunakan Fetch API dan jQuery adalah dua pendekatan yang berbeda dalam mengintegrasikan teknologi AJAX ke dalam proyek web.

1. **Fetch API**:
Vanilla JavaScript: Fetch API adalah bagian dari JavaScript itu sendiri, yang berarti Anda tidak perlu mengunduh atau memasang library tambahan. Ini adalah pendekatan JavaScript murni.
Modern Standard: Fetch API adalah standar modern yang direkomendasikan oleh World Wide Web Consortium (W3C) dan merupakan cara yang direkomendasikan oleh komunitas web untuk mengambil dan mengirim data secara asinkron.
Promise-Based: Fetch API mengembalikan objek Promise, yang memungkinkan Anda mengatasi permintaan HTTP dengan lebih baik menggunakan async/await atau konsep Promise.
Lebih Ringan: Lebih ringan dalam hal ukuran, yang berarti tidak ada overheard library yang harus diunduh.
2. **jQuery**:
Library: jQuery adalah library JavaScript yang memiliki banyak fitur, dan AJAX adalah salah satu komponennya. Saat Anda menggunakan jQuery untuk AJAX, Anda juga mendapatkan akses ke banyak fitur dan utilitas lain yang disediakan oleh jQuery.
Sintaksis yang Mudah: Sintaksis jQuery umumnya dianggap lebih sederhana dan mudah dipahami oleh pengembang pemula.
Kompatibilitas Browser yang Baik: jQuery dirancang untuk mendukung berbagai jenis browser yang berbeda. Itu bisa menjadi pilihan yang baik jika Anda perlu memastikan kompatibilitas lintas browser yang kuat.


Pilihan antara Fetch API dan jQuery untuk penggunaan AJAX tergantung pada kebutuhan dan preferensi pengembang. Berikut adalah beberapa pertimbangan:

* Proyek Modern: Untuk proyek-proyek modern dengan dukungan browser yang baik, Fetch API adalah pilihan yang kuat. Ini adalah pendekatan JavaScript murni dan merupakan standar modern yang dianjurkan.

* Kebutuhan Library Tambahan: Jika Anda memerlukan banyak fitur tambahan yang disediakan oleh jQuery, seperti animasi, manipulasi DOM, dan lainnya, jQuery mungkin menjadi pilihan yang baik.

* Sintaksis dan Kekuatan: Fetch API lebih kuat dan ekspresif dalam hal mengelola permintaan HTTP, terutama ketika digunakan bersama dengan async/await. Namun, jika Anda mengutamakan kesederhanaan sintaksis dan sudah akrab dengan jQuery, Anda mungkin merasa lebih nyaman dengan jQuery.

* Ukuran dan Kinerja: Fetch API lebih ringan dari segi ukuran, dan dapat mengurangi overhead yang dihasilkan dari penggunaan library tambahan. Ini dapat berkontribusi pada kinerja yang lebih baik.

#### Kesimpulannya, jika Anda memiliki proyek modern dan ingin memanfaatkan fitur JavaScript ES6, Fetch API adalah pilihan yang lebih baik. Namun, jika Anda sudah akrab dengan jQuery atau memerlukan banyak fitur tambahan yang disediakan oleh jQuery, itu masih merupakan pilihan yang valid. Sebaiknya pilih teknologi yang sesuai dengan kebutuhan proyek Anda.

</details>

<details>
<summary>
5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>

- [x] AJAX GET

    - [x] Ubahlah kode cards data item agar dapat mendukung AJAX GET.

    Adapun pengubahan menjadi cards sebagai berikut

    ```js
    <script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }

    async function refreshCards() {
        document.getElementById("item_cards").innerHTML = ""
        const items = await getItems()
        let htmlString = ""
        items.forEach((item) => {
            htmlString += `
            <div class="card">
                <div class="card-body">
                    <h2>${item.fields.name}</h2>
                    <p><img src="${item.fields.link_image}" alt="{ item.name }"></p>
                    <div class="item-description">
                        <p>Description: ${ item.fields.description }</p>
                        <p>Amount: ${ item.fields.price }</p>
                        <p>Type: ${ item.fields.item_level }</p>
                        <p>Amount: ${ item.fields.amount }</p>
                        </div>
                    <a><button onclick="trashItem(${item.pk})" type="submit"><img src="https://static.wikia.nocookie.net/terraria_gamepedia/images/b/b1/Trash_Slot.png/revision/latest?cb=20171214025354&format=original" /></button></a>
                </div>
            </div>` 
        })
        
        document.getElementById("item_cards").innerHTML = htmlString
    }
    ```

    - [x] Lakukan pengambilan task menggunakan AJAX GET.

    get dilakukan sebagai berikut

    ```js
    <script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }

    ```

- [x] AJAX POST

    - [x] Buatlah sebuah tombol yang membuka sebuah modal dengan form untuk menambahkan item.

    Pertama saya hapus button untuk add item sebelumnya, lalu menambahkan modal sebagai berikut dengan menyesuaikan models yang saya buat

    ```html
    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog">
        <div class="modal-content">
            <div class="modal-header">
                <h1 class="modal-title fs-5" id="exampleModalLabel">Add New Item</h1>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
            </div>
            <div class="modal-body">
                <form id="form" onsubmit="return false;">
                    {% csrf_token %}
                    <div class="mb-3">
                        <label for="name" class="col-form-label">Name:</label>
                        <input type="text" class="form-control" id="name" name="name"></input>
                    </div>
                    <div class="mb-3">
                        <label for="description" class="col-form-label">Description:</label>
                        <textarea class="form-control" id="description" name="description"></textarea>
                    </div>
                    <div class="mb-3">
                        <label for="price" class="col-form-label">Price:</label>
                        <input type="number" class="form-control" id="price" name="price"></input>
                    </div>
                    <div class="mb-3">
                        <label for="item_level" class="col-form-label">Item Level:</label>
                        <input type="number" class="form-control" id="item_level" name="item_level"></input>
                    </div>
                    <div class="mb-3">
                        <label for="amount" class="col-form-label">Amount:</label>
                        <input type="number" class="form-control" id="amount" name="amount"></input>
                    </div>
                    <div class="mb-3">
                        <label for="link_image" class="col-form-label">Link Image:</label>
                        <textarea class="form-control" id="link_image" name="link_image"></textarea>
                    </div>
                </form>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary" id="button_add" data-bs-dismiss="modal">Add Item</button>
            </div>
        </div>
    </div>
    </div>
    ```

    Modal berikut akan muncul ketika di trigger pada tombol `<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Add Item by AJAX</button>`

    - [x] Modal di-trigger dengan menekan suatu tombol pada halaman utama. Saat penambahan item berhasil, modal harus ditutup dan input form harus dibersihkan dari data yang sudah dimasukkan ke dalam form sebelumnya.

    Selanjutnya membuat scripts js untuk membuatnya fungsional
    
    ```html
    <script>
    async function getItems() {
        return fetch("{% url 'main:get_item_json' %}").then((res) => res.json())
    }

    async function refreshCards() {
        document.getElementById("item_cards").innerHTML = ""
        const items = await getItems()
        let htmlString = ""
        items.forEach((item) => {
            htmlString += `
            <div class="card">
                <div class="card-body">
                    <h2>${item.fields.name}</h2>
                    <p><img src="${item.fields.link_image}" alt="{ item.name }"></p>
                    <div class="item-description">
                        <p>Description: ${ item.fields.description }</p>
                        <p>Amount: ${ item.fields.price }</p>
                        <p>Type: ${ item.fields.item_level }</p>
                        <p>Amount: ${ item.fields.amount }</p>
                        </div>
                    <a><button onclick="trashItem(${item.pk})" type="submit"><img src="https://static.wikia.nocookie.net/terraria_gamepedia/images/b/b1/Trash_Slot.png/revision/latest?cb=20171214025354&format=original" /></button></a>
                </div>
            </div>` 
        })
        
        document.getElementById("item_cards").innerHTML = htmlString
    }

    async function refreshItems() {
        document.getElementById("item_table").innerHTML = ""
        const items = await getItems()
        let htmlString = `<tr>
            <th>Image</th>
            <th>Name</th>
            <th>Description</th>
            <th>Price</th>
            <th>iLvl</th>
            <th>Amount</th>
        </tr>`
        items.forEach((item) => {
            htmlString += `\n<tr>
            <td><img src="${item.fields.link_image}" alt="{ item.name }"></td>
            <td>${item.fields.name}</td>
            <td>${item.fields.description}</td>
            <td>${item.fields.price}</td>
            <td>${item.fields.item_level}</td>
            <td>${item.fields.amount}</td>
        </tr>` 
        })
        
        document.getElementById("item_table").innerHTML = htmlString
    }

    refreshItems()
    refreshCards()

    function addItem() {
        fetch("{% url 'main:add_item_ajax' %}", {
            method: "POST",
            body: new FormData(document.querySelector('#form'))
        }).then(refreshItems)
        .then(refreshCards)

        document.getElementById("form").reset()
        return false
    }
    document.getElementById("button_add").onclick = addItem

    
    </script>
    ```

    - [x] Buatlah fungsi view baru untuk menambahkan item baru ke dalam basis data.

    pada `views.py`, fungsinya pun sebagai berikut

    ```python
    @csrf_exempt
    def add_item_ajax(request):
        if request.method == 'POST':

            name = request.POST.get("name")
            amount = request.POST.get("amount")
            price = request.POST.get("price")
            description = request.POST.get("description")
            link_image = request.POST.get("link_image")
            item_level = request.POST.get("item_level")
            user = request.user

            if amount and price and item_level:
                amount = int(amount)
                price = int(price)
                item_level = int(item_level)
                new_item = Item(name=name, amount=amount, price=price, description=description, link_image=link_image, item_level=item_level, user=user)
                new_item.save()
                return HttpResponse(b"CREATED", status=201)

        return HttpResponseNotFound()
    ```

    - [x] Buatlah path /create-ajax/ yang mengarah ke fungsi view yang baru kamu buat.

    melakukan routing sebagai berikut pada `urls.py`
    ```python
    urlpatterns = [
        path('create-item-ajax/', add_item_ajax, name='add_item_ajax'),
        path('delete-item-ajax/<int:item_id>/', delete_item_ajax, name='delete_item_ajax')
    ]
    ```

    - [x] Hubungkan form yang telah kamu buat di dalam modal kamu ke path /create-ajax/.

    Menambahkan atribut `onclick=addItem` pada tombol `Add Item` dalam modal, agar ketika tombol di 'click' membuat item baru

    - [x] Lakukan refresh pada halaman utama secara asinkronus untuk menampilkan daftar item terbaru tanpa reload halaman utama secara keseluruhan.

    Melakukan refresh cards dan refresh table setiap terjadi perubahan pada items (menghapus item, membuat item)

    ```js
    .then(refreshItems)
    .then(refreshCards)
    ```

- [x] Melakukan perintah collectstatic.

Terakhir saya melakukan collecstatic dengan perintah berikut pada command terminal

```
(env) C:\Ngoding\Pemrograman Berbasis Platform\adventurers_inventory>python manage.py collectstatic

125 static files copied to 'C:\Ngoding\Pemrograman Berbasis Platform\adventurers_inventory\static'.
```

</details>