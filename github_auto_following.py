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

users = ['mahmoudsalah296', 'victor-coder96', 'Temiloluwa22', 'TonnyMpho', 'Rashnotech', 'Riyo3350G', 'tay121222', 'saadouchama', 'Fumbesi', 'Romaric250', 'samit1719', 'aybzakaria5', 'oumatoulacen', 'alijr2018', 'mohamed-elghafiani', 'Reliccode', 'SireME', 'AlolaSunday12', 'horbital1140', 'Abstaina44', 'Inialpha', 'mohamed-Fathy1', 'elyse502', 'Liams-theCreator', 'Rita2024', 'chukwucyprian', 'Mado007', 'Techkene', 'nuuxcode', 'johnechono', 'Jesufemi-A', 'Abdisalam-Abdulahi', 'Ochoja', 'khadijamohamed99', 'BibiObiora', 'Adooz', 'shazaaly', 'KingStaff', 'Aminuv', 'nazarKsn', 'Fabianphilip', 'devbojack', 'KafuiAdaku', 'ggbaguidi', 'THEKINGSTAR', 'aliceada96', 'Mariangithubit', 'success96', 'cartermusee', 'Sumshi', 'wezer-pixel', 'KevinStreetCoder', 'oluwaschunne', 'niyioo', 'aycrown1', 'omobolaji001', 'Xaldovah', 'osadeleke', 'MahmoudEasa', 'koechMR', 'pasej5', 'RObiayo', 'HafsaMAR', 'Sackitey68', 'Kingvadee', 'Fuzzworth', 'TemiladeRebecca', 'ELABDELLAOUI-HAJAR', 'Zak-devz', 'sabbakar', 'nazarKsn', 'OgagaOnuta', 'Ahmedkel', 'Oluwamarcellus', 'laila22haz', 'kiddoraj', 'Abdoul54', 'mahmoud-elbanna', 'ingenious464', 'zee-ham-su']


for user in users:
    follow(user, token)

print(f"\n\nYou have successfully followed {len(users)}")
