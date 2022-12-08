import requests
from os.path import exists
from os import makedirs

def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()

def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"

SESSION_ID_FILE = "session.cookies"
SESSION = get_session_id(SESSION_ID_FILE)
COOKIES = {"session": SESSION}

def get_input(year,day):
    path = f'inputs/{year}'
    file = path + f'/day{day:02d}'

    if not exists(path):
        makedirs(path)

    if not exists(file):
        url = get_url(year, day)
        response = requests.get(url, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(file, "w") as f:
            f.write(response.text[:-1])
    
    with open(file, "r") as f:
        return f.read()