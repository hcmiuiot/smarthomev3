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
        order = (param - active)/10
        if order == 1:
            plug = 17,
        else:
            plug = 18 # Bulb 2
        if active == 0:
            print('Light: ',int(order),' is turn off')
            turnOff(int(plug))
        elif active == 1:
            print('Light: ',int(order),' is turn on')
            turnOn(int(plug))
        else:
            print('Not Valid Param')
    except Exception as e:
        print('Bulb Error: ', e)