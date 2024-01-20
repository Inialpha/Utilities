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

users = ['Riyo3350G', 'cartermusee', 'mohamed-elghafiani', 'sabbakar', 'Liams-theCreator', 'Mado007', 'Adooz', 'chukwucyprian', 'alijr2018', 'zee-ham-su', 'Ahmedkel', 'HafsaMAR', 'Temiloluwa22', 'OgagaOnuta', 'TonnyMpho', 'oluwaschunne', 'KingStaff', 'Abdisalam-Abdulahi', 'niyioo', 'Zak-devz', 'nuuxcode', 'Fuzzworth', 'Inialpha', 'MahmoudEasa', 'KafuiAdaku', 'wezer-pixel', 'Romaric250', 'SireME', 'tay121222', 'elyse502', 'horbital1140', 'KevinStreetCoder', 'osadeleke', 'laila22haz', 'johnechono', 'aycrown1', 'ELABDELLAOUI-HAJAR', 'Aminuv', 'samit1719', 'omobolaji001', 'ggbaguidi', 'saadouchama', 'AlolaSunday12', 'aybzakaria5', 'Rita2024', 'Techkene', 'koechMR', 'TemiladeRebecca', 'koechMR', 'Abstaina44', 'nazarKsn', 'mohamed-Fathy1', 'Rashnotech', 'mahmoudsalah296', 'Reliccode', 'shazaaly', 'Kingvadee', 'BibiObiora', 'Xaldovah']

for user in users:
    follow(user, token)

print(f"\n\nYou have successfully followed {len(users)}")
