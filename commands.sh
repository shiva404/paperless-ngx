pipenv requirements > requirements.txt

# install mysql
brew install mysql
mysql.server start

# install postgres
brew install postgresql

brew install supervisord

pip uninstall python-magic
pip install python-magic-bin==0.4.14

# run migration
python3 manage.py migrate --skip-checks --no-input


gunicorn -c ../gunicorn.conf.py paperless.asgi:application

# redis
brew install redis
brew services start redis
