'''
Created on 25.08.2011

@author: Luki
'''
import clusters
import os

# run 2 times if error occurs

# generate dataset from blogs and save it to a file
if not os.path.isfile('blogdata.txt'):
    execfile("generatefeedvector.py")

# read the dataset from the file
blognames,words,data = clusters.readfile('blogdata.txt')

# generate hierarchical cluster
clust=clusters.hcluster(data)
clusters.printclust(clust,labels=blognames)
clusters.drawdendrogram(clust,blognames,jpeg='blogclust.jpg')
 
 # rotate the matrix and generate hierarchical cluster
rdata = clusters.rotatematrix(data)
wordclust=clusters.hcluster(rdata)
clusters.drawdendrogram(wordclust,labels=words,jpeg='wordclust.jpg')

# generate k-means cluster
kclust=clusters.kcluster(data,k=10)
print [blognames[r] for r in kclust[1]]      

# test of BeautifulSoup API
execfile("beautifulsouptest.py")

# Generate a hierarchical cluster of data that contains only 0 and 1
# zebo doesn't exist anymore so use the 'zebo.txt' from http://kiwitobes.com/PCI_Code.zip
wants,people,data=clusters.readfile('zebo.txt')
clust=clusters.hcluster(data,distance=clusters.tanimoto)
clusters.drawdendrogram(clust,wants,'zebo.jpg')
