'''
Created on 11.09.2011

@author: luki
'''

import searchengine

pagelist=['http://segaran.com/wiki/Categorical_list_of_programming_languages.html']
#pagelist=['http://kiwitobes.com/wiki/Categorical_list_of_programming_languages.html']
#pagelist=['http://en.wikipedia.org/wiki/List_of_programming_languages']
crawler=searchengine.crawler('searchindex.db')

# Execute this line only if database not yet created
crawler.createindextables()

crawler.crawl(pagelist)

#print [row for row in crawler.con.execute('select rowid from wordlocation where wordid=1')]


#e=searchengine.searcher('searchindex.db')
#print e.getmatchrows('functional programming')
