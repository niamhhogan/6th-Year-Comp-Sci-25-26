import serial

ser=serial.Serial() #shortens serial function to ser
ser.baudrate=115200 #needed to get correct signal from microbit

ser.port='COM4' #found in command prompt - chgport or device manager

print("Type Ctrl + C to safety exit")
ser.open() #opens serial port

try:
    while True:
        data=str(ser.readline())
        
        #clean the data
        data=data[2:16].replace(" ", "")
        print(data)
        
except KeyboardInterrupt:
    print("Safely closing serial connection")
    ser.close()
    
    
