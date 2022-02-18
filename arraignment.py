import urllib.request
import http.cookiejar


cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [("User-agent", "Mozilla/5.0")]

# webURL = "https://linxonline.co.pierce.wa.us/linxweb/Calendar/Calendar.cfm?calendar_file=ArraignmentList/20210902.htm"
webprefix = "https://linxonline.co.pierce.wa.us/linxweb/Calendar/Calendar.cfm?calendar_file=ArraignmentList/202109"
websuffix = ".htm"

for day in range(1, 31):
    daystring = str(day)
    if day < 10:
        daystring = "0" + daystring
    webURL = webprefix + daystring + websuffix

    try:
        infile = opener.open(webURL, timeout=15)
        newpage = infile.read().decode("utf-8")
    except:
        newpage = ""
        print("Web page error")

    if newpage != "":
        offensefound = newpage.lower().find("kidnap")
        print("Day =", daystring)
        if offensefound > -1:
            print("Offense found.")
        else:
            print("Offense not found.")
    else:
        print("Blank page error on day", daystring)
