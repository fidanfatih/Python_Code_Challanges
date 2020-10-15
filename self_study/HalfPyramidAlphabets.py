lastLetter= 'Z'
letters="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rowLettters=list( )
for i in range( letters.index( lastLetter ) + 1 ):
    rowLettters.append( letters[i]*(letters.index(letters[i])+1))
for rowLetter in rowLettters:
    print( *rowLetter )
