# Reddit ID Checker

A bot that checks whether a post ID is an English word, and crossposts it with the word in the title if so.

# Installation

The bot depends on the `english-words` submodule. You should therefore clone it recursively to make sure that module is up-to-date:

```
git clone --recursive https://github.com/pawptart/Reddit-ID-Checker.git
```

Then, you can install required dependencies:

```
pip install -r requirements.txt
```

Next you'll need to set the config in `bot.py`:

```python
BOT_USERNAME      = 'BOT_USERNAME'
BOT_PASSWORD      = 'BOT_PASSWORD'
BOT_CLIENT_ID     = 'BOT_CLIENT_ID'
BOT_CLIENT_SECRET = 'BOT_CLIENT_SECRET'
BOT_USER_AGENT    = 'BOT_USER_AGENT'

STREAM_SUBREDDIT  = 'all'
TARGET_SUBREDDIT  = 'test
```

The `STREAM_SUBREDDIT` is the subreddit to stream FROM. If you want to pull posts from all across Reddit, you can use 'all'. You can set it to single subreddits or multireddits (separate each subreddit with '+', such as 'redditdev+requestabot').

The `TARGET_SUBREDDIT` is the crosspost target. **Note: You can't use a multireddit here.**

The base config displayed here would read all submissions on Reddit, and if any have an English word as their ID, it will attempt to crosspost it to `/r/test`.

# Usage

**Note: Your bot needs to be subscribed to the `TARGET_SUBREDDIT`.**

```
python bot.py
```