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

users = ['laila22haz', 'tay121222', 'TonnyMpho', 'Aminuv', 'Abdisalam-Abdulahi', 'Abdoul54', 'Mado007', 'Sackitey68', 'mohamed-elghafiani', 'Abstaina44', 'mahmoudsalah296', 'wezer-pixel', 'Sumshi', 'OgagaOnuta', 'saadouchama', 'Fuzzworth', 'Mariangithubit', 'nazarKsn', 'Zak-devz', 'Ochoja', 'johnechono', 'omobolaji001', 'Liams-theCreator', 'RObiayo', 'ELABDELLAOUI-HAJAR', 'samit1719', 'koechMR', 'KingStaff', 'devbojack', 'Riyo3350G', 'THEKINGSTAR', 'osadeleke', 'Ahmedkel', 'khadijamohamed99', 'success96', 'cartermusee', 'aybzakaria5', 'sabbakar', 'kiddoraj', 'SireME', 'niyioo', 'elyse502', 'MahmoudEasa', 'Fumbesi', 'Rita2024', 'aliceada96', 'mahmoud-elbanna', 'Jesufemi-A', 'victor-coder96', 'aycrown1', 'ggbaguidi', 'Adooz', 'KevinStreetCoder', 'AlolaSunday12', 'Reliccode', 'nuuxcode', 'Rashnotech', 'shazaaly', 'Kingvadee', 'Temiloluwa22', 'oluwaschunne', 'TemiladeRebecca', 'oumatoulacen', 'pasej5', 'KafuiAdaku', 'mohamed-Fathy1', 'Inialpha', 'HafsaMAR', '21Alul21', 'chukwucyprian', 'BibiObiora', 'Fabianphilip', 'ingenious464', 'Xaldovah', 'Oluwamarcellus', 'Romaric250', 'Techkene', 'alijr2018', 'zee-ham-su', 'horbital1140']


for user in users:
    follow(user, token)

print(f"\n\nYou have successfully followed {len(users)}")
