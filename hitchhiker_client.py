import asyncio
import grpc
from hitchhiker_pb2 import Empty, DownloadsRequest, DownloadRequest, DeliveredRequest
from hitchhiker_grpc import HitchhikerSourceStub
import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')

async def run():
        channel = grpc.insecure_channel('127.0.0.1:50051')

        stub = HitchhikerSourceStub(channel)
        logging.info(f"service: {stub}")

        try :
            response = await stub.GetSourceId(Empty())
            print(f"GetSourceId response: {response}")

            # Test GetDownloads
            request = DownloadsRequest(clientId="client1", destinationId="destination1")
            response = stub.GetDownloads(request)

            # Test DownloadFile
            files = []  # Define the "files" variable as an empty list
            request = DownloadRequest(fileId="file1")
            response = stub.DownloadFile(request)
            print(f"GetSourceId response: {response}")

            #Test MarkDelivered
            request = DeliveredRequest(clientId="client1", destinationId="destination1", files=files)
            response = stub.MarkDelivered(request)
            print(f"MarkDelivered response: {response}")
        except Exception as e:
            logging.warning("This is a warning message:: %s", e)
            print(e)

asyncio.run(run())