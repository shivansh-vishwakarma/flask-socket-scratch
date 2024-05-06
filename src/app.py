from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, async_mode="threading")

@app.route('/')
def index():
    return {"message": 'working'}


@socketio.on('my_event')
def my_event(message):
    print(message)


@socketio.on('connect')
def connect():
    print("connected")


@socketio.on('disconnect')
def disconnect():
    print("disconnected")

if __name__ == '__main__':
    app.run(debug=True)

# gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 :app