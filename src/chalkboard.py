'''
Created on Sep. 16, 2023
asks user for a sentence and a value. Then repeats that sentence that many times
@author: Sebastian
'''
phrase = input("What sentence should be repeated?: ") + " " #The space ensures proper separation
number_of_repetition = int(input("How many times should it be repeated?: ")) #this would normally take in input as a string so I had to convert it to an int

print(phrase * number_of_repetition) #repeats the phrase the amount of times