'''
Created on 25.08.2011

@author: Luki
'''
import clusters
import os

if not os.path.isfile('blogdata.txt'):
    execfile("generatefeedvector.py")

blognames,words,data = clusters.readfile('blogdata.txt')
clust= clusters.hcluster(data)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')
print 'Finished drawing dendrogram!'

