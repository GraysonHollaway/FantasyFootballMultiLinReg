from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

#maybe put a loop here for more years
year = 2021 
url = "https://www.pro-football-reference.com/years/{}/fantasy.htm".format(year)
html = urlopen(url)
soup = BeautifulSoup(html, features="html.parser")

headers = [th.getText() for th in soup.findAll("tr")[1].findAll("th")]
headers = headers[1:]
print(len(headers))

rows = soup.findAll("tr", class_= lambda table_rows: table_rows != "thread")
player_stats = [[td.getText() for td in rows[i].findAll('td')] for i in range(len(rows))] 
player_stats  = player_stats[2:]

print(player_stats[:5])

stats = pd.DataFrame(player_stats, columns=headers)

stats.to_csv("2021playerstats.csv")