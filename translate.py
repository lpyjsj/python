
f1= open('D:\\networkx\DB\IS.txt', 'r')
f2 = open('C:\Users\LPY\Desktop\IS.txt', 'w')

for line in f1.readlines():

	# line=line.split(',')
 # 	for j in xrange(0,len(line)):
 #  		f2.write(str(line[j])+" "),
 	f2.write(line.strip()+",1\n") 	


# print "##"
f1.close()   
f2.close()


