import python_tweet 

def get_tweets_from_timelines():

    tweets_timelines_list = []
    for id in range(0, len(ids), 1):
        one_id = (ids[id:id+1])
        one_id = ' '.join(one_id) 

    for tweet in tweepy.Paginator(client.get_users_tweets, id=one_id, max_results=100,
            tweet_fields=['attachments', 'author_id', 'context_annotations', 'created_at', 'entities', \
                'conversation_id', 'possibly_sensitive', 'public_metrics', 'referenced_tweets', \
                 'reply_settings', 'source', 'withheld' ],\
            user_fields=['created_at', 'description', 'entities', 'profile_image_url', 'protected', \
                'public_metrics', 'url', 'verified', 'withheld'],
                  expansions=['referenced_tweets.id', 'in_reply_to_user_id', 'attachments.media_keys', ],
            media_fields=['preview_image_url'],

                     ): 
            tweets_timelines_list.append(tweet)
    return tweets_timelines_list