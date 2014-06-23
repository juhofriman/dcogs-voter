import sys
import json
import urllib2
import pprint

print("Hello, I'm DISCOGS based prototype of best records ever vote counter")
print("I lack of unit testing and proper structure. I don't do any caching.")
print("I'm made of pythons")
print
# HELPERS

votes = {}

def getVotesFileName(args):
    if len(args) == 1:
        printUsage(args)
        exit(1)
    return args[1]

def printUsage(args):
    print
    print "USAGE:"
    print "./python ",
    print args[0],
    print(" votesfile")

def apifyVote(vote):
    splitted = vote.split("/");
    pointer = 0;
    for token in splitted:
        if token == 'release':
            break
        if token == 'master':
            break
        pointer = pointer + 1
    return "http://api.discogs.com/" + "/".join(splitted[pointer:])

def normalizeVote(apiUrl):
    # Kludgish...
    if "/master" in apiUrl:
        return apiUrl.replace("/master", "/masters");
    foo = getJsonFrom(apiUrl)
    if 'master_url' in foo['resp']['release']:
        return foo['resp']['release']['master_url']
    else:
        # Can't normalize
        return apiUrl

def getJsonFrom(url):
    return json.load(urllib2.urlopen(url))

def registerVote(masterUrl):
    if masterUrl in votes:
        votes[masterUrl] = votes[masterUrl] + 1
    else:
        votes[masterUrl] = 1



# Read votes
votesFile = getVotesFileName(sys.argv)
print("Reading votes from " + votesFile)
voteUrls = ""
with open(votesFile) as f:
    voteUrls = f.readlines()

# Do some string handling ... remove whitespaces etc
voteUrls = map(lambda string: string.strip(), voteUrls)

print "Here we go"
print
for vote in voteUrls:
    print "Handling:\t" + vote
    apiUrl = apifyVote(vote)
    print " API-URL:\t", apiUrl
    normalizedUrl = normalizeVote(apiUrl)
    print " NORMALIZED:\t", normalizedUrl
    print
    registerVote(normalizedUrl)

for target in votes.keys():
    data = getJsonFrom(target)
    if 'resp' in data:
        data = data['resp']['release']
    # pprint.pprint(data)
    print target, "\t VOTES: ", votes[target], "\t", data['artists'][0]['name'], ":", data['title']
