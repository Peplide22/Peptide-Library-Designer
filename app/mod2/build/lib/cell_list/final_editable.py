import os

file=open("new_PDB.txt","rt")

for line in file:
    var,atomtype=line.split(" ")
    atomtype=atomtype[:-1]
    print(var+' '+atomtype)

    input="./input/pdb"+var+".ent"
    output="./outdis_"+var+"_"+atomtype+".txt"

    para='python ./src/main.py -f '+input+' -o '+output+' --cutoff 5.0 --atomtypes "ALL" --restypes "ALL" --refchain '+atomtype
    print(para)
    os.system(para)
