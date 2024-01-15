from grpclib.server import Server
from business_logic import BusinessLogic
from hitchhiker_pb2 import SourceId, File, FileList, DownloadsRequest, DownloadRequest, DeliveredRequest, Empty
from hitchhiker_grpc import HitchhikerSourceBase
import sys
import asyncio
sys.path.append('/Users/nsovo/Developer/personal/metrics-app/env/lib/python3.12/site-packages')

DESTINATION_ID = "befit_1"
class HitchhikerSourceImpl(HitchhikerSourceBase):
    async def GetSourceId(self, stream):
        _ = stream
        source_id = BusinessLogic.get_source_id()
        return SourceId(id=source_id)

    async def GetDownloads(self, stream):
        request: DownloadsRequest = await stream.recv_message()
        files = [
            File(fileId="file1", filename="filename1", type="type1", blob=b"blob1"),
            File(fileId="file2", filename="filename2", type="type2", blob=b"blob2"),
        ]
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
    await server.start('localhost', 50051)
    await server.wait_closed()

asyncio.run(start_server())
