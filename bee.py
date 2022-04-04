bee_script = open("bee_script.txt", "rt")
shrek_script = open("shrek_script.txt", "r")
shrek = shrek_script.read()
fixed = open("fixed.txt", "wt")
for line in bee_script:
    fixed.write(line.replace('bee', shrek))
bee_script.close()
shrek_script.close()
fixed.close()