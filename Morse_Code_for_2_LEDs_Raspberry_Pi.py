#welcome to this project for Raspberry Pi.
#code bellow will le you connect LEDs to your Raspberry Pi.
#we assume at this stage, the INPUT will be letters and space only.
#No numbers or special characters.

import RPi.GPIO as GPIO
import time

#here are the 2 LEDs allocations for the Raspberry board:
blue,red = 22,23   

#in here are all the necessary setups:
GPIO.setmode(GPIO.BCM),GPIO.setwarnings(False)
GPIO.setup(blue, GPIO.OUT), GPIO.setup(red, GPIO.OUT)



#turning the red LED on for 0.5 seconds
def redLED():
    GPIO.output(red, GPIO.HIGH) 
    time.sleep(0.5)
    GPIO.output(red, GPIO.LOW)   
    time.sleep(0.30)   

#turning the blue LED on for 0.15 seconds
def blueLED():
    GPIO.output(blue, GPIO.HIGH) 
    time.sleep(0.15)
    GPIO.output(blue, GPIO.LOW)   
    time.sleep(0.30) 
    
#listing of the letters
morse = {'a': ('b', 'r'), 'b' : ('r', 'b', 'b', 'b'), 'c': ('r','b','r','b'),
         'd':('r','b','b'), 'e': ('b'), 'f': ('b', 'b','r','b'), 'g':('r','r','b'),
         'h':('b','b','b','b'), 'i':('b','b'), 'j': ('b', 'r','r','r'), 'k': ('r','b','r'),
         'l': ('b','r','b','b'), 'm': ('r','r'), 'n': ('r','b'), 'o':('r','r','r'),
         'p':('b','r','r','b'), 'r':('b','r','b'), 's': ('b','b','b'), 't': ('b'),
         'u': ('b','b','r'), 'v':('b','b','b','r'), 'w': ('b','r','r'), 'x': ('r','b','b','r'),
         'y': ('r','b','r','r'), 'z': ('r','r','b','b'),  }

#here is a sos signal to play with:
a = 'SOS sos'
b = 'sugAr'


#and here is the function doing all the magic:
def convertToMorse(stringie):
    stringie = stringie.lower()#<converts upper case to lower:
    
    for i in stringie:
        if i == ' ':    # < looks out for a space
            time.sleep(1.5)
        else:
            for x in morse[i]:    # < decoding process itself
                if x == 'b':
                    blueLED()
                else:
                    redLED()
            
        
        
        
                
#and here we test the code:                
convertToMorse(a)
convertToMorse(b)


#hope you like the project. Have a lovely day.

