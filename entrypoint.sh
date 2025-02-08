#!/bin/sh

# Activate virtual environment (if using one)
# source Django_virtual_env/bin/activate  # Change 'venv' to your actual virtual environment name

# Run migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start the Django server
echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8000
