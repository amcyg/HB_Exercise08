import twitter

def main():

    api = twitter.Api()

    user = 'TheDowagerSays'

    statuses = api.GetUserTimeline(user)
    print [s.text for s in statuses]

if __name__ == "__main__":
    main()