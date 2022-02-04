teksts = input("Ievadiet tekstu: ")
def deleteE(teksts):
  if teksts.count("e")>0:
    teksts = teksts.replace("e", " ")
    teksts = teksts.upper()
    print(teksts)
  else:
    teksts = "TEKSTS NESATUR VAJADZIGO BURTU"
    print(teksts)
  return teksts
deleteE(teksts)