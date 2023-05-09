# build_files.sh
pip install -r requirements.txt

# make migrations
python2.75 manage.py migrate 
python2.75 manage.py collectstatic
