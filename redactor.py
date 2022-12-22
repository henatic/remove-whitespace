f = open("Shrek_ScriptSPACED.txt" , "r")

lines = f.readlines()

f = open('Shrek_Script.txt', 'w')

for x in lines:
    if x.strip() != '':
        f.write(x)