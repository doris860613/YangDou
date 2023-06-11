"""
File: webcrawler.py
Name: Doris
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10900879
Female Number: 7946050
---------------------------
2000s
Male Number: 12977993
Female Number: 9209211
---------------------------
1990s
Male Number: 14146310
Female Number: 10644506
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = f'https://www.ssa.gov/oact/babynames/decades/names{year}.html'
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        tags = soup.find_all('tbody')
        for tag in tags:
            male_total = 0  # Calculate the sum of male' numbers
            female_total = 0  # Calculate the sum of female' numbers
            rank_index = 0  # Represents the index of each ranking
            number = tag.text.split()
            # The regular pattern of [rank, male's name, male's number, female's name, female's number]
            for i in range(200):
                male_number = number[rank_index+2].split(',')
                female_number = number[rank_index+4].split(',')
                male_total += int(''.join(male_number))
                female_total += int(''.join(female_number))
                rank_index += 5  # Update the index of the rank
            print(f'Male Number: {male_total}')
            print(f'Female Number: {female_total}')
        # ----- Write your code below this line ----- #


if __name__ == '__main__':
    main()
