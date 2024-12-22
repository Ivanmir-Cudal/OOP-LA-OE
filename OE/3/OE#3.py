print("OE_3")
class SocialMediaAccount():
    def __init__(self, username, password):
        self.username = username
        self.passsword = password
    def login():
        pass
   
    def post():
        pass
class InstagramAccount(SocialMediaAccount):
    def __init__(self, username, password):
        super().__init__(username, password, Number_of_followers)
        self.Number_of_followers = Number_of_followers
       
    def share_story(self):
        pass
   
class TwitterAccount(SocialMediaAccount):
    def __init__(self, username, password, Number_of_tweet):
        super().__init__(username, password)
        self.Number_of_tweet = Number_of_tweet
       
    def tweet(self):
        pass
