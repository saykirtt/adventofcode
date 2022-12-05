import requests
from os.path import exists

def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()

def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"

SESSION_ID_FILE = "session.cookies"
SESSION = get_session_id(SESSION_ID_FILE)
COOKIES = {"session": SESSION}

def get_input(year,day):
    path = f'inputs/{year}/day{day:02d}'

    if not exists(path):
        url = get_url(year, day)
        response = requests.get(url, cookies=COOKIES)
        if not response.ok:
            raise RuntimeError(
                f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
            )
        with open(path, "w") as f:
            f.write(response.text[:-1])
    
    with open(path, "r") as f:
        return f.read()