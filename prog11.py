Chemistry = int(input("Enter marks in Chemistry: "))
Physics = int(input("Enter marks in Physics: "))
Maths = int(input("Enter marks in Maths: "))
English = int(input("Enter marks in English: "))
Computer = int(input("Enter marks in Computer: "))
Total = Chemistry + Physics + Maths + English + Computer
percentage = Total/5
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >=40:
    print("Grade E")
else: print("Grade F")
