# PromoDJ.com album parser

run `python3 parser.py` and paste a link to album (not artist home page or all albums page). Parser will automatically collect all links to `links.txt` from all pages (usually 20 tracks on every page). 

after links collecting you can download full album using your download manager: `wget -i links.txt` for single-thread downloading or `aria2c -i links.txt -j 20` for multi-thread downloading (recommended)
