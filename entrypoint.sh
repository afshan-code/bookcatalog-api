#!/bin/sh

set -e  # Exit on any error

# Default values if not provided
: "${DATABASE_HOST:=db}"
: "${DATABASE_PORT:=5432}"
: "${APP_PORT:=8000}"

echo "Waiting for the database at $DATABASE_HOST:$DATABASE_PORT..."
while ! nc -z "$DATABASE_HOST" "$DATABASE_PORT"; do
    sleep 1
done
echo "Database is ready!"

# Run migrations
echo "Applying migrations..."
python manage.py migrate --noinput

# Start Django development server
echo "Starting Django server on port $APP_PORT..."
python manage.py runserver 0.0.0.0:$APP_PORT
