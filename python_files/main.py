from downloader import rss_downloader
from datetime import datetime, timedelta
from notifier import notify

if __name__ == "__main__":
   ####create timeToCheckAgainst with date of 2 days ago
   timeToCheckAgainst = datetime.utcnow() - timedelta(hours = 2)

   ####get records more recent than the time checked against
   info = rss_downloader(timeToCheckAgainst)

   ####send notification to phone via SMS
   notify(info)

   