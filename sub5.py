import sys

if len(sys.argv) == 6:
    m1 = sys.argv[1]
    m2 = sys.argv[2]
    m3 = sys.argv[3]
    m4 = sys.argv[4]
    m5 = sys.argv[5]
    print("User provided input values:")
else:
    m1 = 0
    m2 = 0
    m3 = 0
    m4 = 0
    m5 = 0
    print("No input given, using default values:")

print("Marks:", m1, m2, m3, m4, m5)

total = int(m1) + int(m2) + int(m3) + int(m4) + int(m5)
average = total / 5

print("Total Marks:", total)
print("Average Marks:", average)

# ----- Grade Logic -----
if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)