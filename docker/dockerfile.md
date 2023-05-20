Dockerfile: An Introduction
Dockerfiles are the building blocks of creating and managing Docker container images. They contain a set of instructions that Docker uses to build a container image. In this documentation, we will cover how Dockerfiles work, commonly used Dockerfile commands, give examples.

How Dockerfiles work
Dockerfiles are plain text files containing a series of commands executed in a specific order. When you run the docker build command, Docker reads the Dockerfile and executes the instructions to create a new container image. Each command in the Dockerfile creates a new layer in the image, which is then cached to optimize the build process. The final container image is an amalgamation of these layers.

Common Dockerfile commands
Here are some of the most commonly used Dockerfile commands, along with their descriptions and examples:

FROM
The FROM command specifies the base image for building the new container image. It is usually the first command in a Dockerfile.

```
FROM ubuntu:22.04
```

In our codebase, we often use the Ubuntu 22.04 image as the base image for our containers.

RUN
The RUN command executes shell commands during the build process. Each RUN command creates a new layer in the image.

```
RUN apt-get update -y && \
  apt-get install -y apt-utils wget lsb-release gnupg software-properties-common libmysqlclient-dev curl
```

ENV
The ENV command sets environment variables in the container image.

```
ENV DEBIAN_FRONTEND=noninteractive
```

COPY & ADD
Both COPY and ADD commands copy files from the local filesystem to the container image. While COPY is a simpler command that only supports basic copying, ADD supports additional features like remote URL support and automatic tar extraction.

```
COPY ./requirements.txt /code
ADD ./requirements_dev.txt /code
```

WORKDIR
The WORKDIR command sets the working directory for any subsequent RUN, CMD, ENTRYPOINT, COPY, and ADD commands.

```
WORKDIR /code
```

EXPOSE
The EXPOSE command informs Docker that the container will listen on the specified network ports at runtime.

```
EXPOSE 8000
EXPOSE 8888
```

We use the EXPOSE command to expose ports for our web application and any other services that need to be accessible.

CMD & ENTRYPOINT
Both CMD and ENTRYPOINT commands define the default command to execute when the container starts. The main difference between them is that CMD provides default arguments that can be overridden, whereas ENTRYPOINT provides a fixed command that cannot be overridden.

```
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```
