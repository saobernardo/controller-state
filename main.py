import sys
import subprocess

joystick = sys.argv
joystick.pop(0)

if len(joystick) == 0:
  sys.exit('Jostick for monitoring not given')

try:
  if joystick[0] == 'dualsense' or joystick[0] == 'DualSense':
    print("Executando joystick dualsense")
    subprocess.run(["python", "dualsense.py"])

except KeyboardInterrupt:
  print('Fim de execução')