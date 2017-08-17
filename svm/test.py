import svm

f=open('./log_100w.pick','r')
g=open('feature','w')
features=[[]]
lines=f.readlines()
a=['4gbizhi.com', '1', '600', '2', '86400', '2', '171155', '1', '2.68804916084', '0.441095890411', 11.0, 0.0, 2.2718685126965625, 0.0, 0.0, 1.0, 0.09090909090909091, 0.09090909090909091, 0.0, 0.0, 1.0, 6.0, 1.0]
for i in xrange(len(lines)):
    if features==[[]]:
        features[0]=lines[i].rstrip('\t\n').split('\t')[0:9]
        for j in svm.get_feature(features[0][0]):
            features[0].append(j)
    else:
        features.append(lines[i].rstrip('\t\n').split('\t')[0:9])
        for j in svm.get_feature(features[i][0]):
            features[i].append(j)
    print features[i]
    for j in xrange(len(features[i])):
        g.write(str(features[i][j]))
        g.write('\t')
    g.write('\n')

f.close()
g.close()

