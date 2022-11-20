# League of Legends Ranked Name Exploit

![Ranked Que](name_exploit.png)

## What is this?
Simple python function that uses LCU endpoints to return a list of player names from your queue even if they are hidden like in ranked.

## Undetected?
Yes

## For users

1. Install python3
1. Create a python3 venv (for windows)
1. Download as zip and extract files into the same directory
1. Open a terminal to the directory (Right click > Open terminal ) 
1. Install the requirements: `pip install -r requirements.txt` (only have to run once)
1. Run `python3 name_exploit.py`  during champion select every time you want to get player names
1. Profit

### Output is multi search ready for op.gg / u.gg ...

#### NOTE:
Names are unordered since the endpoint returns an unordered byte encoded json string array mess, meaning that the order of the names form the script are not aligned with the actual player names in the lobby.

## For devs
idk ... u know what u r doing anyways ... 
