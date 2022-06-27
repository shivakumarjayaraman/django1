django-admin startproject django_project .

./manage.py startapp pages

django_project/settings.py : INSTALLED_APPS
     pages/apps.py (add app in)
pages/views.py : write a function
pages/urls.py : configure that function to be called for a path
django_project/urls.py : configure a path that include("pages.urls")


./manage.py runserver
