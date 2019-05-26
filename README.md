# WebScraper
##**Instructions**
*Must have Python and version should be of the relatively newer releases (such as 3.7.1/3.7.2/3.7.3)*
*We tested it on Windows, and our Python was of 64-bit architecture.*


###How to Test
Download the project, and go inside the folder where all the files are
*Use cd to navigate through command prompt or git bash to the folder and use the following commands*
Inside the directory, you need the modules from requirements.txt so run: **python -m pip install -r requirements.txt** 
Then, use the command **python web.py**
What this does is starts a Flask app and gives a link to **localhost**

###Why localhost?
-We tried hosting it on the website using Amazon AWS Elastic Beanstalk and many other sites, but the problem is the request 
for Amazon products is giving too much strain on our server, thus causing it to crash. We tested it with scraping and request the quotes website in a similar fashion with no problem; thus we determined that our coding was not an issue, but rather the server's.
-However, we did put it on a website, but please try everything else before going to the **price page**
-Just to cover all avenues, we put a video for you guys to see how it works on localhost, but not on the website.

We really worked hard on this project, and we hope you enjoy this!

Websites we scraped (either there was permission / we followed the robots.txt so we didn't break any rules):
http://quotes.toscrape.com/
https://www.amazon.com/s?k=computer/

####Extra
-> The python files are in the scraper folder
-> HTML files (with in-line CSS and in-line JS) are in templates
-> Picture in the static folder
-> All are in **site-packages**

Our test login for the flask app / website is:
Username: Test123
Password: Testing123
-Thank you


