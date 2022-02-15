infilename = "restaurants.tsv"
infile = open(infilename, "r")

outfilename = "manhattaninspects.tsv"
outfile = open(outfilename, "w")

firstline = infile.readline()
secondline = infile.readline()

headerlist = firstline.split("\t")

datalist = secondline.split("\t")

boroughindex = headerlist.index("boro")
scoreindex = headerlist.index("score")

for line in infile:
    datalist = line.split("\t")
    borough = datalist[boroughindex].strip()
    scorestring = datalist[scoreindex].strip()
    score = 0 if (scorestring == "") else int(scorestring)
    if(borough == "Manhattan"):
        if(score >= 30):
            outfile.write(line)

infile.close()
outfile.close()
