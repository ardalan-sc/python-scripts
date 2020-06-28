#Web Scraping By MR.Ant ^_^

import requests,re,time,csv,sys
from bs4 import BeautifulSoup


print("the link should be like\n(http://www.kurdcinama.com/episodes2.aspx?type=211&Stype=394&name=01)")
url = input("Series Link >> ")
#the number of videos in series
try:
    video_number = int(input('Type Videos Number >> '))
except Exception:
    print('Wrong Number (try again)')
    sys.exit()
#matching the url with original url
if re.match(r"\w+://www.kurdcinama.com/episodes\w+.aspx.type=\d+&Stype=\d+&name=\d+",url):
    print('please wait...')
    print('------------------')
    c1 = url.split('?')[1]
    c2 = c1.split('&')
    c2.pop(2)
#getting (Type and Stype) of url
    l = []
    for i in c2:
        c3 = re.search(r"\d+",i)
        l.append(c3.group())
else:
    print('wrong URL (try again)')
    sys.exit()


main_url = f"https://www.kurdcinama.com/episodes2.aspx?type={l[0]}&Stype={l[1]}&name="
num = '0'
#creating csv file
csv_file = open('znjira.csv','w')
c_writer = csv.writer(csv_file)
c_writer.writerow(['Video Number','Video Link'])
#scraping
for x in range(1,video_number+1):
    if x <10:
        r = requests.get(main_url+(num+str(x))).text
    else:
        r = requests.get(main_url+str(x)).text

    soup = BeautifulSoup(r,'html.parser')

    f = soup.find('div',class_='embed-container')
    try:
        g = f.find('iframe')['src']
        print(g)
    except Exception:
        print("Non")
    alqa = 'video'+': '+str(x)
    print(alqa)
    time.sleep(5)
    c_writer.writerow([alqa,g])

csv_file.close()



