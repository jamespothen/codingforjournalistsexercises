import urllib.request
import http.cookiejar  # deal with cookies

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [("User-agent", "Mozilla/5.0")]

webURL = "https://en.wikipedia.org/wiki/Donald_Trump"
outfilename = "djt.html"

infile = opener.open(webURL, timeout=15)
outfile = open(outfilename, "w", encoding="utf-8")

newpage = infile.read().decode("utf-8")
print(newpage, file=outfile)

infile.close()
outfile.close()
