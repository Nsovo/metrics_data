from grpclib.server import Server
from business_logic import BusinessLogic
from hitchhiker_pb2 import SourceId, File, FileList, DownloadsRequest, DownloadRequest, DeliveredRequest, Empty
from hitchhiker_pb2_grpc import HitchhikerSourceBase
import asyncio
import os
import sys
cwd = os.getcwd() # get the current working directory
env_path = os.path.join(cwd, 'env', 'lib')  # construct the environment path
sys.path.append(env_path)

DESTINATION_ID = "befit_1"
    
# Implementation of the HitchhikerSourceBase interface.
# This class handles the communication between the client and the server for source-related operations.
    
class HitchhikerSourceImpl(HitchhikerSourceBase):

    """
        Retrieves the source ID from the BusinessLogic module and returns it as a SourceId object.
        Args:
            stream: The gRPC stream used for communication.
        Returns:
            SourceId: The source ID.
    """
    async def GetSourceId(self, stream):
        _ = stream
        source_id = BusinessLogic.get_source_id()
        return SourceId(id=source_id)

    """
    Retrieves the requested files from the client and sends back the list of files available for download.
        Args:
            stream: The gRPC stream used for communication.
    """
    async def GetDownloads(self, stream):
        request: DownloadsRequest = await stream.recv_message()

        # Extract information from the request.
        # Assuming that the request contains a list of file IDs.
        requested_files = request.files

        files = []
        for file in requested_files:
            files.append(File(
                fileId=file.id, 
                filename=file.name, 
                type=file.type, 
                blob=file.blob
            ))

        await stream.send_message(FileList(files=files))

    """
    Retrieves the requested files from the client and sends back the file contents.
        Args:
            stream: The gRPC stream used for communication.
    """
    async def DownloadFile(self, stream):
        request: DownloadRequest = await stream.recv_message()
        files = [
            File(fileId=file.fileId, filename=file.filename, type=file.type, blob=b"blob") for file in request.files
        ]
        await stream.send_message(FileList(files=files))

    """
    Marks the delivered files and prints the delivery information.
        Args:
            stream: The gRPC stream used for communication.
    """
    async def MarkDelivered(self, stream):
        request: DeliveredRequest = await stream.recv_message()
        for file in request.files:
            print(f"File {file.fileId} delivered by client {request.clientId} to destination {request.destinationId}")

        await stream.send_message(Empty())

async def start_server():
    server = Server([HitchhikerSourceImpl()])
    await server.start('localhost', 50051)
    await server.wait_closed()

asyncio.run(start_server())
