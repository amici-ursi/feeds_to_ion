import feedparser
import praw

r = praw.Reddit(user_agent="rss to reddit by /u/amici_ursi")
r.login('username', 'password', disable_warning=True)

feeds = ["https://www.flickr.com/services/feeds/groups_pool.gne?id=47583010@N00&lang=en-us&format=atom", "https://www.flickr.com/services/feeds/groups_pool.gne?id=1403197@N21&lang=en-us&format=atom"]

def main():
    for feed in feeds:
        thisfeed = feedparser.parse(feed)
        print("this feed's title is {}".format(thisfeed.feed.title))
        for i in range(len(thisfeed.entries)):
            print("posting {}".format(thisfeed.entries[i].title))
            try:
                r.submit('imagesoftesting', title=thisfeed.entries[i].title, url=thisfeed.entries[i].link, captcha=None, send_replies=True, resubmit=False)
            except praw.errors.AlreadySubmitted as e:
                print("Already submitted. Skipping.\n")
            except praw.errors.APIException as e:
                print(e)
                print("API error. Skipping.")

main()
