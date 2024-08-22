def calculatetemp_1(temp):
    return ((9 / 2 * temp)+ 32)
def calculatetemp_2(temp):
    return  ((f - 32) * 5/9)
while True:
 temp = float(input("enter the  temp in celsius:"))
 f = float(input("enter the temp in fahrenheit:"))
 Choise= int(input("enter the choise:"))
 if Choise == 1:
  print("The conversion  celsius to fahrenheit is :  ", calculatetemp_1(temp))
 elif Choise ==2:
   print("The conversion  fahrenheit to celsius  is :  ", calculatetemp_2(f))
 next_calculation = input("Let's do next calculation? (yes/no): ")
 if next_calculation.lower() != 'yes':
        break
