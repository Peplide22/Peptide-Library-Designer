import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(uid):

    input_dir=os.path.join("output/10.0/",uid)
   
    output_dir=os.path.join("output/10.0/",uid,"Output_Files/") 
    make_dir(output_dir)

    fin=open(input_dir+"All_peptides_range.txt","rt")

    for line in fin:

        PDB,spike,AB=line.split("-")
        PDB=PDB.lower()
        AB=AB.split(".")[0]
        seq=line.split(" : ")[1][:-1]
        
        m=seq.split(":")[0]
        
        print(PDB+' '+spike+' '+AB+' '+m)

        PDBa=input_dir+"Split_Chains/"+PDB+"_"+spike+".pdb"
        PDBb=input_dir+"Peptide_Model/""1_"+PDB+"_"+AB+"_"+m+".pdb"

        para='python app/mod10/pdb_merge.py '+PDBa+' '+PDBb+' > '+output_dir+'Final_'+PDB+'_'+spike+'_'+AB+'_'+m+'.pdb'
    
        print(para)
        os.system(para)  
   