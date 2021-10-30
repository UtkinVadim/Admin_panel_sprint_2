make restart_server:
	make remove_server /
	make run_server

run_server:
	docker-compose -f docker-compose.yaml up --build -d

stop_server:
	docker-compose -f docker-compose.yaml stop

remove_server:
	docker-compose -f docker-compose.yaml down -v

create_superuser:
	docker exec -it movies_app python manage.py createsuperuser
