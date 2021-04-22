def getTemperature(param):
    try:
        param = int(param)
        print('Temperature: ', param)
    except Exception as e:
        print('Temperature Error: ', e)

def getHumidity(param):
    try:
        param = int(param)
        if param < 0 or param > 100:
            print('Not Valid Param')
        else:
            print('Humidity: ', param,'%')
    except Exception as e:
        print('Humidity Error: ', e)