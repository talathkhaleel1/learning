# Accidentally I got the wrong URL for a funny subreddit. It's probably "odds" and not "bots"
# Also, the URL is missing a crucial component, find out what it is and insert it too!

current_url = "https//www.reddit.com/r/nevertellmethebots"

to_add_missing_component = current_url.find("//")
changed_url = current_url[:to_add_missing_component] + ":" + current_url[to_add_missing_component:]
final_url = changed_url.replace("bots", "odds")
print(final_url)