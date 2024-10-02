## FAILED PHASE

- The Failed phase occurs when one or more containers in a pod terminate unexpectedly due to errors, and the process exits with a non-zero exit code. 
- This phase is commonly observed in scenarios where something goes wrong during the execution of the container, such as running an invalid command, encountering unhandled exceptions, or resource exhaustion.
- When a pod enters the Failed phase, it indicates that the container or pod encountered a problem during execution. 
- This might be due to incorrect command syntax, invalid logic, application crashes, missing resources, or other issues.
- A non-zero exit code means the container did not finish its task successfully. 
- Exit codes are important for determining why the failure occurred.

### Example:
```yaml
# pod-failed.yaml

apiVersion: v1
kind: Pod
metadata:
  name: failed-pod
spec:
  containers:
  - name: busybox
    image: busybox
    command: ["false"] # "false" returns a non-zero exit code
  restartPolicy: Never
```

### Create Pod:
- Command to create a pod using the above manifest:
```bash
kubectl create -f pod-failed.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/failed-create.png)

### Check Pod Status:
- Command to check the status of the pods:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/failed-get-pods.png)

### Pod Details:
- Command to check the details of the pod:
```bash
kubectl describe pod failed-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/failed-describe.png)

### Delete Pod:
- Command to delete the above pod:
```bash
kubectl delete pod failed-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/failed-delete.png)