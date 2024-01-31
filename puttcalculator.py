# Putt Running Calculator

from getData import getData, getPlayers, dumpPlayers
from calculate import calculateOdds

def main():

  dict_status = input("Reset Dict (y/n): ").rstrip()
  pdga = input("Enter your pdga number: \n")
  o_pdga = input("Enter your opponent's pdga number: \n")
  h_left = int(input("Enter the holes left: \n"))
  strokes = int(input("Enter the stroke difference: \n"))
  putt_pct = float(input("Enter percent of making putt: \n"))
  comebacker_pct = float(input("Probability of making the comebacker: \n"))

  run, layup = puttCalculator(dict_status, pdga, o_pdga, h_left, strokes, putt_pct, comebacker_pct)

  print("The odds that you win if you run this putt are %.2f%%." % run)
  print("The odds that you win if you layup this putt are %.2f%%." % layup)
  if(run > layup):
    print("This model says you should run this putt with an expected win percentage %.2f%% greater." % (run - layup))
  else:
    print("This model says you should layup this putt with an expected win percentage %.2f%% greater." % (layup - run))
  
  return


def puttCalculator(dict_status, pdga, o_pdga, h_left, strokes, putt_pct, comebacker_pct):

  players = getPlayers(dict_status)

  getData(pdga, players)
  getData(o_pdga, players)

  p = players[pdga]
  o = players[o_pdga]

  dumpPlayers(players)

  p_adj = (p[0]/9, p[1]/9)
  o_adj = (o[0]/9, o[1]/9)

  return calculateOdds(p_adj, o_adj, h_left, strokes, putt_pct, comebacker_pct)
  

if __name__ == "__main__":
  main()






