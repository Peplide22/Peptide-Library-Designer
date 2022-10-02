import os,shutil

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(uid):

    src_dir=os.path.join("output/1.0/",uid)
    input_dir=os.path.join("output/7.0/",uid)

    output_dir=os.path.join("output/10.0/",uid)
    make_dir(output_dir)
    make_dir(output_dir+"Input_Files/")

    fin=open(input_dir+"All_peptides_summary.txt","rt")
    fout=open(output_dir+"All_peptides_range.txt","wt")

    for line in fin:
        name,data=line.split(" : ")
        data=data.split(":")[0].strip("[]").split(", ")

        src=src_dir+"completedpdb"+name.split("-")[0].lower()+".ent"
        dest=output_dir+"Input_Files/"

        shutil.copy(src,dest)
        fout.write(name+" : "+data[0]+":"+data[-1]+"\n")



    
