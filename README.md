# Simple Python Flask Docker App

A minimal Python Flask web application containerized with Docker. This repository demonstrates how to build and run a lightweight web app inside a Docker container. The app runs on port 5000 and serves a simple “Hello, World” message.

## Features

- Python 3.11 + Flask
- Dockerized for easy deployment
- Exposes port 5000 for web access
- Ready-to-run with a single Dockerfile

## Project Structure

```
simple-app/
├── app.py           # Flask application
├── requirements.txt # Python dependencies
└── Dockerfile       # Docker configuration
```

## Usage

### Build the Docker Image

```bash
docker build -t simple-python-app .
```

### Run the Docker Container

```bash
docker run -d -p 5000:5000 --name simple-app simple-python-app
```

### Access the App

Open your browser and go to:

```
http://localhost:5000
```

You should see:

```
Hello, World from Dockerized Python app!
```

## Deployment

This app can be deployed to any cloud provider that supports Docker, such as:

- [Render.com](https://render.com)

## License

This project is open-source and available under the MIT License.
