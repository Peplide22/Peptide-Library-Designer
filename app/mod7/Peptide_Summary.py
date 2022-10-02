import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(uid):

    input_dir=os.path.join("output/6.0/",uid)

    output_dir=os.path.join("output/7.0/",uid)
    make_dir(output_dir)
    fout=open(output_dir+"All_peptides_summary.txt","wt")

    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir,filename)
        
        if os.path.isfile(f):
            fin=open(f,"rt")
            name=filename.split("_")[1]

            for line in fin:
                fout.write(name+" : "+line)