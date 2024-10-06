## POST START HOOK

- The PostStart hook is triggered immediately after the container is created but before the main application or command starts running.
- This hook is typically used to run some initialization tasks after the container has started.

### Example Overview:
- We have an application running in a container that depends on some temporary files being created in the file system. 
- You can use the PostStart hook to create those files as soon as the container starts.

```yaml
# poststart-ex.yaml

apiVersion: v1
kind: Pod
metadata:
  name: poststart-example
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
      lifecycle:
        postStart:
          exec:
            command: ["/bin/sh", "-c", "echo 'Nginx has started!!!' > /usr/share/nginx/html/poststart.txt"]
```

### Explanation:

```yaml
apiVersion: v1
```
- Specifies the API version of Kubernetes that this configuration uses. 
- Here, v1 indicates that this is a stable version of the API.

```yaml
kind: Pod
```
- Indicates the type of Kubernetes resource being defined. 
- Here, it’s a Pod, which is the smallest deployable unit in Kubernetes that can run containers.

```yaml
metadata:
  name: poststart-example
```
- **metadata**: Contains metadata about the Pod, such as its name, labels, and annotations.
- **name: poststart-example**: Sets the name of the Pod to poststart-nginx. This name is used to uniquely identify the Pod within the namespace.

```yaml
spec:
  containers:
    - name: nginx-container
      image: nginx
      ports:
        - containerPort: 80
      lifecycle:
        postStart:
          exec:
            command: ["/bin/sh", "-c", "echo 'Nginx has started!!!' > /usr/share/nginx/html/poststart.txt"]
```
- **spec**: Defines the desired state of the Pod, including the containers it should run and their configuration.
- **containers**: This field contains a list of containers that will run inside the Pod.
- **name: nginx-container**: Specifies the name of the container. Here, it is named nginx-container. The name is used to identify the container within the Pod.
- **image: nginx**: Specifies the container image to use. In this case, it uses the official nginx image from Docker Hub, which is a popular web server.
- **ports**: Defines the ports that the container will listen on.
- **containerPort: 80**: Indicates that the container will expose port 80, which is the default port for HTTP traffic. This means the nginx server will be accessible on this port.
- **lifecycle**: This section is part of a Kubernetes Pod specification, specifically within a container definition. It allows you to define specific actions (hooks) that should occur during the container's lifecycle events.
- **postStart**: This is a lifecycle hook that is triggered immediately after the container is started but before the container's main process (defined in the command section) begins execution. It allows you to perform setup tasks that are necessary before the container begins its main operations.
- **["/bin/sh", "-c", "echo 'Nginx has started!!!' > /usr/share/nginx/html/poststart.txt"]**: 
    - '/bin/sh' specifies the shell to use for executing the command. 
    - '-c' flag indicates that the following string is a command to be executed. 
    - 'echo 'Nginx has started!!!' > /usr/share/nginx/html/poststart.txt' uses the echo command to write the text Nginx has started!.The output is redirected to a file named poststart.txt located in /usr/share/nginx/html/, which is the default directory for serving files in the nginx container.
    
- **Flow**:
    - When the container starts, the PostStart hook is triggered immediately.
    - The command inside the PostStart hook is executed, it writes "Nginx has started!!!" into /usr/share/nginx/html/poststart.txt file.
    - After the PostStart hook completes, the main process of the container starts executing.
    
### Create Pod:
- Command to create the pod using the above manifest:
```bash
kubectl create -f poststart-ex.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/create-post-nginx.png)

### CHeck Pod Status:
- Command to check the status of the pod:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/get-pods-post-nginx.png)

### Pod Details:
- Command to check the details of the pod:
```bash
kubectl describe pod poststart-example
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/describe-pod-post-nginx.png)

### Accessing NGINX:
- Port forwarding in Kubernetes is a technique used to access services running inside a Kubernetes cluster from outside the cluster, typically from a local machine. 
- Command to set up port forwarding for the above created nginx pod:
```bash
kubectl post-forward poststart-example 8080:80
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/port-forward-post-nginx.png)

- Access the nginx from:
```bash
http://localhost:8080/poststart.txt
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/containers/lifecycle-hooks/images/output-post-nginx.png)