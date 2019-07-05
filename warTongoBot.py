# -*- coding: utf-8 -*-
import os
import sys
import json
import random

def Error(message):
  print(message)
  sys.exit(1)

def exportUpdatedData(data):
    with open(os.path.join(sys.path[0], str(len(data))+".json"), "w", encoding='utf-8') as gradiant_updated_data:
        json.dump(data, gradiant_updated_data)

def selectRandomAttackAndVictim(tam):
    attackerIndex = random.randint(0,tam)
    victimIndex = random.randint(0,tam)

    #posiblidad de suicidarse, solo si attackerIndex y victimIndex es el mismo y isSuicidePosibility is mayor al 95%, si no se repite
    if (attackerIndex == victimIndex):
        if (random.randint(0,100)<95):
            return selectRandomAttackAndVictim(tam)

    return (attackerIndex, victimIndex)

def main():
    #En esta primera versión, el fichero de entrada se espera que sea un array tipo:
    #["nombre1", "nombre2", "nombre3"]
    if (len(sys.argv) != 2):
        Error ("Usage: python " + sys.argv[0] + " <data_input.json>")
    with open(os.path.join(sys.path[0], sys.argv[1]), encoding='utf-8') as names_data:
        allNames = json.loads(names_data.read())

    total = len(allNames)
    indexArray = total-1

    (attackerIndex, victimIndex) = selectRandomAttackAndVictim(indexArray)
    attacker = allNames[attackerIndex]
    victim = allNames[victimIndex]
    if (attackerIndex == victimIndex):
        print(victim + " committed suicide ");
    else:
        print(attacker + " killed " + victim);
    allNames.pop(victimIndex)
    if (len(allNames)!=1):
      print ("Remaining:" + str(len(allNames)))
      exportUpdatedData(allNames)
    else:
      print("The winner is: " + allNames[0])
    

if __name__ == '__main__':
  main()
