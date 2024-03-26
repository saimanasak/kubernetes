#base image
FROM ubuntu:latest

#maintainer
LABEL maintainer="Sai Manasa" 

#updates package list and installs nginx
RUN  apt-get -y update && apt-get -y install nginx

#copies from the build context to directory within container
COPY default /etc/nginx/sites-available/default
COPY index.html /usr/share/nginx/html/

#container will listen on port 80 at runtime
EXPOSE 80

#default command that runs when container starts
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]