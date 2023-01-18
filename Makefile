run:
	sudo docker-compose -p excar -f local.yml up

migrations:
	docker-compose -p excar -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -p excar -f local.yml run --rm django python manage.py migrate

build:
	sudo docker-compose -p excar -f local.yml build

shell:
	docker-compose -p excar -f local.yml run --rm django python manage.py shell