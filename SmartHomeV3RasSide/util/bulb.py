# Hardware Code
try:
    import RPi.GPIO as GPIO
except Exception as e:
    print('Hardware Lib Error: {}'.format(e))

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

def turnOn(plug):
    try:
        GPIO.setup(plug,GPIO.OUT)
        GPIO.setup(plug,GPIO.HIGH)
    except Exception as e:
        print('Bulb Process Error: ',e)

def turnOff(plug):
    try:
        GPIO.setup(plug,GPIO.OUT)
        GPIO.setup(plug,GPIO.LOW)
    except Exception as e:
        print('Bulb Process Error: ',e)

# Util Code
def controlBulb(param):
    try:
        param = int(param)
        active = param%10
        order = (param - active)/10
        if order == 1:
            plug = 17
        if order == 2:
            plug = 18
        if active == 0:
            print('Light: ',int(order),' is turn off')
            turnOff(plug)
        elif active == 1:
            print('Light: ',int(order),' is turn on')
            turnOn(plug)
        else:
            print('Not Valid Param')
    except Exception as e:
        print('Bulb Error: ', e)