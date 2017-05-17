class configuration:
    esn = "12345678"
    rate_limit = 1024*1024*1024     #1 Gbps
    nw_telemetry_duration = 20*60      #20 minutes
    wifi_telemetry_duration = 20*60     #20 minutes


    def getEsn(self):
        return self.esn

    def setEsn(self, esn_value):
        self.esn = esn_value

    def getRateLimit(self):
        return self.rate_limit

    def setRateLimit(self, rate_value):
        self.rate_limit = rate_value

    def getNwTelemetryDuration(self):
        return self.nw_telemetry_duration

    def setNwTelemetryDuration(self, duration_value):
        self.nw_telemetry_duration = duration_value

    def getWifiTelemetryDuration(self):
        return self.wifi_telemetry_duration

    def setWifiTelemetryDuration(self, duration_value):
        self.wifi_telemetry_duration = duration_value
