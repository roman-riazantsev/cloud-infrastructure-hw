#!/usr/bin/env bash

minikube start
kubectl create -f deployment.yml
kubectl create -f service.yml
