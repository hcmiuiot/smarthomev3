try:
    from flask import Flask
    from modules import mqttmodule
    from config import conf
    from constant import const
    from util import bulb,\
            fan,\
            temphumidity
except Exception as e:
    print('Some modules are missing {}'.format(e))

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Develop: Smarthomev3 - IoTClubs'

try:
    mqtt = mqttmodule.appConfig(app)
except Exception as e:
    print('Error at define mqtt: ',e)

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    try:
        mqtt.subscribe('kuerl')
        for x in const.smarthomev3:
            mqtt.subscribe(x)
        print('Subscribe Successfully')
    except Exception as e:
        print('Error: ', e)

@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    try:
        if data['topic'] == const.smarthomev3[1]:
            print('---------------- Bulb Process ----------------')
            bulb.controlBulb(data['payload'])
        if data['topic'] == const.smarthomev3[2]:
            print('---------------- Fan Process ----------------')
            fan.controlFan(data['payload'])
        if data['topic'] == const.smarthomev3[3]:
            print('---------------- Temperature Process ----------------')
            temphumidity.getTemperature(data['payload'])
        if data['topic'] == const.smarthomev3[4]:
            print('---------------- Humidity Process ----------------')
            temphumidity.getHumidity(data['payload'])
    except Exception as e:
        print('Get Messages Error: ', e)