**Sync data**

```shell
./script/run python app/config/daily.py
```

**Hacky local dev w/ live reload**

```
```shell
pip install -r requirements.txt
gunicorn --config="app/config/gunicorn.py" --reload app:app --pid=gunicorn.pid
script/watch
```

#### Run migrations
```
script/dbmigrate
```

#### Autogenerate migrations
```
./script/app-env alembic revision --autogenerate
```
