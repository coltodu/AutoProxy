#https:://www.github.com/coltodu
#Give credit where credit is due.
#This is a simple script to make proxychains get proxies autmatically.
#It is planned to get autorun and a timer.
#E.x If proxie is down get another
#E.x After 1 week autorun


import bs4 as bs
import urllib2
url = "https://www.socks-proxy.net/"
req = urllib2.Request(url, headers={'User-Agent' : "Magic Browser"})
sauce = urllib2.urlopen(req).read()
number = raw_input("Please enter the number of proxies you  need: ")
done = 0
soup = bs.BeautifulSoup(sauce, 'lxml')
bob = soup.table
table_rows = bob.find_all('tr')
proxybase = "dynamic_chain\nproxy_dns\ntcp_read_time_out 15000\ntcp_connect_time_out 8000\n\n"
base = open('/etc/proxychains.conf', "w")
base.write(proxybase)
base.close()
for tr in table_rows:
	done = done + 1
	td = tr.find_all('td')
	fow = [i.text for i in td]		
	if len(fow) > 0:
		ip = fow[0]
		port = fow[1]
		proxytype = fow[4]
		proxyconf = open('/etc/proxychains.conf', "a")
		proxyconf.write(proxytype.lower() + "\t" + ip + " " + port + "\n")
		print ("Written: " + proxytype + "\t" + ip +" " + port)
	if done > int(number):
		break
		#Ok this took me a while if you change int(number) to number it will print as it pleases
		#It took me many minutes of yelling to find it out. Because it is a string.
		#If 0 > "4": instead of If 0 > 4:

