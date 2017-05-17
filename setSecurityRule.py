import json

def setSecurityRule(request):
    #having no idea how to use security rule
    list = json.loads(request)
    list_of_devices = [] #compile some list from configuration
    for device in list_of_devices:
        device_param = json.loads(list[device])
        #set the device parameters in configuration
        #Do what you need for configuring network
