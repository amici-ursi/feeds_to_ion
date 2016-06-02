import feedparser

#example texas feed: https://www.flickr.com/services/feeds/groups_pool.gne?id=47583010@N00&lang=en-us&format=atom

onefeed = feedparser.parse('https://www.flickr.com/services/feeds/groups_pool.gne?id=47583010@N00&lang=en-us&format=atom')

print("this feed's title is {}".format(onefeed.feed.title))
