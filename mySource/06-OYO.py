# Create a class for a smaller distance conversion
class Length:
    def __init__(self, inches):
        self._inches = inches

    @property
    def inches(self):
        return self._inches
    
    @inches.setter
    def inches(self, value):
        self._inches = value

    @property
    def cm(self):
         return self._inches * 2.54
    
    @cm.setter
    def cm(self, value):
        self._inches = value / 2.54

length1 = Length(12)
print(f"12 inches is {length1.cm} centimeters.")

length1.cm = 30
print(f"30 centimeters is {length1.inches} inches.")