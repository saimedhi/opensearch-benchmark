# from opensearchpy import AsyncTransport
# import json

# class CustomAsyncTransport(AsyncTransport):
#     async def perform_request(self,method, url, params=None, body=None, headers = None, timeout = None,ignore= ()):
#         print("CustomAsyncTransport printed")
#         data = await super().perform_request( method, url,
#                     params,
#                     body,
#                     headers=headers,
#                     ignore=ignore,
#                     timeout=timeout)
#         # s_dict = json.loads(type(data))
#         # if(type(data)!=bool):
#         #     print("CustomAsyncTransport osbenchmark  status, headers_response, data", data.decode('utf-8'))
#         return  data 