# Usar una imagen base de Python
FROM python:3.9

# Instalar Nginx
RUN apt-get update && apt-get install -y nginx

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al directorio de trabajo
COPY . /app

# Copiar la configuración de Nginx
COPY nginx.conf /etc/nginx/sites-available/default

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ejecutar las migraciones y recopilar archivos estáticos
RUN python manage.py makemigrations seguridad delivery
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

# Exponer el puerto que Gunicorn usará
EXPOSE 8000

# Iniciar Nginx y Gunicorn
CMD ["sh", "-c", "nginx && gunicorn --bind 0.0.0.0:8000 djangoDelivery.wsgi:application"]
