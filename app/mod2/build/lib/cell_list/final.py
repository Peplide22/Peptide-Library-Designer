import os

file=open("PDB_67.txt","rt")

for line in file:
    var,atomtype=line.split(" ")
    atomtype=atomtype[:-1]
    var=var.lower()
    print(var+' '+atomtype)

    input="./input/completedpdb"+var+".ent"
    output="./output_67/outdis_"+var+"_"+atomtype+".txt"

    para='python ./src/main.py -f '+input+' -o '+output+' --cutoff 5.0 --atomtypes "ALL" --restypes "ALL" --refchain '+atomtype
    
    # print(para)
    os.system(para)
