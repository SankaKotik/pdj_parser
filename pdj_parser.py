import requests
from bs4 import BeautifulSoup

url = input ('Ссылка на альбом: ') # Например: https://promodj.com/aeroritmix/groups/516503/Emotional_Impulse_50_Shades_Of_Vocal_Trance

with open ('links.txt', 'a') as outfile:
    next_page, page = True, 1
    
    while next_page:
        resp = requests.get (f'{url}?page={page}')
        soup = BeautifulSoup (resp.text, 'lxml')
        
        dl_buttons = soup.find_all ('a', class_="player_standard_tool player_standard_tool__downloads")
        print (f'С {page} страницы было записано {len (dl_buttons)} ссылок')
        
        for dl_button in dl_buttons:
            outfile.write (dl_button.get ('href') + '\n')
        
        next_page = soup.find ('a', id='next_page')
        page += 1
