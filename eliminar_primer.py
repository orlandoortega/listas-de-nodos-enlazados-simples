#https://repl.it/X3G/4106
def elimin_primer(self):
  if(self.__primero==None):
    return
  temp=self.__primero
  self.__primero=temp.sig
  self.__n=self.__n-1
  self.__pos=self.__pos-1
  if(self.__primero==None):
    self.__ultimo=None
    self.__actual=None
  if(self.__actual==temp):
    self.__actual=self.__actual.sig
  del temp
