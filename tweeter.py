
import twitter
import markov
import secret


api = twitter.Api(consumer_key=CON_SEC,
    consumer_secret=CON_SEC_KEY, access_token_key=TOKEN, access_token_secret=TOKEN_KEY)

msg = markov.main()

print msg

status = api.PostUpdate(msg)