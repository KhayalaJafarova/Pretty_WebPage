from bs4 import BeautifulSoup
from urllib.request import urlopen

#URL of web page
url = 'http://oxu.az/'
#get content of url as response
response = urlopen(url)
#read response
data = str(response.read())
soup = BeautifulSoup(data)

#create a file for writing on it
with open("index1.txt", "w") as fp:
	fp.write(soup.prettify())
#print(fp)
fp.close()

#print(soup.prettify())