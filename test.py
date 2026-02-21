import time
from instagrapi import Client

# Configuration
USERNAME = "me"
PASSWORD = "your_password"  # Replace with actual password
TARGET_USER = "target_username"  # Replace with target username
FOLLOW_INTERVAL = 60  # Seconds between follow attempts

def login_to_instagram():
    cl = Client()
    try:
        cl.login(USERNAME, PASSWORD)
        print("Login successful!")
        return cl
    except Exception as e:
        print(f"Login failed: {e}")
        return None

def follow_user(cl, target_username):
    try:
        user_id = cl.search_users(target_username)[0]['pk']
        cl.follow(user_id)
        print(f"Followed {target_username}")
    except Exception as e:
        print(f"Error following {target_username}: {e}")

def main():
    cl = login_to_instagram()
    if not cl:
        return
    
    while True:
        follow_user(cl, TARGET_USER)
        time.sleep(FOLLOW_INTERVAL)

if __name__ == "__main__":
    main()