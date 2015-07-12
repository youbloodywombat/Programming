import urllib2
from bs4 import BeautifulSoup

# http://www.realestate.com.au/sold/property-apartment-with-studio-in-kensington%2c+nsw+2033/list-1?maxBeds=any&includeSurrounding=false&source=refinements
# http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-with-studio-in-maroubra%2c+nsw+2035/list-1?maxBeds=any&includeSurrounding=false&misc=ex-no-sale-price&activeSort=list-date&source=refinements



# where='melbourne'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-in-melbourne%2c+vic+3000%3b+/list-'
# urlPartTwo='?newOrEstablished=established&activeSort=list-date&source=location-search'

# where='rhodes'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-in-rhodes/list-'
# urlPartTwo='?newOrEstablished=established&activeSort=list-date&source=location-search'

# where='pendleHills'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-in-pendle+hill/list-'
# urlPartTwo='?newOrEstablished=established&activeSort=list-date&source=location-search'

# where='castleHill'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-in-castle+hill%2c+nsw+2154%3b+/list-'
# urlPartTwo='?newOrEstablished=established&activeSort=list-date&source=location-search'

# where='sydney'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-in-sydney,+nsw+2000/list-'
# urlPartTwo='?activeSort=list-date&newOrEstablished=established'

# where='surryHills'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-with-studio-in-surry+hills%2c+nsw+2010/list-'
# urlPartTwo='?maxBeds=any&includeSurrounding=false&misc=ex-no-sale-price&activeSort=list-date&source=refinements'

# where='maroubra'
# urlPartOne='http://www.realestate.com.au/sold/property-unit-apartment-unit+apartment-with-studio-in-maroubra%2c+nsw+2035/list-'
# urlPartTwo='?maxBeds=any&includeSurrounding=false&misc=ex-no-sale-price&activeSort=list-date&source=refinements'

# where='kensington'
# urlPartOne='http://www.realestate.com.au/sold/property-apartment-with-studio-in-kensington%2c+nsw+2033/list-'
# urlPartTwo='?maxBeds=any&includeSurrounding=false&source=refinements'

# where='laneCove'
# urlPartOne='http://www.realestate.com.au/sold/property-apartment-in-lane+cove%2c+nsw+2066/list-'
# urlPartTwo='?source=location-search'

# where='laneCoveNorth'
# urlPartOne='http://www.realestate.com.au/sold/property-apartment-in-lane+cove+north%2c+nsw+2066%3b+/list-'
# urlPartTwo='?source=location-search'

print("Starting Price\n")
text_file = open(where+"Price.txt", "w")
# obs=1
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for price in soup.find_all('p',"price"):
# 		obs_text = str(obs)
		print "x=%s" %y
		text_file.write(price.get_text()+"\n")
		# print(price.get_text())
		# print("#"+obs_text+" "+price.get_text())
# 		obs=obs+1
text_file.close()

print("Starting soldDate\n")
text_file = open(where+"soldDate.txt", "w")
# obs=1
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for soldDate in soup.find_all('p','soldDate'):
# 		obs_text = str(obs)
		print "x=%s" %y
		soldText = soldDate.get_text()
		text_file.write(soldText[9:]+"\n")
		# print(soldDate.get_text())
# 		print("#"+obs_text+" "+soldDate.get_text())
# 		obs=obs+1
text_file.close()

print("Starting location\n")
text_file = open(where+"location.txt", "w")
# obs=1	
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for location in soup.find_all('a','name'):
# 		obs_text = str(obs)
		print("x=%s" %y)
		text_file.write(location.get_text()+"\n")
		# print(location.get_text())
# 		print("#"+obs_text+" "+location.get_text())
# 		obs=obs+1
text_file.close()

print("Starting Bedrooms\n")
text_file = open(where+"bedroom.txt", "w")
# obs=1	
for x in range(0,75):
	y=str(x)
	soup = BeautifulSoup(urllib2.urlopen(urlPartOne+y+urlPartTwo).read())
	for bedroom in soup.find_all('img',alt="Bedrooms"):
# 		obs_text = str(obs)
		print"x=%s" %y
		text_file.write(bedroom.next_sibling.get_text()+"\n")
		# print(bedroom.next_sibling.get_text())
# 		print("#"+obs_text+" "+bedroom.next_sibling.get_text())
# 		obs=obs+1
text_file.close()

from itertools import izip

g=open(where+'ALL.txt','w')

with open(where+"Price.txt",'r') as price, open(where+"soldDate.txt",'r') as soldDate, open(where+"location.txt",'r') as location, open(where+"bedroom.txt",'r') as bedroom: 
    for x, y, z, t in izip(price,soldDate,location,bedroom):
        price = x.strip()
        soldDate = y.strip()
        location = z.strip()
        bedroom = t.strip()
        print >> g, "{0}\t{1}\t{2}\t{3}".format(price,soldDate,location,bedroom)
