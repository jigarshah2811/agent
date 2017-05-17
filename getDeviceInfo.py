import json
import logging
import agent_info
logger = logging.getLogger('WebSocketClient')

"""
Figure out how many devices are reachable through this Raspberry Pi
    #   We will figure it out using either querying to GPIO pins or using ONVIF to communicate to camera
    #       for this camera has to be ONVIF S-Profile supported
    #       Or Camera and Sensors has to provide APIs to talk to them through GPIO
"""
def getDeviceInfo(request):
    logger.debug("Preparing device list...")
    device_list = []
    for count in xrange(agent_info.total_device):
        device_list.append(
            {"IP": agent_info.ip,
             "MAC": agent_info.mac,
             "SerialNo": agent_info.serial,
             "Firmware": agent_info.firmware
             }
        )


    logger.debug("Prepare response to cloud...")
    response = {"api": "getDeviceInfo", "result": "SUCCESS", "total_devices": len(device_list)}
    for count in xrange(len(device_list)):
        response["device-".format(count)] = device_list[count]

    return response
