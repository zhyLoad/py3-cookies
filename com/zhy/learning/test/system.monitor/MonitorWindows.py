import psutil


class Windows_CPU(object):

  def times(self):
      return psutil.cpu_times()

  def percent(self):
      return psutil.cpu_percent(interval=1)

#注意：psutil的sensors不支持Windows系统 https://psutil.readthedocs.io/en/latest/#sensors
class Sensors_Util(object):
  def temperatures(self):
      return psutil.sensors_temperatures()
  def fans(self):
      return psutil.sensors_fans()


def test_windows_cpu():
    windows_cpu = Windows_CPU()
    print(windows_cpu.times())
    print(windows_cpu.percent())

def test_sensors():
    sensors_util = Sensors_Util()
    print(sensors_util.temperatures())
    print(sensors_util.fans())









if __name__ == '__main__':
  #test_sensors()
  test_windows_cpu()