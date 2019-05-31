import json
import code

import requests

# Put your Are.na and Hypothes.is tokens here
atoken = ''
htoken = ''

###### ARE.NA

# This will create the channel for your annotations
def createChannel(title):
    url = 'https://api.are.na/v2/channels'
    r = requests.post(url, params={'title': title},
        headers={"Authorization": "Bearer %s" % atoken,
                            "Content-Type": "application/json"})

# The thing we need to return is the slug
# This will be used when we post annotations to a channel
    return r.json()['slug']

# This will create a block for an annotation
def createBlock(channel, content, title=None):

    data = {
    "title" : title,
    "content" : content
    }

    url = 'https://api.are.na/v2/channels/{}/blocks'.format(channel)

    try:
        r = requests.post(url, data=json.dumps(data),
        headers={"Authorization": "Bearer %s" % atoken,
        "Content-Type": "application/json"}
            )

    except Exception as e:
        print("Exception in createBlock: %s" % e)
        return e


    return r.json()

##### HYPOTHES.IS

# This will grab all of our annotations from our Hypothes.is account
def getAll():
    list = []
    url = 'https://api.hypothes.is/api/search'
    params = {'limit': 100,
            'user': 'acct:CJEller1592@hypothes.is'}
    r = requests.get(url, headers={'Authorization': 'Bearer %s' % htoken,
                        'Content-Type':'application/json'},
                        params=params)

    annotations = r.json()['rows']

    for annotation in annotations:
        list.append(annotation)

    return list

# This is how we will grab the specific annotations for an article/post/etc
def search(resource):
	# List for the search results
	results = []

	# Grab all my annotations
	annotations = getAll()

	#For each annotation, see if resource is same as arg
	for annotation in annotations:
	# Grab the resource...
		r = annotation['document']['title'][0]
	# If it matches arg, put into results list
		if r == resource:
			results.append(annotation)

	return results
