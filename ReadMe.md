## Install requirements

```bash
pip install requirements.txt
```

## Running the development server

```bash
export FLASK_DEBUG=1
export FLASK_APP=server.py
flask run
```

## Deployment

The files in infrastructure can be used to deploy the site, using gunicorn + supervisor with apache + mod_proxy.

For a fresh installation, the files will need to be copied to the correct locations, and services restarted eg.

### Apache
```bash
ln -s /home/local_dev_example/infrastructure/apache.conf /etc/httpd/conf.d/local_dev_example.conf

service httpd restart
```

### Supervisor
```bash
ln -s /home/local_dev_example/infrastructure/supervisor.conf /etc/supervisor/conf.d/local_dev_example.conf

supervisorctl reread

supervisorctl reload

supervisorctl restart all
```
