# Checking for a Leap Year , 2024 → Yes
# Leap day occurs in each year that is a multiple of 4,
# except for years evenly divisible by 100 but not by 400.
from xml.dom.minidom import CDATASection

year = int(input("enter the year\n"))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print(" leap year")
else:
    print ("not leap year")


