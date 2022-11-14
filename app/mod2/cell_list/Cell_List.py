import os
import openpyxl
import time

input_dir="output/1.0/"
root_dir="output/2.0/"

def segregate(uid,file_path):

    global input_dir,root_dir
    input_dir=os.path.join(input_dir,uid)
    root_dir=os.path.join(root_dir,uid)

    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active

    if(os.path.exists(root_dir+"PDB_67.txt")):
        os.remove(root_dir+"PDB_67.txt")
        os.remove(root_dir+"PDB_133.txt")

    f67=open(root_dir+"PDB_67.txt","a")
    f133=open(root_dir+"PDB_133.txt","a")

    rows=sheet.max_row

    for i in range(1,rows+1):

        if(type(sheet['A'+str(i)].value)!=str):
            continue

        j=ord('E')

        if(sheet['D'+str(i)].value=="Spike glycoprotein"):

            print(sheet['A'+str(i)].value+" "+sheet[chr(j)+str(i)].value)
            
            while(sheet[chr(j)+str(i)].value!=None):
                f133.write(sheet['A'+str(i)].value.strip()+" "+sheet[chr(j)+str(i)].value.strip()+"\n")
                j+=1

        elif(sheet['D'+str(i)].value=="Spike protein S1"):

            print(sheet['A'+str(i)].value+" "+sheet[chr(j)+str(i)].value)
            
            while(sheet[chr(j)+str(i)].value!=None):
                f67.write(sheet['A'+str(i)].value.strip()+" "+sheet[chr(j)+str(i)].value.strip()+"\n")
                j+=1

    f67.close()
    f133.close()

def fn(obj):

    file=open(root_dir+"PDB_"+obj+".txt","rt")

    try:
        os.makedirs(root_dir+"output_"+obj)
    except:
        pass

    for line in file:
        var,atomtype=line.split(" ")

        if(os.path.exists(input_dir+"completedpdb"+var+".ent")):

            atomtype=atomtype[:-1]
            var=var.lower()
            print(var+' '+atomtype)

            input=input_dir+"completedpdb"+var+".ent"
            output=root_dir+"output_"+obj+"/outdis_"+var+"_"+atomtype+".txt"

            para='python app/mod2/cell_list/src/main.py -f '+input+' -o '+output+' --cutoff 5.0 --atomtypes "ALL" --restypes "ALL" --refchain '+atomtype
        
            os.system(para)


def main(obj):

    a=time.time()
    fn(obj)
    print(time.time()-a)