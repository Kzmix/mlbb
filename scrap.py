import requests
from bs4 import BeautifulSoup
import csv
import re

# URL halaman web
url = 'https://mobile-legends.fandom.com/wiki/Category:Heroes'

# Mengambil konten halaman web
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Mencari semua tag <a> dengan class 'category-page__member-link'
hero_links = soup.find_all('a', class_='category-page__member-link')

# Menyimpan nama-nama hero ke dalam list
heroes = [link.text.strip() for link in hero_links]

# Fungsi untuk membersihkan nama hero
def clean_hero_name(name):
    # Menghapus karakter yang tidak diinginkan dengan regex
    return re.sub(r'[^\w\s]', '', name).replace(' ', '_').lower()

# Menyimpan nama-nama hero ke dalam file CSV
for hero in heroes:
    # Membersihkan nama hero
    cleaned_hero_name = clean_hero_name(hero)
    # Nama file
    file_name = f"{cleaned_hero_name}.csv"
    # Membuka file CSV untuk ditulis
    with open(file_name, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # Menulis nama hero ke dalam file CSV
        writer.writerow([hero])

    print(f"File {file_name} telah dibuat.")

print("Proses selesai.")
