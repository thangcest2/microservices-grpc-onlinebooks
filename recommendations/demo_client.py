from recommendations_pb2 import BookCategory, RecommendationRequest
import grpc
from recommendations_pb2_grpc import RecommendationsStub

channel = grpc.insecure_channel("localhost:50051")
client = RecommendationsStub(channel)

request = RecommendationRequest(user_id=1, category=BookCategory.SCIENCE_FICTION, max_results=3)
res = client.Recommend(request)
print('RAW recommendations:')
print(type(res.recommendations))
print(res.recommendations)
print(len(res.recommendations))

print('__str__ response:')
print(type(res))
print(res)
