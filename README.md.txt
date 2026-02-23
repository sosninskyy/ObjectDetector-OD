#Slipper detector v1.0 & SD
#Credits: Movement detection logic is based on OpenCV tutorials, adapted and integrated with hardware by me.

#That project was born by hours of work, and end at 5 am
#It's a movement detector system , dont work on too tiny objects
#only on something like SLIPPER or similiar by size:)

#How it worrrk?
1. **Python + openCV** #Look at video from ip camera, detection motion contours
2. **Serial Bridge** #Lib in python that sends signals to the COM port arduino when something detected
3. **Arduino** #And arduion finnaly, controll 3 red leds , they light on when movement detected

# Hardware
* Arduino Uno (or any compatible)
* 3 red LEDs + 3 Resistors 330 ohm or something what dont burn out led
* Smartphone as an IP Camera and some app like Ip webcam

#Author
Young developer, just exploring the world of CV and Robotics.