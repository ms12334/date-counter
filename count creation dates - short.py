import re
from datetime import datetime
#import matplotlib

y2015 = [0,0,0,0,0,0,0,0,0,0,0,0]
y2016 = [0,0,0,0,0,0,0,0,0,0,0,0]
y2017 = [0,0,0,0,0,0,0,0,0,0,0,0]

with open('dates.csv', 'r') as fin:
    for line in fin:
        line = line.strip()
        if re.match(r'[0-9][0-9]/[0-9][0-9]/201[567]', line):
            d = datetime.strptime(line, '%m/%d/%Y %I:%M:%S %p')
            if d.year == 2015:
                count = y2015[d.month - 1]
                y2015[d.month - 1] = count + 1
            elif d.year == 2016:
                count = y2016[d.month - 1]
                y2016[d.month - 1] = count + 1
            elif d.year == 2017:
                count = y2017[d.month - 1]
                y2017[d.month - 1] = count + 1
            else:
                break

with open('ListContentShort.txt', 'a') as fout:
    fout.write("2015\nJan: " + str(y2015[0]) + "\tFeb: " + str(y2015[1]) + "\tMar: " + str(y2015[2]) + "\tApr: " + str(y2015[3]) + "\tMay:" + str(y2015[4]) + "\tJun:" + str(y2015[5]) + "\tJul:" + str(y2015[6]) + "\tAug:" + str(y2015[7]) + "\tSep:" + str(y2015[8]) + "\tOct:" + str(y2015[9]) + "\tNov:" + str(y2015[10]) + "\tDec:" + str(y2015[11]) + "\n")
    fout.write("2016\nJan: " + str(y2016[0]) + "\tFeb: " + str(y2016[1]) + "\tMar: " + str(y2016[2]) + "\tApr: " + str(y2016[3]) + "\tMay:" + str(y2016[4]) + "\tJun:" + str(y2016[5]) + "\tJul:" + str(y2016[6]) + "\tAug:" + str(y2016[7]) + "\tSep:" + str(y2016[8]) + "\tOct:" + str(y2016[9]) + "\tNov:" + str(y2016[10]) + "\tDec:" + str(y2016[11]) + "\n")
    fout.write("2017\nJan: " + str(y2017[0]) + "\tFeb: " + str(y2017[1]) + "\tMar: " + str(y2017[2]) + "\tApr: " + str(y2017[3]) + "\tMay:" + str(y2017[4]) + "\tJun:" + str(y2017[5]) + "\tJul:" + str(y2017[6]) + "\tAug:" + str(y2017[7]) + "\tSep:" + str(y2017[8]) + "\tOct:" + str(y2017[9]) + "\tNov:" + str(y2017[10]) + "\tDec:" + str(y2017[11]) + "\n")

