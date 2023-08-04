import requests
import threading
import random
import string
import time
from colorama import Fore, Style
import os

def fire(text):
    os.system(""); fade = ""
    green = 250
    for line in text.splitlines():
        fade += (f"\033[38;2;255;{green};0m{line}\033[0m\n")
        if not green == 0:
            green -= 25
            if green < 0:
                green = 0
    return fade

# Function to check username availability
def check_instagram_username(username):
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)

    if response.status_code == 404:
        print(f"{Fore.GREEN}The username '{username}' is available on Instagram!{Style.RESET_ALL}")
        return username
    else:
        print(f"{Fore.RED}The username '{username}' is not available on Instagram.{Style.RESET_ALL}")

# Function to generate a list of random usernames
def generate_random_usernames(num_usernames, username_length):
    characters = string.ascii_lowercase + string.digits + "._"
    usernames = []
    for _ in range(num_usernames):
        username = ''.join(random.choice(characters) for _ in range(username_length))
        usernames.append(username)
    return usernames

# Function to process a batch of usernames
def process_usernames(usernames, available_usernames):
    for username in usernames:
        available_username = check_instagram_username(username)
        if available_username:
            available_usernames.append(available_username)
        # Introduce a delay to avoid overloading the server (adjust as needed)
        time.sleep(sleep_duration)

# Main function
if __name__ == "__main__":
    print(fire(f"""
                             
                    ██╗███╗░░██╗░██████╗████████╗░█████╗░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
                    ██║████╗░██║██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
                    ██║██╔██╗██║╚█████╗░░░░██║░░░███████║██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
                    ██║██║╚████║░╚═══██╗░░░██║░░░██╔══██║██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
                    ██║██║░╚███║██████╔╝░░░██║░░░██║░░██║╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
                    ╚═╝╚═╝░░╚══╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
                                             https://discord.com/invite/sYZ96zzUnW
                                                       Made by 3ntr
"""))
    # Number of random usernames to generate and check
    num_usernames_to_check = int(input("How Many username do u want: "))

    # Length of random usernames (letters, numbers, and special characters combined)
    username_length = int(input("How Many letters&numbers do u want: "))

    # Number of sleep cycles between API requests
    sleep_cycles = int(input("Enter the number of sleep cycles between requests (recomneded 10-20sec): "))
    sleep_duration = float(input("Enter the sleep duration (in seconds) for each cycle (recomneded 3-5sec): "))

    # Number of threads to use for parallel processing (adjust based on your system)
    num_threads = 5

    # Generate random usernames to check
    random_usernames = generate_random_usernames(num_usernames_to_check, username_length)

    # Split usernames into chunks for parallel processing
    chunks = [random_usernames[i:i + num_threads] for i in range(0, len(random_usernames), num_threads)]

    # List to store available usernames
    available_usernames = []

    # Start threads for each chunk
    threads = []
    for chunk in chunks:
        thread = threading.Thread(target=process_usernames, args=(chunk, available_usernames))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Save available usernames to a new file
    with open("available_usernames.txt", "w") as file:
        for username in available_usernames:
            file.write(username + "\n")

    print("Username checking is complete.")
    input("Press Enter to exit...")
