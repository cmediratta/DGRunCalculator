from statistics import NormalDist
import math
import time

c = 1.5

def calculateOdds (p, o, h, s, p_pct, c_pct):

  w_make = getWinOdds (p, o, h-1, s+1)
  w_miss_comebacker = getWinOdds (p, o, h-1, s-1)
  w_miss_three = getWinOdds (p, o, h-1, s-2)

  w_layup = getWinOdds (p, o, h-1, s)

  w_run = w_make * p_pct
  w_run += w_layup * (1-p_pct) * c_pct
  w_run += w_miss_comebacker * (1-p_pct) * (1-c_pct) * c_pct
  w_run += w_miss_three * (1-p_pct) * (1-c_pct)**2

  return round(100*w_run,2), round(100*w_layup,2)

  
def getWinOdds (p, o, h, s):

  if (h==0):
    if (s==0):
      return (o[1] + p[1] - c) / 18 + c
    return s > 0

  m = (p[0] - o[0]) * h / 18
  sigma_s = (o[1] + p[1] - c) * h / 18 + c

  return 1 - NormalDist(mu=m, sigma=sigma_s).cdf(-m/math.sqrt(sigma_s)-s)


def calculateRoundWinner (rounds, pdga_nums, dists):

  current_best = 0
  current_winner = ""
  for p in pdga_nums:
    s = sum(dists[p].samples(rounds))/rounds
    if (current_best < s):
      current_best = s
      current_winner = p
  return current_winner, current_best
    


def calculateTournament (N, rounds, players, pdga_nums):

  dists = {}
  for p in pdga_nums:
    dists[p] = NormalDist(mu=players[p][0], sigma=players[p][1])

  rtg_sum = 0
  for n in range(N):

    p, rtg = calculateRoundWinner(rounds, pdga_nums, dists)

    pdga_nums[p]+=100/N
    rtg_sum+=rtg/N

  return rtg_sum






