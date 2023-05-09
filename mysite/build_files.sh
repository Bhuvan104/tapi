# build_files.sh
pip install -r requirements.txt

# make migrations
# make migrations
python manage.py collectstatic
python manage.py runserver
