# Use the official Python base image
FROM python:3.10.4

# Set the working directory in the container
WORKDIR /black

# Set the locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Install system locales
RUN apt-get update && apt-get install -y locales locales-all

# Generate and set the desired locale
RUN locale-gen fa_IR.UTF-8
ENV LANG fa_IR.UTF-8
ENV LC_ALL fa_IR.UTF-8

# Copy project
COPY . .

# Create a virtual environment
RUN python -m venv data

# Activate the virtual environment
SHELL ["/bin/bash", "-c"]
RUN source data/bin/activate

RUN pip3 install --upgrade pip

# Install project dependencies
RUN pip3 install -r requirements.txt
RUN pip3 install wagtail-color-panel django-user-visit django-user-agents geoip2 django-summernote

# Run migrations
RUN python3 manage.py makemigrations --empty blog && python3 manage.py makemigrations --empty product && python3 manage.py makemigrations --empty category && python3 manage.py makemigrations --empty brand && python3 manage.py makemigrations --empty cart && python3 manage.py makemigrations user_accounts && python3 manage.py makemigrations index && python3 manage.py makemigrations product && python3 manage.py makemigrations blog && python3 manage.py makemigrations category && python3 manage.py makemigrations brand && python3 manage.py makemigrations cart
RUN python3 manage.py migrate

# Create a superuser
RUN echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('09129585714', 'QUEADMINISTRATOR174%!AbfsbflbdbPSJAFISHF@UNIQUEDOMIN.com')" | python manage.py shell

# Run tests
Run python3 manage.py collectstatic

#RUN python manage.py test

# Expose the Django development server port
EXPOSE 8000

# Start the Django development server
CMD python manage.py runserver 0.0.0.0:8000