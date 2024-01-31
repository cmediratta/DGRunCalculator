#Tournamnt Simulator
from getData import getPlayers, dumpPlayers, getTournamentPlayers, getData
from calculate import calculateTournament
import operator
from tabulate import tabulate

def main():

  dict_status = input("Reset Dict (y/n): \n").rstrip()
  event_id = input("Input the pdga event_id: \n")
  division = input("Input the divison you want to simulate: \n").rstrip()
  rounds = int(input("Input the number of rounds: \n"))
  N = int(input("Input the number of iterations to run: \n"))

  winner_avg, players_chances = simulateTournament(dict_status, event_id, division, rounds, N)

  p_sorted = sorted(players_chances.items(), key=operator.itemgetter(1), reverse=True)

  header = ["Name", "Win Probability (%)"]
  print("On average, the winner shoots %.1f rated." % winner_avg)
  print(tabulate(p_sorted, headers=header, tablefmt="list"))

  return


def simulateTournament(dict_status, e_id, division, rounds, N):

  players = getPlayers(dict_status)

  pdga_nums = getTournamentPlayers(e_id, division, players)

  dumpPlayers(players)

  avg = calculateTournament(N, rounds, players, pdga_nums)

  player_names = {}
  for p in pdga_nums:
    player_names[players[p][2]] = pdga_nums[p]
  
  return avg, player_names


if __name__ == "__main__":
  main()