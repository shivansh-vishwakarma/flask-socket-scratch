from src.app import app, socketio
from unittest import TestCase
from flask_socketio import SocketIOTestClient


class TestSocketEmit(TestCase):
    def setUp(self):
        self.client = app.test_client()
        self.socketio_test_client = SocketIOTestClient(app, socketio=socketio)
        self.socketio_test_client.connect()

    def test_websocket_emit(self):
        self.socketio_test_client.emit('your_event', {'data': 'test'})
        response = self.socketio_test_client.get_received()
        self.assertEquals(len(response), 1, "Should be one")
        print(response)

    def tearDown(self):
        self.socketio_test_client.disconnect()