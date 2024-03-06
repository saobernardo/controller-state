from time import sleep
from dualsense_controller import DualSenseController

device_info = DualSenseController.enumerate_devices()
if len(device_info) < 1:
  raise Exception('No DualSense Controller available')

is_running = True

controller = DualSenseController()

def stop():
  global is_running
  is_running = False

def on_error(error):
  print(f'An error occured: {error}')
  stop()

def on_battery_lower_than(battery_level):
  print(f'Battery at {battery_level}. Please, recharge')

controller.activate()

try:
  while is_running:
    controller.battery.on_lower_than(20, on_battery_lower_than)
    sleep(0.001)
except KeyboardInterrupt:
  controller.deactivate()
  print('parou')