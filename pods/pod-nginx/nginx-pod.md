```yaml
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

### Explanation:

<table><tr><td>
apiVersion: v1
<table><tr><td>  

- This specifies the version of the Kubernetes API you're using to create the object. Here, v1 is the version for core resources like Pods.
- It tells Kubernetes which API version to use when handling this manifest.