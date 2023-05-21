# Простой Django проект

`dataset_csv-json.py` пересохраняет данные из csv файлов в пригодные для загрузки json файлы

### Загрузка данных в БД
```shell
python3 manage.py makemigrations
python3 manage.py mirgate
python3 manage.py loaddata ../datasets/ads.json
python3 manage.py loaddata ../datasets/categories.json
```
