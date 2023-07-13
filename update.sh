git clone https://github.com/MrNereof/nereof.com tmp &&
rm tmp/nereof/settings.py &&
cp -R tmp/* . &&
rm -rf tmp &&
venv/bin/pip install -r requirements.txt
venv/bin/python manage.py migrate &&
venv/bin/python manage.py collectstatic --noinput &&
touch .restart-app &&
echo Done!