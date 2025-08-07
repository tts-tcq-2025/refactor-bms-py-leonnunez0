
from time import sleep
import sys


def display_message(msg):
  print(msg)
  for i in range(6):
    print('\r*', end='')
    sys.stdout.flush()
    sleep(1)
    print('\r *', end='')
    sys.stdout.flush()
    sleep(1)

def is_within_range(value, min, max):
  return min < value < max

class Vitals:
  temp_min = 95
  temp_max = 102
  pulse_min = 60
  pulse_max = 100
  spo2_min = 90
  spo2_max = 100
  def check_temperature(self, val):
    if not is_within_range(val,self.temp_min, self.temp_max):
      display_message("Temperature is out of range")
      return False
    return True
  def check_pulse(self, pulse):
    if not is_within_range(pulse, self.pulse_min, self.pulse_max):
      display_message("Pulse is out of range")
      return False
    return True
  def check_spo2(self, spo2):
    if not is_within_range(spo2, self.pulse_min, self.pulse_max):
      display_message("SPO2 is out of range")
      return False
    return True

def vitals_ok(temperature, pulseRate, spo2):
  c = Vitals()
  if not c.check_temperature(temperature):
    return False
  if not c.check_pulse(pulseRate):
    return False
  if not c.check_spo2(spo2):
    return False
  return True
