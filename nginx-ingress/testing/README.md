# Simple hands-on guide:
## Task Overview:  
- The objective is to access a URL with your preferred name included as a path segment, as illustrated in the provided screenshot below. This task demonstrates the functionality of the NGINX Ingress Controller deployed in a Kubernetes environment to achieve this.

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/nginx-ingress/images/snapshot.png)  

**Step 1:** Create an image from a Dockerfile.  
- A Dockerfile is a blueprint for creating a Docker image.
- This Dockerfile creates an image with Nginx installed and configured to serve static web content.
- A container created from this image will automatically start the Nginx web server and listen for incoming connections on port 80.
- Commands to be run after creating the Dockerfile:
```
# Command to build an image from the Dockerfile
docker build .

# Login to the appropriate container registry
docker login <registry_URL>

# Tag the image:
docker tag <local_image_ID> <registry_URL>/<repository_name>:<tag>

# Push the image to registry:
docker push <registry_URL>/<repository_name>:<tag>

# To delete an image:
docker rmi <image_name/ID>
```

**Step 2:** Create a namespace.  
- A namespace is a virtual cluster within a Kubernetes cluster.
- Command:
```
# To create a namespace:
kubectl create ns <namespace-name>

# To delete a namespace:
kubectl delete ns <namespace-name>
```

**Step 3:** Create a Deployment manifest file.  
- A deployment in Kubernetes is an object that manages the deployment and scaling of a set of identical pods.
- A pod is the smallest deployable unit in Kubernetes and represents a single instance of a containerized application.
- This deploys a single replica/pod as specified in which the dynamic application (based on the image specified, image: saimanasak/dynamic-webpage:v1.0.0) is running.
- Commands to deploy:
```
# To create the deployment:
kubectl apply -f <deploy-file-name>

# To delete the deployment, this deletes the replicas as well:
kubectl delete -f <deploy-file-name>
```

**Step 4:** Create a Service manifest file.  
- A Service in Kubernetes is like a front door that provides a reliable address for accessing the different parts of an application or multiple applications within a Kubernetes cluster.
- It hides the complex networking details and ensures that communication between these parts is smooth and consistent.
- This creates a service named ‘dynamic-service’ of the type ‘ClusterIP’.
- Commands:
```
# To create/apply the changes in the service:
kubectl apply -f <service-file-name>

# To list the services in a namespace:
kubectl get svc -n <namespace>

# To list all the services:
kubectl get svc - A

# To list the endpoints:
kubectl get endpoints -n <namespace-name>

# To delete a service:
kubectl delete svc <service-name> -n <namespace>
```

**Step 5:** Create an IngressClass manifest file.  
- IngressClass is a resource that provides info about how an Ingress controller should be implemented.
- It allows users to specify which controller should be responsible for managing Ingress resources in the cluster.
- Here, I used NGINX Ingress Controller as specified ‘controller: nginx.org/ingress-controller’
- It is a cluster-level resource, not a namespace-level resource.
- Command:
```
# To deploy:
kubectl apply -f <ingressclass-file-name>

# To list the IngressClass:
kubectl get ingressclass

# To delete:
kubectl delete ingressclass <ingressclass-name>
```

**Step 6:** Create an Ingress manifest file.  
- An Ingress is a resource that is designed to facilitate the inbound traffic into your Kubernetes cluster.
- Make sure that ingressClassName is specified correctly as given in the previous step(5).
- This is a namespace-level resource.
- Command:
```
# To deploy:
kubectl apply -f <ingress-file-name>

# To list the ingress:
kubectl get ingress -n <namespace-name>
```

**Step 7:** Deploy NGINX Ingress Controller.  
- I’ve deployed the controller using helm:
```
# Set the ingressClass name so that they can communicate correctly:
helm install my-nginx-ingress ingress-nginx   --set controller.ingressClass=nginx   --namespace ingress-nginx

helm install <release-name> <helm-chart-name> --set controller.ingressClass=<ingressClassName> --namespace <namespace-name>

# To uninstall:
helm uninstall <release-name>
```

**Step 8:** Load Balancer IP.
- You can find the external load balancer IP using the below command.
`kubectl get svc -A`
- This is of LOAD BALANCER service type and Helm installs this when the previous step(7) is done.

**Step 9:** Access the URL.  
- Once you get the load balancer IP, try to access the webpage.
- URL- http://LB-IP/your-name/
- And it’s done 🙌

## Architecture Diagram:

![screenshot](https://github.com/saimanasak/kubernetes/blob/main/nginx-ingress/images/NGINX-Ingress-Controller-Architecture.png)  