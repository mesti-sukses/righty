# Righty - Tool That Make You A Right-Typer

Sesuai dengan namanya, tool kali ini membuat kalian menjadi seorang pengetik yang lebih benar dan baku (sesuai dengan bahasa Indonesia yang berlaku)

Kami menggunakan library tesseract untuk mengenali teks dalam gambar sehingga bisa digunakan untuk mengecek berbagai macam tulisan yang ada. Penginstallannya cukup mudah, hampir seperti nodeJS dan npm karena kami menggunakan *pipenv* sebagai project manager kami.

1. Pertama kalian harus menginstall pip terlebih dahulu pada sistem kalian  
Karena kami menggunakan sistem operasi ArchLinux maka kami menggunakan pacman untuk menginstallnya
`sudo pacman -S python-pip`

2. Lalu install pipenv menggunakan pip sebagai project manager kita  
`pip install pipenv`

3. Setelah itu kalian bisa clone git ini dengan perintah git clone

4. Baru kemudian pindah ke dalam direktori tempat repository ini berada dan melakukan penginstallan depedency
`pipenv install`

5. Setelah itu install juga depedency tesseract mandiri untuk engine OCR nya

6. Baru kemudian masuk kedalam pipenv shell dan mengeksekusi main.py
`pipenv shell`
`pipenv run python main.py`

7. Kalian bisa mengakses tool ini dengan menggunakan alamat
`http://localhost:5000

Gunakan dengan sebaik-baiknya agar kalian tidak salah ketik lagi.
