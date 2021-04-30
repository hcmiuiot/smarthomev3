#Authen-Import  
import jwt
import json
import datetime
from flask import  jsonify, request, make_response,session
from functools import wraps
from Crypto.PublicKey import RSA 
#     ##########
from flask import Flask
#     from modules import mqttmodule
#     from config import conf
#     from constant import const
  
    
#     from util import bulb,\
#             fan,\
#             temphumidity

app = Flask('iot')
 
@app.route('/')
def hello():
    return 'Develop: Smarthomev3 - IoTClubs'

# mqtt = mqttmodule.appConfig(app)

# @mqtt.on_connect()
# def handle_connect(client, userdata, flags, rc):
#     try:
#         mqtt.subscribe('kuerl')
#         for x in const.smarthomev3:
#             mqtt.subscribe(x)
#         print('Subscribe Successfully')
#     except Exception as e:
#         print('Error: ', e)

# @mqtt.on_message()
# def handle_mqtt_message(client, userdata, message):
#     data = dict(
#         topic=message.topic,
#         payload=message.payload.decode()
#     )
#     try:
#         if data['topic'] == const.smarthomev3[1]:
#             print('---------------- Bulb Process ----------------')
#             bulb.controlBulb(data['payload'])
#         if data['topic'] == const.smarthomev3[2]:
#             print('---------------- Fan Process ----------------')
#             fan.controlFan(data['payload'])
#         if data['topic'] == const.smarthomev3[3]:
#             print('---------------- Temperature Process ----------------')
#             temphumidity.getTemperature(data['payload'])
#         if data['topic'] == const.smarthomev3[4]:
#             print('---------------- Humidity Process ----------------')
#             temphumidity.getHumidity(data['payload'])
#     except Exception as e:
#         print('Get Messages Error: ', e)
#################################################################################################################
#authen
#Session['secretToken']=payload
#Flow_1 : login() -> generate_RSA() -> store privateKey in Session ; publicKey + header -> client.cookie ;
#Flow_n : connect -> token_required() -> accessibility 

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get('authen')+"."+session['secretPayload']
        if not token:
            return jsonify({'message' :  token}), 403

        try: 
            data = jwt.decode(token, session['publicKey'], algorithms=["RS256"])
        except:
            return jsonify({'message' : 'Token is invalid'}), 403
        return f(*args, **kwargs)

    return decorated

@app.route('/unprotected')
def unprotected():
    return jsonify({'message' : 'Anyone can view this!'})

@app.route('/protected')
@token_required
def protected():
    return jsonify({'message' : 'This is only available for people with valid tokens.'})

@app.route('/login')
def login():
    auth = request.authorization
    
    if auth and auth.password == 'password':
        ##Generate RSA key pair
        private_key,public_key=generate_RSA()
        #Store private_key on session
        private_key=private_key.decode('UTF-8')
        public_key=public_key.decode('UTF-8')
        session['publicKey']=public_key
        session['secretKey']=private_key
        
        ## Encode jwt RS256(RSA)
        headerType=dict({'public':public_key,'user':auth.username})
        token = jwt.encode({'user' : auth.username,'password':auth.password, 'exp' : datetime.datetime.utcnow() + datetime.timedelta(seconds=15)},headers=headerType ,algorithm='RS256',key=private_key)
        header, payload, signature = token.split(".")
        session['secretPayload']=payload+"."+signature
        ##Respone
        respone=make_response()
        respone.set_cookie('authen',header)
        return respone

    return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'})
def generate_RSA():
    
    new_key = RSA.generate(bits=2048, e=65537) # e must be odd positive number >= 65537 ; bits : key length
    public_key = new_key.publickey().exportKey("PEM") # export keys as PEM container type
    private_key = new_key.exportKey("PEM")
    return private_key, public_key
def log_out():
    session.pop('secretKey', None)
    session.pop('publicKey', None)