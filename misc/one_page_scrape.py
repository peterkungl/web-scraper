import pandas as pd
from ZConfig._compat import urllib2
from bs4 import BeautifulSoup



html = urllib2.urlopen("https://www.hasznaltauto.hu/szemelyauto/volkswagen/passat_cc/volkswagen_passat_cc_2_0_cr_tdi_business_dsg-13033481").read()
soup = BeautifulSoup(html,'html.parser')

table = soup.find('table', attrs={'class':'hirdetesadatok'})
rows = table.find_all('tr')
data = []

for row in rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append(cols)

df = pd.DataFrame(data)
df


