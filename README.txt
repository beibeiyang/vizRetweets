Simple Visualization on Retweets

Based on the example from book Mining the Social Web, by Matthew A. Russell:
http://www.amazon.com/Mining-Social-Web-Analyzing-Facebook/dp/1449388345

Improved by Beibei Yang (byang1 @ cs.uml.edu)

Required libraries:
	- twitter (https://github.com/sixohsix/twitter/)
	- networkx (http://networkx.lanl.gov/)
	- d3 (http://d3js.org/)

vizRetweets.py  -- Main program
retweet_template.html	-- HTML template

To execute, use command-line:
	python vizRetweets.py [keyword]

For example:
	python vizRetweets.py #bigdata
	
	This will retrieve all the users on retweets that contain the #bigdata hashtag.
	
	Directory "out" will be created. Inside you would find:
		- retweets.bigdata.dot
		- retweets.bigdata.html
		- retweets.bigdata.json

	Launch out/retweets.bigdata.html in Firefox, Chrome or Safari.





