# About: microservices-grpc-onlinebooks in python3
I need to see grpc in more real-life services, real different with JSON, how the client-server works. Code here was from realpython.com. But I packed them all and will give a video/my real account for saving your time.

### What we will play with:
1. Local client-server with grpc
2. Local client-server with grpc - but with docker/docker-compose/poetry
3. Host images to our own docker hub
4. Deploy to docker desktop
5. Deploy to a real gcp account (Skip this part. You can check here: https://github.com/thangcest2/kubernetes-learn#kubernetes-cluster-in-real-gcp-account)

### Key highlights:
- Generation from .proto file to read-only python codes. You can see in recommendations/Dockerfile, too.
```
python -m grpc_tools.protoc -I ../protobufs --python_out=. --grpc_python_out=. ../protobufs/recommendations.proto
# recommendations_pb2.py file: Descriptor/manifest 
# recommendations_pb2_grpc.py file: Client/Server code correspond to .proto file 
```
- `recommendations/recommendations.py`: Start proto server to serve request. Imagine this is as same as a starting a http server that serves JSON API request.
- `marketplace/marketplace.py`: Client that will call the server
- To summary:
  - recommendations/Dockerfile -> recommendations/recommendations starts Protobuf Server.
  - marketplace/Dockerfile -> marketplace/marketplace.py start a Web Server, serve a route in which this route make call to Protobuf Server
  - Browser localhost:5001 -> make call to the Web Server 

### Run it:
- By local docker & web: `docker-compose up` => `localhost:5001`
- By local docker & command line: `docker-compose up` => `docker-compose exec recommendations python demo_client.py`
- By kubernetes with Docker Desktop cluster: `kubectl apply -f kubernetes.yml` => `localhost:4000`

### Push images to docker hub:
- After the `docker-compose up`. Local docker image will be created. Then we push to our own dockerhub for the kubernetes.yml to use
```commandline
docker login
docker image tag recommendations thangcest2/onlinebooks_recommendations:latest
docker image push thangcest2/onlinebooks_recommendations:latest
docker image tag marketplace thangcest2/onlinebooks_marketplace:latest
docker image push thangcest2/onlinebooks_marketplace:latest
```

### Original tutorial:
https://realpython.com/python-microservices-grpc/#production-ready-python-microservices

### Youtube Video: TBD

# License:
MIT


