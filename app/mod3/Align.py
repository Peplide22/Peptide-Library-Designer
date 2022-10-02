import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
  else:
    for f in os.listdir(dir):
      os.remove(os.path.join(dir,f))

def split_chains(split_dir,line,vard,atomtyped,vari):
       
  fout = open(split_dir+"selected_"+vard+"-"+atomtyped+"-"+vari+"_.txt", "a")
  fout.write(line)

def main(obj,uid=""):

  input_dir=os.path.join("output/2.0/",uid)
  input_dir=input_dir+"output_"+obj+"/"

  root_dir=os.path.join("output/3.0/",uid)
  
  align_dir=root_dir+"Alignment "+obj+"/"
  split_dir=root_dir+"Splitting Chains "+obj+"/"

  make_dir(align_dir)
  make_dir(split_dir)

  count=0
  for filename in os.listdir(input_dir):

    print(count," ",filename)
    count+=1
    
    f = os.path.join(input_dir, filename)
    aout = os.path.join(align_dir, filename.replace("outdis","final"))

    filename=filename.split('.')[0]

    if os.path.isfile(f):
      fin=open(f,"rt")
      aout=open(aout,"wt")

      vard,atomtyped=filename.split("_")[1:]
      print(vard,atomtyped)

      for line in fin:
        var,gar,atomtype=line.split("\t")

        if gar.split(":")[3] == atomtyped:
          line= gar+'\t'+var+'\t'+atomtype
          gar=var

        vari=gar.split(":")[3]
        split_chains(split_dir,line,vard,atomtyped,vari)
    
        aout.write(line)

if __name__=="__main__":
  main("67")
  main("133")