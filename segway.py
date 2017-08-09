class Segway:
    # Constructor - used to make a new Segway
    def __init__(self, w, c, s, p):
        self.wheels = w
        self.color = c
        self.speed = s
        self.charge = p
    # To String function - used when printing out a Segway
    def __str__(self):
        wheelInfo = "Wheels: " + str(self.wheels)
        colorInfo = "Color: " + self.color
        speedInfo = "Speed: " + str(self.speed)
        chargeInfo = "Charge: " + str(self.charge) + "%"
        # Important: return the string, don't print it
        return wheelInfo + " " + colorInfo + " " + speedInfo + " " + chargeInfo
    # A method that charges the segway by 5%
    def chargeItUp(self):
        self.charge = self.charge + 5
    # A method that changes the segway's color
    def changeTheColorTo(self, newColor):
        self.color = newColor

# Call the constructor to make an object
mikaylas_segway = Segway(2, "purple", 50, 75)

# Print an object
print(mikaylas_segway)

# Get a field of an object
print(mikaylas_segway.color)

# Update a field of an object
mikaylas_segway.color = "blue"

# Print out the object to see if it changed
print(mikaylas_segway)

# Call a method on the object
mikaylas_segway.changeTheColorTo("silver")

# Print it out again to see if it worked
print(mikaylas_segway)
