

class FilePosition : 
   line : int
   column : int

   def __init__( self ) :
      self. line = 1
      self. column = 1

   def advance( self, i : int ) :
      self. column += i

   def nextLine( self ) :
      self. line += 1
      self. column = 1

   def __repr__( self ) -> str : 
      return "( {}, {} )". format( self. line, self. column )

   def __str__( self ) -> str :
      return "line " + str( self. line ) + ", column " + str( self. column )



   def __hash__( self ) -> int :
      return hash (self.line) * 2 + hash (self.column)

   def __eq__( self, other ) -> bool :
      if isinstance (other, FilePosition):
         return self.line == other.line and self.column == other.column
      else:
         return False

   def __lt__( self, other ) -> bool :
      if isinstance(other, FilePosition):
         if self.line < other.line:
            return True
         elif self.line == other.line:
            if self.column < other.column:
               return True
            else:
               return False
         return False
