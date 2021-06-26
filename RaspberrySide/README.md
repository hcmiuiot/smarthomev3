## Define mqtt topic
    root:  'smarthomev3'
        token?
    bulb:  'smarthomev3/items/bulb'
        bulborther*10+boolean
    fan:  'smarthomev3/items/fan'
        fanorther*10+boolean
    temperature:  'smarthomev3/items/temperature'
        temperature
    humidity:  'smarthomev3/items/humidity'
        humidity

## To venv
    & d:/WorkSpace/SmartHomeV3RasSide/venv/Scripts/Activate.ps1

### Note
        # check list order
        # How to name bulb?