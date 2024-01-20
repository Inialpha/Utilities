#!/usr/bin/python3
""" This  script automate the process of following github accounts """
import requests


def follow(user_name, token):
    """
    makes a request to te github api endpoint
    user_name: str -> the user name to be followed
    token: str -> your personal access token
    """
    # construct the url
    url = f"https://api.github.com/user/following/{user_name}"
    # construct the headers
    headers = {"Authorization": f"Bearer {token}",
               "Accept": "application/vnd.github+json"}

    # make request
    response = requests.put(url, headers=headers)
    if response.status_code == 204:
        print(f"Successfully followed {user_name}")
    elif response.status_code == 404:
        print(f"User {user_name} not found. Please check the username.")
    elif response.status_code == 401:
        print(f"Bad credentials Please make sure you are using a valid token")
        exit()
    else:
        print(f"Failed to follow {user_name}")


# input token
token = input("Pease Enter your personal access token:\n")

# user names

users = ['mahmoudsalah296', 'Romaric250', 'nuuxcode', 'zee-ham-su', 'HafsaMAR',
         'osadeleke', 'ELABDELLAOUI-HAJAR', 'aybzakaria5', 'shazaaly', 'MahmoudEasa',
         'saadouchama', 'laila22haz', 'OgagaOnuta', 'Liams-theCreator',
         'Abdisalam-Abdulahi', 'Mado007', 'Rashnotech', 'Abstaina44',
         'Fuzzworth', 'Inialpha', 'Techkene', 'KingStaff', 'sabbakar',
         'Ahmedkel', 'oluwaschunne', 'horbital1140','alijr2018', 'Reliccode',
         'Rita2024', 'koechMR', 'Oussama-hamdi', 'codeabuu', 'lawrence1986',
         'Temiloluwa22', 'cartermusee']
for user in users:
    follow(user, token)
