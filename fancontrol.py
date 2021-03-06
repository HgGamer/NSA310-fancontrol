import time
path = "/sys/class/i2c-dev/i2c-0/device/0-002e/"

def enable():
    file = open(path+"pwm1_enable","w") 
    file.write("1")
    file.close() 


def setPwm(pwm):
    if(pwm>255):
        pwm = 255
    if(pwm<0):
        pwm = 0
    file = open(path+"pwm1","w") 
    file.write(str(pwm))
    file.close() 

def getTemp():
    def readTemp(temp_type):
        file = open(path+"temp"+str(temp_type)+"_input","r") 
        temp = file.read()
        file.close() 
        return temp
    temps = []
    temps.append(readTemp(1))
    temps.append(readTemp(2))
    temps.append(readTemp(3))
    temps.sort()
    return temps[-1]


enable()
while True:
    temp = int(getTemp())
    if(temp<=42000):
        setPwm(0)
    elif(temp>54000):
        setPwm(255)
    else:
        setPwm(int((temp - 43000)/100+145))
    time.sleep(0.1)


