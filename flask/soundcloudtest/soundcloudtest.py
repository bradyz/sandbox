import soundcloud

# create client with access token
client = soundcloud.Client(client_id='d7c7244051bcb9356130e6fd65e30844')

# a permalink to a track
track_url = 'http://soundcloud.com/forss/voca-nomen-tuum'

# resolve track URL into track resource
track = client.get('/resolve', url=track_url)

# now that we have the track id, we can get a list of comments, for example
for comment in client.get('/tracks/%d/comments' % track.id):
    try:
        print('Someone said: %s at %d' % (comment.body, comment.timestamp))
    except:
        pass
