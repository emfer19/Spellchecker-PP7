#Name: Emily Ferretti
#Email: ferrettiek@slu.edu
#Current date: 4/22/16
#Course Information: CSCI-1300-01
#Instructor: Judy Etchison

#Sources Consulted: textbook, my past programming knowledge

'''Honor Code Statement: In keeping with the honor code policies of St.Louis University, the Department of Mathematics and Computer Science, I affirm that I have neither given nor received assistance on this programming assignment. This assignment represents my individual, original effort.'''



def ReadFile():
  """reads the correctly spelled words from the given 'words.txt' file
     saves and returns a set"""
  wordsfile=file('words.txt')
  line=wordsfile.readline()
  wordset=set()
  while line:
    line=line.strip()
    wordset.add(line)
    line=wordsfile.readline()
  wordsfile.close()
  return wordset

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

ReadFile()


