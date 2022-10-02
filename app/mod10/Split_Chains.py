import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(uid):

    input_dir=os.path.join("output/10.0/",uid)
   
    output_dir=os.path.join("output/10.0/",uid,"Split_Chains/") 
    make_dir(output_dir)

    fin=open(input_dir+"All_peptides_range.txt","rt")
    input_dir+="Input_Files/"

    for line in fin:

        PDB,spike,AB=line.split(" : ")[0].split("-")
        PDB=PDB.lower()
        AB=AB.split(".")[0]

        filename="completedpdb"+PDB+".ent"

        para="python app/mod10/pdb_selchain.py -"+spike+"  "+input_dir+filename+">"+output_dir+PDB+"_"+spike+".pdb"
        gara="python app/mod10/pdb_selchain.py -"+AB+"  "+input_dir+filename+">"+output_dir+PDB+"_"+AB+".pdb"
        
        print(para)
        os.system(para)  
        print(gara)
        os.system(gara)
