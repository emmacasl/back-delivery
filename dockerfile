# Usar una imagen base de Python
FROM python:3.9

# Establecer los argumentos de construcción para las credenciales
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

# Establecer las variables de entorno a partir de los argumentos
ENV DB_NAME=$DB_NAME
ENV DB_USER=$DB_USER
ENV DB_PASSWORD=$DB_PASSWORD
ENV DB_HOST=$DB_HOST
ENV DB_PORT=$DB_PORT

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
EXPOSE 8001

# Iniciar Nginx y Gunicorn
CMD ["sh", "-c", "nginx && gunicorn --bind 0.0.0.0:8001 djangoDelivery.wsgi:application"]
