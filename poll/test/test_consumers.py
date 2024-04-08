import json
import logging
import unittest
from unittest.mock import MagicMock
from channels.testing import WebsocketCommunicator
from myapp.consumers import PollConsumer

class TestPollConsumer(unittest.TestCase):
    def setUp(self):
        self.logger = logging.getLogger(__name__)
        self.consumer = PollConsumer()
        self.consumer.room_group_name = "test_room"
        self.consumer.channel_layer = MagicMock()

    def test_connect(self):
        self.consumer.connect()
        self.assertTrue("test_room" in self.consumer.messages)
        self.consumer.channel_layer.group_add.assert_called_once_with(
            "test_room", self.consumer.channel_name
        )

    def test_receive(self):
        data = json.dumps({"username": "user", "vote": "yes"})
        self.consumer.receive(data)
        self.consumer.channel_layer.group_send.assert_called_once_with(
            "test_room",
            {
                "type": "poll_message",
                "vote": "yes",
                "username": "user"
            }
        )

    def test_poll_message(self):
        event = {"vote": "yes", "username": "user"}
        self.consumer.usernames = []
        self.consumer.messages = {}
        self.consumer.poll_message(event)
        self.assertIn("user", self.consumer.usernames)
        self.assertIn("user voted  yes", self.consumer.messages["test_room"]["user"])

if __name__ == "__main__":
    print("ANA hena")
    unittest.main()
