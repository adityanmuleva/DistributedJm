Author : Aaditya Muleva
Date : Feb 11 2023

This project is for distributed load testing using jmeter using kubernetes cluster

#To run this project install dependencies :
1. Docker
2. Kubernetes
3. python3
4. requirements.txt
5. helm


How to run :
#Navigate to helm folder
helm package <target zip>
helm install <release name> <zip file name>

To check status of deployment 
helm list

To check service running 
kubectl get svc

To check deployments 
kubectl get deploy
