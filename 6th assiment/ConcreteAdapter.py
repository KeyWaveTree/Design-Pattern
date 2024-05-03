#third party apis
class TwitterAPI:
    def get_tweets(self):
        print("fetching tweets form Twitter")
        stat = {"tweet": "Hello Twitter!", "likes": 10 , "date": "2022-01-01"}
        return stat

class FacebookAPI:
    def get_posts(self):
        print("fetching posts form facebook")
        stat = {"post": "Hello Facebook!", "reactions": 5, "date": "2022-01-02"}
        return stat

class InstagramAPI:
    def get_phtos(self):
        print("fetching posts form Instagram")
        stat = {"post": "Hello Instagram!", "likes": 15, "date": "2022-01-03"}
        return stat

#third party api 기능 연계
class SocialMediaAdapter:
    def fetch_posts(self):
        pass

#adapter and concreate adapters
#각 api를 연결하고, fatch_posts를 구현
class TwitterAdapter(SocialMediaAdapter):
    def __init__(self, api: TwitterAPI):
        self.twitterApi = api
    def fetch_posts(self):
        return self.twitterApi.get_tweets()

class FacebookAdapter(SocialMediaAdapter):
    def __init__(self, api: FacebookAPI):
        self.facebookApi = api
    def fetch_posts(self):
        return self.facebookApi.get_posts()


class InstagramAdapter(SocialMediaAdapter):
    def __init__(self, api: InstagramAPI):
        self.instagramApi = api
    def fetch_posts(self):
        return self.instagramApi.get_phtos()
#client
def main():
    twitter = TwitterAdapter(TwitterAPI())
    facebook = FacebookAdapter(FacebookAPI())
    instagram = InstagramAdapter(InstagramAPI())
    for adapter in [twitter, facebook, instagram]:
        posts = adapter.fetch_posts()
        print(posts)

if __name__ == "__main__":
    main()
