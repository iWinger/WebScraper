# WebScraper
##**Instructions**
*Python version should be of the newer releases (such as 3.7.1/3.7.2/3.7.3)*
*We tested it on Windows, and Python should be of 64-bit architecture.*
*No requirements.txt is needed since the modules is already downloaded in the virtual environment (but must have Python)*

###How to Test
Download the project, and go to ../WebScraper/venv/Lib/site-packages using Command Prompt
Inside the site-packages directory, use the command **python web.py**
What this does is starts a Flask app and gives a link to **localhost**

###Why localhost?
-We tried hosting it on the website using Amazon AWS Elastic Beanstalk and many other sites, but the problem is the request 
for Amazon products is giving too much strain on our server, thus causing it to crash. We tested it with scraping and request the quotes website in a similar fashion with no problem; thus we determined that our coding was not an issue, but rather the server's.
-However, we did put it on a website, but please try everything else before going to the **price page**
-Just to cover all avenues, we put a video for you guys to see how it works on localhost, but not on the website.

We really worked hard on this project, and we hope you enjoy this!

####Extra
-> The python files are in the scraper folder
-> HTML files (with in-line CSS and in-line JS) are in templates
-> Picture in the static folder
-> All are in **site-packages**




