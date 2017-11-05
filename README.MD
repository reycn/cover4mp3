# WHAT'S THIS?
A project aimng at simplify embedding albumn cover for songs downloaded from XIAMI MUSIC or QQ MUSIC, which do not contain full ID3 informations.
  
# COVERS FROM?
For now, all the covers are searched, matched and downloaded from NETEASE MUSIC, coz the author is justing doing something related which provided  a kind of convenience.
  
# HOW TO USE(Tested on Ubuntu 17.04)?
-- `git clone` this repo  
-- Open a new terminal windows in the repo, install requirements using `pip install -Ur requirements.txt`  
-- Cpoy all your target songs(only mp3 supported) to the folder `songs`  
-- run `python3 run.py`  
SPEED UP: Configure your NETEASEMUSIC account at `LINE 17` in auth.py to avoid servers' anti-crawl strategies.  
  
# NOTICE
-- For now, songs are searched by <b>FILE NAME</b> (could be easily modified by pressing <b>F2</b>)  
-- ONLY support mp3  
-- ONLY fetch album covers from NETEASE MUSIC  
  
# TODO
Nope,really...
