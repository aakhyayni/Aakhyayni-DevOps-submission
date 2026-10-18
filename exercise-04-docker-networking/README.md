# Exercise 4: Docker Networking

## Goal

Create a user-defined bridge network and run Flask, MySQL, and Redis containers attached to it.

## Work

The Flask app is in `app.py`; `Dockerfile` builds its image. MySQL and Redis are official images. A local-only test password is used for the MySQL container and is not part of the repository.

## Verification

- Created the `my-bridge-net` user-defined bridge network.
- Built `devops-lab-flask-api:local` and launched the `flask` container on port 5001.
- Started the official `mysql:8.4` and `redis:7-alpine` containers on the same network.
- `curl http://localhost:5001/about` returned the expected JSON response.
- From inside `flask`, Python DNS resolution and TCP checks succeeded for `mysql:3306` (`172.18.0.4`) and `redis:6379` (`172.18.0.3`). This checks the same service-to-service connectivity as the lab's `ping` step without adding ping tools to the app image.

MySQL was started with a lab-only root password through a local container environment variable. It is not saved in the repository.
