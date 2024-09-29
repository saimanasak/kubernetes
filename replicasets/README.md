## REPLICASET

- A ReplicaSet is a Kubernetes resource that ensures a specified number of pod replicas are running at any given time. 
- It monitors the state of the pods and, if any of them fail or are terminated, it automatically creates new pods to maintain the desired number of replicas.
- A ReplicaSet uses label selectors to identify the pods it should manage.
- Maintaining application availability by ensuring a certain number of instances (pods) are always running.
- Scaling applications up or down by increasing or decreasing the number of replicas.