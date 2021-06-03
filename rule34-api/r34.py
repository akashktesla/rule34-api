from bs4 import BeautifulSoup
import requests
import validators

def rule34_image(tag,n):
    base_url = 'https://rule34.xxx/index.php?page=post&s=list&tags='
    base_view_url = 'https://rule34.xxx/index.php?page=post&s=view&id='
    url = base_url+tag
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'lxml')

    valzkai = soup.find_all('span',class_='thumb')
    a=valzkai[n].a['id']
    a=a.replace('p','')
    view_url=base_view_url + str(a)
    view_page = requests.get(view_url)
    view_soup = BeautifulSoup(view_page.content,'lxml')
    aki=view_soup.find('div',id='content')
    attribute_array=aki.find('div',class_='link-list').find_all('a')
    flag_image_src=1
    while flag_image_src==1:
      for a in attribute_array:
        valid=validators. url(a['href'])
        if valid:
          image_src_link=a['href']
          flag_image_src=0
    return image_src_link
 def rule34_number(tag):
    base_url = 'https://rule34.xxx/index.php?page=post&s=list&tags='
    url = base_url+tag
    page = requests.get(url)
    soup = BeautifulSoup(page.content,'lxml')

    valzkai = soup.find_all('span',class_='thumb')
    return len(valzkai)
