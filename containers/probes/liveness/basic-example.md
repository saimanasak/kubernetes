```yaml
apiVersion: v1
kind: Pod
metadata:
  name: liveness-pod
spec:
  containers:
  - name: nginx-container
    image: nginx
    ports:
    - containerPort: 80
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 10
      periodSeconds: 5
      timeoutSeconds: 2
      failureThreshold: 3
```

### Overview:
- The above manifest defines a Pod named liveness-pod that runs a single container called nginx-container using the nginx image. 
- The container exposes port 80 and has a liveness probe configured to perform an HTTP GET request on the root path (/) every 5 seconds. 
- It waits 10 seconds after the container starts before performing the first check and considers the container unhealthy if it fails to respond 3 times in a row within 2 seconds each time. 
- If the container is deemed unhealthy, Kubernetes will automatically restart it.

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
  name: liveness-pod
```
- **metadata**: Provides metadata about the pod, such as its name and other labels.
- **name: liveness-pod**: Assigns the name liveness-pod to this pod. This name is used to identify the pod within the Kubernetes cluster.

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
    livenessProbe:
      httpGet:
        path: /
        port: 80
      initialDelaySeconds: 10
      periodSeconds: 5
      timeoutSeconds: 2
      failureThreshold: 3
```
- **livenessProbe**: Configures a liveness probe for the container. The liveness probe is used to determine if the container is running and healthy.
- **httpGet**: This specifies that the probe will use an HTTP GET request to check the health of the container.
- **path: /**: The HTTP GET request will be made to the root path (/) of the NGINX server running inside the container. If this path returns a 2xx or 3xx status code, the probe is considered successful.
- **port: 80**: Specifies that the HTTP GET request will be sent to port 80 of the container, where NGINX is serving content.
- **initialDelaySeconds: 10**: The liveness probe will wait for 10 seconds after the container starts before performing the first health check. This allows the application to have some time to start up before the probe starts checking its health.
- **periodSeconds: 5**: The liveness probe will check the health of the container every 5 seconds. This means that after each check, it waits for 5 seconds before running the next check.
- **timeoutSeconds: 2**: Specifies that each liveness probe request will wait for a maximum of 2 seconds for a response. If the container does not respond within 2 seconds, the probe is considered failed.
- **failureThreshold: 3**: If the liveness probe fails 3 consecutive times, Kubernetes will consider the container to be unhealthy and will restart it. This helps recover from situations where the container becomes unresponsive.

> **_NOTE_**:
> 
> Everything is done in the **default** namespace.

### Create Pod:
- Using the below command create a pod:
```bash
kubectl apply -f basic-example.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-create.png)

### Check Pod Status:
- Check the status of the pod using the below command:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-initial-get-pods.png)

### View Pod Details:
- See the details of the pod using the below command:
```bash
kubectl describe pod liveness-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-initial-describe.png)

### Simulate A Failure:
- To test the liveness probe’s functionality, can simulate a failure by making the / endpoint unresponsive:
- Login to the pod's container:
```bash
kubectl exec -it liveness-pod -- sh
```
- Rename or delete the default HTML directory:
```bash
mv /usr/share/nginx/html /usr/share/nginx/html-bak
```
- This will cause NGINX to return a 404 Not Found for requests to /, which will trigger liveness probe failures.

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-simulate.png)

### Monitor Liveness Probe:
- Check the details of the pod, events section:
```bash
kubectl describe pod liveness-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-after-describe.png)

### Observe Pod Restarts:
- Check the pod status:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-after-get-pods.png)

### Delete Pod:
- Using the below command delete the above pod:
```bash
kubectl delete pod liveness-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/images/liveness-delete.png)