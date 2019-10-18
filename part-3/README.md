# Part-3
  
## Challange :-

Describe briefly how will you provide CI/CD pipeline for the microservices

## Solution :-
```
Architecting a CI/CD pipeline for container and microservice-based applications


To create a CI/CD pipeline , we have multiple options and I am choosing the below one.

The legacy DevOps pipeline consists of a CI/CD pipeline which includes a code repository (Bit Bucket), an automation server for continuous integration (Jenkins) for rolling out deployments. 
While the Jenkins pipeline extends beyond CI to CD, the existing CI/CD automation was not befitting in leveraging the benefits of immutable infrastructure. 
Jenkins wasn’t designed for deployment in Kubernetes and as the team was new to kubectl terminology there was a need for an easy to manage platform to make reliable deployments . 
We rolled out a CI/CD pipeline using Jenkins and Spinnaker, an open source, multi-cloud continuous delivery platform to help the client deliver code with zero impact to customers
```
```
Spinnaker is a continuous delivery platform (open source)
Jenkins is a continuous integration platform (open source)
```

Steps to setup a pipeline :- 

## Prerequisites
```
A running Kubernetes cluster. If you don’t already have one running, use eksctl to get an EKS cluster up and running with one command.
At least eight GB of free memory and two vCPU in the Kubernetes cluster for Spinnaker microservices. An m5.large instance should do the job.
kubectl  installed, configured, and working on your machine.
Helm installed. To install it, follow the Kubernetes Helm instructions.
Jenkins installed. To install it, follow the instructions in the documentation on Jenkins on AWS.
Docker and the Amazon ECR plugin installed for Jenkins and configured to work.
A Docker registry account. If you don’t have one, you can use Amazon ECR, as we will be doing in this post. You could also use Docker Hub.
An authentication provider (LDAP/SAML/Oauth2). In this post we will be using Active Directory (LDAP) authentication. If you don’t already have one, follow the AWS Managed Microsoft AD documentation.
```

## Steps
```
Once you have all the prerequisites in place, you can begin the actual steps to set up the pipeline. We will go through each of these steps in detail; here’s an overview of what we’ll be doing:

1.Build a sample application.
2.Install Spinnaker on EKS using Helm.
3.Set up LDAP/AD authentication.
4.Expose Spinnaker by setting up an ingress controller.
5.Add a GitHub account to Spinnaker.
6.Configure Amazon ECR in your AWS account to store Docker images pushed by Jenkins.
7.Configure Jenkins for Docker image build and ECR push.
8.Build the CI/CD pipeline in Spinnaker – automated build using web-hook from GitHub, manual approval for deployment to production.
9.Run the pipeline and deploy the application.
```


## Explaining NO.8 from above setps :- 

## Build the CI/CD pipeline in Spinnaker
```
1. Create application
2. Create pipeline
3. Set up configuration
4. Set up artifacts
5. Helm template – sample-microservice-0.1.0.tgz
6. Helm dev override – values/dev.yaml
7. Helm prod override – values/prod.yaml
8. Docker image – 12345678.dkr.ecr.us-west-2.amazonaws.com/sample-microservice
9. Set up pipeline trigger
10. Create stages
11. Bake dev
12. Bake prod
13. Deploy to dev
14. Manual judgement
15. Deploy to prod

```

## Spinnaker-staging looks :-

![Screenshot](https://github.com/Gaurav2586/saloodo/blob/master/screenshot/Spinnaker-staging.png?raw=true "Spinnaker-staging")

## Spinnaker-Prd looks :-

![Screenshot](https://github.com/Gaurav2586/saloodo/blob/master/screenshot/Spinnaker-prod.png?raw=true "Spinnaker-prod")

# THE END






