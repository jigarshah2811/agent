import psutil
import time
import pyspeedtest

class bandwidth_calculator():
    bandwidth = 0
    ping_speed = 0
    ul_speed = 0
    dl_speed = 0
    exit = 0

    def provide_bandwidth(self):
        st = pyspeedtest.SpeedTest()
        #server = "speedtest.serv.pt"
        self.ping_speed = (st.ping() / (1024*1024))
        self.dl_speed = (st.download() / (1024*1024))
        self.ul_speed = (st.upload() / (1024*1024))

    def convert_to_mbit(self, value):
        value = value*8 #convert bytes to bits
        bandwidth_calculator.bandwidth = value/(1024*1024)  #devide by 1 M_bits

    def calculate_bandwidth(self):
        prev_value = 0

        while True:
            if self.exit:
                break

            new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

            if new_value:
                if prev_value:
                    self.convert_to_mbit(new_value - prev_value)

                prev_value = new_value

            time.sleep(1)

    #def send_stat(value):
    #    print ("%0.3f" % convert_to_mbit(value))