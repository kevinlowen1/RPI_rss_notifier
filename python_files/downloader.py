import feedparser
from datetime import datetime, timedelta

####calculate the new records from the rss feed
def rss_downloader(timeLastRun):
    ####save feed to variable
    piFeed = feedparser.parse("https://rpilocator.com/feed.rss")
    # print(piFeed)
    modifiedPiFeed = []

    print('---------------------------------------------')
    today = datetime.today()
    utcnow = datetime.utcnow() 
    print("current datetime:       ", today)
    print("current datetime (utc): ", utcnow)

    ####for loop through rss feed to get time and summary of info from website
    for i in range(len(piFeed.entries)):
        # print(piFeed.entries[i].published, ' : ', piFeed.entries[i].title)
        t1 = datetime.strptime(piFeed.entries[i].published, "%a, %d %b %Y %H:%M:%S %Z")
        n = [i,t1,piFeed.entries[i].title]
        # print(n)
        modifiedPiFeed.append(n)


    ################ make a list of only pi records that meet the criteria for my notification system ###################
    #
    # 
    #     
    ####modify created list to only those records more recent than the specified time
    modifiedPiFeed = [x for x in modifiedPiFeed if timeLastRun < x[1]]
    ####modify created list to only those records relevant to the USA
    modifiedPiFeed = [x for x in modifiedPiFeed if '(US)' in x[2]]
    ####modify created list to only those records relevant to the USA
    modifiedPiFeed = [x for x in modifiedPiFeed if 'Zero 2 W' in x[2]]


    print(modifiedPiFeed)
    return(modifiedPiFeed)
    # piFeedDecoded = json.loads(piFeed)
    # print(piFeedDecoded)

if __name__ == "__main__":
    ####create lastRunTime with date of 2 days ago
    lastRun = datetime.utcnow() - timedelta(hours = 2)
    # print(lastRun)

    rss_downloader(lastRun)