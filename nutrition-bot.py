import praw
import pdb
import re
import os

# Create the Reddit instance & login
print("Logging in...")
reddit = praw.Reddit(client_id='TfPyWHY2wocniA',
                     client_secret='Aeiln32MWKQ_3svl85FEyTUX5Jg',
                     password='N@lg3n3!4227',
                     user_agent='nutritionBot.v0.1',
                     username='nutritionbot')

print("Logged in!")

# Create a new list
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# Or load the list of posts we've already replied to
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = list(filter(None, posts_replied_to))
        
# Pull the hottest 10 entries from a subreddit of your choosing
subreddit = reddit.subreddit('pythonforengineers')
for submission in subreddit.hot(limit=10):
    print(submission.title)

    # Make sure you didn't already reply to this post
    if submission.id not in posts_replied_to:

        # Not case-sensitive
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply
            submission.reply("I like this post!")
            print("Bot replying to : ", submission.title)

            # Store id in list
            posts_replied_to.append(submission.id)


# Write updated list to txt file
with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
