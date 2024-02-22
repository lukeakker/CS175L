#CS175

#Lucas Vandenakker

#Temperature Conversions

def main():
    controlLoop()

def convertToKelvin(temp):
    kelvin = (temp - 32) * 5/9 + 273.15
    return kelvin
    

def convertToCentigrade(temp1):
    centigrade = (temp1 - 32) * 5/9
    return centigrade


def doConversion():
    f = getFahrenheit()
    k = convertToKelvin(f)
    c = convertToCentigrade(f)
    print('Fahrenheit:', f, '°F')
    print('Kelvin:', k, 'K') 
    print('Centigrade:', c, '°C')
    

def repeat():
    repeats = int(input('How many conversions would you like to do this time?'))
    for x in range(repeats):
        doConversion()
    

def controlLoop():
    control = str(input('Do you want to do some conversions(Yes or No)?'))
    if((control == 'yes')or (control == 'Yes')):
        repeat()
    

def getFahrenheit():
    Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130):'))
    while((Fahrenheit < -50) or (Fahrenheit > 130)):
       print('Please re-enter')
       Fahrenheit = float(input('Enter Fahrenheit temperature (must be -50 to 130):'))
    return Fahrenheit
    

# Call the main function.
if __name__ == '__main__':
    main()
