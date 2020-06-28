import praw
from words import Words

BOT_USERNAME      = 'BOT_USERNAME'
BOT_PASSWORD      = 'BOT_PASSWORD'
BOT_CLIENT_ID     = 'BOT_CLIENT_ID'
BOT_CLIENT_SECRET = 'BOT_CLIENT_SECRET'
BOT_USER_AGENT    = 'BOT_USER_AGENT'

STREAM_SUBREDDIT  = 'all'
TARGET_SUBREDDIT  = 'test

class Bot:

    reddit = praw.Reddit(username=BOT_USERNAME,
                         password=BOT_PASSWORD,
                         client_id=BOT_CLIENT_ID,
                         client_secret=BOT_CLIENT_SECRET,
                         user_agent=BOT_USER_AGENT)

    def run(self):
        english_words = Words.load_dictionary()

        print('Successfully loaded {} English words.'.format(len(english_words)))

        for submission in self.reddit.subreddit(STREAM_SUBREDDIT).stream.submissions(skip_existing=True):
            if submission.id in english_words:
                print('Submission with ID "{}" found!'.format(submission.id))

                crosspost_title = '{}: {}'.format(submission.id, submission.title)
                submission.crosspost(TARGET_SUBREDDIT, title=crosspost_title)

if __name__ == '__main__':
    while True:
        try:
            bot = Bot()
            bot.run()
        except Exception as e:
            print(e)
