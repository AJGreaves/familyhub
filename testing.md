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
1. **Bug 1**

- details: 
    - fix:
    - 

#### Unsolved bugs

1. **Custom modal opacity issues**

    - The entire contence of my custom search modal was becoming transparent when I tried to use the opacity css property on it's container. 
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