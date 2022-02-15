import urllib.request
import http.cookiejar


cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

webURL = "https://archive.org/stream/mobydickorwhale01melvuoft/mobydickorwhale01melvuoft_djvu.txt"
outfilename = "ishmael.txt"

infile = opener.open(webURL, timeout = 15)
outfile = open(outfilename,"w",encoding="utf-8")

ishmaelcounter = 0

# Method 1: line by line
#   1a: for loop
# for line in infile:
#     decodedline = line.decode("utf-8")
#     if decodedline.lower().find("ishmael") > -1:
#         ishmaelcounter += 1
#         outfile.write(decodedline)

# 1b: while loop
keepgoing = True
while keepgoing:
    newline = infile.readline().decode("utf-8")
    if newline.lower().find("ishmael") > -1:
        ishmaelcounter += 1
        outfile.write(newline)
    if newline == "":
        keepgoing = False

# Method 2: whole file
# wholepage = infile.read().decode("utf-8")
# linelist = wholepage.split("\n")
#
# for line in linelist:
#     if line.lower().find("ishmael") > -1:
#         ishmaelcounter += 1
#         outfile.write(line)

print(f"Ishmael Count: {ishmaelcounter}")

infile.close()
outfile.close()
