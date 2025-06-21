# Docker Compose

Docker Compose is a tool that allows you to define and manage multi-container Docker applications. It simplifies the process of running multiple Docker containers as a single application stack, making it easier to develop, test, and deploy complex applications.

## Installation

To use Docker Compose, you need to install Docker first. Follow the instructions for your specific operating system:

- [Docker for Mac](https://docs.docker.com/docker-for-mac/install/)
- [Docker for Windows](https://docs.docker.com/docker-for-windows/install/)
- [Docker for Linux](https://docs.docker.com/engine/install/)

Docker Compose is included with Docker Desktop on Mac and Windows.

## Usage

1. Create a `docker-compose.yml` file in your project directory to define your application's services and their configurations. The file uses the YAML format to describe the services, networks, volumes, and other options. Here's an example of a basic `docker-compose.yml` file:

   ```yaml
   version: '3'
   services:
     web:
       image: nginx:latest
       ports:
         - 80:80
       volumes:
         - ./html:/usr/share/nginx/html
   ```

   In this example, we define a service called `web` using the `nginx` image, expose port 80, and mount a local directory as a volume inside the container.

2. Open a terminal or command prompt, navigate to your project directory containing the `docker-compose.yml` file, and run the following command to start your application:

   ```bash
   docker-compose up
   ```

   Docker Compose reads the `docker-compose.yml` file and starts the defined services. You will see logs for each service in the terminal.

3. Access your application in a web browser by navigating to `http://localhost`.

4. To stop your application, press `Ctrl + C` in the terminal where you ran the `docker-compose up` command. This stops the containers and associated services.

## Configuration Options

The `docker-compose.yml` file allows you to configure various aspects of your application stack:

- `version`: Specifies the version of the Compose file format. The current stable version is `3`.
- `services`: Defines the services (containers) that make up your application stack. You can specify the image, ports, volumes, environment variables, and more for each service.
- `networks`: Creates custom networks for services to communicate with each other. You can define network aliases, IP addresses, and other network-specific configurations.
- `volumes`: Mounts local directories or named volumes into containers, allowing data persistence and sharing between containers.
- `environment`: Sets environment variables for the service containers, providing configuration options and dynamic values.
- `depends_on`: Defines dependencies between services, ensuring that one service starts only after its dependencies are ready.

For a comprehensive list of configuration options and their usage, refer to the [Compose file reference](https://docs.docker.com/compose/compose-file/).

## Additional Commands

Here are some additional commands you can use with Docker Compose:

- `docker-compose down`: Stops and removes the containers, networks, and volumes defined in the `docker-compose.yml` file. It cleans up the resources created by the application stack.
- `docker-compose start`: Starts the containers defined in the `docker-compose.yml` file, even if they were stopped previously.
- `docker-compose stop`: Stops the running containers defined in the `docker-compose.yml` file, preserving their state.
- `docker-compose restart`: Restarts the containers defined in the `docker-compose.yml` file, stopping and starting them

.
- `docker-compose logs`: Displays the logs for the running containers.
- `docker-compose ps`: Lists the running containers.

For more detailed documentation and advanced usage, refer to the [Docker Compose documentation](https://docs.docker.com/compose/).