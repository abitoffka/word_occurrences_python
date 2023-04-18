
from fileposition import FilePosition
from typing import List, Dict, Set, Optional 

class Occurrences : 
   occs : Dict[ str, Dict[ str, Set[ FilePosition ]]] 

   def __init__( self ) :
      self. occs = dict( ) 


   def add( self, word : str, filename : str, pos : FilePosition ) -> None :
      word = word.lower()
      filesDict : Dict[ str, Set[ FilePosition ]]
      positionsSet : Set[ FilePosition ]
      positionsSet2 : Set[ FilePosition ]
      occsKeys = self.occs.keys()
      if word in (occsKeys):
         filesDict = self.occs[word]
         if filesDict.get(filename) == None:
               positionsSet2 = set()
               positionsSet2.add(pos)
               filesDict.update({filename : positionsSet2})
         else: 
               positionsSet = filesDict[filename]
               positionsSet.add(pos)
               filesDict.update({filename: positionsSet})
               self.occs.update({word : filesDict})
      else:
         positionsSet = set()
         positionsSet.add(pos)
         filesDict = {}
         filesDict.update({filename : positionsSet})
         self.occs.update({word : filesDict})
 
   # Should return the number of distinct words:
 
   def distinctWords( self ) -> int : 
         return len(self.occs)
    
   # Should return the total number of words occurrences: 
 
   def totalOccurrences( self, word : Optional[str] = None, 
                               fname : Optional[str] = None ) -> int : 
         if word == None and fname == None:
            count = 0
            files1 = self.occs.values()
            for x in files1:
               positions = x.values()
               for y in positions:
                  count += len(y)
         elif fname == None:
            count = 0
            if self.occs.get(word) != None:
               files2 = self.occs[word]
               positions = files2.values()
               if positions:
                  for x in positions:
                     count += len(x)
         else: 
            count = 0
            if self.occs.get(word) != None:
               files = self.occs[word]
               if files.get(fname) != None:
                  positions = files[fname]
                  count = len(positions)
         return count

   # This is for debugging, so it doesn't need to be pretty: 

   def __repr__( self ) -> str : 
      return str( self. occs )

 
   # Here the occurrences must be sorted and shown in a nice way: 

   def __str__( self ) -> str : 
      result = ""
      words = sorted(self.occs.keys())
      for x in words:
         result += f"\"{x}\" has {self.totalOccurrences(x)} occurrence(s):\n"
         filesDict = self.occs[x]
         filenames = sorted(filesDict.keys())
         for y in filenames:
            result += f"   in file {y}\n"
            positionsSet = filesDict[y]
            positions = sorted(positionsSet)
            for z in positions:
               result += f"      at {z}\n"

      return result



