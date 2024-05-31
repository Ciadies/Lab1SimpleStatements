'''
Created on Sep. 16, 2023
Asks for temperature in Celsius then returns it as a Fahrenheit value
@author: Sebastian
'''
celsius = int(input("What is the temperature in Canada?: "))
fahrenheit = str(int((celsius * 9 / 5) + 32)) #I used str(int()) to remove the decimal place before converting to str for the final response

print(str(celsius) +" degrees in Canada would be " + fahrenheit + " degrees in Springfield. D'oh!")