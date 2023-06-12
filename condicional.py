#uma pequena atividade utilizando if,elif,else.
#tambem utilizamos o operador logico OR
#e utilizamos o in para encontrar determinada paralabra dentro da string qualquer que o usuario escrever
if __name__ == '__main__':
    action= str(input("informe a sua açao\n ex :comendo,dormindo,correndo,falando\n ex2 :viajando,caminhando,lendo,rindo,escutando musica\n"))
action.lower()
if (action=="viajando"or  ("dormindo" in action)):
  print("descansando~")
elif(("caminhando" in action)or ("correndo" in action)):
    print("mexendo o corpo")

elif(("lendo" in action)or action=="rindo"or ("escutando" in action)):
    print("voce esta sendo feliz")
else:
  print("voce esta "+action+",\nvivendo a vida como pode")
