import csv

##This tool will allow you to find both the most frequent and least frequent word(s) in a .csv file containing one
##word per line.

nl = []
cl = []
maxli = []
minli = []
maxwl = []
minwl = []

print('Welcome!')
inp = input("Please enter the complete name of your desired .csv file (including the '.csv' extension): ")

with open(inp, 'r') as csvfile:
    tl = csvfile.readlines()
    for line in tl:
        new = line.replace("\n", "")
        nl.append(new)
    nl2 = set(nl)
    for nline in nl2:
        co = 0
        for enline in nl:
            if enline == nline:
                co = co + 1
        cl.append(co)
    nl3 = list(nl2)
    nl3, cl = zip(*sorted(zip(nl3, cl)))
    nl4 = list(nl3)
    cl2 = list(cl)
    maxnum = max(cl2)
    maxnumi = cl.index(maxnum)
    maxword = nl4[maxnumi]
    minnum = min(cl2)
    minnumi = cl.index(minnum)
    minword = nl4[minnumi]
    cl2i = 0
    cl2next = cl2.copy()
    print(f"'{inp}' has been entered.")
    print(f"Results regarding word frequency within '{inp}' are as follows: ")
    for cnums in cl2:
        if cnums == maxnum:
            maxli.append(cnums)
            cnumsi = cl2next.index(cnums)
            wordco = nl4[cnumsi]
            maxwl.append(wordco)
            cl2next[cnumsi] = 0
    cl2nextn = cl2.copy()
    for cnumsn in cl2:
        if cnumsn == minnum:
            minli.append(cnumsn)
            cnumsni = cl2nextn.index(cnumsn)
            wordmin = nl4[cnumsni]
            minwl.append(wordmin)
            cl2nextn[cnumsni] = 0
    if len(maxli) > 1:
        results = str(maxwl)[1:-1]
        print(f'Most frequent words: {results} / Number of appearances for each word: {maxnum}')
    elif len(maxli) == 1:
        results = str(maxwl)[1:-1]
        print(f'Most frequent word: {maxword} / Number of appearances: {maxnum}')
    if len(minli) > 1:
        resultsn = str(minwl)[1:-1]
        print(f'Least frequent words: {resultsn} / Number of appearances for each word: {minnum}')
    if len(minli) == 1:
        resultsn = str(minwl)[1:-1]
        print(f'Least frequent word: {minword} / Number of appearances: {minnum}')

    print('Thank you for using this word frequency finding tool!')











