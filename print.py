import struct
print 'print info of label'
f1=open('/home/lipeiyang/code/islabel/undirected_version/example.bin.label','r')
for i in xrange(2):
	print '--------------'
	u,=struct.unpack('i',f1.read(4))
	deg,=struct.unpack('i',f1.read(4))
	print u
	print deg

	for i in xrange (0,deg):
		nodeid,=struct.unpack('I',f1.read(4))
		weight,=struct.unpack('B',f1.read(1))
		print 'nodeid='+str(nodeid),'weight='+str(weight)
	print '************************'
f1.close()

print 'print info of graph_gk'
f2=open('/home/lipeiyang/code/islabel/undirected_version/example.bin.info','r')
nGraph,=struct.unpack('i',f2.read(4))
max_node_m,=struct.unpack('i',f2.read(4))
max_edge_m,=struct.unpack('i',f2.read(4))
max_label_m,=struct.unpack('i',f2.read(4))
print 'nGraph',nGraph,'max_node_m',max_node_m,'max_edge_m',max_edge_m,'max_label_m',max_label_m
f2.close()

print 'print offset of graph vertex'
f3=open('/home/lipeiyang/code/islabel/undirected_version/example.bin.offset','r')
for j in xrange(5):
	offset,=struct.unpack('q',f3.read(8));
	print offset,  
f3.close()
