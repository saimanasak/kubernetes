## POD CREATION FLOW

### Overview:
- Creating a Pod in Kubernetes using a definition file involves a series of interactions between various components in the Kubernetes architecture.

### Flow:
1. Prepare the pod definition file, written in JSON or YAML format.
2. This file contains the specifications of the pod, including metadata like names, labels, container images, and other configuration details.
3. The below manifest defines a Pod my-nginx-pod, which runs a single container called nginx-container, using the nginx image.
```yaml
# nginx-pod.yaml

apiVersion: v1
kind: Pod
metadata:
  name: my-nginx-pod
  labels:
    app: mynginx
spec:
  containers:
  - name: nginx-container
    image: nginx
```
4. The Pod creation process starts when you submit the pod definition file to the Kubernetes cluster using the below kubectl command:
```bash
kubectl create -f nginx-pod.yaml
```
5. This command sends the contents of the file to the Kubernetes API Server. 
6. The API server is the front-end interface for the Kubernetes control plane.
7. The API Server validates the request by checking if the submitted YAML file is well-formed and conforms to the Kubernetes schema (ex: correct API version, kind: Pod, and required fields).
8. If valid, the API Server writes the pod definition into etcd, the cluster’s distributed key-value store, where the cluster's state is maintained.
9. Authentication and Authorization
10. Once the pod specification is stored in etcd, the Kubernetes Scheduler continuously watches the API Server for unscheduled Pods.
11. When the scheduler detects the new Pod (i.e., a Pod without a node assigned), it starts the process of selecting an appropriate worker node for the Pod based on the available resources and scheduling policies (e.g., resource requests, node affinity, taints, and tolerations).
12. The Scheduler selects a node for the Pod and assigns it by updating the Pod object in the API server, indicating which worker node will host the Pod.
13. This update is again written to etcd, marking the Pod as scheduled.
14. Each worker node runs a kubelet, which is responsible for managing Pods on that node.
15. The kubelet on the selected worker node continuously polls the API Server to identify new Pods assigned to it. Upon detecting the newly scheduled Pod, it fetches the pod specification from the API Server.
16. The kubelet communicates with the container runtime (e.g., Docker, containerd, or CRI-O) on the worker node to pull the required container image(s) (e.g., nginx in this case) from the container registry.
17. If the image is not already present on the node, the container runtime pulls it from a container registry (like Docker Hub, Google Container Registry, etc.).
18. After pulling the image, the container runtime creates and starts the container(s) as defined in the Pod specification.
19. Once the container is running, the kubelet continues to monitor the Pod's health by executing the specified liveness and readiness probes.
20. If the Pod fails (e.g., due to crashes or health issues), the kubelet may restart the container based on the Pod's restart policy (e.g., Always, OnFailure, or Never).
21. As the Pod moves through different stages (e.g., Pending, Running, Succeeded, or Failed), the kubelet continuously updates the Pod's status in the API Server.
22. The API server updates the pod’s status in etcd, and the user can query the API server to check the state of the newly created pod.

## Flow:

![image](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-creation-flow/images/Pod_Creation_Flow.png)