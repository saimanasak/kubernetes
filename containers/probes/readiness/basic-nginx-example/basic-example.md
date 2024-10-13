```yaml
apiVersion: v1
kind: Pod
metadata:
  name: readiness-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
    ports:
    - containerPort: 80
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
      timeoutSeconds: 2
      successThreshold: 1
      failureThreshold: 3
```

### Overview:
- The above manifest defines a Kubernetes Pod named readiness-pod, which contains a single container running the NGINX web server. 
- The container exposes port 80 for HTTP traffic. 
- A readiness probe is configured to check if the NGINX server is ready to serve requests by sending HTTP GET requests to the root path (/) every 5 seconds after an initial delay of 5 seconds. 
- The probe will wait for 2 seconds for a response, and if it fails three consecutive checks, the pod will be marked as not ready. 
- This setup helps ensure that traffic is only routed to the NGINX container once it is fully operational and ready to handle incoming requests.

### Explanation:
```yaml
apiVersion: v1
```
- Specifies the version of the Kubernetes API that is used to create this resource. 
- Here, v1 is the stable API version for basic resources like Pods.

```yaml
kind: Pod
```
- Specifies the type of Kubernetes object that is being defined. 
- Here, we are defining a Pod, which is the smallest deployable unit in Kubernetes. A pod can contain one or more containers.

```yaml
metadata:
  name: readiness-pod
```
- **metadata**: Provides metadata about the pod, such as its name and other labels.
- **name: readiness-pod**: Assigns the name readiness-pod to this pod. This name is used to identify the pod within the Kubernetes cluster.

```yaml
spec:
  containers:
  - name: nginx-container
    image: nginx
    ports:
    - containerPort: 80
```
- **spec**: The spec field contains the specification for the pod, including details about the containers that will run inside the pod.
- **containers**: This is a list of containers that will run inside the pod. A pod can have one or more containers, but here we have only one.  
- **name: nginx-container**: The name of the container within the pod. This name is used to identify the container within this specific pod. It is called nginx-container here.
- **image: nginx**: Specifies the Docker image that will be used to create the container. Here, it uses the nginx image from Docker Hub, which is the default public repository for Docker images. This means an NGINX web server will run in this container.
- **ports**: This defines the list of ports that are exposed by the container.
- **containerPort: 80**: This tells Kubernetes that the container listens on port 80, which is the default HTTP port for NGINX. It allows other services and pods to communicate with this container on port 80.

```yaml
    readinessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 5
      periodSeconds: 5
      timeoutSeconds: 2
      successThreshold: 1
      failureThreshold: 3
```
- **readinessProbe**: This section defines the readiness probe configuration for the container, which is used to determine if the container is ready to accept traffic.
- **httpGet**: Specifies that the readiness probe will perform an HTTP GET request.
- **path: /**: Defines the HTTP path that the readiness probe will request. Here, it is set to /, which is the root URL of the NGINX server.
- **port: 80**: Specifies the port number that the readiness probe will use to send the HTTP request. In this case, it will send requests to port 80.
- **initialDelaySeconds: 5**: The number of seconds to wait after the container has started before performing the first readiness probe check. This is set to 5 seconds, allowing time for the NGINX server to start up.
- **periodSeconds: 5**: The interval (in seconds) between successive readiness checks. This is set to 5 seconds, meaning the readiness probe will be executed every 5 seconds after the initial delay.
- **timeoutSeconds: 2**: The number of seconds the probe will wait for a response before considering it a failure. If the probe does not receive a response within 2 seconds, it will be marked as failed.
- **successThreshold: 1**: This specifies how many consecutive successful probes are required to mark the container as ready. Here, it is set to 1, meaning the container only needs to pass a single check to be considered ready.
- **failureThreshold: 3**: The number of consecutive failed probes required to mark the container as not ready. In this manifest, it is set to 3, indicating that if the readiness probe fails three times in a row, the container will be marked as not ready.

> **_NOTE_**:
> 
> Everything is done in the **default** namespace.

### Create Pod:
- Using the below command create a pod:
```bash
kubectl apply -f basic-example.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-create.png)

### Check Pod Status:
- Check the status of the pod using the below command:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-initial-get-pods.png)

### View Pod Details:
- See the details of the pod using the below command:
```bash
kubectl describe pod readiness-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-initial-describe.png)

### Simulate A Failure:
- To test the readiness probe, you can simulate a condition where NGINX is temporarily not able to serve requests:
- Login to the pod's container:
```bash
kubectl exec -it readiness-pod -- sh
```
- Rename or delete the default HTML directory:
```bash
mv /usr/share/nginx/html /usr/share/nginx/html-bak
```
- This will cause NGINX to return a 404 Not Found for requests to /, which will trigger readiness probe failures.

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-simulate.png)

### Monitor Readiness Probe:
- Check the details of the pod, events section:
```bash
kubectl describe pod readiness-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-after-describe.png)

### Observe Pod Details:
- Check the pod status:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-after-get-pods.png)

### Delete Pod:
- Using the below command delete the above pod:
```bash
kubectl delete pod readiness-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/readiness-delete-pod.png)