# Hardware Code
try:
    from gpiozero import LED
    from time import sleep
except Exception as e:
    print('Hardware Lib Error: {}'.format(e))

led = LED(17)

def turnOn():
    try:
        led.on()
    except Exception as e:
        print('Bulb Process Error: ',e)

def turnOff():
    try:
        led.off()
    except Exception as e:
        print('Bulb Process Error: ',e)

# Util Code
def controlBulb(param):
    try:
        param = int(param)
        active = param%10
        order = (param - active)/10
        if active == 0:
            print('Light: ',int(order),' is turn off')
            turnOff()
        elif active == 1:
            print('Light: ',int(order),' is turn on')
            turnOn()
        else:
            print('Not Valid Param')
    except Exception as e:
        print('Bulb Error: ', e)