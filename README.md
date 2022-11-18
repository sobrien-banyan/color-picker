# color picker

## steps taken to create this
1. Create virtual environment  ->      ‘python3 -m venv venv’
2. Activate it  ->   source venv/bin/activate
3. Install Django ‘pip3 install django’
4. Create a django project with ‘django-admin startproject <project_name>’
5. ‘pip3 freeze > requirements.txt’
6. Run ‘python3 manage.py runserver’ to see if it worded. -> install Django in the app  ` ‘pip install django’`
7. Create an ‘app’ inside your project with ‘python3 manage.py startapp <app_name>’
8. Install your new app in your projects setting file


### In paint_site/setting add:
```
INSTALLED_APPS = [
    'paint_app.apps.PaintAppConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

### In paint_app/urls.py add:
```
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sandwich/', include('sandwich_app.urls')),
]
```

### In sandwich_app create a file called urls.py and add:
```
from django.urls import path

urlpatterns = []
```