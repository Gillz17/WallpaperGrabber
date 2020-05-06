import praw

class WallpaperReddit():
    def __init__(self):
        self.reddit = praw.Reddit(client_id = 'K4BziSJIqhaMEQ', 
            client_secret = 'typCn3ZtMPPACL3RHidScozFffU', 
            username='ThinWeakness4', 
            password='25Dipg.*PP7sTCg', 
            user_agent='test script')

    def Grabber(self):

        size1 = '2560'
        size2 = '5120'

        with open("C:/Users/zmc17/Documents/Python Scripts/WallpaperGrabber/Links.txt", "w") as file:
            subreddit = self.reddit.subreddit("WidescreenWallpaper")
            for submission in subreddit.hot():
                title = submission.title
                if size1 in title:
                    file.write(submission.url + "\n")
                elif size2 in title:
                    file.write(submission.url + "\n")
        file.close()
        print("Got all of the links.  Check the file!")


testCase = WallpaperReddit()
testCase.Grabber()