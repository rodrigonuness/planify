#!/bin/bash

echo "Instalando dependências do backend..."
pip install django djangorestframework pandas openpyxl django-cors-headers

echo "Aplicando migrações do backend..."
python manage.py makemigrations
python manage.py migrate

echo "Iniciando servidor backend..."
nohup python manage.py runserver 0.0.0.0:8000 &

echo "Instalando dependências do frontend..."
cd frontend
npm install

echo "Iniciando servidor frontend..."
nohup npm start &

echo "Setup completo! Acesse http://localhost:3000"
