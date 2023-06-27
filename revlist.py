#found this reverse list interesting
"""this function prints a list in reverse
inlist: function objest
"""
def revlist(inlist):
      #create a new list and append items from inlist
  new = []
  for i in range(len(inlist)):
      #append to new. When i ==0 then inlist index is 2 according to the list below
    new.append(inlist[len(inlist)-1-i])
  return new
#print(revlist([1,2,3]))