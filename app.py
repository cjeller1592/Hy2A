from utils import createChannel, search, createBlock

### Function for creating Are.na channel of annotations that belong to a resource (post, pdf, article, etc)

def res(resource):
# Create channel for the resource
    channel = createChannel(resource)

# Grab the list of annotations for the resource
    annotations = search(resource)

# Go through the annotations in the list and grab the good stuff
    for a in annotations:
        text = a['text']
        link = a['links']['incontext']
        source = a['document']['title'][0]

 # Grab the quoted text...sometimes it is in different place so I do a try/except block
        for i in range(0, 4):
            try:
                q = a['target'][0]['selector'][i]['exact']

                if q != None:
                    quotedText = q
                    break

            except Exception:
                continue

            quotedText = 'Error: could not find annotation'

# Create the text that will appear in the Are.na block
        body = '>%s\n\n-- "%s" ([source](%s))\n\n%s' % (quotedText, source, link, text)

        block = createBlock(channel, body, title=None)

# TODO: figure out what to return for real - the channel now updated w/ annotations?
    return 'See if it worked!'



### Function for creating an Are.na channel of annotations that belong to a certain tag

def tag(tag):
# Create channel for the tag
    channel = createChannel(tag)

# Grab the list of annotations for the tag
    annotations = getTA(tag)

# Go through the annotations in the list and grab the good stuff
    for a in annotations:
        text = a['text']
        link = a['links']['incontext']
        source = a['document']['title'][0]

 # Grab the quoted text...sometimes it is in different place so I do a try/except block
        for i in range(0, 4):
            try:
                q = a['target'][0]['selector'][i]['exact']

                if q != None:
                    quotedText = q
                    break

            except Exception:
                    continue

            quotedText = 'Error: could not find annotation'

# Create the text that will appear in the Are.na block
        body = '>%s\n\n-- "%s" ([source](%s))\n\n%s' % (quotedText, source, link, text)

        block = createBlock(channel, body, title=None)

# Same TODO as above... 
     return 'See if it worked!'
