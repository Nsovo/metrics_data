import unittest
from unittest.mock import MagicMock
from hitchhiker_server import HitchhikerSourceImpl, File, FileList, SourceId, DownloadsRequest, DownloadRequest, DeliveredRequest, Empty

class TestHitchhikerSourceImpl(unittest.TestCase):
    def setUp(self):
        self.source_impl = HitchhikerSourceImpl()

    def test_GetSourceId(self):
        stream = MagicMock()
        source_id = self.source_impl.GetSourceId(stream)
        self.assertIsInstance(source_id, SourceId)

    def test_GetDownloads(self):
        stream = MagicMock()
        request = DownloadsRequest(files=[File(id=1, name="file1", type="txt", blob=b"blob1"), File(id=2, name="file2", type="txt", blob=b"blob2")])
        stream.recv_message.return_value = request

        self.source_impl.GetDownloads(stream)

        expected_files = [File(fileId=1, filename="file1", type="txt", blob=b"blob1"), File(fileId=2, filename="file2", type="txt", blob=b"blob2")]
        stream.send_message.assert_called_with(FileList(files=expected_files))

    def test_DownloadFile(self):
        stream = MagicMock()
        request = DownloadRequest(files=[File(fileId=1, filename="file1", type="txt"), File(fileId=2, filename="file2", type="txt")])
        stream.recv_message.return_value = request

        self.source_impl.DownloadFile(stream)

        expected_files = [File(fileId=1, filename="file1", type="txt", blob=b"blob"), File(fileId=2, filename="file2", type="txt", blob=b"blob")]
        stream.send_message.assert_called_with(FileList(files=expected_files))

    def test_MarkDelivered(self):
        stream = MagicMock()
        request = DeliveredRequest(clientId=1, destinationId=2, files=[File(fileId=1), File(fileId=2)])
        stream.recv_message.return_value = request

        self.source_impl.MarkDelivered(stream)

        stream.send_message.assert_called_with(Empty())

if __name__ == "__main__":
    unittest.main()import unittest
from unittest.mock import MagicMock
from hitchhiker_server import HitchhikerSourceImpl, File, FileList, SourceId, DownloadsRequest, DownloadRequest, DeliveredRequest, Empty

class TestHitchhikerSourceImpl(unittest.TestCase):
    def setUp(self):
        self.source_impl = HitchhikerSourceImpl()

    def test_GetSourceId(self):
        stream = MagicMock()
        source_id = self.source_impl.GetSourceId(stream)
        self.assertIsInstance(source_id, SourceId)

    def test_GetDownloads(self):
        stream = MagicMock()
        request = DownloadsRequest(files=[File(id=1, name="file1", type="txt", blob=b"blob1"), File(id=2, name="file2", type="txt", blob=b"blob2")])
        stream.recv_message.return_value = request

        self.source_impl.GetDownloads(stream)

        expected_files = [File(fileId=1, filename="file1", type="txt", blob=b"blob1"), File(fileId=2, filename="file2", type="txt", blob=b"blob2")]
        stream.send_message.assert_called_with(FileList(files=expected_files))

    def test_DownloadFile(self):
        stream = MagicMock()
        request = DownloadRequest(files=[File(fileId=1, filename="file1", type="txt"), File(fileId=2, filename="file2", type="txt")])
        stream.recv_message.return_value = request

        self.source_impl.DownloadFile(stream)

        expected_files = [File(fileId=1, filename="file1", type="txt", blob=b"blob"), File(fileId=2, filename="file2", type="txt", blob=b"blob")]
        stream.send_message.assert_called_with(FileList(files=expected_files))

    def test_MarkDelivered(self):
        stream = MagicMock()
        request = DeliveredRequest(clientId=1, destinationId=2, files=[File(fileId=1), File(fileId=2)])
        stream.recv_message.return_value = request

        self.source_impl.MarkDelivered(stream)

        stream.send_message.assert_called_with(Empty())

if __name__ == "__main__":
    unittest.main()