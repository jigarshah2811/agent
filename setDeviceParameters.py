import json
from configuration import configuration

def setDeviceParameters(request):
    config = configuration()
    list = json.loads(request)
    list_of_devices = [] #compile some list from configuration
    for device in list_of_devices:
        device_param = json.loads(list[device])

        print device_param['rate_limit'], device_param['nw_telemetry_duration'], device_param['wifi_telemetry_duration']

        # Do what you need for configuring network

        config.setRateLimit(device_param['rate_limit'])
        config.setNwTelemetryDuration(device_param['nw_telemetry_duration'])
        config.setWifiTelemetryDuration(device_param['wifi_telemetry_duration'])