from time import sleep
import os

from scraper import SteamSpecialsScraper
from sms_notifications import SMSNotifications


def main():
    notifications = SMSNotifications(
        os.getenv("ACCOUNT_SID"), os.getenv("AUTH_TOKEN"), os.getenv("FROM_NUMBER")
    )
    steam_scraper = SteamSpecialsScraper("https://store.steampowered.com/specials")
    
    # Load initial data to steam_scraper.ids
    list(steam_scraper.parse_html())
    while True:
        new_items = list(steam_scraper.parse_html())
        for item in new_items:
            text = f'{item.name} is now {item.price} | was: {item.org_price}'
            notifications.send(text, os.getenv("TO_NUMBER"))
        sleep(3600)

if __name__ == "__main__":
    main()
