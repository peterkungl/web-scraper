import pandas as pd
from ZConfig._compat import urllib2
from bs4 import BeautifulSoup
import time


# get and show the pandas
def getAndShow(urlString):

    html = urllib2.urlopen(urlString).read()
    soupIn = BeautifulSoup(html,'html.parser')

    table = soupIn.find('table', attrs={'class':'hirdetesadatok'})
    rowsIn = table.find_all('tr')
    data = []

    for rowIn in rowsIn:
        cols = rowIn.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        data.append(cols)

    df = pd.DataFrame(data)
    print(df)


mainHtml = urllib2.urlopen('https://www.hasznaltauto.hu/talalatilista/PDNG2VCZR2RTAEF5RNHRAQWSRPZTTUSI7WJSXIGKKAIMOS2FWZAR3IW4PXFEA53DHJPZJXVL4XKWEQEWUW6AOWLMUXIBBMJFV7QIRPJYGBLEQEIGWRUG5UCFDKQZ2FDAOLDSHY3PKKOKQVYRMOOIAFG3MNCAHPVSZKS5RDIUMLG4BZ4S3FFYDHNPWK4OGMZCQUOWOOLHBCBQGE5LBN4NXDLZUQUMN35LCQWXQ4H7CQMBLHRYNRJYGYGIHXQ3RZQJHWNDGRT2IKT4VSWXVQUPIUFTAZYTRSKNY3IF7OCEXDAKZFN3NRMD56362T2DHJIZLN2LWBF7HLSVMPEGZ3CJBKVT5ZRDHSTYLPF7QE346O6RGC26IOS6UWPZJP5L4M2MGUNDHY7T6DMTXKTLC4XGQVWLYKPLXB7YMSG56TFWI2LKUVN2QUWBCS3O7CEGFVDWTUU2HMSUVS26GAYEO6BTNLYAY3AJL6GYIDXOKXKNSMPXPI3EGHM5WZDPE65UY5RZ3G5WJ3ZGPMXQ4DZWJKPCFOQWPXTX75MZOP44C4QGLYY6TCVPZDBKVJ6OMDAN6FHXYQZTM2AH2JET5O66Y7Y2ON3GEHBLZLGN5RGCCDE2B5IS74IXFFKKART5F3AYEUJUVCRSOS5BQKJYCLBI2UYB3H4WKNFZQD25DNSWDZI22FPJHHVMYL4GBUHXNLIOI3X5SLRTSYNYV3CPPZHIJSPNULAL56HXHIF3MGUBV4RNDCNSS6U57YIPY4T72DD6GP3JJBYSK/page1')
soup = BeautifulSoup(mainHtml,'html.parser')

sth = soup.find('div', attrs={'id':'w24'})
hirdetesek = sth.find_all('h3')

for i in range(5):
    for hird in hirdetesek:
        inside = hird.find('a')
        urlRef = inside['href']
        getAndShow(urlRef)
        time.sleep(1)

        # get new page
        nextPageLi = soup.find('li', attrs={'class':'visible-lg-inline-block visible-xs-inline-block visible-sm-inline-block visible-md-inline-block'})
        inA = nextPageLi.find('a')
        mainHtml = urllib2.urlopen(inA['href'])
        soup = BeautifulSoup(mainHtml,'html.parser')

        sth = soup.find('div', attrs={'id':'w24'})
        hirdetesek = sth.find_all('h3')

