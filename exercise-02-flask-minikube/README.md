# Exercise 2: Flask on Minikube

## Goal

Build and deploy a Flask container with kubectl and Kubernetes YAML.

## Work

The app listens on port 15000. Its Deployment and NodePort Service are declared in `flask-deployment.yaml`.

## Verification

- Built `flask-app:latest` and loaded it into the Minikube node.
- `kubectl rollout status deployment/flask-app` reported a successful rollout; the Pod was `1/1 Running` at `10.244.0.4`.
- The NodePort Service maps port 15000 to node port 31363.
- Port-forwarded the Service to `127.0.0.1:18081`; `curl` returned `Hello from Flask on Kubernetes!`.
