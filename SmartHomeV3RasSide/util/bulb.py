# Hardware Code
try:
    from gpiozero import LED
    from time import sleep
except Exception as e:
    print('Hardware Lib Error: {}'.format(e))

def turnOn(plug):
    try:
        led = LED(plug)
        led.on()
    except Exception as e:
        print('Bulb Process Error: ',e)

def turnOff(plug):
    try:
        led = LED(plug)
        led.off()
    except Exception as e:
        print('Bulb Process Error: ',e)

# Util Code
def controlBulb(param):
    try:
        param = int(param)
        active = param%10
        if active == 0:
            order = (param - active)/10
            print('Light: ',int(order),' is turn off')
            turnOff(int(order))
        elif active == 1:
            order = (param - active)/10
            print('Light: ',int(order),' is turn on')
            turnOn(int(order))
        else:
            print('Not Valid Param')
    except Exception as e:
        print('Bulb Error: ', e)