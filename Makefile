.PHONY: up down

IMAGE_NAME=text2sql-app
CONTAINER_NAME=text2sql-container

up:
	docker-compose up -d
	docker build -t $(IMAGE_NAME) .
	docker run -d --name $(CONTAINER_NAME) -p 8501:8501 $(IMAGE_NAME)

down:
	docker rm -f $(CONTAINER_NAME) || true
	docker-compose down
