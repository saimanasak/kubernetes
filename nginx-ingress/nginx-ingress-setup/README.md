## NGINX Ingress Controller:  
- There are multiple ways to install NGINX Ingress Controller. 
1. Using Helm Chart   
2. Using Manifests  
3. Using NGINX Ingress Operator  

### Steps to install in each way:  
1. **Using Helm Chart**:  
    - Install Helm:  
        - Download the binary of desired version: [Release](https://github.com/helm/helm/releases)  
        - Extract the binary: `tar -zxvf helm-v3.7.0-linux-amd64.tar.gz`  
        - Move the extracted Helm binary to a location in the system path: `sudo mv linux-amd64/helm /usr/local/bin/helm`  
        - Verify the installation: `helm version`  
        - Initialize helm: `helm init`  
        - (optional) Helm uses repositories to fetch charts. We can add repositories to Helm using the `helm repo add` command.  
        - To add the official Helm stable charts repo to local Helm configuration: `helm repo add stable https://charts.helm.sh/stable` We can choose any name, but, it's named stable for the official stable repo.  
        - Other ways to install: [Helm](https://helm.sh/docs/intro/install/)  
    - Install NGINX Ingress Controller using Helm Chart:  
        - Command to install:  
        ```
        # Set the ingressClass name so that they can communicate correctly:
        helm install my-nginx-ingress ingress-nginx   --set controller.ingressClass=nginx   --namespace ingress-nginx

        helm install <release-name> <helm-chart-name> --set controller.ingressClass=<ingressClassName> --namespace <namespace-name>
        ```
        - Command to uninstall a release:  
        ```
        helm uninstall <release-name>
        ```
    - There are many other ways to install the controller: [NGINX Ingress Controller using Helm](https://docs.nginx.com/nginx-ingress-controller/installation/installing-nic/installation-with-helm/)  
    
2. **Using Manifests**:  
    