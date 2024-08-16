# Usar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo en el contenedor
WORKDIR /app

# Copiar los archivos del proyecto al directorio de trabajo
COPY . /app

# Instalar las dependencias
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Ejecutar las migraciones y recopilar archivos estáticos
RUN python manage.py makemigrations seguridad delivery
RUN python manage.py migrate
#RUN python manage.py collectstatic --noinput
ENV DJANGO_SETTINGS_MODULE=djangoDelivery.settings.base
ENV PYTHONUNBUFFERED=1
RUN python manage.py collectstatic --noinput
# Exponer el puerto que Gunicorn usará
EXPOSE 8000

# Definir el comando por defecto para ejecutar Gunicorn
#CMD ["gunicorn", "--bind", "0.0.0.0:8000", "djangoDelivery.wsgi:application"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]