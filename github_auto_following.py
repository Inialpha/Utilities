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
token = input("\nPease Enter your personal access token:\n")

# user names

users = ['Reliccode', 'Abstaina44', 'Kingvadee', 'koechMR', 'KingStaff', 'osadeleke', 'MahmoudEasa', 'oluwaschunne', 'Riyo3350G', 'aybzakaria5', 'Techkene', 'TonnyMpho', 'saadouchama', 'shazaaly', 'Temiloluwa22', 'sabbakar', 'wezer-pixel', 'johnechono', 'chukwucyprian', 'zee-ham-su', 'aycrown1', 'OgagaOnuta', 'Romaric250', 'horbital1140', 'Ahmedkel', 'Mado007', 'nuuxcode', 'mohamed-elghafiani', 'mahmoudsalah296', 'Liams-theCreator', 'Rita2024', 'niyioo', 'Aminuv', 'cartermusee', 'nazarKsn', 'Fuzzworth', 'HafsaMAR', 'Abdisalam-Abdulahi', 'AlolaSunday12', 'KevinStreetCoder', 'alijr2018', 'ELABDELLAOUI-HAJAR', 'Inialpha', 'Zak-devz', 'laila22haz', 'Rashnotech', 'omobolaji001']


for user in users:
    follow(user, token)

print(f"\n\nYou have successfully followed {len(users)}")
