def controlFan(param):
    try:
        param = int(param)
        active = param%10
        if active == 0:
            order = (param - active)/10
            print('Fan: ',int(order),' is turn off')
        elif active == 1:
            order = (param - active)/10
            print('Fan: ',int(order),' is turn on')
        else:
            print('Not Valid Param')
    except Exception as e:
        print('Fan Error: ', e)