import requests
from bs4 import BeautifulSoup
import os

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
save_path = "./movie_list.txt"

# print(soup.prettify())
movies_listing = soup.find_all(name="h3", class_="title")

movies_list = [movie.get_text() for movie in movies_listing]
# for movie in movies_listing:
#     print(movie.get_text())

# check if a file exists before writing. If it does, delete it.
if os.path.exists(save_path):
    os.remove(save_path)

# create new text file to house the movie listing.
# https://www.tutorialspoint.com/backward-iteration-in-python
with open(save_path, 'w') as file:
    for item in movies_list[::-1]:
        if movies_list.index(item) != 0:
            file.write(f"{item}\n")
        else:
            file.write(f"{item}")
