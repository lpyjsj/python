
f1= open('C:\Users\LPY\Desktop\in.txt', 'r')
f2 = open('C:\Users\LPY\Desktop\out.txt', 'w')

for i in xrange(1,8):
 line = f1.readline()
#print type(line)
#print line
 line=line.split(' ')
 for j in xrange(0,len(line)):
 	if(j!=0):
 		 #f2.write(str(i)+str(j)+","+line[j]+"\n");
 		 f2.write("{id:"+str(i)+str(j)+",pId:"+str(i)+", name:\""+line[j]+"\"},\n")
 		 f2.write("{id:"+str(i)+str(j)+"1,pId:"+str(i)+str(j)+", name:\"abc\"},\n")
 		 f2.write("{id:"+str(i)+str(j)+"3,pId:"+str(i)+str(j)+", name:\"xyz\"},\n")
 		 f2.write("{id:"+str(i)+str(j)+"4,pId:"+str(i)+str(j)+", name:\"def\"},\n")
 		 f2.write("{id:"+str(i)+str(j)+"5,pId:"+str(i)+str(j)+", name:\"mnq\"},\n")
  	else:
  	  	f2.write("{id:"+str(i)+",pId:"+str(i)+", name:\""+line[j]+"\"},\n")


		 

# print "##"
f1.close()   
f2.close()


