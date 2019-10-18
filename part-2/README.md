# part-2

# challange :-

Write configuration files to deploy the microservices in one of the following
orchestrator
1) Kubernetes(Minikube)
2) Docker swarm
3) ECS

# Solution:- 
As per the challange I need to choose any one option , but I choose two option to show some terraform skill from my end . I hope you like it .
1) # Minikube , under this task I created part-2 folder which is having two folder.

1st-folder:- microservice-1-Dockerfile >> Dockerfile,micro-1.py,requirements.txt
2nd-folder:- microservice-2-Dockerfile >> Dockerfile,micro-2.py,requirements.txt
3rd-folder:- k8s >> k8s-app-deployment.yaml

## Command to perform the above task:-
cd k8s
kubectl create -f k8s-app-deployment.yaml

2) # ECS
In this , I create ECR adn ECS setup using "Terraform". So our all the deplyment is only one click process.
# note:- its # Demo shows only single mirco-service istallation.
Please check part-4 for terraform-ECR/ECS setup.

  
