import urllib.request
import http.cookiejar  # deal with cookies
import xml.etree.ElementTree as ET

cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [("User-agent", "Mozilla/5.0")]

webURL = "https://clinicaltrials.gov/ct2/show/NCT01396239?displayxml=true"

try:
    infile = opener.open(webURL, timeout=3)
    newpage = infile.read().decode("utf-8")
except:
    print("Page error")
    newpage = ""

root = ET.fromstring(newpage)

# <tag attribute>TEXT</tag>

print(root.tag)
print(root.attrib)
print(root.text)

print(root[0].tag)
print(root[1].tag)
print(root[2].tag)
print()

for child in root:
    print(child.tag)
print()

titleelement = root.find("brief_title")
print(titleelement.text)
print()

primaryoutcome = root.find("primary_outcome")
for child in primaryoutcome:
    print(child.text)
print()

for secondaryoutcome in root.findall("secondary_outcome"):
    for child in secondaryoutcome:
        print(child.text)
    print()
