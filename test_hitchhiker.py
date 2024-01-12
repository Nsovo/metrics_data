import unittest
from unittest.mock import MagicMock
from hitchhiker_server import HitchhikerSourceImpl

class HitchhikerSourceImplTestCase(unittest.TestCase):

    def setUp(self):
        self.source = HitchhikerSourceImpl()

    def test_GetSourceId(self):
        stream = MagicMock()
        source_id = self.source.GetSourceId(stream)
        self.assertEqual(source_id.id, "pilot04")

    def test_GetDownloads(self):
        stream = MagicMock()
        stream.recv_message.return_value = MagicMock(client_id="client01", destination_id="befit_1")
        file_list = self.source.GetDownloads(stream)
        self.assertEqual(file_list.files, [])

    def test_DownloadFile(self):
        stream = MagicMock()
        stream.recv_message.return_value = MagicMock(client_id="client01", files=["file1", "file2"])
        files = list(self.source.DownloadFile(stream))
        self.assertEqual(files, ["file1", "file2"])

    def test_MarkDelivered(self):
        stream = MagicMock()
        stream.recv_message.return_value = MagicMock(client_id="client01", destination_id="befit_1", files=["file1", "file2"])
        result = self.source.MarkDelivered(stream)
        self.assertIsInstance(result, Empty)

if __name__ == '__main__':
    unittest.main()