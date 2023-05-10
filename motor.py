import RPi.GPIO as GPIO
import time

MIN_ROTATION = 0
MAX_ROTATION = 68000
class StepperMotor():

    def __init__(self):
        #read in servo location
        try:
            with open("servo_location.txt", 'r') as fp:
                self.servo_location = int(fp.read().strip())
        except:
            pass
        if self.servo_location is None:
            self.servo_location = 0
        self.in1 = 17
        self.in2 = 18
        self.in3 = 27
        self.in4 = 22

        # careful lowering this, at some point you run into the mechanical limitation of how quick your motor can move
        self.step_sleep = 0.002

        # self.step_count = 4096 # 5.625*(1/64) per step, 4096 steps is 360°
        self.step_count = 100

        self.direction = False # True for clockwise, False for counter-clockwise

        # defining stepper motor sequence (found in documentation http://www.4tronix.co.uk/arduino/Stepper-Motors.php)
        self.step_sequence = [[1,0,0,1],
                        [1,0,0,0],
                        [1,1,0,0],
                        [0,1,0,0],
                        [0,1,1,0],
                        [0,0,1,0],
                        [0,0,1,1],
                        [0,0,0,1]]
        
        # setting up
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.in1, GPIO.OUT)
        GPIO.setup(self.in2, GPIO.OUT)
        GPIO.setup(self.in3, GPIO.OUT)
        GPIO.setup(self.in4, GPIO.OUT)

        # initializing
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)

    def write_location(self):
        # write out servo location
        with open("servo_location.txt", 'w') as fp:
            fp.write(str(self.servo_location))
    
    def cleanup(self):
        GPIO.output(self.in1, GPIO.LOW)
        GPIO.output(self.in2, GPIO.LOW)
        GPIO.output(self.in3, GPIO.LOW)
        GPIO.output(self.in4, GPIO.LOW)
        GPIO.cleanup()
        self.write_location()



    def DriveMotors(self, rotation=1, direction='down'):
        if direction == 'down':
            motor_pins = [self.in1, self.in2, self.in3, self.in4]
        elif direction == 'up':
            motor_pins = [self.in4, self.in3, self.in2, self.in1]
        else:
            return
        
        motor_step_counter = 0

        try:
            i = 0
            for i in range(int(self.step_count*rotation)):
                if direction == 'down' and self.servo_location < MAX_ROTATION:
                    self.servo_location += 1
                elif direction == 'up' and self.servo_location > MIN_ROTATION:
                    self.servo_location -= 1
                else:
                    return -1
                for pin in range(0, len(motor_pins)):
                    GPIO.output( motor_pins[pin], self.step_sequence[motor_step_counter][pin] )
                
                if self.direction==True:
                    motor_step_counter = (motor_step_counter - 1) % 8
                elif self.direction==False:
                    motor_step_counter = (motor_step_counter + 1) % 8
                else: # defensive programming
                    print("uh oh... direction should *always* be either True or False")
                    self.cleanup()
                    exit(1)
                time.sleep(self.step_sleep)
                if not i % 20:
                    self.write_location()
            self.write_location()
            print(self.servo_location)
        except KeyboardInterrupt:
            self.cleanup()
            exit(1)
