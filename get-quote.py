import random

def printQuote():
  #print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  #last = 13
  last = len(quotes) - 1
  rnd = random.randint(0, last)
  mdo = rnd

  #print(quotes)
  for x in range(mdo):
    print(quotes[rnd], end="")
    rnd = random.randint(0, last)
   
if __name__== "__main__":
  printQuote()
