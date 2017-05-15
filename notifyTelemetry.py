#!/usr/bin/python

import psutil
import json
from bandwidth_calculator import bandwidth_calculator
from threading import Thread
from pythonwifi.iwlibs import Wireless

def notifyTelemetry():

    #the following two lines will give wifi APNs and its strength, but they will run only on linux
    #you will get fcntl error on other systems
    #wifi = Wireless('eth1')
    #print wifi.getStatistics()[1].getSignallevel()

    bw = bandwidth_calculator()

    bw.provide_bandwidth()

    #thread = Thread(target = bw.calculate_bandwidth)
    #print "starting thread"
    #thread.start()
    #print "thread started"

    cpu_usage_1sec = psutil.cpu_percent(interval=1)
    cpu_usage_5sec = psutil.cpu_percent(interval=5)

    # NOTE: list of highest talkers can be identified if all data going through rapsberry pi is observed and noted

    nw_stat = psutil.net_io_counters()
    interface_stat = psutil.net_if_addrs()

    response = json.dumps({"msg": "notifyTelemetry", "status": "success", "cpu_usage_1sec": cpu_usage_1sec,
                         "cpu_usage_5sec": cpu_usage_5sec, "avg_bandwidth": 0, "ping_speed": bw.ping_speed,
                           "ul_speed": bw.ul_speed, "dl_speed": bw.dl_speed,
                           "nw_stat": nw_stat, "interface_stat": interface_stat})

    #print "joining thread"
    #bw.exit = 1
    #thread.join()
    #print "thread joined"

    return response

print notifyTelemetry()