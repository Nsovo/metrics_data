# hitchhiker_server.py
import asyncio
import os
from pathlib import Path
from grpclib.server import Server
from hitchhiker_pb2 import SourceId, FileList, Empty
from hitchhiker_pb2_grpc import HitchhikerSourceBase

class HitchhikerSourceImpl(HitchhikerSourceBase):

    async def GetSourceId(self, stream) -> SourceId:
        _ = stream
        return SourceId(id="pilot04")

    async def GetDownloads(self, stream) -> FileList:
        request = await stream.recv_message()
        client_id = request.client_id
        destination_id = request.destination_id

        if destination_id != "befit_1":
            return FileList(files=[])

        return FileList(files=[])

    async def DownloadFile(self, stream) -> FileList:
        request = await stream.recv_message()
        files = request.files

        for file in files:
            yield file

    async def MarkDelivered(self, stream) -> Empty:
        request = await stream.recv_message()
        files = request.files

        for file in files:
            print(f'Marked file {file.file_id} as delivered')
            try:
                os.remove(file.file_id)
                print(f'Deleted file {file.file_id}')
            except FileNotFoundError:
                print(f'File {file.file_id} not found')
            except PermissionError:
                print(f'Permission denied for deleting file {file.file_id}')
            except Exception as e:
                print(f'Error occurred while deleting file {file.file_id}: {str(e)}')

        return Empty()

async def main():
    server = Server([HitchhikerSourceImpl()])
    await server.start('localhost', 50051)
    path = os.path.join(os.path.dirname(__file__), "data/metrics.json")

    asyncio.create_task(server.services[0].garbage_collector(path, 500))
    try:
        await server.wait_closed()
    except KeyboardInterrupt:
        await server.close()

if __name__ == "__main__":
    asyncio.run(main())
