#!/bin/bash

# Mueve archivos estáticos generados a la carpeta correspondiente
echo "Moviendo archivos estáticos generados..."
mv tabbycat/static/vue/* $HOME/site/wwwroot/static/vue/
mv tabbycat/static/css/* $HOME/site/wwwroot/static/css/
mv tabbycat/static/js/vendor/* $HOME/site/wwwroot/static/js/vendor/
mv tabbycat/static/fonts/* $HOME/site/wwwroot/static/fonts/
mv tabbycat/static/jsi18n/* $HOME/site/wwwroot/static/jsi18n/

# Instala dependencias de Python
echo "Instalando dependencias de Python..."
pip install -r requirements.txt

# Recoge archivos estáticos
echo "Recogiendo archivos estáticos..."
python tabbycat/manage.py collectstatic --noinput

# Inicia el servidor de Django usando Gunicorn
echo "Iniciando el servidor de Django..."
gunicorn tabbycat.wsgi:application --bind=0.0.0.0 --timeout 600