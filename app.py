from utils import createChannel, search, createBlock

def main(resource):

    channel = createChannel(resource)

    annotations = search(resource)

    for a in annotations:
        text = a['text']
        link = a['links']['incontext']
        source = a['document']['title'][0]

        for i in range(0, 4):
            try:
                q = a['target'][0]['selector'][i]['exact']

                if q != None:
                    quotedText = q
                    break

            except Exception:
                continue

            quotedText = 'Error: could not find annotation'


        body = '>%s\n\n-- "%s" ([source](%s))\n\n%s' % (quotedText, source, link, text)

        block = createBlock(channel, body, title=None)

# Will need to figure out what to return for real
# Maybe the channel now updated w/ annotations?
    return 'See if it worked!'
