#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/22/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''

#function definitions

def readFile():
  """reads the correctly spelled words from the given 'words.txt' file
     saves and returns a set"""
  wordsfile=file('words.txt')
  line=wordsfile.readline()
  wordset=set()
  while line:
    line=line.strip()
    wordset.add(line)
    line=wordsfile.readline()
 
  return wordset

def validateWord(word,correctSet):
  """receives a word to check, and the set of correct words, follows the following rules:
     1. words with a length of less than 4 have no replacement value.
     2. if the two words are equal in length and longer than 4 characters, add an
        entry to the dictionary if the misspelled word and the replacement word have 4 letters that
        are the same in the same position.
     3. if the two words are not equal in length but are both longer than 3 characters and 
        the first three letters of the words are the same, add an entry to the dictionary"""
  replacements={} #create a dictionary for replacement words
  entry=0
  if word in correctSet:
    return replacements
  elif word not in correctSet:
    if len(word)<4:
      return replacements
    elif len(word)>=4:
      for w in correctSet:
        if len(word)==len(w):
          counter=0
          for i in range(len(word)):
            if word[i]==w[i]:
              counter+=1
          if counter>=4:
            entry+=1
            replacements[entry]=w  
        elif len(word)!=len(w) and len(word)>3 and len(w)>3:
          if word[0]==w[0] and word[1]==w[1] and word[2]==w[2]:
            entry+=1
            replacements[entry]=w
  return replacements


#main body of program
#receive the name of file to check and make output file name

infile=None
while not infile:
  infilename=raw_input('File to spell check? ')
  try:
    infile = file(infilename,'r')
  except IOError:
    print 'sorry. unable to open file', infilename


outfilename=infilename.strip('.txt')
outfilename=outfilename+'Chk.txt'
outfile=file(outfilename,'w')


setofCorrectWords=readFile()

line=infile.readline()
while line:
  words=line.split()
  for w in words:
    correct=validateWord(w,setofCorrectWords)
  line=infile.readline()

aword='scientst'
replacementDict=validateWord(aword,setofCorrectWords)
for keys,values in replacementDict.items():
  print 'option',str(keys),values
