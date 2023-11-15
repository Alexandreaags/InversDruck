from hx711 import HX711
from utime import sleep_us


class Scales(HX711):
    def __init__(self, d_out, pd_sck):
        super(Scales, self).__init__(d_out, pd_sck)
        self.offset = -74000
        self.resolution = 0.0097659

    def reset(self):
        self.power_off()
        self.power_on()

    def tare(self):
        tare = 0
        for i in range(50):
            tare = tare + self.read()
        tare = tare / 50 
        self.offset = tare

    def raw_value(self):
        return self.read() - self.offset

    def measure_weight(self):
        self.weight = ((self.read() - self.offset) * self.resolution)/1000
        
    def measure_force(self, raw=True):
        self.force = ((self.read() - self.offset) * self.resolution)/1000*9.810

    def stable_value(self, reads=10, delay_us=500):
        values = []
        for _ in range(reads):
            values.append(self.raw_value())
            sleep_us(delay_us)
        return self._stabilizer(values)

    @staticmethod
    def _stabilizer(values, deviation=10):
        weights = []
        for prev in values:
            weights.append(sum([1 for current in values if abs(prev - current) / (prev / 100) <= deviation]))
        return sorted(zip(values, weights), key=lambda x: x[1]).pop()[0]

if __name__ == "__main__":
    scales = Scales(d_out=5, pd_sck=4)
    scales.tare()
    val = scales.measure_weight()
    print(val)
    #scales.power_off()