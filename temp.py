import sys
if len(sys.argv) == 2:
    temp = float(sys.argv[1])
    print("User provided temperature:")
else:
    temp = 25
    print("No input given - using default temperature:")

if temp < 15:
    status = "Cold"
elif temp <= 30:
    status = "Normal"
else:
    status = "Hot"

print("Temperature Status:", status)
