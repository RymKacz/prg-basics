class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username} added a new post: {content}")

    def display_timeline(self):
        print(f"{self.username}'s Timeline:")
        print(self.posts)
def main():
    username1 = SocialMediaProfile(username="JohnDoe")
    username1.add_post("Hello, world!")
    username1.add_post("Had a great day at the park!")
    username1.add_post("What's up, Natalie? How are you?")
    username1.display_timeline()

if __name__ == "__main__":
    main()