# Setting up the project

The following commands are execured for the first time if no python, venv or nginx are installed

---

*START FIRST_TIME*

```
apt update
apt upgrade
```

Python 3 setup

```
sudo apt install -y python3-pip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

Virtual environment setup

```
sudo apt install -y python3-venv
```

Nginx setup

```
apt install nginx
```

*END FIRST TIME*

---

Clone project inside `/var/www`

```
cd /var/www

git clone https://github.com/markofrontend/api.nabavi.ga.git
cd api.nabavi.ga
```

Create neccessary directories & files

```
mkdir media && mkdir static && mkdir -p .venv/var/run && mkdir -p .venv/etc && cp server/uwsgi.ini .venv/etc/uwsgi.ini
```

Create virtual environment & install dependencies
```
python3 -m venv .venv
. .venv/bin/activate

pip install -r requirements.txt
```

Nginx configuration

```
# Remove 127.0.0.1 server name from the following config
cp server/nginx.conf /etc/nginx/sites-available/api.nabavi.ga

ln -s /etc/nginx/sites-available/api.nabavi.ga /etc/nginx/sites-enabled/api.nabavi.ga
service nginx reload
nginx -t
```

Make linux uwsgi.ini service

```
cp server/app.service /etc/systemd/system/api.nabavi.ga.service

#Reload the service files to include the new service.
sudo systemctl daemon-reload

#Start your service
sudo systemctl start api.nabavi.ga.service
```

Collect static files

```
python manage.py collectstatic
```