This is a set of programs to determine different relevant disc golf stats.

To run putt calculator:
python3 puttcalculator.py < puttinput.txt 

puttinput.txt format:

  +------------------------------+
  |<y for reset dict, n for not> |
  |<Your PDGA #>                 |
  |<Your Opponent's PDGA #>      |
  |<# of Holes Left>             |
  |<Net Strokes Up>              |
  |<% Chance Putt is Made>       |
  |<% Chance Comebacker is Made> |
  +------------------------------+

This will output the percent chance you win if you run the putt or if you lay up.

TBD: 
OB/Rollaway Chance
Multiple Opponents


To run tournament simulator:
python3 tournamentsimulator.py < tournamentinput.txt

tournamentinput.txt format:

  +------------------------------+
  |<y for reset dict, n for not> |
  |<The PDGA event_id>           |
  |<The PDGA Division>           |
  |<# of Rounds in Event>        |
  |<Total # of Samples>          |
  +------------------------------+

This will output the total percent chance players will win the given tournamnet.

