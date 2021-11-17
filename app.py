import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def Action_Adventure():
    resp = requests.get('https://www.amazon.in/gp/bestsellers/books/1318158031/ref=zg_bs_nav_b_1_b')
    soup = BeautifulSoup(resp.content, 'html.parser')
    list = soup.find("ol", {"id": "zg-ordered-list"})
    print('Loading...')
    autors = []
    autors_list = list.find_all('a',{'class':'a-size-small a-link-child'})
    for autor in autors_list:
        autors.append(autor.text)

    badges = []
    badges_list = list.find_all('span',{'class':'zg-badge-text'})
    for badge in badges_list:
        badges.append(badge.text)
    
    prices = []
    prices_list = list.find_all('span',{'class':'p13n-sc-price'})
    for price in prices_list:
        prices.append(price.text)
    
    editions = []
    editions_list = list.find_all('span',{'class':'a-size-small a-color-secondary'})
    for edition in editions_list:
        editions.append(edition.text)

    stars = []
    stars_list = list.find_all('span',{'class':'a-icon-alt'})
    for star in stars_list:
        stars.append(star.text)
    
    return [autors,badges,prices,editions,stars,]

def Arts_Film_Photography():
    resp = requests.get('https://www.amazon.in/gp/bestsellers/books/1318052031/ref=zg_bs_nav_b_2_1318158031')
    soup = BeautifulSoup(resp.content, 'html.parser')
    list = soup.find("ol", {"id": "zg-ordered-list"})
    print('Loading...')
    autors = []
    autors_list = list.find_all('a',{'class':'a-size-small a-link-child'})
    for autor in autors_list:
        autors.append(autor.text)
    
    badges = []
    badges_list = list.find_all('span',{'class':'zg-badge-text'})
    for badge in badges_list:
        badges.append(badge.text)
    
    prices = []
    prices_list = list.find_all('span',{'class':'p13n-sc-price'})
    for price in prices_list:
        prices.append(price.text)

    editions = []
    editions_list = list.find_all('span',{'class':'a-size-small a-color-secondary'})
    for edition in editions_list:
        editions.append(edition.text)

    stars = []
    stars_list = list.find_all('span',{'class':'a-icon-alt'})
    for star in stars_list:
        stars.append(star.text)

    return [autors,badges,prices,editions,stars]
 
def Biographies_Diaries_Accounts():
    resp = requests.get('https://www.amazon.in/gp/bestsellers/books/1318064031/ref=zg_bs_nav_b_2_1318158031')
    soup = BeautifulSoup(resp.content, 'html.parser')
    list = soup.find("ol", {"id": "zg-ordered-list"})
    print('Loading...')
    autors = []
    autors_list = list.find_all('a',{'class':'a-size-small a-link-child'})
    for autor in autors_list:
        autors.append(autor.text)

    badges = []
    badges_list = list.find_all('span',{'class':'zg-badge-text'})
    for badge in badges_list:
        badges.append(badge.text)
    
    prices = []
    prices_list = list.find_all('span',{'class':'p13n-sc-price'})
    for price in prices_list:
        prices.append(price.text)

    editions = []
    editions_list = list.find_all('span',{'class':'a-size-small a-color-secondary'})
    for edition in editions_list:
        editions.append(edition.text)

    stars = []
    stars_list = list.find_all('span',{'class':'a-icon-alt'})
    for star in stars_list:
        stars.append(star.text)
    return [autors,badges,prices,editions,stars]

def Business_Economics():
    resp = requests.get('https://www.amazon.in/gp/bestsellers/books/1318068031/ref=zg_bs_nav_b_2_1318158031')
    soup = BeautifulSoup(resp.content, 'html.parser')
    list = soup.find("ol", {"id": "zg-ordered-list"})
    print('Loading...')
    autors = []
    autors_list = list.find_all('a',{'class':'a-size-small a-link-child'})
    for autor in autors_list:
        autors.append(autor.text)

    badges = []
    badges_list = list.find_all('span',{'class':'zg-badge-text'})
    for badge in badges_list:
        badges.append(badge.text)
    
    prices = []
    prices_list = list.find_all('span',{'class':'p13n-sc-price'})
    for price in prices_list:
        prices.append(price.text)

    editions = []
    editions_list = list.find_all('span',{'class':'a-size-small a-color-secondary'})
    for edition in editions_list:
        editions.append(edition.text)

    stars = []
    stars_list = list.find_all('span',{'class':'a-icon-alt'})
    for star in stars_list:
        stars.append(star.text)

    return [autors,badges,prices,editions,stars]

def Children_YoungAdult():
    resp = requests.get('https://www.amazon.in/gp/bestsellers/books/1318073031/ref=zg_bs_nav_b_2_1318158031')
    soup = BeautifulSoup(resp.content, 'html.parser')
    list = soup.find("ol", {"id": "zg-ordered-list"})
    print('Loading...')
    autors = []
    autors_list = list.find_all('a',{'class':'a-size-small a-link-child'})
    for autor in autors_list:
        autors.append(autor.text)

    badges = []
    badges_list = list.find_all('span',{'class':'zg-badge-text'})
    for badge in badges_list:
        badges.append(badge.text)
    
    prices = []
    prices_list = list.find_all('span',{'class':'p13n-sc-price'})
    for price in prices_list:
        prices.append(price.text)

    editions = []
    editions_list = list.find_all('span',{'class':'a-size-small a-color-secondary'})
    for edition in editions_list:
        editions.append(edition.text)

    stars = []
    stars_list = list.find_all('span',{'class':'a-icon-alt'})
    for star in stars_list:
        stars.append(star.text)

    return [autors,badges,prices,editions,stars]

