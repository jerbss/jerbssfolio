web: mkdir -p staticfiles staticfiles/media && python manage.py collectstatic --noinput --clear && python manage.py migrate && gunicorn jerbss_portfss.wsgi:application --bind 0.0.0.0:$PORT
build: bash build.sh