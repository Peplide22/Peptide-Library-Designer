import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(uid):

    input_dir=os.path.join("output/10.0/",uid)
   
    output_dir=os.path.join("output/10.0/",uid,"Peptide_Model/") 
    make_dir(output_dir)

    fin=open(input_dir+"All_peptides_range.txt","rt")
    input_dir+="Split_Chains/"

    for line in fin:
        PDB,spike,AB=line.split("-")
        PDB=PDB.lower()
        AB=AB.split(".")[0]
        seq=line.split(" : ")[1][:-1]

        print(PDB+' '+spike+' '+AB+' '+seq)

        fin=input_dir+PDB+"_"+AB+".pdb"

        m=seq.split(":")[0]
        seq="-"+seq

        para='python app/mod10/pdb_selres.py '+seq+' '+fin+' > '+output_dir+'1_'+PDB+'_'+AB+'_'+m+'.pdb'
      
        print(para)
        os.system(para)  
      