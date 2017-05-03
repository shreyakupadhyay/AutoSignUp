# AutoSignUp
This repo tells a workflow of how to get into websites using fake mails and extracting data from those websites using there cookies.
## Workflow
- **First Step** Generating a fake mail using [Fake Mail Generator](http://www.fakemailgenerator.com/) and using this mail to signup for the target website. Defined in file (stepwise/generateFakeMail)
- **Second Step** SignUp for the target website using the fake email ID generated in the previous step. Put all the *required parameters* and make a post request to get the authentication mail from the target website to you fake email ID. Defined in file (stepwise/getAuthMail)
- **Third Step** Read the mail in your fake inbox using regex and BeautifulSoup and parsing them with lxml to get the link of confirmation url. Defined in file (stepwise/getAuthMailContent)
- **Fourth Step** Use the confirmation link from the previous step and send a get request using the link. This will redirect you to a different path on the target website. Use cookies and headers and finally you are in. Defined in file (stepwise/getVerifiedLoggedIN)
- All these step are properly defined and implemented in the structure of authentication folder in the repo. I have implemented this for several website. **(BUT THAT IS A SECRET IF I TELL YOU I WILL BECOME A SECRET)**

## Requirements
- **Python3** Use python3 for the whole process as in case of website which are encrypted with https you do not have to give path to the SSL certificated seperately as this is automatically done by python3 which was not there in the previous versions of python.
- **Selenium** If you want to generate mails with a script of library use selenium otherwise doing manully is also good when you are not planning to make a huge lose to the website.
- **Regex** Regular expressions use **re** library for python to use regex
- **BeautifulSoup** Use beautifulSoup for parsing the data and this uses lxml as a parser engine.


## Suggestions 
- To get the workflow of a target website first look all these step using a web browser rather then imnplementing it directly.
- Be careful about the legal issues of the target website otherwise you will be in trouble unless you can deal with these things.

