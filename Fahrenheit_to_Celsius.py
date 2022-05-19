def FahToCel(f):
    return (f-32)/1.8

#print("Enter Temperature in Fahrenheit: ", end="")
fah = float(input())

cel = FahToCel(fah)
print("{:.2f}".format(cel))