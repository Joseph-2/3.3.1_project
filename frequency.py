import matplotlib.pyplot as plot
import pandas as fl

data = fl.read_csv('Book1.csv', header=0)
ltr_count = []
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']
total_ltr_count = 0

April_WR = data['Date A']
March_WR = data['Date M']
Feb_WR = data['Date F']

months = [April_WR,March_WR,Feb_WR]

#print(April_WR)
#print(March_WR)
#print(Feb_WR)

def graph(letter,count):
  pass

for x in alph:
  tally = 0
  current_letter = x
  for month in months:
    for x in month:
      current_word = x
      #print(current_word)
      try:
        for x in current_word:
          if x == current_letter:
            tally += 1
      except TypeError:
        pass
  total_ltr_count += tally
  print(current_letter,tally)