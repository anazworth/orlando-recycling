# Orlando Recycling

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Run the application](#run-the-application)
- [Testing](#testing)
- [API Documentation](#api-documentation)
- [How to contribute](#how-to-contribute)
- [Reporting bugs, issues, or feature requests](#reporting-bugs-issues-or-feature-requests)
- [Devcontainer](#devcontainer)

## Overview

To create an application that helps citizens of Orlando and its surrounding areas to
differentiate between recyclable and non-recyclable goods and provide more
information on how they can properly recycle. We will also support the Mobile-Development teams through a Backend API.

## Installation

### Prerequisites
- [Python 3.12](https://www.python.org/downloads/)
- [MySQL 8.3.0](https://dev.mysql.com/downloads/mysql/)

### Setup

1. Clone the repository

```bash
git clone https://github.com/anazworth/orlando-recycling.git
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root of the project and add the environment variables found in the `.example-env` file.

```bash
cp .example-env .env
```

4. (Optional) User the [docker-compose](https://docs.docker.com/compose/) file to create a MySQL database

```bash
cp example-docker-compose.yml docker-compose.yml
```

Edit the `docker-compose.yml` file to add the MySQL environment variables.

```bash
docker-compose up -d # Start the MySQL database
```

5. Run the database migrations

```bash
python manage.py migrate
```

## Run the application

```bash
python manage.py runserver
```

## Testing

```bash
python manage.py test
```

## API Documentation

The API documentation is available at `/swagger` when the application is running and the `ENV` environment variable is set to `development`.

## How to contribute

All development is done in the `dev` branch.

To contribute to the project, follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Push your changes to your fork
5. Create a pull request to the 'dev' branch.
6. Wait for the pull request to be reviewed and merged.

Before creating a pull request, please ensure that all tests pass and that the code is formatted correctly. Ensure that no secrets are pushed to the repository. Create tests for any new features and bug fixes.

Use pylint to check the code for formatting issues.

```bash
pylint <changed_files>
```

## Reporting bugs, issues, or feature requests

If you find a bug, issue, or have a feature request, please open an issue in the repository.

## devcontainer

This project includes a devcontainer configuration for Visual Studio Code. To use it, you must have the [Remote - Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) extension installed.

To open the project in a container, click on the green icon in the bottom left corner of Visual Studio Code and select "Reopen in Container".

All the dependencies are installed in the container and the application is ready to run.

Don't forget to create a `.env` file in the root of the project and add the environment variables found in the `.example-env` file.

[Docker](https://docker.com) is required to use the devcontainer.