import smbus
import time

# Get I2C bus
bus = smbus.SMBus(1)

# How many measurements ?
temp = input("Enter how many times you want to display the measurements: ")
nbrOfIteration = int(temp)

# How much time between each measurements ?
temp = input("Enter the sleep time between each measurements (in seconds): ")
sleepTime = int(temp)

# Open a file to save the data
saveData = open("data.txt", "a")
saveData.write("------\n" + time.strftime("%d/%m/%y %H:%M") + "\n")

counter = 0
while (counter != nbrOfIteration):
    counter += 1
    
    # Reading Coefficents for compensation 
    # Sensor address: 0x60, Read: 0x04, 8 bytes
    data = bus.read_i2c_block_data(0x60, 0x04, 8)

    # Convert the data to floating points
    A0 = (data[0] * 256 + data[1]) / 8.0
    B1 = (data[2] * 256 + data[3])
    if B1 > 32767 :
            B1 -= 65536
    B1 = B1 / 8192.0
    B2 = (data[4] * 256 + data[5])
    if B2 > 32767 :
            B2 -= 65535
    B2 = B2 / 16384.0
    C12 = ((data[6] * 256 + data[7]) / 4) / 4194304.0

    # Sensor address: 0x60, Start conversion: 0x12, Send: 0x00 
    bus.write_byte_data(0x60, 0x12, 0x00)

    time.sleep(0.5)

    # Sensor address: 0x60, Read: 0x00, 4 bytes
    data = bus.read_i2c_block_data(0x60, 0x00, 4)

    # Convert the data to 10-bits
    pres = ((data[0] * 256) + (data[1] & 0xC0)) / 64
    temp = ((data[2] * 256) + (data[3] & 0xC0)) / 64

    # Calculate pressure compensation
    presComp = A0 + (B1 + C12 * temp) * pres + B2 * temp

    # Convert the data
    pressure = (65.0 / 1023.0) * presComp + 50
    cTemp = (temp - 498) / (-5.35) + 25

    # Output data to screen
    print ("Pressure : %.2f kPa" %pressure)
    print ("Temperature : %.2f C \n" %cTemp)


    # Save data into a file
    saveData.write("[%d]\n" %counter)
    saveData.write("Pressure : %.2f kPa\n" %pressure)
    saveData.write("Temperature : %.2f C\n\n" %cTemp)
  
    # Wait between each measurements
    if (counter != nbrOfIteration):
        time.sleep(sleepTime)

# Close the file for the saved data
saveData.close()

# To not close the window 
raw_input("Enter a letter to close the window...")
