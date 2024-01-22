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

users = ['Liams-theCreator', 'SireME', 'shazaaly', 'Ahmedkel', 'success96', 'aliceada96', 'nazarKsn', 'saadouchama', 'RObiayo', 'oumatoulacen', 'THEKINGSTAR', 'aycrown1', 'johnechono', 'niyioo', 'Kingvadee', 'zee-ham-su', 'alijr2018', 'MahmoudEasa', 'Riyo3350G', 'Jesufemi-A', 'felixayot', 'KingStaff', 'Fumbesi', 'sabbakar', 'mohamed-elghafiani', 'Xaldovah', 'Fuzzworth', 'KevinStreetCoder', 'kiddoraj', 'Ingenious464', 'TonnyMpho', 'tay121222', 'Abdisalam-Abdulahi', 'laila22haz', 'chukwucyprian', 'Rita2024', 'mohamed-Fathy1', 'Sumshi', 'mahmoud-elbanna', 'Mariangithubit', 'HafsaMAR', 'saaid323', 'wezer-pixel', 'omobolaji001', 'samit1719', 'Romaric250', 'RealKingTino', 'cartermusee', 'nuuxcode', 'Ochoja', 'victor-coder96', 'Abstaina44', 'BibiObiora', 'khadijamohamed99', 'OgagaOnuta', 'Sackitey68', 'oluwaschunne', 'Oluwamarcellus', 'Mado007', 'Zak-devz', 'ggbaguidi', '21Alul21', 'AlolaSunday12', 'devbojack', 'Techkene', 'pasej5', 'Adooz', 'mahmoudsalah296', 'Rashnotech', 'Oussama-hamdi', 'Aminuv', 'koechMR', 'TemiladeRebecca', 'Abdoul54', 'Reliccode', 'horbital1140', 'ELABDELLAOUI-HAJAR', 'KafuiAdaku', 'elyse502', 'osadeleke', 'Temiloluwa22', 'Inialpha', 'ingenious464', 'aybzakaria5', 'Fabianphilip']

for user in users:
    follow(user, token)

print(f"\n\nYou have successfully followed {len(users)}")
