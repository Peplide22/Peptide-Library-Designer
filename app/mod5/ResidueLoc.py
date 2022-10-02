import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(obj,uid=""):
    
    input_dir=os.path.join("output/3.0/",uid)
    input_dir=input_dir+"Splitting Chains "+obj+"/"

    output_dir=os.path.join("output/5.0/",uid)
    make_dir(output_dir)

    Residue_no=[]

    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir,filename)
 
        if os.path.isfile(f):
            
            PDB=filename.split("_")[1]+".txt"
            fsub=open(f,"rt")
            
            output=open(output_dir+PDB,"wt")
            
            for line in fsub:
                cb=line.split("\t")[1]
                nc=cb.split(":")[2]
                Residue_no.append(int(nc))
                            
            Residue_no=list(set(Residue_no))
            Residue_no.sort()
            print(PDB,Residue_no)
                            
            for element in Residue_no:
                val=str(element)
                if(Residue_no.index(element)!=len(Residue_no)-1):
                    val+=","
                output.write(val)
        
            Residue_no.clear()
        
            fsub.close()
            output.close()
