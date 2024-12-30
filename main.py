#main file for Schrodingers Gift code
#selects Central or Peripheral based on pin being pulled down
from machine import Pin
from machine import PWM
from machine import ADC
# from servo import Servo
import time

pin_enable_client = Pin(1, Pin.IN, Pin.PULL_UP)
pin_enable_server = Pin(2, Pin.IN, Pin.PULL_UP)

if(pin_enable_client.value() == 0):
	import ble_simple_central
	print("activating client mode")
	ble_simple_central.run()
elif(pin_enable_server.value() == 0):
	import ble_simple_peripheral
	print("activating server mode")
	ble_simple_peripheral.run()

#use this as a test bed for servo positions and light sensor values
print("triggered neither client or server mode, entering test mode")

# pin_roof_switch = Pin(22, Pin.IN, Pin.PULL_UP)
# pin_light_sensor = ADC(Pin(28, Pin.IN))
# pin_card_servo_enable = Pin(12, Pin.OUT, Pin.PULL_DOWN)

# servoStop= 1500000
# servoForward = 900000
# servoReverse = 2100000

# pin_card_servo = PWM(Pin(14), freq=50)
# pin_card_servo.freq(50)
# pin_card_servo_enable.value(0)
# pin_card_servo.duty_ns(servoReverse)
# pin_card_servo_enable.value(1)
# time.sleep_ms(2000)
# pin_card_servo.duty_ns(servoStop)
# time.sleep_ms(1000)
# pin_card_servo.deinit()
# time.sleep_ms(4000)
# while(pin_light_sensor.read_u16()<20000):
# 	print("waiting for light sensor")

# pin_glitter_servo = PWM(Pin(15), freq=50)
# pin_glitter_servo.freq(50)
# pin_glitter_servo.duty_u16(1802)#1802
# time.sleep_ms(2000)
# pin_card_servo_enable.value(0)
# pin_glitter_servo.deinit()

while(True):
	print("loop")
