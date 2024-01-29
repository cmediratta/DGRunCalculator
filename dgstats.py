# Putt Running Calculator

from getData import getData
from calculate import calculateOdds

pdga = input("Enter your pdga number: \n")
o_pdga = input("Enter your opponent's pdga number: \n")
h_left = int(input("Enter the holes left: \n"))
strokes = int(input("Enter the stroke difference: \n"))
putt_pct = float(input("Enter percent of making putt: \n"))
comebacker_pct = float(input("Probability of making the comebacker: \n"))

p = getData(pdga)
o = getData(o_pdga)

p_adj = (p[0]/9, p[1]/9)
o_adj = (o[0]/9, o[1]/9)

run, layup = calculateOdds(p_adj, o_adj, h_left, strokes, putt_pct, comebacker_pct)
print("The odds that you win if you run this putt are %.2f%%." % run)
print("The odds that you win if you layup this putt are %.2f%%." % layup)
if(run > layup):
  print("This model says you should run this putt with an expected win percentage %.2f%% greater." % (run - layup))
else:
  print("This model says you should layup this putt with an expected win percentage %.2f%% greater." % (layup - run))







