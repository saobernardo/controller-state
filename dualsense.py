from time import sleep
from dualsense_controller import DualSenseController
from plyer.utils import platform
from plyer import notification

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
  #print(f'Battery at {battery_level}. Please, recharge')
  notification.notify(
    title = "Low Battery: DualSense",
    message = "Battery is below 10%. Please, recharge",
    app_name = "Controller State"
  )

def on_battery_charging(battery_level):
  print(f'Battery Charging, currently at {battery_level}')

controller.activate()

try:
  while is_running:
    controller.battery.on_charging(on_battery_charging)
    controller.battery.on_lower_than(10, on_battery_lower_than)
    sleep(0.001)
except KeyboardInterrupt:
  controller.deactivate()
  print('parou')