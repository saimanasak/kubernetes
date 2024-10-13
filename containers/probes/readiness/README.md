## READINESS PROBE

- A readiness probe in Kubernetes is used to determine whether a container is ready to accept traffic or serve requests. 
- Unlike a liveness probe, which checks if a container should be restarted when unhealthy, a readiness probe tells Kubernetes if the container should be included in the pool of endpoints for services and load balancers. 
- When a readiness probe fails, the container is temporarily removed from the list of available endpoints without being restarted.

### Why???

- **Control Over Traffic Routing**: Readiness probes ensure that a container does not receive traffic until it is fully ready to handle requests. This prevents users from experiencing errors or timeouts during startup. For example, an application might take time to load configurations, connect to databases, or perform initial data caching before it can serve requests. Until these steps are complete, the readiness probe will keep the container in a not ready state, ensuring that no traffic is directed to it prematurely.
- **Graceful Handling of Temporary Unavailability**: Sometimes, a container might be temporarily unable to handle requests due to ongoing background tasks, such as reindexing a database, performing data migrations, or reloading configurations. During such periods, a readiness probe can detect the temporary unavailability and mark the container as not ready, removing it from the list of endpoints. This ensures that the load balancer or service does not route requests to the container during this time, avoiding potential request failures. Once the container is ready to accept requests again, the readiness probe will mark it as ready, and traffic routing will resume.
- **Smooth Rolling Updates and Deployments**: Kubernetes performs rolling updates when deploying new versions of an application. During this process, new pods are started while old ones are gradually terminated. Readiness probes help control the timing of these updates. Kubernetes only considers a pod as ready when the readiness probe is successful, meaning it won't terminate old pods until the new pods are fully ready. This ensures zero-downtime deployments, where new instances only start receiving traffic when they are fully capable of handling it, maintaining service continuity during updates.
- **Load Balancing and Service Discovery**: Readiness probes play a critical role in load balancing within a Kubernetes cluster. Only pods that pass their readiness checks are included in the pool of endpoints for a service. If a pod fails its readiness probe, it is removed from the pool of endpoints, meaning that no traffic is routed to it. This helps maintain a healthy pool of pods that can reliably serve user requests, enhancing the overall performance and stability of the service.
- **Separation from Liveness Probes**: While liveness probes help ensure that a container is restarted when it’s in an unhealthy state, readiness probes focus on whether the container is prepared to accept requests. For example, a pod might be alive (it hasn't crashed or encountered a fatal error) but not ready to handle incoming traffic (e.g., it is still booting up). In such cases, the readiness probe is crucial to avoid routing traffic to a pod that isn’t prepared to handle it yet. This distinction allows you to create more precise health checks and provides better control over how Kubernetes manages pod availability.

### When to use?

- Should use readiness probes in Kubernetes when we need to control when a pod starts receiving traffic, ensuring that the application inside the pod is fully ready to handle requests.
- When we want to ensure traffic is routed only to fully ready instances.
- When application needs time to become fully functional after startup.
- When application can be temporarily unavailable due to background tasks.
- When we are deploying updates and want a smooth transition.
- When application’s readiness depends on external services or connections.

### Example:
- Create a YAML manifest for an NGINX pod that includes a readiness probe to check if the server is ready to accept traffic.
- Modify the NGINX server to simulate unavailability, and observe how Kubernetes marks the pod as not ready, preventing it from receiving traffic until it is restored.
- [Manifest](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/readiness/basic-nginx-example/basic-example.yaml)
- [Explanation](https://github.com/saimanasak/kubernetes/blob/main/containers/probes/readiness/basic-nginx-example/basic-example.md)