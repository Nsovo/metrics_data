# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: hitchhiker.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.const
import grpclib.client
if typing.TYPE_CHECKING:
    import grpclib.server

import hitchhiker_pb2


class HitchhikerSourceBase(abc.ABC):

    @abc.abstractmethod
    async def GetSourceId(self, stream: 'grpclib.server.Stream[hitchhiker_pb2.Empty, hitchhiker_pb2.SourceId]') -> None:
        pass

    @abc.abstractmethod
    async def GetDownloads(self, stream: 'grpclib.server.Stream[hitchhiker_pb2.DownloadsRequest, hitchhiker_pb2.FileList]') -> None:
        pass

    @abc.abstractmethod
    async def DownloadFile(self, stream: 'grpclib.server.Stream[hitchhiker_pb2.DownloadRequest, hitchhiker_pb2.FileList]') -> None:
        pass

    @abc.abstractmethod
    async def MarkDelivered(self, stream: 'grpclib.server.Stream[hitchhiker_pb2.DeliveredRequest, hitchhiker_pb2.Empty]') -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            '/HitchhikerSource.HitchhikerSource/GetSourceId': grpclib.const.Handler(
                self.GetSourceId,
                grpclib.const.Cardinality.UNARY_UNARY,
                hitchhiker_pb2.Empty,
                hitchhiker_pb2.SourceId,
            ),
            '/HitchhikerSource.HitchhikerSource/GetDownloads': grpclib.const.Handler(
                self.GetDownloads,
                grpclib.const.Cardinality.UNARY_UNARY,
                hitchhiker_pb2.DownloadsRequest,
                hitchhiker_pb2.FileList,
            ),
            '/HitchhikerSource.HitchhikerSource/DownloadFile': grpclib.const.Handler(
                self.DownloadFile,
                grpclib.const.Cardinality.UNARY_UNARY,
                hitchhiker_pb2.DownloadRequest,
                hitchhiker_pb2.FileList,
            ),
            '/HitchhikerSource.HitchhikerSource/MarkDelivered': grpclib.const.Handler(
                self.MarkDelivered,
                grpclib.const.Cardinality.UNARY_UNARY,
                hitchhiker_pb2.DeliveredRequest,
                hitchhiker_pb2.Empty,
            ),
        }


class HitchhikerSourceStub:

    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.GetSourceId = grpclib.client.UnaryUnaryMethod(
            channel,
            '/HitchhikerSource.HitchhikerSource/GetSourceId',
            hitchhiker_pb2.Empty,
            hitchhiker_pb2.SourceId,
        )
        self.GetDownloads = grpclib.client.UnaryUnaryMethod(
            channel,
            '/HitchhikerSource.HitchhikerSource/GetDownloads',
            hitchhiker_pb2.DownloadsRequest,
            hitchhiker_pb2.FileList,
        )
        self.DownloadFile = grpclib.client.UnaryUnaryMethod(
            channel,
            '/HitchhikerSource.HitchhikerSource/DownloadFile',
            hitchhiker_pb2.DownloadRequest,
            hitchhiker_pb2.FileList,
        )
        self.MarkDelivered = grpclib.client.UnaryUnaryMethod(
            channel,
            '/HitchhikerSource.HitchhikerSource/MarkDelivered',
            hitchhiker_pb2.DeliveredRequest,
            hitchhiker_pb2.Empty,
        )