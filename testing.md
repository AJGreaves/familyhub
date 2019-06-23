# Family Hub - Testing details

[Main README.md file](README.md)

[View website on Heroku](#)

## Table of Contents

1. [**Automated Testing**](#automated-testing)
    - [**Validation services**](#validation-services)
    - [**Jasmine**](#jasmine)
2. [**Client Stories Testing**](#client-stories-testing)
3. [**Manual Testing**](#manual-testing)
    - [**Testing undertaken on desktop**](#testing-undertaken-on-desktop)
    - [**Testing undertaken on tablet and phone devices**](#testing-undertaken-on-tablet-and-phone-devices)
4. [**Bugs discovered**](#bugs-discovered)
    - [**Solved bugs**](#solved-bugs)
    - [**Unsolved bugs**](#unsolved-bugs)
5. [**Further Testing**](#further-testing)

## Automated Testing

### Validation services
The following validation services and linter were used to check the validity of the website code.
- [W3C Markup Validation]( https://validator.w3.org/) was used to validate HTML.
- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.
- [JSHint](https://jshint.com/) was used to validate JavaScript.

### Jasmine

[Jasmine-Jquery CDN](https://github.com/velesin/jasmine-jquery) has been imported into the jasmine testing to allow for jQuery within the JavaScript functions.

The files for jasmine testing Family Hub can be found here:
- HTML page to run jasmine tests from: [jasmine-testing.html](assets/jasmine-testing/jasmine-testing.html)
- JavaScript specifications (tests): [familyhubSpec.js](assets/jasmine-testing/spec/familyhubSpec.js)
- Family Hub JavaScript functions to be tested: [familyhub.js](assets/js/familyhub.js)

#### How to run jasmine tests

Before going further please make sure you have already cloned this project from the [PicFlip GitHub repository](https://github.com/AJGreaves/familyhub) 
by following the steps in the [README.md](readme.md) under "How to run this project locally" and that you have the entire project running on your own IDE.

To run the jasmine tests: 
1. Open the [jasmine-testing.html](assets/jasmine-testing/jasmine-testing.html).
2. Run the html file and view it in your browser to see the test results. 

#### How to create jasmine tests

To create jasmine tests: 
1. Open the [familyhubSpec.js](assets/jasmine-testing/spec/familyhubSpec.js) file.
2. Write your own tests using the jasmine 3.1 framework.
3. Save [familyhubSpec.js](assets/jasmine-testing/spec/familyhubSpec.js), and then run/refresh [jasmine-testing.html](assets/jasmine-testing/jasmine-testing.html).

## Client stories testing

The following section goes through each of the user stories from the UX section of [README.md](README.md)

**As a user I want**

1. **User story 1**

    - list items here
    
## Manual testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

1. first site feature
    - List items here

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile specific elements on the developers 2 Samsung phones and tablet. 
And also in the Chrome Developer Tools device simulators on all options and orientations.

1. first site feature
    - List items here


### Bugs discovered: 
#### Solved bugs

1. **Custom modal opacity issues**

    - The entire contents of my custom search modal was becoming transparent when I tried to use the opacity css property on it's container. 
    - To solve this I switched to using rgba values instead, which have built in transparency but do not effect any further elements contained within. 
```css
#search-modal {
    height: 100vh;
    width: 100vw;
    position: fixed;
    z-index: 100;
    bottom: 0; 
    right: 0; 
    /* 
    I stopped using the following code, 
    and replaced it with the code below it:
    background-color: black;
    opacity: 0.4;
    */
    background-color: rgba(0,0,0,0.4);
}
```

2. **pylinter on vscode causing errors**
- Trying to import one py file into another was throwing confusing errors, running only once and then refusing to work again.
- Fix: installed pylint-flask and the pylinter started working correctly again.

3. **Connection issues with vscode to MongoDB**
- Despite my connection string to mongodb working perfectly on cloud9, and other students vscode machines. If I tried to connect to it from my machine I got the following error: 
```
pymongo.errors.ConfigurationError: The DNS response does not contain an answer to the question: _mongodb._tcp.<clustername>-qtxun.mongodb.net. IN SRV
```

- multiple attempts to fix this involved: 
- checking my mongodb password was correct (it was)
- logging my MONGO_URI connection string to the terminal to check it was coming through from the enviroment variable (it was)
- giving the connection string to another student to try on his machine (it worked fine!)
- Checking that I had installed dnspython in both my .venv and also globally
- FIX: After a lengthy call with MongoDB customer service, the solution was to change the connection string from an SRV to the following which allowed me to connect. 
```
mongodb://<username>:<password>@<clustername>-shard-00-00-qtxun.mongodb.net:27017,<clustername>-shard-00-01-qtxun.mongodb.net:27017,<clustername>-shard-00-02-qtxun.mongodb.net:27017/test?ssl=true&replicaSet=<clustername>-shard-0&authSource=admin&retryWrites=true&w=majority
``` 


- The explanation for why this happend from MongoDB customer service was as follows: 

_The issue you encountered has to do with how your python driver or network is resolving the DNS records in relation to the SRV string._

_The root cause could be due to an older python version that is installed, a network environment restriction or an old pymongo version._

4. **Go back button js would not work**
- On my custom "permission denied" page, the "Go Back" button was designed to return the user to whichever page they were previously on. 
- Fix: Used an line script on the button in html.

5. **Session variable not building url as expected**
- For my logged in users I used a session variable to store their username and used this to construct urls for parts of the site they could only access when logged in.
- However I hit a problem when trying to provide the users with links to their account pages on login. 
- The reason for this was although the `session['name']` variable was assigned on login, the user was not then immediately taken to a new page, so the session variable had not existed to create the links in the modal on the same page, that loaded once login was complete. 
- To get around this problem I used javascript to construct the needed urls once login was complete, as the confirm login modal was launched. Using a variable returned during the fetch function. 
```javascript
function openLoggedInModal(username) {
  let name = capFirst(username);
  $("#accountUrl").attr("href", `/editor/account/${username}`)
  $("#newEventUrl").attr("href", `/editor/${username}/add-new-event`)
  $("#newActivityUrl").attr("href", `/editor/${username}/add-new-activity`)
  $('#welcomeMessage').text('Welcome ' + name + '.');
  $('#loggedInModal').addClass('active');
}
  ```
  
6. **Carousel on home page not moving**
- The reason for this bug was that I was looping through my activities to create my carousel, so every one of the slides had the class `.active` on them. When in order for the carousel to move this class has to be removed and applied using the bootstrap javascript. 
- To get around this I wrote a function to remove all but the first `.active` class from my elements with `.carousel-item` on them.
```javascript
document.addEventListener("DOMContentLoaded", function() {
    let slides = $('.carousel-item').not(':first');
    slides.each(function() {
        $(this).removeClass('active');
    })
});

```


7. **2nd carousel on home page refusing to display**
- This bug took hours to track down as I originally blamed it on a cursor problem with mongoDB. Of course now I am writing my bug report with the one right above it I realise now how obvious it was!! The function above also removed the "active" class from all the slides on the second carousel. 
- To fix this I adjusted my javascript function to be more specific to removing all but the first `.active` class from **each** one. 

#### Unsolved bugs

1. 



## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. FamilyHub viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.

### A note to my fellow Code Institute students

I am happy that you have come to look at my testing.md file as an example 
of how to write a good one for your second Milestone project. 
You are welcome to learn how to structure and format your own testing.md from mine.

However, it is not ok to copy and paste large portions of it into your own project. 
Please remember to write your own, rather than copying mine or someone elses.

Many thanks! Anna