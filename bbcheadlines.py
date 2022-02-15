import urllib.request
import http.cookiejar # deal with cookies

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

webURL = "https://www.bbc.com/"

infile = opener.open(webURL, timeout = 15)

newpage = infile.read().decode("utf-8")

keepgoing = True
currentplace = 0

target = 'data-bbc-container="news"'
targetindex = newpage.find(target, currentplace)

while keepgoing:
    target2 = 'rev="news|headline" >'
    target2index = newpage.find(target2, currentplace)
    if target2index == -1:
        keepgoing = False
    else:
        target3 = "<"
        target3index = newpage.find(target3, target2index)
        print(newpage[target2index+len(target2):target3index].strip())
        currentplace = target3index

# while keepgoing:
#
#     if target2index == -1:
#         keepgoing = False
#     else:
#         target2 = "mw-changeslist-date"
#         target2index = newpage.find(target2, targetindex)
#
#         target3 = ">"
#         target3index = newpage.find(target3, target2index)
#
#         currentplace = target4index
#

infile.close()
