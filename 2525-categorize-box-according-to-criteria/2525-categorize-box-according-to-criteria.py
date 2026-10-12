class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        vol = length * width * height

        if (length >= pow(10,4) or width >= pow(10,4) or height >= pow(10,4) or vol >= pow(10,9)) and mass >= 100:
            return "Both"

        elif not (length >= pow(10,4) or width >= pow(10,4) or height >= pow(10,4) or vol >= pow(10,9)) and not (mass >= 100):
            return "Neither"

        elif (length >= pow(10,4) or width >= pow(10,4) or height >= pow(10,4) or vol >= pow(10,9)):
            return "Bulky"

        else:
            return "Heavy"