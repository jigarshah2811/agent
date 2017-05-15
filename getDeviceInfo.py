import json
import logging
logger = logging.getLogger('WebSocketClient')

"""
Figure out how many devices are reachable through this Raspberry Pi
    #   We will figure it out using either querying to GPIO pins or using ONVIF to communicate to camera
    #       for this camera has to be ONVIF S-Profile supported
    #       Or Camera and Sensors has to provide APIs to talk to them through GPIO
"""
def getDeviceInfo(request):
    IP_address = '192.168.1.60'
    MAC_address = '00-15-E9-2B-99-3C'
    Serial_Number = '1L080B50230'
    Firmware_Version = 'V1.0.0'
    total_devices = 1

    logger.debug("Preparing device list...")
    device_list = []
    for count in xrange(total_devices):
        device_list.append(
            {"IP": IP_address,
             "MAC": MAC_address,
             "SerialNo": Serial_Number,
             "Firmware": Firmware_Version
             }
        )


    logger.debug("Prepare response to cloud...")
    response = {"api": "getDeviceInfo", "result": "SUCCESS", "total_devices": len(device_list)}
    for count in xrange(len(device_list)):
        response["device-".format(count)] = device_list[count]

    response = json.dumps(response, ensure_ascii=False)
    return response
