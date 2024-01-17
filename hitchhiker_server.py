from grpclib.server import Server
from hitchhiker_pb2 import SourceId, File, FileList, DownloadsRequest, DownloadRequest, DeliveredRequest, Empty
from hitchhiker_grpc import HitchhikerSourceBase
from business_logic import BusinessLogic
import asyncio

import logging

logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s')


DESTINATION_ID = "befit_1"

class HitchhikerSourceImpl(HitchhikerSourceBase):
    def __mapping__(self):
        return {}

    async def GetSourceId(self, stream):
        _ = stream
        logging.info("get source id")
        source_id = BusinessLogic.get_source_id()
        return SourceId(id=source_id)

    async def GetDownloads(self, stream):
        request: DownloadsRequest = await stream.recv_message()
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

    async def DownloadFile(self, stream):
        request: DownloadRequest = await stream.recv_message()
        files = [
            File(fileId=file.fileId, filename=file.filename, type=file.type, blob=b"blob") for file in request.files
        ]
        await stream.send_message(FileList(files=files))

    async def MarkDelivered(self, stream):
        request: DeliveredRequest = await stream.recv_message()
        for file in request.files:
            print(f"File {file.fileId} delivered by client {request.clientId} to destination {request.destinationId}")
        await stream.send_message(Empty())

async def start_server():
    server = Server([HitchhikerSourceImpl()])
    logging.info("Server has started")
    await server.start('localhost', 50051)
    await server.wait_closed()

asyncio.get_event_loop().run_until_complete(start_server())
