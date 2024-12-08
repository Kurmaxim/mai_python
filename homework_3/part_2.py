import collections


def unique_count(string):
    myDict = collections.Counter([word.strip(", ") for word in string.lower().split()])
    return len([k for k, v in myDict.items()])


myStr = "This, this this is really really good."
print(unique_count(myStr))