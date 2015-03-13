__author__ = 'Danijel'

import requests
import urllib.request
from bs4 import BeautifulSoup


# ------ Functions ------

#depending on development method of certain site, pictures can be stored in multiple ways

'''
This method connects image url with site url in order to get real image link
example:
for website -> http://www.awwwards.com/awards-of-the-month/
retrieved image url is -> /bundles/tvawwwards/images/pages/img-lovedays.png
as a result you get -> http://www.awwwards.com/awards-of-the-month//bundles/tvawwwards/images/pages/img-lovedays.png
'''
def getAllImageLinksMethod1(url):
    print('\n****** Trying to download image via method 1 ******')
    counter = 0
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('img'):
        imagelink = url + link.get('src')
        try:
            downloadWebImage(imagelink)
            print('Picture: ', imagelink, ' is successfully downloaded :)')
            counter +=1
        except:
            print('Error downloading', imagelink.split("/")[-1], '-.-')

    print('\nNumber of downloaded images: ', counter)

'''
Some pages already contain direct source to image

for website -> http://www.awwwards.com/awards-of-the-month/
retrieved image url is -> /bundles/tvawwwards/images/pages/img-lovedays.png
as a result you get -> /bundles/tvawwwards/images/pages/img-lovedays.png

This doesn't work of course, but in some cases result link is a real link
'''

def getAllImageLinksMethod2(url):
    print('\n****** Trying to download image via method 2 ******')
    counter = 0
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('img'):
        imagelink = link.get('src')
        try:
            downloadWebImage(imagelink)
            print('Picture: ', imagelink, ' is successfully downloaded :)')
            counter +=1
        except:
            print('Error downloading', imagelink.split("/")[-1], '-.-')

    print('\nNumber of downloaded images: ', counter)

'''
This method is for sites that store all images in subdirectories

for website -> http://www.awwwards.com/awards-of-the-month/
retrieved image url is -> /bundles/tvawwwards/images/pages/img-lovedays.png
we remove the part after .com
result url is -> http://www.awwwards.com/bundles/tvawwwards/images/pages/img-lovedays.png
'''
def getAllImageLinksMethod3(url):
    print('\n****** Trying to download image via method 3 ******')
    counter = 0
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('img'):
        imagelink = link.get('src')
        website = str(url)
        realImageLink = 'http://' + website.split("/")[2] + imagelink
        try:
            downloadWebImage(realImageLink)
            print('Picture: ', realImageLink, ' is successfully downloaded :)')
            counter +=1
        except:
            print('Error downloading', realImageLink.split("/")[-1], '-.-')

    print('\nNumber of downloaded images: ', counter)


'''
This method if for rare cases like polleosport.hr

Their website doesn't use www prefiks, so that part is removed and retrieved link looks like http://[pageURL]/+ link

'''
def getAllImageLinksMethod4(url):
    print('\n****** Trying to download image via method 4 ******')
    counter = 0
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    for link in soup.find_all('img'):
        imagelink = link.get('src')
        website = str(url)
        realImageLink = ""
        try:
            realImageLink = 'http://' + website.split("www.")[1] + '/' + imagelink
        except:
            print("Error retrieving image link")

        try:
            downloadWebImage(realImageLink)
            print('Picture: ', realImageLink, ' is successfully downloaded :)')
            counter +=1
        except:
            print('Error downloading', realImageLink.split("/")[-1], '-.-')

    print('\nNumber of downloaded images:: ', counter)


def downloadWebImage(url):
    filename = url.split("/")[-1]
    urllib.request.urlretrieve(url,filename)

# ------ End function ------


# ------ Main ------

print('This is a really simple image downloading program')
print('Enter website URL in the following format:')
print('http://www.pageURL.com|hr|org etc. \n')
print('or try example: https://stupid-studio.com \nor \nhttp://www.hyperquake.com/work/old-spice-gallery')

linkWebStraniceInput = str(input('Enter website url: '))

getAllImageLinksMethod1(linkWebStraniceInput)
getAllImageLinksMethod2(linkWebStraniceInput)
getAllImageLinksMethod3(linkWebStraniceInput)
getAllImageLinksMethod4(linkWebStraniceInput)