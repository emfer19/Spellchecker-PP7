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
    wordset.add(line) #add to the set of words
    line=wordsfile.readline()
  return wordset

def validateWord(word,correctSet):
  """receives a word to check, and the set of correct words, follows the following rules:
     1. words with a length of less than 4 have no replacement value.
     2. if the two words are equal in length and longer than 4 characters, add an
        entry to the dictionary if the misspelled word and the replacement word have 4 letters that
        are the same in the same position.
     3. if the two words are not equal in length but are both longer than 3 characters and 
        the first three letters of the words are the same, add an entry to the dictionary
     Entries are indexed by a integer"""
  replacements={} #create a dictionary for replacement words
  entry=0
  if word in correctSet:
    return replacements
  elif word not in correctSet:
    if len(word)<4:  #rule 1
      return replacements
    elif len(word)>=4: #rule 2 and 3
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

def findReplacement(replacementWords,wrongWord):
  """receives and displays the dictionary containing possible replacement words
     and the misspelled word. 
      User must enter the integer number representing the replacement word they desire
      OR a -1 to keep the misspelled word with no change.
       Corresponding dictionary entry is returned if integer is entered.
       Misspelled word is returned if -1 is entered."""
  print '\nPossibly misspelled word:',wrongWord
  print '\nReplacement Options:\n'

  for keys,values in replacementWords.items(): #print all the replacement options
    print 'Option',str(keys),':\t'+values

  userWordChoice=''

  replacekey=None
  while str(replacekey)!='-1' and replacekey not in replacementWords.keys():
    try:
      print '\nCurrently Checking Spelling of:',wrongWord
      replacekey=int(raw_input('\nEnter which replacement option you want (-1 for no change):\n'))
      if str(replacekey)=='-1':
        userWordChoice= wrongWord
      elif int(replacekey) in replacementWords:
        userWordChoice=replacementWords[replacekey]
      elif int(replacekey) not in replacementWords:
        print 'Your input must be an option or -1'
    except ValueError:
      print str(replacekey),'is not a valid key or -1'
    except EOFError:
      print 'Please enter an integer of the replacement word or -1 to keep it the same'
  return userWordChoice

#main body of program
#receive the name of file to check and make output file name

infile=None
while not infile:
  infilename=raw_input('File to spell check? ')
  try:
    infile = file(infilename,'r')
  except IOError:
    print 'sorry. unable to open file', infilename

#create the filename and file for the checked data
outfilename=infilename.strip('.txt')
outfilename=outfilename+'Chk.txt'
outfile=file(outfilename,'w')

#create the set of correct words
setofCorrectWords=readFile()

#read each line of the file
line=infile.readline()
while line:
  words=line.split() #split up the words in the line
  for w in words: #check every word
    correct=validateWord(w,setofCorrectWords)
    replacementWord=w
    if len(correct)!=0:
      replacementWord=findReplacement(correct,w)
    outfile.write(replacementWord) #write the word after checking and making any changes
    outfile.write(' ') #maintain spacing
  line=infile.readline() 
  outfile.write('\n') #maintain line breaks

#close all files
outfile.close()
infile.close()

#allow the user to end the program when ready
print
raw_input('Press ENTER to close')
