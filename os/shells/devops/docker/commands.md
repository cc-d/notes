# Useful Docker Commands

Docker is a powerful platform that allows you to develop, test, and deploy applications in containers. This document contains a list of useful Docker commands, along with explanations and examples.

## Basic Commands

- `docker container ls`: List all running containers.

- `docker container ls -a`: List all containers, including stopped ones.

- `docker container start <container_id>`: Start a stopped container.

- `docker container stop <container_id>`: Stop a running container.

- `docker container rm <container_id>`: Remove a stopped container.

- `docker container prune`: Remove all stopped containers.

- `docker logs <container_id>`: Display the logs of a running container.

- `docker exec -it <container_id> /bin/bash`: Open a terminal inside a running container.

- `docker container stats`: Display live resource usage statistics of all running containers.

- `docker-compose up`: Start all services defined in the docker-compose.yml file.

- `docker-compose down`: Stop and remove all containers, networks, and volumes defined in the docker-compose.yml file.

- `docker-compose logs`: Display the logs of all services defined in the docker-compose.yml file.

- `docker-compose exec <service_name> <command>`: Run a command inside a running service container.

## Docker Images

- `docker image ls`: List all Docker images on the local machine.

- `docker image rm <image_id>`: Remove a Docker image from the local machine.

- `docker image prune`: Remove all unused images from the local machine.

- `docker build -t <image_name>:<tag> <build_context>`: Build a Docker image using the Dockerfile in the specified build context directory.

## Docker Networks

- `docker network ls`: List all Docker networks on the local machine.


- `docker network create <network_name>`: Create a new Docker network.

- `docker network rm <network_name>`: Remove a Docker network.

## Docker Volumes

- `docker volume ls`: List all Docker volumes on the local machine.


- `docker volume create <volume_name>`: Create a new Docker volume.

- `docker volume rm <volume_name>`: Remove a Docker volume.
