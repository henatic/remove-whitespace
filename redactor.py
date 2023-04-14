f = open("RobotsScriptSPACED.txt" , "r")

lines = f.readlines()
f.close()
f = open('RobotsScript.txt', 'w')

for x in lines:
    if x.strip() != '':
        f.write(x)
f.close()