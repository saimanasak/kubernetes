## PRE STOP HOOK

- The PreStop hook in Kubernetes is triggered just before a container is terminated. 
- It provides an opportunity to run tasks or perform actions before the container stops. 
- This is especially useful when you need to gracefully shut down a container, allowing it to complete ongoing tasks or clean up resources properly.
- The PreStop hook helps avoid sudden termination of processes that might still be handling important operations, like serving requests, writing data, or interacting with external systems.

### Example Overview:
- The example provided shows a scenario where a message is written to a file, and a delay is introduced to ensure that cleanup activities can complete before the container is shut down. 

```yaml
# prestop-ex.yaml

apiVersion: v1
kind: Pod
metadata:
  name: prestop-example
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
      lifecycle:
        preStop:
          exec:
            command: ["/bin/sh", "-c", "echo 'Nginx is shutting down...!!!' > /usr/share/nginx/html/prestop.txt && sleep 10"]
```

### Explanation:

```yaml
apiVersion: v1
```
- Specifies the Kubernetes API version (v1).

```yaml
kind: Pod
```
- Indicates that this configuration defines a Pod.

```yaml
metadata:
  name: prestop-example
```
- **metadata**: Contains metadata about the Pod.
- **name: prestop-example**: Sets the name of the Pod to prestop-example.

```yaml
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
      lifecycle:
        preStop:
          exec:
            command: ["/bin/sh", "-c", "echo 'Nginx is shutting down...!!!' > /usr/share/nginx/html/prestop.txt && sleep 10"]
```
- **spec**: Defines the desired state of the Pod.
- **containers**: Lists the containers that will run inside the Pod.
- **name: nginx-container**: Specifies the name of the container as nginx-container.
- **image: nginx**: Uses the nginx image from Docker Hub, which is a web server.
- **ports**: Defines the ports that the container listens on.
- **containerPort: 80**: Exposes port 80 inside the container, which is the default HTTP port.
- **lifecycle**: Specifies lifecycle hooks for the container.
- **preStop**: This lifecycle hook is triggered when a Pod is about to be terminated (stopped).
- **exec**: Runs a command in the container as part of the preStop hook.
- **command: ["/bin/sh", "-c", "echo 'Nginx is shutting down...!!!' > /usr/share/nginx/html/prestop.txt && sleep 10"]**:
    - "/bin/sh": Runs the command in a shell environment.
    - "-c": Executes the following command.
    - "echo 'Nginx is shutting down...' > /usr/share/nginx/html/prestop.txt && sleep 10": Uses echo to write the message "Nginx is shutting down..." into a file named prestop.txt in the nginx document root. The sleep 10 command delays the container shutdown by 10 seconds, allowing time for any cleanup activities.
    
### Create Pod:
- Command to create the pod using the above manifest:
```bash
kubectl create -f prestop-ex.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/create-pre-nginx.png)

### Check Pod Status:
- Command to check the status of the above created pod:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/get-pods-pre-nginx.png)

### View Pod Details (Pre-Delete):
- Command to check the details of the pod before deleting it:
```bash
kubectl describe pod prestop-example
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/describe-pod-before-pre-nginx.png)

### Delete Pod:
- Command to delete the pod:
```bash
kubectl delete pod prestop-example
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/delete-pod-pre-nginx.png)

### Verification:
- To verify the execution of the pre stop command, run the below command as soon as the above delete command is executed:
```bash
kubectl exec -i prestop-example -- //bin//sh -c "cat /usr/share/nginx/html/prestop.txt"
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/output-pre-nginx.png)

- Command to check the pod details after deleting it (can see the details after deleting because the sleep command will be executing for a while):
```bash
kubectl describe pod prestop-example
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/describe-pod-after-pre-nginx.png)