#https://repl.it/X3G/4105

def pos_actual(self,actual):
  valor=self.__primero
  cont=0
  if(self.__primero==None):
    return
  if(self.__n<actual):
    self.__actual==self.__ultimo
  while(valor!=None):
    if(cont==actual):
      self.__pos=cont
      self.__actual=valor
    cont=cont+1
    valor=valor.sig
