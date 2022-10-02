import os
import shutil

def make_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
  else:
    for f in os.listdir(dir):
      os.remove(os.path.join(dir,f))

def main(obj,uid=""):

	root_dir=os.path.join("output/3.0/",uid)
	remove_dir=root_dir+"Removing Inter-Spike Pairs "+obj+"/"

	make_dir(remove_dir)

	pdb_id,asym_id=[],[]
	cur_pdb,counter=None,-1

	fin=os.path.join("output/2.0/",uid,"PDB_"+obj+".txt")
	fin=open(fin,"rt")

	for line in fin:

		temp=line.split(" ")
		try:
			pdb,asym=temp[0],temp[1][:-1]
			pdb=pdb.lower()
		except:
			continue
		
		if pdb not in pdb_id:
			cur_pdb=pdb
			counter+=1
			pdb_id.append(pdb)
			asym_id.append([])
			
		if cur_pdb==pdb:
			asym_id[counter].append(asym)
		
	input_dir = 'output'
	
	input_dir=os.path.join("output/3.0/",uid)
	input_dir=input_dir+"Splitting Chains "+obj+"/"
	
	for filename in os.listdir(input_dir):
		f = os.path.join(input_dir, filename)
		
		if os.path.isfile(f):
			core=filename.split("_")
			core=core[1].split("-")
			
			if(len(core)==3):
				index=pdb_id.index(core[0])
				
				if core[1] in asym_id[index] and core[2] in asym_id[index]:
					shutil.move(f,remove_dir)
				print(f," ",core)
