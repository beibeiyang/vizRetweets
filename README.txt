Simple Visualization of users who retweet on a specific keyword

Copyright (c) 2012-2014 Beibei Yang <byang1@cs.uml.edu>

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.


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




