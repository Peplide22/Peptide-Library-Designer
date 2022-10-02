fin = open("67_Output.txt", "rt")
fout = open("getup.txt", "wt")

for line in fin:
        
        if(len(line)>6):
                       fout.write(line)
	
