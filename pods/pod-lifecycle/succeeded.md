## SUCCEEDED PHASE

- The Succeeded phase occurs when all containers in a pod have successfully completed their execution and exited with an exit code of 0, which indicates that the container has finished its task without any errors. 
- This phase is most commonly associated with batch jobs or one-time tasks where a container performs a specific action (e.g., data processing, printing a message, or running a script) and exits upon completion.
- The Succeeded phase represents the final state of a pod for containers that are meant to complete a specific task and terminate.
- Unlike services or applications that run indefinitely, pods in the Succeeded phase signal that the job or task they were assigned has finished.
- Once a pod enters the Succeeded state, the containers within the pod will not be restarted, even if a restart policy is set (such as Always). 
- This behavior is typically used for one-time tasks or jobs that do not require continuous execution.

### Example
```yaml
# pod-succeeded.yaml

apiVersion: v1
kind: Pod
metadata:
  name: succeeded-pod
spec:
  containers:
  - name: busybox
    image: busybox
    command: ["echo", "Hello, Kubernetes...!!!"]
```

### Create Pod:
- Command to create a pod using the above manifest file:
```bash
kubectl create -f pod-succeeded.yaml

kubectl apply -f pod-succeeded.yaml
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/succeeded-create.png)

### Check Pod Status
- Command to check the status of the pod:
```bash
kubectl get pods
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/succeeded-get-pods.png)

### Check Output:
- Check the output for the above manifest file's task:
```bash
kubectl logs succeeded-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/succeeded-logs.png)

### Pod Details:
- Check the details of the pod:
```bash
kubectl describe pod succeeded-pod
```

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/pods/pod-lifecycle/images/succeeded-describe.png)