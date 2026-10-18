# Exercise 3: Scale Flask with a ReplicaSet

## Goal

Deploy the flash-sale API with three replicas, scale it to five, and observe which Pod serves requests.

## Work

`app.py` includes `/`, `/buy`, and `/health`. `flashsale.yaml` defines the ReplicaSet and Service. The image name and object names are consistent throughout this submission.

## Verification

- Built `flashsale:1.0` and loaded it into Minikube.
- The ReplicaSet reached 3/3 Ready Pods, then scaled successfully to 5/5.
- Sent 12 requests to the Service ClusterIP from the Minikube node. Responses came from all five Pod hostnames: `flashsale-rs-4s8c6`, `flashsale-rs-nd7nf`, `flashsale-rs-nr6fj`, `flashsale-rs-pslhv`, and `flashsale-rs-q7prp`.
- `/buy?user=student` returned a successful result and included `served_by_pod` in each response.
