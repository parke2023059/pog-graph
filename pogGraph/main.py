import time
import matplotlib.pyplot as plt
import os
import random




x = [0]
y = [0]


def clock():
    seconds = 0
    minutes = 0
    hours = 0
    day = 0
    days = 0
    pogs = random.random()
    
    while True:
        seconds = seconds + 1
        time.sleep(1)
        
        if seconds == 5:
            seconds = 0
            
            print(x)
            minutes = minutes + 1
            
            if minutes == 5:
                minutes = 0
                hours = hours + 1
                
                if hours == 1:
                    hours = 0
                    day = day + 1
                    days = days + 1
                    x.extend([days])
        os.system('cls')
        print(day, hours, minutes, seconds)
        print(x)





def graph():
    #pogs = 0
    usrInput = int(input("1 = add, 2 = subtract"))
    if usrInput == 1:
        input = int(input("Add: "))
        #newPog = pogs + input
    elif usrInput == 2:
        input = int(input("Subtract: "))
        #newPog = pogs - input
        
    plt.plot(x,y)
    plt.show()
graph()