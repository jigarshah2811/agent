import json
import psutil
import datetime
from configuration import configuration

def getHealthStatus():
    config = configuration()

    cpu_usage = psutil.cpu_percent(interval=1)
    mem_usage = psutil.virtual_memory()
    swap_mem_usage = psutil.swap_memory()
    nw_stat = psutil.net_io_counters()
    interface_stat = psutil.net_if_addrs()
    boot_time = datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")
    esn = config.getEsn()

    #write code using onvif or using GPIO to get information about sensors and camera

    response = json.dumps( {"msg": "getHealthStatusResult", "status": "success", "esn": esn, "cpu_usage": cpu_usage,
                            "mem_usage": mem_usage, "swap_mem_usage": swap_mem_usage, "nw_stat": nw_stat,
                            "interface_stat": interface_stat, "boot_time": boot_time} )

    return response

print getHealthStatus()