# Family Hub - Testing details

[Main README.md file](README.md)

[View website on Heroku](https://family-hub-nl.herokuapp.com/)

## Table of Contents

1. [Automated Testing](#automated-testing)
    - [Validation services](#validation-services)
    - [Jasmine](#jasmine)
    - [Python Testing](#python-testing)
2. [User Stories Testing](#user-stories-testing)
    - [Visitor Stories](#visitor-stories)
    - [Business Stories](#business-stories)
3. [Manual Testing](#manual-testing)
    - [Testing undertaken on desktop](#testing-undertaken-on-desktop)
    - [Testing undertaken on tablet and phone devices](#testing-undertaken-on-tablet-and-phone-devices)
4. [Bugs discovered](#bugs-discovered)
    - [Solved bugs](#solved-bugs)
    - [Unsolved bugs](#unsolved-bugs)
5. [Further Testing](#further-testing)

## Automated Testing

### Validation services
The following validation services and linter were used to check the validity of the website code.

- [W3C Markup Validation]( https://validator.w3.org/) was used to validate HTML.

    - **Important note** On the pages that use [Gijgo](https://gijgo.com/) date and time pickers (Add New Listing Page and Edit Listing Page), the W3c validator throws many errors to do with the html code that is inserted by Gijo.js. I have double-checked that I am using the most up to date version of Gijgo. These errors are due to code I have not written myself, and that is added when the page is rendered via the Gijgo JavaScript file. 

- [W3C CSS validation](https://jigsaw.w3.org/css-validator/) was used to validate CSS.

- [JSHint](https://jshint.com/) was used to validate JavaScript.

    - To save on loading times and to keep my JavaScript code organized I chose to break up the JS into several separate files. 
    - When running JSHint, the errors `undefined variable` and `unused variable` appear when one file either creates or uses a function that is utilized or created in another file. As validates one JS file at a time, it is not aware of the other files. 
    - To double-check that no errors occur with the entire files loaded I pasted in all the JavaScript code into JSHint and then it ran with no errors. 

- [Python extension for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python) was used to validate Python.

### Jasmine

- [Jasmine-Jquery CDN](https://github.com/velesin/jasmine-jquery) has been imported into the jasmine testing to allow for jQuery within the JavaScript functions.

The files for jasmine testing Family Hub can be found here:
- HTML page to run jasmine tests from: [jasmine-testing.html](testing/jasmine/jasmine-testing.html)
- JavaScript specifications (tests): [familyhubSpec.js](testing/jasmine/spec/familyHubSpec.js)
- Family Hub JavaScript functions to be tested are in the [js directory](static/js)
    - [common.js](static/js/common.js)
    - [date-time-pickers.js](static/js/date-time-pickers.js)
    - [filters.js](static/js/filters.js)
    - [forms.js](static/js/forms.js)
    - [index.js](static/js/index.js)
    - [listings.js](static/js/listings.js)
    - [sendemail.js](static/js/sendemail.js)

#### How to run Jasmine tests

Before going further please make sure you have already cloned this project from the [Family Hub GitHub repository](https://github.com/AJGreaves/familyhub) 
by following the steps in the [README.md](readme.md#how-to-run-this-project-locally) under "How to run this project locally" and that you have the entire project running on your own IDE.

To run the Jasmine tests: 
1. Open [jasmine-testing.html](testing/jasmine/jasmine-testing.html).
2. Run the html file and view it in your browser to see the test results. 

#### How to create Jasmine tests

To create Jasmine tests: 
1. Open the [familyhubSpec.js](testing/jasmine/spec/familyHubSpec.js) file.
2. Write your own tests using the jasmine 3.1 framework.
3. Save [familyhubSpec.js](testing/jasmine/spec/familyHubSpec.js), and then run/refresh [jasmine-testing.html](testing/jasmine/jasmine-testing.html).

### Python Testing

- Testing for my python code was run in the [test_familyhubapp.py](testing/test_familyhubapp.py) file. 
- Family Hub Python files tested
    - [app.py](app.py)
    - [helpers.py](familyhubapp/helpers.py)

#### How to run Python tests

Before going further please make sure you have already cloned this project from the [Family Hub GitHub repository](https://github.com/AJGreaves/familyhub) 
by following the steps in the [README.md](readme.md#how-to-run-this-project-locally) under "How to run this project locally" and that you have the entire project running on your own IDE.

To run the Python tests: 
1. Open [test_familyhubapp.py](testing/test_familyhubapp.py).
2. In the terminal `cd` to the correct `testing` directory then input the following command:
```
python test_familyhubapp.py
``` 
_NOTE: Your Python command may differ, such as python3 or py_ 

3. If all tests pass the terminal will simply print out `All tests passed`

### A note about TDD

This project did not utilize Test Driven Development for Jasmine or Python while it is a student project. The reason for this was that I am still very new to both JavaScript and Python and found it impossible to write tests for languages I did not understand well. 

The automated tests for this project were created after the vast majority of the project was already complete, once I had a firmer grasp of how my functions were working and what their expected output was. Now that I have a better understanding of how automated tests work, I intend to attempt TDD with my next project.

## User Stories Testing

### Visitor Stories

The following section goes through each of the user stories from the UX section of [README.md](README.md)

**As a visitor to FamilyHub I expect/want/need**

1. *To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it.*

    - The Family Hub navbar is laid out in the conventional way: 

        - Navbar is at the top of the screen.

        - The logo on the far left of the navbar and links to the home page.

        - The primary purpose of the site - the Activities page - is easily found in the navbar.

        - create account, log in links or my account dropdown links are all provided in the navbar where the user would expect to find them.

        - The navbar shows the user appropriate links depending on if they are logged in or out. 

    - The footer is also laid out in a conventional way: 

        - Contact information and links are provided in the footer.

        - A brief introduction to the goals behind the site are featured.

        - Popular links section.

        - Social media links also provided in the footer where the user would expect to find them. 

    - Everything on the site is clearly labeled, with the users journey through the site carefully considered and buttons/links provided where they would need them. 

2. *The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.*

    - On full listing pages, where all the data for the user is displayed: 

        - The page is broken up into easy to understand sections, and the data displayed in a way that is most easy to digest. 

        - Tables and icons are used where applicable, which all aid in easily accessible and digestible information for the user.

3. *The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.*

    - On search pages where multiple activities are displayed, only the most important information is provided on cards, in bite size amounts. Clear links on these cards lead the user to more information should they wish to see it. 

4. *To filter the events and activities to find the entries that are best for the age(s) of my child(ren).*

    - The filter navbar on the activities page provides multiple ways to filter results from the activities database collection.

5. *As a user who does not want to travel far for the activity I am looking for, I want to search for activities in my town.*

    - A dropdown menu allows user to filter results by town.'

6. *The site to provide easy access to the contact information, phone number, email, website, social media links, and a google map link for an activity or event I am interested in attending.*

    - All of these are provided in the listing page of each activity.

7. *As a user on a budget, I want to be able to filter results by free entry. I also want to know at which events I am allowed to bring my own food to.*
    - The Activities page provides: 

        - a filter for all database entries that have free entry.

        - A filter for all database entries that allow people to bring their own food.

8. *As a user searching for things to do on a rainy day, I want to be able to filter results for ones suitable for poor weather.*
    - The Activities page provides a filter for all database entries that are suitable for poor weather.

9. *As a parent planning a birthday party, I am looking for ideas on places to hold it. I want to be able to filter results by those that run birthday parties.*
    - The Activities page provides a filter for all database entries that host birthday parties.

10. *As a parent looking for something to do on a certain day of the week, I want to be able to filter results for which days of the week they are open.*
    - The Activities page provides filters to search for activities open on a certain day of the week, on a weekday or at the weekend.

11. *As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices. *
    - Family Hub was carefully planned and designed to be responsive and work well on mobile, tablet and desktop devices. 

12. *As a parent searching for ideas for things for my child(ren) to do, I want to be able to filter activities by categories they are interested in.* 
    - The Activities page provides a dropdown menu to choose from a range of categories and interests.

13. *As a regular user of the Family Hub website, I expect to be able to connect to their social media channels, to keep up to date with new entries on the site.* 
    - Social media links are provided on the footer of every page.

14. *As a user of Family Hub, I expect to be able to easily get in contact via a contact form.*
    - An email contact form can be found on the contact page, a link to which is in the navbar and footer on every page.

15. *As a user I expect feedback from the website I am using when I interact with it, I expect loading spinners when pages are taking a while to load, I expect pop ups and modals to inform me when my forms have been completed and sent correctly.*

    - Loading spinner runs on each page as it is loading, and also shows when the database is being accessed via `fetch` to display data on the screen.

    - Information modals are provided for every step of the site that they are needed on, which give the user feedback for correct and incorrect input or if there is an unexpected error. 

### Business Stories

**As a Business user on FamilyHub I expect/want/need**

1. *To see that the information other businesses have put on the site are being displayed in an attractive and useful way for the user.* 
    - The home page, activities page and listing pages are all attractive and easy to navigate and understand.

2. *To see that various methods of contacting my business are available to users using Family Hub.*
    - Family Hub makes it possible for businesses to enter all of the following links to their own contacts:
        - Website url
        - Email form
        - Phone number
        - Facebook url
        - Instagram url
        - Twitter url
        - Address

3. *To be able to log in to access my existing entries, and for my data to only be editable with my account.*
    - Business users can create an account and only have access to edit and delete the listings they created when logged in. 
    - When returning to the site and logging in again all their activities are saved and accessible in their account page.

4. *To create, edit and delete entries in my account.*
    - Business users have easy access to The "Add New" and "Edit" pages, and the delete button is easily accessible on the account page too. 

5. *A user interface that is simple and easy to use, that is laid out in a logical way with clear indications where necessary about the type and format of the data I need to provide.* 
    - The "Add New" and "Edit" pages have a clearly laid out and easy to understand structure to them, with alerts and messages that pop up when incorrect data has been entered. 

6. *Forms for inputting my data to make the process easy, that there is no wasting my time or making the process difficult or slow.* 
    - Though the data input for an activity is large, it is arranged in learnable small chunks that walk the user through the steps clearly. 

7. *Protections have been put in place to prevent me from accidentally deleting an activity listing.*
    - When a business user clicks the "Delete" button for one of their listings in their account page, a modal pops up asking them to confirm they want to delete this listing by typing "DELETE" into the input field. Only when the input field's value is equal to `DELETE` will the confirm delete button become clickable. Once this is clicked the request will be sent to do the database to delete that entry.
    
## Manual testing
Below is a detailed account of all the manual testing that has been done to confirm all areas of the site work as expected. 

### Testing undertaken on desktop

All steps on desktop were repeated in browsers: Firefox, Chrome and Internet Explorer and on two different desktop screen sizes.

#### Elements on every page

1. Navbar 
    - Hover over each link, confirm the hover effect works as expected. 
    - Click the **Family Hub logo**, confirm it takes the user to the home page.
    - Click the **Home** link, confirm it takes the user to the home page.
    - Click the **Activities** link, confirm it takes the user to the activities page.
    - Click the **Contact** link, confirm it takes the user to the contact page.
    - Click the **Create Account** link, confirm it takes the user to the create account page.
    - Click the **Log In** link, confirm it takes the user to the login page.
    - Log into Family hub, confirm that the navbar no longer displays the **Create Account** or **Log In** links but does now display the **My Account** dropdown menu.
    - Click the **My Listings** link, confirm it takes the user to their account page.
    - Click the **Add New** link, confirm it takes the user to the create new listing page.
    - Click the **Settings** link, confirm it takes the user to their account settings page.
    - Click the **Log out** link, confirm the user is logged out and the navbar returns to the logged out configuration.

2. Footer
    - Hover over each link, confirm the hover effect works as expected. 
    - Click the **address link**, confirm this opens a google maps link to the address in a new tab.
    - Click the **email link**, confirm this takes the user to the contact page.
    - Click the **Search Activities link**, confirm it takes the user to the activities page. 
    - Click the **Privacy Policy link**, confirm it takes the user to the privacy policy page.
    - Click the **Create an Account link**, confirm it takes the user to the add new account page.
    - Click the **Log in link**, confirm it takes the user to the log in page.
    - Click the **Facebook**, **Instagram** and **Twitter icons** and confirm they open the relevant social media pages in separate browser tabs.

3. Loading Spinner
    - Open any page and confirm that the **loading spinner** displays for 2 seconds as the page content is loaded.
    - Confirm the spinner animates as expected.

4. Floating to-top button
    - Confirm that the **to-top button** is not visible when user is at the top of the page. 
    - Scroll the page down, confirm that the button is gently animated opacity increases.
    - Confirm that as the user scrolls the button remains in the same place on the screen. 
    - Click the button, confirm the user is taken smoothly back up to the top of the page. 
    - Confirm that when back up at the top of the page, the button animates back to invisible. 

#### Home Page

1. Hero Image
    - Confirm that hero image loads at a reasonable speed, and that the image is sharp and clear. 
    - Confirm the heading for the page is easy to read.

2. Event Cards
    - View the event cards and confirm that they are all the same size.
    - Confirm the card images are loading. 
    - Confirm that the town they are based in is overlaid at the bottom right of the image.
    - Confirm the activity title is correct and displaying correctly.
    - Confirm the shadow effect on the card increases when the card is hovered over. 
    - Click in various places on the cards, confirm that the entire card is clickable to take the user to the listing page. 
    - Confirm that the link to the activities full listing page takes the user to the correct page.
    
3. Carousels
    - View the carousels and confirm that they slide a comfortable speed and interval. 
    - Hover over a carousel card, confirm that the carousel stops moving while hovered. 
    - Move mouse away from carousel, confirm that carousel starts moving again.
    - Click the carousel slide indicators below the carousels, confirm that the carousels move to match the slide selected.
    - Reload the page and confirm that the cards displayed have been randomized, and that that other listings are being shown that were not before.

4. Top Tip Feature box
    - View the Top Tip Feature box, confirm that it displays the featured activity title and first 2 paragraphs of its description correctly.
    - Hover over the box, confirm that the box-shadow hover effect increases when the box is hovered over.
    - Click the Read More link confirm it takes the user to the listing for this activity.

5. Search More buttons
    - Click each of the "Search More" buttons on the home page, confirm that they all take the user to the activities page.

#### Activities Page

- When the activities page is loaded, check what number of results displayed at the top of the page. 
- Log in and go to my account page, choose to edit one of my activities, click "preview" - which sets `{ "published": false }` on that listing, and to _not_ click to publish it on the next page. 
- Return to the activities page, confirm that the number of results displayed has dropped by one, and the activity I edited is no longer in the results show on the activities page. 
- Go back to my edited listing and publish it, confirm that this change is reflected on the activities page again.

1. Activity Cards
    - The same html code is imported using Jinja to construct these cards as is used on the home page, so testing for these is already complete. 

2. Filters
    - Click the location dropdown menu, select a town, confirm that all listings loaded are in the town selected. Repeat this action for other towns in the list.
    - Click the category dropdown menu, select a town, confirm that the listings loaded have this category selected. Repeat this action for other categries in the list.
    - Repeat this action for all the filters in the filters side navigation. 
    - Combine several filters at the same time, confirm that the results given match the filters selected. 
    - Repeat several more times with different filters. 
    - Click the "clear filters" button and confirm that it does indeed clear all filters selected.
    - Scroll page downwards, confirm that filters remain fixed to the side of the page.

3. Pagination
    - Scroll to the bottom of the page and confirm that pagination has been loaded when there are more than 12 results. 
    - Click each page in turn, confirm that the pages change and in the right order. 
    - Click the previous and next buttons in pagination, confirm that they do load the correct pages results. 
    - Filter results so there are less than 13 results, confirm that the pagination is not loaded in this case. 
    - Filter results to load around 26 listings, confirm that pagination creates 3 pages (12 listings per page)


#### Listing Page
1. Url

    - Check url for the listing page, confirm that the url includes the title of the activity, but that it has formatted as a slug. For example if the listing title is **Jungle in the library!**, the url is `https://family-hub-nl.herokuapp.com/listing/jungle-in-the-library`

2. Listing details

    - Confirm that the **title** is displaying correctly.

    - Confirm that the **listing image** has loaded correctly, and is styled with box shadow and curved corners.

    - Confirm that the **opening times** displayed are correct, and that the table is laid out in an easy to read manner. 

    - Confirm that the **dates** section of the page **is visible** for a listing that has a start and end date. And that the dates are displayed correctly (Day/Month?Year)

    - Confirm that the dates section of the page is **not visible** for a listing that has selected "ongoing" rather than start and end dates.

    - Confirm that the **ages list** is displaying as desired, that the green check marks and red crosses display on the correct selections for age range for the listing.

    - Confirm that the **address** the business user has input is displayed correctly, and that it links to the correct google maps page for that address, with a link that opens in a separate tab. 

    - Check that the **categories** displayed on the listing page correspond with the ones selected when it was created. 

    - Confirm that the correct **icons** for each categories are displaying on this page as well. 

    - In the **More Info** section, confirm that the selections chosen are displaying and that the icons with them are the relevant ones. 

    - Check that the **description** section is displaying the text supplied correctly, and that new paragraphs are started as expected. 

    - Click the **share icons** at the bottom of the page, confirm that they each in turn launch pages where the user can either post a link to the page on facebook, twitter or send the link to a friend as an email. 

    - Click the **Search More Activities** button, confirm that it takes the user back to the Activities page.

    - Confirm that the **contact links** provided on the listing page are correct. 

        - That the url to the activities **website** opens in tha new tab and leads to the correct website. 

        - That the **telephone** button when clicked will launch an application to make a phone call to that number.

        - That the **Email Organisers button** launches the email business modal

    - Email business form:

        - Confirm that the **email business modal** is launched with the business's email address in the top input field, and that this field is deactivated so the email address cannot be changed. 

        - Confirm that trying to send the form without filling out any fields causes the form to prompt the user to fill out the fields. 

        - Confirm that all fields are **required** and the form will not send without everything being filled in. 

        - Confirm that after completing the email form and submitting it that the **email sent modal** is launched. 

        - Break the email code so that the form will not send, confirm that the user is given a **error message modal** to inform them there was a problem. (fixed the code afterwards!)

        - Open an activity I created that was set up to my own email address, confirm that on sending the form I receive the email laid out as expected.

<div align="center">
<img src="https://i.ibb.co/WvRBjrS/Clipboard01.jpg" alt="Example received email" width="400px" >
</div>

#### Create Account Page

#### log In Page

#### Account settings page

#### Account page

### Testing undertaken on tablet and phone devices
All steps below were repeated to test mobile specific elements on the developers 2 Samsung phones and tablet. 
And also in the Chrome Developer Tools device simulators on all options and orientations.

### Elements on every page

1. Navbar 
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
- Despite my connection string to MongoDB working perfectly on cloud9, and other students vscode machines. If I tried to connect to it from my machine I got the following error: 
```
pymongo.errors.ConfigurationError: The DNS response does not contain an answer to the question: _mongodb._tcp.<clustername>-qtxun.mongodb.net. IN SRV
```

- multiple attempts to fix this involved: 
- checking my MongoDB password was correct (it was)
- logging my MONGO_URI connection string to the terminal to check it was coming through from the enviroment variable (it was)
- giving the connection string to another student to try on his machine (it worked fine!)
- Checking that I had installed dnsPython in both my .venv and also globally
- FIX: After a lengthy call with MongoDB customer service, the solution was to change the connection string from an SRV to the following which allowed me to connect. 
```
mongodb://<username>:<password>@<clustername>-shard-00-00-qtxun.mongodb.net:27017,<clustername>-shard-00-01-qtxun.mongodb.net:27017,<clustername>-shard-00-02-qtxun.mongodb.net:27017/test?ssl=true&replicaSet=<clustername>-shard-0&authSource=admin&retryWrites=true&w=majority
``` 


- The explanation for why this happend from MongoDB customer service was as follows: 

_The issue you encountered has to do with how your Python driver or network is resolving the DNS records in relation to the SRV string._

_The root cause could be due to an older Python version that is installed, a network environment restriction or an old pymongo version._

4. **Go back button js would not work**
- On my custom "permission denied" page, the "Go Back" button was designed to return the user to whichever page they were previously on. 
- Fix: Used an line script on the button in html.

5. **Session variable not building url as expected**
- For my logged in users I used a session variable to store their username and used this to construct urls for parts of the site they could only access when logged in.
- However I hit a problem when trying to provide the users with links to their account pages on login. 
- The reason for this was although the `session['name']` variable was assigned on login, the user was not then immediately taken to a new page, so the session variable had not existed to create the links in the modal on the same page, that loaded once login was complete. 
- To get around this problem I used JavaScript to construct the needed urls once login was complete, as the confirm login modal was launched. Using a variable returned during the fetch function. 
```JavaScript
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
- The reason for this bug was that I was looping through my activities to create my carousel, so every one of the slides had the class `.active` on them. When in order for the carousel to move this class has to be removed and applied using the bootstrap JavaScript. 
- To get around this I wrote a function to remove all but the first `.active` class from my elements with `.carousel-item` on them.
```JavaScript
document.addEventListener("DOMContentLoaded", function() {
    let slides = $('.carousel-item').not(':first');
    slides.each(function() {
        $(this).removeClass('active');
    })
});

```


7. **2nd carousel on home page refusing to display**
- This bug took hours to track down as I originally blamed it on a cursor problem with MongoDB. Of course now I am writing my bug report with the one right above it I realise now how obvious it was!! The function above also removed the "active" class from all the slides on the second carousel. 
- To fix this I adjusted my JavaScript function to be more specific to removing all but the first `.active` class from **each** one. 

8. **Pagination on click events not firing**
- A simple jQuery on-click event on my pagination links refused to fire. 
- The reason for this was that the html for pagination was inserted into the page using JavaScript after page was loaded. Which in turn meant that the event listeners were not being added to the newly inserted elements. 
- Bug was fixed by adding the onclick event in the callback right after the html for the pagination was inserted into the page. 

9. **Input URLs with http: in them threw errors in the browser**
- While I could keep all the links I put into my site to https:, I could not stop users from adding http: links to their listings. This caused the browser to throw errors. 
- Fix: To get around this I wrote a simple function to remove all http: and https: from links given, so that the links on my site always begin with the // part of the url, allowing the browser to fill in the correct https requirement. And applied this function to all urls provided by the user. 
```python
    def remove_http(url):
        url = url.replace("https:", "")
        url = url.replace("http:", "")
        return url
```

10. **Navbar display in Safari and Samsung Internet browsers**
- Bug discovered by fellow students with these browsers on their phones. Navbar was displaying squashed, the dropdown menu was underneeth the content and did not push the content down when opened as it did on other browsers.

![](https://i.ibb.co/DWcpBpK/Clipboard01.jpg)

- Several hours of debugging led to a solution by changing the navbar position property to absolute, and adding margin above the rest of my content to push it down under the navbar. 
- With this fix the content is not being pushed down when the navbar icon is clicked, I may add some JavaScript to change this later. 
```css
.navbar {
    position: absolute;
    top: 0;
    right: 0;
    left: 0;
    z-index: 1030;
}
```

#### Unsolved bugs

1. 



## Further testing: 
1. Asked fellow students, friends and family to look at the site on their devices and report any issues they found.
2. FamilyHub viewed on all devices and orientations available in Chrome DevTools, as well at a local tech store.
