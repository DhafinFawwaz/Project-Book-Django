<h1 align="center">Project Book</h1>
![Preview](Images/Preview.png)

Tugas besar mata kuliah Pengenalan Komputasi Institut Teknologi Bandung. Project berupa website eccomerce buku. Dapat di akses pada https://tubes-eccomerce.herokuapp.com/
Update, heroku sudah tidak gratis lagi, jadi silahkan ikuti instruksi di bawah saja

## 📖 Instruction
### ✨ Getting Started

Run the following command to get started. Just copy, paste, execure these commands. The local website is usually http://127.0.0.1:8000/. If you just copy paste these commands, don't forget to execute the latest line.
```
git clone https://github.com/DhafinFawwaz/Project-Book-Django.git
cd ./Project-Book-Django
py -m venv venv
venv\Scripts\activate.bat
py -m pip install Django
py -m pip install Pillow
cd ./ProjectBook
py -m pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
py manage.py runserver

```

### 🔃 Run Local Server
Run following command to run the server locally
```
venv\Scripts\activate.bat
cd ./ProjectBook
py manage.py runserver
```
