# Exercise 1: Hello Pod

## Goal

Run an Nginx Pod in a local Kubernetes cluster and reach it through a NodePort Service.

## Work

Started a local Minikube cluster using the Docker driver, then created the `hello-k8s` Pod from the `nginx` image and exposed port 80 as a NodePort Service.

## Verification

- `kubectl get nodes` showed the Minikube node as `Ready` on Kubernetes v1.37.0.
- `kubectl get pods` showed `hello-k8s` as `1/1 Running`.
- `kubectl get services` showed `hello-k8s` as a `NodePort` Service on `80:30964/TCP`.
- `minikube service hello-k8s` opened the Nginx welcome page in the browser.

## Evidence

- [`screenshot/01-nginx-welcome.png`](screenshot/01-nginx-welcome.png): Nginx welcome page served through the Minikube service tunnel.
- [`screenshot/02-pod-service-terminal.png`](screenshot/02-pod-service-terminal.png): Terminal output showing the Pod, Service, and service tunnel command.

Commands run: `minikube start --driver=docker`, `kubectl get nodes`, `kubectl run hello-k8s --image=nginx --port=80`, `kubectl get pods`, `kubectl expose pod hello-k8s --type=NodePort --port=80`, `kubectl get services`, and `minikube service hello-k8s`.
