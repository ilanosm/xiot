from flask import render_template, request, session, jsonify
from flask_socketio import emit, send, SocketIO
from flask_session import Session
from main import app, socketio

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
socketio = SocketIO(app,manage_session=False)

users = {}
answers = {
    'hello': 'Hello, how are you?',
    'how are you?': "I'm fine thanks for asking, how are you?",
    'did barca win today?': 'Yes they did, 3:1.',
    "what's your name?": "I can't say that, I'm shy",
    "bok": "I' can't understand that, did you mean book? What book?",
    "kako si": "What is kako? Is this spanish? Yes?"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/login', methods=['POST'])
def login():
   username = request.form.get('username')
   return jsonify({'username': username})

@socketio.on('question')
def send_response(question):
    print(question)
    if question == 'i want to buy a mobile':
        emit('response', {'data': 'can I know the mobile brand'})
    elif question == 'motorola':
        emit('response', {'data': 'oh great , we are having moto x4 and moto g5 , please select one'})
    elif question == 'moto x4':
        emit('response', {'data': 'we already had you address , please provide mobile number'})
    elif question == 'moto g5':
        emit('response', {'data': 'we already had you address , please provide mobile number'})
    elif question == '9951120311':
        emit('response', {'data': 'wow, you order will be placed soon , thankyou for the your time'})
    else:
        emit('response', {'data': 'i cannot help you'})
