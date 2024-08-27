# Simple Website creation using kubernetes and docker

To access the app, visit http://34.69.43.90/    followed by argument. In this case, it will be something like "factorial?number=" followed by a number

Reference example
http://34.69.43.90/factorial?number=8


while trying to copy this project, make sure to edit the deployment.yaml file

Sample Build process (Using Google Cloud):
1. setup billing and enable API
   - Kubernetes Engine API
   - one more i forgot just continue with the commands   #cloud shell will tell you the API required when the time is right, re run the command after enabling required API
2. Open cloud shell
3. add files, either via upload, or create using your favourite editor (mine is nano)
4. Create Docker image
    - command for creating docker image
        docker build -t gcr.io/GCP_PROJECT_ID/factorial-app .
        docker push gcr.io/GCP_PROJECT_ID/factorial-app
    - Change the repository location! use that to edit the deployment file too.
5. Create Kubernetes Cluster
    - command for creating cluster
      gcloud container clusters create factorial-cluster --zone us-central1-c --num-nodes=3
      gcloud container clusters get-credentials factorial-cluster --zone us-central1-c
    - Change according to your needs

7. apply the deployment and service files using these commands
    kubectl apply -f deployment.yaml
    kubectl apply -f service.yaml
8. Verify using these commands
    kubectl get nodes
    kubectl get services
9. After you get the external ip address of the load-balancer, access your project using
    ETERNAL_IP_ADDRESS/factorial?number=8
   change number and check if it works

Note: Does not contain any fancy front-end, you are free to add it.
