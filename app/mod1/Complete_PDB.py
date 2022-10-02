import os
from modeller import *
from modeller.scripts import complete_pdb

root_dir="app/mod1/"

allowed = ["ent","pdb"]

def main(uid):

    input_dir = os.path.join("uploads",uid)
    output_dir = os.path.join("output/1.0/",uid)

    for filename in os.listdir(input_dir):
        f = os.path.join(input_dir,filename)
        ext = filename.split('.')[1]
 
        if os.path.isfile(f) and ext in allowed:
            
            env = Environ()
            env.libs.topology.read('${LIB}/top_heav.lib')
            env.libs.parameters.read('${LIB}/par.lib')

            m = complete_pdb(env, f)

            m.write(file=output_dir+"completed"+filename)
