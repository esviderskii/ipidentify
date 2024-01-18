# Analog ident.me service (response visitor's ip address)

## Install
```
virtualenv -p $(which python3) venv
pip install -r requirements.txt
```

## Dev mode run
```
flask --app server run --host=0.0.0.0 --port=8000
```
## Production mode run
```
gunicorn -w 4 -b 0.0.0.0:8000 'server:app'
```
