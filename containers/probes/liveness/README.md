## LIVENESS PROBE

- A Liveness Probe in Kubernetes is used to check if a container is healthy and functioning properly. 
- It helps ensure that the application running inside a container is not stuck or in an unrecoverable state. 
- If a liveness probe fails, Kubernetes will assume that the container is unhealthy and restart it. 
- This helps ensure high availability and self-healing of applications.

### Why???

- **Detecting Application Failures**: Applications can crash, hang, or enter states where they are no longer functioning as expected. For instance, an application might encounter a deadlock, become unresponsive due to high memory usage, or simply freeze. A liveness probe continuously checks the health of a container. If the container stops responding (e.g., the application is stuck or in an unrecoverable state), the liveness probe will fail, triggering Kubernetes to restart the container automatically. This ensures that any failed or stuck applications can be revived without human intervention.
- **Self-Healing**: Kubernetes uses the liveness probe to implement self-healing for containers. When the liveness probe fails for a specified number of times, Kubernetes restarts the affected container. This automatic recovery helps maintain the health of the system and minimizes downtime. By enabling this self-healing capability, you reduce the need for manual intervention and improve the reliability of your services.
- **Ensuring High Availability**: In distributed systems, downtime of even a single instance of an application can lead to a degraded user experience. With liveness probes, Kubernetes can quickly detect unhealthy containers and restart them, thereby maintaining the availability of services. This is particularly important in systems that require high uptime and minimal disruptions.
- **Restarting Legacy Applications**: Some applications are not designed to recover gracefully from certain failures and might require a restart to function properly again. Liveness probes are particularly useful for legacy applications or those that do not have robust error-handling mechanisms built in. By configuring a simple liveness probe, Kubernetes can manage these applications effectively, ensuring that they remain operational without requiring extensive code changes.
- **Graceful Recovery from Resource Exhaustion**: Applications may sometimes use up all available resources, like CPU or memory, causing them to become unresponsive. A liveness probe can detect such resource exhaustion by monitoring endpoints or processes within the container. Once the issue is detected, Kubernetes can restart the container to free up resources and allow the application to start afresh.

### When to use?

- Liveness probes are useful when:
    - An application might enter an unresponsive state, and restarting the container can recover it.
    - When we want to ensure that an application remains healthy and responsive throughout its lifecycle.
    
### Example:

- A simple example of a liveness probe using an NGINX container in Kubernetes. 
- Then configure the liveness probe to check an HTTP endpoint provided by NGINX, and then simulate a failure to observe how Kubernetes restarts the container.
- [Manifest](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/liveness/basic-example.yaml)
- [Explanation](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/liveness/basic-example.md)