from flask_mqtt import Mqtt

# Flask-Mqtt: Config
def appConfig(app):
    try:
        app.config['MQTT_BROKER_URL'] = 'broker.mqttdashboard.com'
        app.config['MQTT_BROKER_PORT'] = 1883
        app.config['MQTT_USERNAME'] = ''
        app.config['MQTT_PASSWORD'] = ''
        app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
        mqtt = Mqtt(app)
        return mqtt
    except Exception as e:
        print('Error appConfig: ',e)

# Flask-Mqtt: Subscribe

# Flask-Mqtt: Public