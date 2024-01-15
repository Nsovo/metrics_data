from grpclib.client import Channel
from hitchhiker_pb2 import Empty, DownloadsRequest, DownloadRequest, DeliveredRequest, File
from hitchhiker_pb2_grpc import HitchhikerSourceStub

async def main():
    channel = Channel('localhost', 50051)
    service = HitchhikerSourceStub(channel)

    # Test GetSourceId
    response = await service.GetSourceId(Empty())
    print(f"GetSourceId response: {response}")

    # Test GetDownloads
    request = DownloadsRequest(clientId="client1", destinationId="destination1")
    response = await service.GetDownloads(request)
    print(f"GetDownloads response: {response}")

    # Test DownloadFile
    files = [
        File(fileId="file1", filename="filename1", type="type1"),
        File(fileId="file2", filename="filename2", type="type2"),
    ]
    request = DownloadRequest(clientId="client1", files=files)
    response = await service.DownloadFile(request)
    print(f"DownloadFile response: {response}")

    # Test MarkDelivered
    request = DeliveredRequest(clientId="client1", destinationId="destination1", files=files)
    response = await service.MarkDelivered(request)
    print(f"MarkDelivered response: {response}")

    channel.close()

# Run the main function
import asyncio
asyncio.run(main())