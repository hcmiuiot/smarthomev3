# Hardware Code
try:
    from gpiozero import LED
    from time import sleep
except Exception as e:
    print('Hardware Lib Error: {}'.format(e))

def turnOn(led):
    try:
        led.on()
    except Exception as e:
        print('Bulb Process Error: ',e)

def turnOff(led):
    try:
        led.off()
    except Exception as e:
        print('Bulb Process Error: ',e)

def turnLight(plugLED, bool):
    led = LED(plugLED)
    if bool == 0:
        turnOff(led)
    if bool == 1:
        turnOn(led)
    print(led)

# Util Code
def controlBulb(param):
    try:
        param = int(param)
        active = param%10
        order = (param - active)/10
        if order == 1:
            plug = 17
        else:
            plug = 18 # Bulb 2
        if active == 0:
            print('Light: ',int(order),' is turn off')
        elif active == 1:
            print('Light: ',int(order),' is turn on')
            turnOn(plug)
        else:
            print('Not Valid Param')
        turnLight(plug, active)
    except Exception as e:
        print('Bulb Error: ', e)