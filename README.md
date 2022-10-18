<h1 align="center">Project Book</h1>

Tugas besar mata kuliah Pengenalan Komputasi Institut Teknologi Bandung. Project berupa website eccomerce buku.


## 📖 Instruction
### ✨ Getting Started

Run the following command to get started. Just copy, paste, execure these commands. The local website is usually http://127.0.0.1:8000/
```
git clone https://github.com/DhafinFawwaz/Project-Book.git
cd ./Project-Book
py -m venv venv
venv\Scripts\activate.bat
py -m pip install Django
py -m pip install Pillow
py -m pip install -r requirements.txt
cd ./ProjectBook
python manage.py makemigrations
python manage.py migrate
py manage.py runserver
```

### 🔃 Run Local Server
Run following command to run the server locally
```
cd ./ProjectBook
py manage.py runserver
```

### 🤖 Enable Auto Reload
Run the following command to enable auto refresh when saving
```
py -m pip install django-livereload-server
```
Add ``'livereload'`` to the ``INSTALLED_APPS``, before ``'django.contrib.staticfiles'`` if this is used::

    INSTALLED_APPS = (
        ...
        'livereload',
        ...
    )

Next you need to inject the loading of the livereload javascript. You can do this in one of two ways:

* Through middleware by adding  ``'livereload.middleware.LiveReloadScript'`` to ``MIDDLEWARE_CLASSES`` (probably at the end)::

    MIDDLEWARE_CLASSES = (
        ...
        'livereload.middleware.LiveReloadScript',
    )

* Through a templatetag in your ``base.html`` (or similar) template::

    {% load livereload_tags %}
    ...
    {% livereload_script %}
    </head>

Either of these options will inject the ``livereload.js`` script into your webpages if ``DEBUG`` setting is on.

* Run the local server by
```
cd ./ProjectBook
python manage.py runserver localhost:8000
```
* Run in other bash
```
cd ./ProjectBook
python manage.py livereload
```
It will have a different link which is localhost:8000. Save the project again if it won't immedietly reload