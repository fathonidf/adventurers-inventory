# :school_satchel: Adventurer's Inventory :tent:
`Daffa Mohamad Fathoni 2206824161
PBP E`

## Tautan Aplikasi
[Link to Adventurer's Inventory](https://adventurers-inventory.adaptable.app/main)
(*sebelum deactivated*)


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

1. Disalahgunakan oleh pihak ketiga yang tidak berwenang untuk melacak aktivitas online pengguna, mengumpulkan data pribadi.

2. Dicuri peretas untuk mengakses informasi sensitif seperti data, token, kredensial dengan tujuan pencurian, pembajakan, atau penipuan.

3. Dapat menimbulkan masalah privasi dan keamanan jika tidak dikelola dengan baik oleh pengembang web, seperti tidak menghapus cookie yang sudah tidak diperlukan atau tidak mengenkripsi cookie yang berisi data penting.

Beberapa hal yang bisa dijadikan sebagai *Best Practice* untuk diikuti seperti:

1. Menggunakan cookie pihak pertama untuk situs web sendiri

2. Cookie hanya berlaku selama pengguna **sedang** menjelajah situs web

3. Menggunakan cookie untuk data yang benar-benar diperlukan untuk fungsionalitas web

4. Hanya dapat diakses melalui protokol HTTPS yang aman.

</details>

<details>
<summary>5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).</summary>
</details>
