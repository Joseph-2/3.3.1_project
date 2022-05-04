import matplotlib.pyplot as plot
import pandas as fl

data = fl.read_csv('Book1.csv', header=0)
ltr_count = []
alph = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
'O','P','Q','R','S','T','U','V','W','X','Y','Z']
months = [data['Date A'],data['Date M'],data['Date F']]

for letter in alph:
  tally = 0
  current_letter = letter
  for month in months:
    for word in month:
      current_word = word
      try:
        for letter in current_word:
          if letter == current_letter:
            tally += 1
      except TypeError:
        pass
  ltr_count.append(tally)
  print(current_letter,tally)
print(alph)
print(ltr_count)

plot.bar(alph,ltr_count,align='center',color='green')
plot.ylabel('Total Letter Count')
plot.xlabel('Letter')
plot.title('Frequency of Letters in Wordle')
plot.show()