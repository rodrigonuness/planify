@echo off

echo Instalando dependencias do backend...
pip install django djangorestframework pandas openpyxl django-cors-headers

echo Aplicando migracoes do backend...
python manage.py makemigrations
python manage.py migrate

echo Iniciando servidor backend...
start cmd /k python manage.py runserver

echo Instalando dependencias do frontend...
cd frontend
npm install

echo Iniciando servidor frontend...
start cmd /k npm start

echo Setup completo! Acesse http://localhost:3000
