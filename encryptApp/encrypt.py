#Increases each letter in input by magnitude of shift, looping around alphabet as neccessary
def ceasar(input,shift):
    shift = abs(shift % 26)
    output = ""
    for c in input:
        newChar = ord(c)+shift
        if newChar > 122 or (newChar > 90 and ord(c) < 91):
            newChar-=26
        output+= chr(newChar)
    return output
