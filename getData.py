import requests
from lxml import etree
from io import StringIO
import pickle
import random
import time

def getStd(rtgs):

  mean = sum(rtgs) / len(rtgs) 
  variance = sum([((x - mean) ** 2) for x in rtgs]) / len(rtgs) 
  res = variance ** 0.5
  return res


def getRatings(root):

  tourneys = root[1][2][1][0][0][0][0][2][0][0][0][0][0][-1][1][-1][0][1]

  rtgs = []

  for child in tourneys:
    if (child[7].text=="Yes"):
      rtgs.append(int(child[6].text))

  return rtgs


def getTournamentPlayers(e_id, division, players):

  parser = etree.HTMLParser()

  r = requests.get('https://www.pdga.com/tour/event/' + e_id)

  html = r.content.decode("utf-8")

  tree = etree.parse(StringIO(html), parser=parser)
  root = tree.getroot()

  r = root[1][2][1][0][0][0][0][2][0][0][0][0][0][8][0][2]
  for i in range(len(r)):
    if (r[i].attrib=={'open': ''}):
      if (r[i][0][0].attrib['id'] == division):
        r = r[i]
        break


  pdga_nums = {}
  for i in range(1,len(r)-1):
    pdga_nums[r[i][0].text.split('#')[1]] = 0

  for p in pdga_nums:
    getData(p, players)

  return pdga_nums


def getData(p, players):

  if (p in players):
    return players[p]

  time.sleep(3*random.random())

  parser = etree.HTMLParser()

  r = requests.get('https://www.pdga.com/player/' + p + '/details')
  html = r.content.decode("utf-8")

  tree = etree.parse(StringIO(html), parser=parser)
  root = tree.getroot()

  print("Grabbing " + root[1][2][1][0][0][0][0][1].text)
  name = root[1][2][1][0][0][0][0][1].text.split('#')[0][:-1]

  r = root[1][2][1][0][0][0][0][2][0][0][0][0][0]
  for c in r:
    if (c.attrib == {'class': 'panel-pane pane-player-player-info'}):
      r = c[1][0]
  for c in r:
    if c.attrib == {'class': 'current-rating'}:
      r = c
      break

  rtg = int(r[0].tail)
  rtgs = getRatings(root)

  std = getStd(rtgs)

  players[p] = (rtg, std, name)

  return


def getPlayers(dict_status):
  if (dict_status=='y'):
    players = {}

  else:
    try:
      with open('players.pickle', 'rb') as handle:
        players = pickle.load(handle)
    except:
      players = {}

  return players


def dumpPlayers(players):
  with open('players.pickle', 'wb') as handle:
    pickle.dump(players, handle, protocol=pickle.HIGHEST_PROTOCOL)