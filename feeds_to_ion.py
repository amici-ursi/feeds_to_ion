import feedparser

#example texas feed: https://www.flickr.com/services/feeds/groups_pool.gne?id=47583010@N00&lang=en-us&format=atom
#another: https://www.flickr.com/services/feeds/groups_pool.gne?id=1403197@N21&lang=en-us&format=atom

feeds = ["https://www.flickr.com/services/feeds/groups_pool.gne?id=47583010@N00&lang=en-us&format=atom", "https://www.flickr.com/services/feeds/groups_pool.gne?id=1403197@N21&lang=en-us&format=atom"]

for feed in feeds:
    thisfeed = feedparser.parse(feed)
    print("this feed's title is {}".format(thisfeed.feed.title))
    for i in range(len(thisfeed.entries)):
        print("this item is {}".format(thisfeed.entries[i].title))
    
    
