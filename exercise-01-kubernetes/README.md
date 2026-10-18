# Exercise 1: Hello Pod

## Goal

Run an Nginx Pod in a local Kubernetes cluster and reach it through a NodePort Service.

## Work

Applied `pod.yaml` and `service.yaml` to Minikube. The Pod and Service use the names and concepts from the lab, with declarative manifests saved here for repeatability.

## Verification

- Minikube node reached `Ready` on Kubernetes v1.37.0.
- `kubectl wait --for=condition=Ready pod/hello-k8s` succeeded.
- The Pod reached `1/1 Running` with IP `10.244.0.3`.
- The NodePort Service exposed port 80 as `30982`.
- Port-forwarded the Service to `127.0.0.1:18080`; `curl` returned the Nginx welcome page.

Commands: `kubectl apply -f pod.yaml -f service.yaml`, `kubectl get pods -o wide`, `kubectl get service hello-k8s -o wide`, and `kubectl port-forward service/hello-k8s 18080:80`.
