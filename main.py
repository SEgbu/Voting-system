from googleapiclient.discovery import build

# credentials
apiKey = "YOUR_API_KEY"
videoID = "" # channel ID 

# build a resource for youtube
resource = build("youtube", "v3", developerKey=apiKey)

#create a request to get the most recent 100 comments on the video
request = resource. commentThreads().list(
                            part="snippet",
                            videoId=videoID,
                            maxResults=100,
                            order="time")
#execute the request
response =request.execute()

items = response["items"]

votes = [] # change to suit voting system, for example: ["[A]", "[B]", "[C]"]
voteCounter = [0,0,0,0,0,0,0] # change to suit voting system, for example: [0,0,0]

# checks if votes are in the comments 
for item in items:
    itemInfo = item["snippet"]
    for i in range(len(votes)):
        if votes[i] in itemInfo["topLevelComment"]["snippet"]["textDisplay"]:
            voteCounter[i] += 1
    print(itemInfo["topLevelComment"]["snippet"]["textDisplay"])

# prints the votes 
print(voteCounter)




        





