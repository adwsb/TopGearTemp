Python Assignment
(Solved using Python 2.7)
========================================================================================================================
1. Given a list, url = [www.annauniv.edu, www.google.com, www.ndtv.com, www.website.org, www.bis.org.in, www.rbi.org.in]; 
Sort the list based on the top level domain (edu, com, org, in) using custom sorting
========================================================================================================================

topDomainList=["edu","com","org","in"]
urlList = ["www.annauniv.edu", "www.google.com", "www.ndtv.com", "www.website.org", "www.bis.org.in", "www.rbi.org.in"]

def sortDomainNames(domainList,urlList):
	tempDomainList = domainList
	tempUrlList = urlList
	sortedUrlList = []
	
	for i,v in enumerate(tempDomainList):
		for i1,v1 in enumerate(tempUrlList):
			if v1.endswith(v):
				sortedUrlList.append(v1)

	print sortedUrlList


sortDomainNames(topDomainList,urlList)
