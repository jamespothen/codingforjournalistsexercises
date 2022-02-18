import urllib.request
import http.cookiejar  # deal with cookies

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [("User-agent", "Mozilla/5.0")]

webURL = "https://en.wikipedia.org/w/index.php?title=Kamala_Harris&action=history"

infile = opener.open(webURL, timeout=15)

newpage = infile.read().decode("utf-8")

keepgoing = True
currentplace = 0

while keepgoing:
    target = "<li data-mw-revid"
    targetindex = newpage.find(target, currentplace)
    if targetindex == -1:
        keepgoing = False
    else:
        target2 = "mw-changeslist-date"
        target2index = newpage.find(target2, targetindex)

        target3 = ">"
        target3index = newpage.find(target3, target2index)

        target4 = "<"
        target4index = newpage.find(target4, target3index)
        currentplace = target4index

        print(newpage[target3index + len(target3) : target4index])

infile.close()
