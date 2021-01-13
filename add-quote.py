import sys


def cmdArguments():
#    arguments = len(sys.argv) - 1
#    print ("The script is called with %i arguments" % (arguments))
    new_line = sys.argv[1]
    return(new_line)

def addQuote(new_quote):

  print(new_quote)
  
  with open("quotes.txt", "a") as a_file:
    a_file.write("\n")
    a_file.write(new_quote)
    a_file.close()
   
if __name__== "__main__":
   new_quote=cmdArguments()
   #print(new_quote)
   addQuote(new_quote)