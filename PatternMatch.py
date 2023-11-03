from unittest.mock import patch

def StringMatch(txt,pat):
    print ("checking for the pattern '", pat, "' in the text '", txt, "' ")
    t = len(txt)
    p = len(pat)
    patHash = hash(pat)
    counter = 0
    numComparisons = 0
    for i in range (t-p+1):
        chunk = txt[i:i+p]
        if (hash(chunk)==patHash):
            numComparisons += 1
            for a in range (p):
                if (pat[a]==chunk[a]):
                    continue
                else:
                    break
            counter += 1
            print ("Match found at index", i)
    print ("'", pat, "' occurs ", counter, " times in '", txt, "' ")
    print (numComparisons, " character by character comparisons were made!")
    print ()

StringMatch('hellollolololliesbyzantineallowedmenstrnbcglllhithreellls', 'll') # pattern overlaps in the text!
StringMatch('booooooooooooooooooooboooooooooooooooooooooooooobooooooooooooooo', 'ooooooo') # highly overlapping, long pattern
StringMatch('knjsjrghuijhidbdofhgsjkkbgwjenjcnosfgihbnjhguergjtksjfvibjniohgh', 'him') # no occurrence!
StringMatch('aklkakgdjHREdtGNsgsbSnjsfnsSHghgSbNsgfhegAHGgeehgeygeAdgvigrgrgGHh', 'Ge') # Including caps
StringMatch('DdhdFHBtDhn53y7$^7uHETY4664$y64y547ghby44yB45476h9hrdyr664857*tg656v^G7578F#FG&67yV(4W$Fy', 'W$') # including letters, numbers, special chars

