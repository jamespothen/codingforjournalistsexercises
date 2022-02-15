import urllib.request
import http.cookiejar


cj = http.cookiejar.MozillaCookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]

webprefix = "https://apod.nasa.gov/apod/ap"
websuffix = ".html"

for year in range(18,22):
    yearstring = str(year)

    for month in range(1,13):
        monthstring = str(month)
        if month < 10:
            monthstring = "0" + monthstring

        for day in range(1,32):
            daystring = str(day)
            if day < 10:
                daystring = "0" + daystring
            webURL = webprefix + yearstring + monthstring + daystring + websuffix

            try:
                infile = opener.open(webURL, timeout = 15)
                newpage = infile.read().decode("utf-8")
            except:
                newpage = ""

            if newpage!="":
                marsfound = newpage.lower().find("mars")
                if marsfound > -1:
                    print(f" Mars pic found on date: {monthstring}/{daystring}/20{yearstring}")
            else:
                print(f"Blank page error on on date: {monthstring}/{daystring}/20{yearstring}")
