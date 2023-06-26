#!/bin/bash

# login docker before running: `docker login`
docker tag marketplace:latest thangcest2/onlinebooks_marketplace:latest
docker push thangcest2/onlinebooks_marketplace:latest

docker tag recommendations:latest thangcest2/onlinebooks_recommendations:latest
docker push thangcest2/onlinebooks_recommendations:latest
