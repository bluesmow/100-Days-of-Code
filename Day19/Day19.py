print("Loan Calculator")
print()
print("$1000 over 10 years at 5% APR")
print()
loan = 1000
percen =0.05
for i in range(10):
  loan +=(percen*loan)
  print("Year", i+1, "is",round(loan,2))
interest  = loan -1000
print("The interest is",round(interest,2))
