## SERVICES

- Kubernetes services provide a stable interface for accessing a group of pods, allowing for efficient communication and load balancing in containerized applications. 
- They abstract the complexities of pod management and networking by enabling users to connect to pods through a consistent IP address and port, regardless of the underlying pod lifecycle. 
- As pods can be dynamically created or terminated, services ensure that any incoming traffic is directed to the healthy and active pods, thereby enhancing the resilience and reliability of the application.
- Overall, services play a critical role in simplifying the networking layer of Kubernetes, ensuring seamless connectivity and interaction between different components of an application.
- Kubernetes services provide several key benefits that streamline application deployment and management. 
- Firstly, they facilitate service discovery by enabling pods to communicate with one another using stable DNS names rather than relying on ephemeral pod IPs. This feature significantly reduces the complexity associated with managing network connections in dynamic environments, where pods can frequently change. As a result, developers can focus on building and scaling their applications without worrying about network configurations.
- Secondly, services enhance the availability and reliability of applications through load balancing. By distributing incoming traffic among multiple pod replicas, services ensure that the application can handle increased loads and provide uninterrupted service to users. In case of pod failures, the service automatically redirects traffic to healthy pods, minimizing downtime. Additionally, Kubernetes services integrate seamlessly with other components, such as Ingress controllers and network policies, allowing for advanced routing and security configurations. Overall, Kubernetes services are essential for building robust, scalable, and maintainable applications in containerized environments.
- There are three types of services:
    1. [Node Port](https://github.com/saimanasak/kubernetes/tree/main/services/nodeport)
    2. [Cluster IP](https://github.com/saimanasak/kubernetes/tree/main/services/clusterIP)
    3. [Load Balancer](https://github.com/saimanasak/kubernetes/tree/main/services/loadbalancer)