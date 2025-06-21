# Django Cloud

Cloud-ready Django app

## Requirements

- [Python](https://www.python.org/downloads/)
- [Postgres](https://www.postgresql.org/download/)

## Development

```shell
bash ./scripts/init.sh
bash ./scripts/lint.sh
bash ./scripts/run.sh
```

## Docker

### Build

```shell
docker build -t app .
```

### Run

```shell
docker run --detach --publish 8080:8000 --name app --env-file .env app
```

### Init

```shell
docker exec -it app python manage.py makemigrations
docker exec -it app python manage.py migrate
docker exec -it app python manage.py createsuperuser --noinput --username user --email user@email.com
```

### Stop

```shell
docker stop app
docker rm app
docker rmi app
```
