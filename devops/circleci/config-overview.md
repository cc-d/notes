# CircleCI Configuration Documentation

CircleCI is a continuous integration and delivery platform that automates the build, test, and deploy process of software. CircleCI uses a YAML file to manage the configuration of your CI/CD pipeline, which is defined in a `.circleci/config.yml` file in the root of your project repository.

## Basic Concepts

### Pipelines

A pipeline is an object that encompasses a workflow. It is the most high-level unit of work in CircleCI. A pipeline is triggered by a change to your repository and contains the entire configuration including workflows, jobs, etc.

### Jobs

Jobs are collections of steps to be executed in a single run/executable. They are the basic unit of execution in CircleCI and are executed in the environment defined in the image key of your configuration.

```yaml
jobs:
  build:  # This is the job identifier
    docker:  # This job runs in a Docker container
      - image: circleci/ruby:2.4.1  # This is the image the container will use
    steps:  # These are the steps of the job
      - checkout
      - run: echo "A first hello"
```

### Workflows

Workflows are sets of rules for defining a collection of jobs and their run order. It coordinates the jobs that should be run.

```yaml
workflows:
  version: 2
  build_and_test:  # This is the workflow identifier
    jobs:  # These are the jobs to be run in this workflow
      - build
      - test:
          requires:
            - build  # "test" job will be executed only after the "build" job succeeds
```

### Steps

Steps are a collection of executable commands which are run during a job. CircleCI provides a number of step types to control the flow of a job, including:

- `checkout`: Special step used to check out source code to the configured path.
- `run`: Used for executing a specific command.
- `store_artifacts`: Used to store artifacts (a file or directory) produced in your job that might be needed later.

```yaml
steps:
  - run:
      name: Running tests
      command: make test
  - store_artifacts:
      path: test-results.xml
      destination: test-results
```

## Key Concepts from the Given `config.yml`

### Orbs

Orbs are reusable snippets of code that help automate repeated processes, speed up project setup, and make easy integration with third parties. They are imported into your config file using the `orbs` key.

```yaml
orbs:
  codecov: codecov/codecov@1.0.2
```

### Commands

Commands define a sequence of steps to be executed, they can be invoked as a step in a job.

```yaml
commands:
  publish-image:
    description: "Build and push Docker image"
    parameters:
      dname:
        type: string
        description: "Name of the Docker image"
      dockerfile:
        type: string
        description: "Dockerfile path"
    steps:
      - checkout
      ...
```

### References

YAML allows for creating reusable config snippets. In this config file, references are used for this purpose and are defined using `&` and can be referred using `*`. This avoids duplication of code.

```yaml
references:
  publish-setup: &publish-setup
    machine:
      image: ubuntu-2004:202201-02
    resource_class: large
```

### Docker Images

CircleCI supports the use of Docker, a platform that provides OS-level virtualization to deliver software in packages called containers. This is

 specified under the `docker` key, in which you provide the Docker image you want to use for your build environment.

```yaml
docker:
  - image: us-central1-docker.pkg.dev/pict-app/webapp/webapp:latest
```

### Resource Classes

You can configure your job to run with a specific resource class. This helps you to specify the size of the container you want to use to run your jobs.

```yaml
resource_class: large
```

### Checkout

The `checkout` step checks out the source code for a job. It is a special step provided by CircleCI.

```yaml
steps:
  - checkout
```

### Workspaces and Artifacts

Artifacts persist data after a job is completed and can be used for longer-term storage of the outputs of your build process. Workspaces, on the other hand, are used for sharing data between jobs in a single workflow.

```yaml
- store_artifacts:
    path: webapp/coverage/html
- persist_to_workspace:
    root: workspace
    paths:
      - app-version
```

### Filters

Filtering provides control of the branches and tags that are used in a workflow. If a job requires any other jobs (directly or indirectly), you must use regular expressions to specify branch or tag names for the job.

```yaml
filters:
  branches:
    only:
      - master
```

### Approval Type

In a workflow, you can set a job to require manual approval in the CircleCI web application with the `type: approval` key. This setting enables you to manually approve job runs from the 'Pending Approval' area on the Jobs page of the CircleCI web application.

```yaml
staging-auto-deploy:
  type: approval
  requires:
    - publish-backend-image-staging
```

## Learn More

For more information and advanced configurations, refer to the [CircleCI documentation](https://circleci.com/docs/2.0/).