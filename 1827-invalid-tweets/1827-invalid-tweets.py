import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    filt = (tweets['content'].str.len() > 15)
    return tweets.loc[filt,['tweet_id']]