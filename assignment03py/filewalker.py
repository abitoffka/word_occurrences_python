
import io
from fileposition import FilePosition
from typing import Tuple, Generator, TextIO 

import os
import syntax
import copy
import codecs


class FileWalker : 
   topdir : str  # Python uses strings for representing file names. 
  
   def __init__( self, topdir ) :
      self. topdir = topdir # No checks here. 


   def recDirIterator( self ) -> Generator[ Tuple[ str, str, FilePosition ], None, None ] : 
      if os.path.exists(self.topdir) == False:
         raise FileNotFoundError(f"{self.topdir} doesn't exist!")
      
      if os.path.isdir(self.topdir) == False:
         raise NotADirectoryError(f"{self.topdir} is not a directory!")

      for i in os.walk(self.topdir):
         dir = i[0]
         files = i[2]
         for filename in files:
            filepath = os.path.join(dir, filename)
            for occ in FileWalker.fileIterator(open(filepath, "r", encoding = "utf8" )) :
               str = occ[0]
               filepos = occ[1]
               yield (filepath, str,filepos)
         

   @staticmethod 
   def fileIterator( f : TextIO ) -> Generator[ Tuple[ str, FilePosition ], None, None ] :
      word = ""
      position = FilePosition()
      currentColumn = 0

      while True:
         ch = f.read(1)
         ch = ch.lower()
         currentColumn += 1
         if syntax.inWord(str(ch)) == False:
            if len(word) > 0:
               position1 = copy.copy(position)
               yield (word, position1)
               word = ""
            if syntax.isNewLine(str(ch)) == True:
               position.nextLine()
               currentColumn = 0
         else:
            if word == "":
               position.advance(currentColumn-position.column)
            word = word + str(ch)
         if ch == '':
            break
      f.close()

      

   def __repr__( self ) -> str : 
      return "FileWalker: " + self. topdir 

   def __str__( self ) -> str :
      return "FileWalker: " + self. topdir


