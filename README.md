# Title

Micro-controllers: Promoting Structurally Flexible Controllers in Self-Aware Computing Systems

# Abstract 

To promote structurally flexible controllers in systems such as self-aware computing systems, this paper proposes the use of micro-controllers. Instead of generic monolithic controllers, like Rainbow, we advocate the use of service-specific micro-controllers which can be based on microservices.
Although traditional generic controllers can be configured parametrically according to system needs, their use and reuse are nevertheless restrictive because of the wide range of services expected from the different stages of the feedback control loop. The solution being advocated is to have structurally flexible controllers that can be composed from micro-controllers. Controlling the architectural configuration of these micro-controllers is a meta-controller that is able to configure the controller according to the services required for controlling the target system. The feasibility of the proposed approach was published in the [Paper](https://ieeexplore.ieee.org/abstract/document/9196296).

A [video](https://www.youtube.com/watch?v=mNT64knfeUM) was recorded to an overview to [SeAC_2020](http://seac2020.informatik.uni-wuerzburg.de/program/) 

In this repository we provide improvements using the approaches and we extend it using different technologies. The next figure present an initial ideia of this repository.

![draft_architecture](/docs/initialArchitecture.png)



## Environment Deployments

# Cluster configurations (Windows + hyperv)

minikube start --cpus=5 --vm-driver hyperv --hyperv-virtual-switch "Primary Virtual Switch" --kubernetes-version=v1.16.10
minikube addons enable ingress

## Tools and Target System
# monitoring: 
kubectl apply -k .\tools\monitoring\

# target system - kube-znn
kubectl apply -k .\targetSystem\kube-znn\overlay\default\

# nginxc-ingress
kubectl apply -f .\tools\nginxc-ingress\

## Microcontrollers

# kubow-based
kubectl apply -k .\Microcontrollers\kubow_based\fidelity_microcontroller\kubow\overlay\kube-znn\
kubectl apply -k .\Microcontrollers\kubow_based\scalability_microcontroller\kubow\overlay\kube-znn\

# customised-based

## Metacontoller


## Utilities for testing

# generating data
kubectl apply -k .\Testing\k6\

# Generating logs

kubectl logs pod/metacontroller-kubow-84c9b6ff8d-4nhnb >> arquivo23112020.log

# Monitoring manually the PowerShell terminal

while (1) {clear; kubectl get all; sleep 5}
while (1) {clear; kubectl describe deployment kube-znn; sleep 5}

# To analyse event failures for a specific pod
kubectl describe pod kube-znn-644ff8f5d6-59r9n

# query prometheus in K8s

kubectl port-forward pod/prometheus-d4499d495-rh2rt 9090:9090