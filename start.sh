python -m pip install django
cd server
python manage.py makemigrations
python manage.py migrate
python manage.py runserver