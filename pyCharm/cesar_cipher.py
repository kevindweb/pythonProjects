import requests
from bs4 import BeautifulSoup
my_url = "https://www.hackthissite.org/missions/prog/11/index.php"
r = requests.get(my_url)
soup = BeautifulSoup(r.text)

for thing in soup.select(".siteheader"):
    print thing
line = re.split(r"[^a-zA-Z0-9\s]", line)
line = line[0: len(line) - 1]
#for thing in range(0, len(line)):
#    line[thing] = chr(int(line[thing]) + amount)
#print "".join(line)