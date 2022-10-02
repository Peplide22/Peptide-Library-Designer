import os

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)

def main(uid):

    input_dir=os.path.join("output/5.0/",uid)

    output_dir=os.path.join("output/6.0/",uid)
    make_dir(output_dir)

    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir,filename)
        
        if os.path.isfile(f):
            fin=open(f,"rt")
            txt=""

            k=list(map(int,fin.read().split(",")))
          
            counter,i=0,0        

            for j in range(1,len(k)):

                # print(k[j],k[j-1],counter,i,j)

                if(k[j]-k[j-1]<=3):
                    counter=counter+k[j]-k[j-1]-1

                    if(j==len(k)-1):
                        j+=1
                        txt=txt+str(k[i:j])+":"+str(j-i)+":"+str(counter+j-i)+":"+str(counter)+"\n"
                
                else:
                    if(j-i>5):
                        txt=txt+str(k[i:j])+":"+str(j-i)+":"+str(counter+j-i)+":"+str(counter)+"\n"
                  
                    i,counter=j,0

            if(txt!=""):
                fout=open(output_dir+"output_"+filename,"wt")
                fout.write(txt)

                
