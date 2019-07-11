<div align="center">
    <img src="https://i.ibb.co/Pm36prG/fh-logo-readme.png" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Family Hub Logo" aria-label="Family Hub Logo" />
    <img src="https://i.ibb.co/Pj9RZW5/tagline.png" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Family events and activities for kids in Haarlemmermeer" aria-label="Family events and activities for kids in Haarlemmermeer" />
</div> 

<div align="center">
    <img src="https://i.ibb.co/CBw04v7/home.jpg" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>

## Introduction

[Family Hub](http://family-hub-nl.herokuapp.com) was created by Anna Greaves, to serve the English speaking international community of families living in the Haarlemmermeer area of The Netherlands. 

As a British mother of two, who moved to The Netherlands in 2003, I know what a difference it makes to newcomers to a country to be able to get out and connected to the community around. The Family Hub goal is to inform and connect English speaking families to the events and activities available in their local area.

## Table of Contents
1. [UX](#ux)
    - [Goals](#goals)
        - [Visitor Goals](#visitor-goals)
        - [Business Goals](#business-goals)
        - [Family Hub Goals](#family-hub-goals)
    - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Design Choices](#design-choices)
    - [Wireframes](#wireframes)
    - [Flowcharts](#flowcharts)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)

4. [Technologies Used](#technologies-used)

5. [Testing](#testing)

6. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [How to run this project locally](#how-to-run-this-project-locally)

7. [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
    - [Code](#code)
    - [Acknowledgements](#acknowledgements)

8. [Contact](#contact)

9. [Disclaimer](#disclaimer)

----

## UX

### Goals

#### Visitor Goals

The central target audience for Family hub are:
- Families with children aged 14 and under.
- English speaking.
- Moved to The Netherlands less than 3 years ago.
- Live in or around the Haarlemmermeer area of The Netherlands.

User goals are:

- Have somewhere to search for events in my local area, that offers its listings in English as my Dutch is not strong enough to understand the sites in Dutch.

- Get out of the house in this new country I have moved to, find things to do with my kids. 

- Have the confidence to start exploring the events in my new home, because I have been better informed in a language I understand.

A few of the possible goals users might have: 
- Find an after school activity for my child to enjoy.
- Find swimming lessons for my 5yo son. 
- Find something to do with my kids this weekend. 
- Find out about upcoming events I might be interested in attending.
- Find family friendly music festivals to attend this summer.
- Find things to fill the kids summer holidays up with.
- Find summer camps to occupy my kids in the holidays while I work.
- Find all the events in my town.
- Find art lessons for my daughter. 
- Find dance lessons for my son.
- Find technology themed courses for my child. 
- Get new ideas on where to celebrate my child's birthday party this year.
- Find my local sports centres for kids activities. 
- Find out if there is a kids pony club near me. 
- Find activities for my pre-school child. 
- Find free family events in my local area.

FamilyHub is a great way to meet these user needs because:

- There are no other websites offering event and activity information in English outside of the city of Amsterdam. 

- As a part of the community I want to serve, I understand the needs and wants of the users of my website well.

- The design of this site fits the conventions of similar sites, and lays out the information in a user friendly and accessible way.

- The Family Hub activities page allows users to search by location, category, age range, days of the week open, indoor or outdoor as well as a few other possible options.

#### Business Goals

The target businesses to use Family Hub to advertise:
- Provide family events or activities for kids.
- Are located in the Haarlemmermeer area.
- Want to reach a wider audience to attend their events / activities. 
- Are welcoming to international families. 

Business user goals are:

- A well thought-out, well designed, user-friendly platform that will benefit my business to advertise on.

- A user interface that is user friendly for me to input my data easily and efficiently. 

- Value for money (at the moment the website is a student project, but eventual planning is to monetise this site, so it is worth adding this important goal here now.)

FamilyHub is a great way to meet these user needs because:

-  The user interface for inputting activity data has been carefully controlled to validate input and make sure what is provided fits the needs of the database structure. For example date pickers have been used to make sure input dates fit the correct format, and the user cannot click on anything but the date picker in order to add a date. Time pickers have also been used, and well as setting input field types to `email`, `number`, `url` etc makes sure the user is prompted when the data they provide is incorrect. 

- The editor page is clearly structured and laid out in a simple and easy to understand way. 

- The editor has a preview page in it so the user can see how their activity will look on the site before it has been published, and gives them the opportunity to go back and make changes if they wish. 

- The account page for the business user shows all their existing listings and gives them the option to view, edit or delete them from this location. 

- The users needs on each page have been thought about and buttons provided for these paths through the site, to make navigating easy.

#### Family Hub Goals

- Provide an effective, easy to use site for English speaking international families to search and filter through entries to find the listings that suit their needs.

- So that I can learn and practice frontend and backend programming together for the first time. To combine the use of HTML, CSS, Bootstrap and JavaScript with Python, MongoDB, Flask and Jinja.

- While this is currently a student project, the future goal of Family Hub to monetise the website to charge businesses for advertising their events and activities on it. This will come later once the site has a few more features to offer those who use it (see [Features Left to Implement](#features-left-to-implement)).

----

### User Stories

#### Visitor Stories

As a visitor to FamilyHub I expect/want/need:

1. To easily find what I am looking for, I want the layout of the site to make sense so I am not confused or put off using it. 

2. The information I am presented with to be laid out in a way that is easy for me to navigate and digest, so that I find what I need quickly and efficiently.

3. The ability to search through small amounts of information to find what I need, and then be able to easily click to get more detailed information when I need it.

4. To filter the events and activities to find the entires that are best for the age(s) of my child(ren).

5. As a user who does not want to travel far for the activity I am looking for, I want to search for activities in my town.

6. The site to provide easy access to the contact information, phone number, email, website, social media links, and a google map link for an activity or event I am interested in attending. 

7. As a user on a budget, I want to be able to filter results by free entry. I also want to know at which events I am allowed to bring my own food to.

8. As a user searching for things to do on a rainy day, I want to be able to filter results for ones suitable for poor weather.

9. As a parent planning a birthday party, I am looking for ideas on places to hold it. I want to be able to filter results by those that run birthday parties. 

10. As a parent looking for something to do on a certain day of the week, I want to be able to filter results for which days of the week they are open.

11. As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices. 

12. As a parent searching for ideas for things for my child(ren) to do, I want to be able to filter activities by categories they are interested in. 

13. As a regular user of the Family Hub website, I expect to be able to connect to their social media channels, to keep up to date with new entires on the site. 

14. As a user of Family Hub, I expect to be able to easily get in contact via a contact form.

15. As a user I expect feedback from the website I am using when I interact with it, I expect loading spinners when pages are taking a while to load, I expect pop ups and modals to inform me when my forms have been completed and sent correctly.

----

#### Business Stories

As a Business advertising on FamilyHub I expect/want/need:
1. To see that the information other businesses have put on the site are being displayed in an attractive and useful way for the user. 

2. To see that various methods of contacting my business are available to users using Family Hub. 

3. To be able to log in to access my existing entries, and for my data to only be editable with my account.

4. To create, edit and delete entries in my account.

5. A user interface that is simple and easy to use, that is laid out in a logical way with clear indications where necessary about the type and format of the data I need to provide. 

6. Forms for inputting my data to make the process easy, that there is no wasting my time or making the process difficult or slow. 

----

### Design Choices

The Family Hub website has an overall family friendly feel, with emphasis on providing complex information in a bite size, learnable format. The following design choices were made with this in mind:

#### Fonts

- The primary font `News Cycle` was chosen for the main text of the site because it is easy to read and complements the fonts chosen for titles very well. A extra reason for picking this font is that it is still easy to read when printed small, and as this site provides a large amount of information, using a smaller font is occasionally necessary.

- The secondary font `Delius` was chosen for the main headings because it resembles simple clear handwriting that a parent or teacher might use when teaching a child. The font has a personal feel to it, and when combined with the colours chosen for this project, refers well to families. Being a cursive font it complements in the main sans-serif type font very well from a design perspective

- The tertiary font `Patrick Hand SC` was chosen for its contrast with the two main fonts. Only used in a handful of places across the site, it brings a little extra flavour to the fonts while not overwhelming the user with too many. 

---

#### Icons

![Example listing page with icons](https://i.ibb.co/hXkxsM1/Clipboard01.jpg)

- It is important to use icons on the Family Hub website for three main reasons:

    1. The site shares a lot of different information about each activity listed on it. Icons help the user to identify the parts of the information that is relevant to their needs much faster. 

    2. Icons break up the information visually, creating space for the user and not overwhelming them with too much info at once. 

    3. The international community in The Netherlands is made up of people from many other countries, and often English is their 2nd or 3rd language. Providing information to them in a visual way as well as in English enhances these users ability to understand the site even when their English is not very strong (though likely stronger than their Dutch).

- Each icon was chosen for it's clarity in quickly explaining the relavent meaning with an image. 

- Icons are most used on the individual listing pages for each activity. And were also added to the navigation bar as well. 

- Social media icons for facebook, instagram and twitter are used in 3 places on the site. 

    1. In the footer, to link to the social media outlets for Family Hub. these links do not yet exits, so currently the icons link to the main pages for each social media network.

    2. On each listing page for any links provided by the organizers to their events and activities. 

    3. At the bottom of each activity page with a link to share that page on each of the social media platforms. (does not include instagram, but does include an icon to email the page instead).

---

#### Colours
<div align="center">
    <img src="https://i.ibb.co/4Z8xPnT/colours.jpg" alt="Family Hub Brand Colours" aria-label="Family Hub Logo" />
</div>
- The colours chosen for this project were picked for their colorful feeling, which references to family well, while still choosing tones and shades that worked well together without overwhelming the eyes. 

- Colorful highlights that draw the eye to headings are provided by the terracotta colour, which is accented with the light blues in horizontal lines and links. 

- A dark navy blue was chosen for the main text as it contrasts with the white background clearly. 

- The navbar background colour is a classy platinum colour, light enough to provide contrast with the navy blue headings, while still setting itself apart from the white background in the main content.

- In the footer a darker shade of greenish-blue provides the background, setting the footer apart from the rest of the content and making it dark enough that the text can be in white and still have enough contrast to be easily readable. 

- The same darker green-blue is used for the filters bar on the activities page. Green-blue is a colour for outdoors, adventure and learning, so was a good choice for the feeling of this website. 

#### Styling

- Spinner 
- buttons and readmore links
- cards (town overlays)
- images (curved corners, shadows)
- tables
- hover effects

### Wireframes

These wireframes were created using [Balsamiq](https://balsamiq.com/) during the Scope Plane part of the design and planning process for this project. 

- [Home](https://ibb.co/52Z3P4r)
- [Search](https://ibb.co/Wcgbtqs)
- [Activity search](https://ibb.co/Nm8FYbd)
- [Activity listing](https://ibb.co/PMb9jCm)
- [Event search](https://ibb.co/MR8BFC3)
- [Event listing](https://ibb.co/njnP5C5)
- [Create or Edit account](https://ibb.co/1TyV9sN)
- [Log in](https://ibb.co/yhbBSV0)
- [My account](https://ibb.co/nr2s9cw)
- [Create or Edit Activity page](https://ibb.co/Wv349RB)
- [Create or Edit Event page](https://ibb.co/sqj60xb)

#### Flowcharts 

- This flowchart was created to plan and explain the flow of behavior between the user, javascript, data and the modal messages the user sees based on their interactions.
- [Account and login pages flowchart](https://i.ibb.co/x1wxDsZ/flowchart.jpg)

---

## Features
 
### Existing Features

---

#### Elements on every page
- Navbar
- Footer
- To top button

#### Home page

<div align="center">
<img src="https://i.ibb.co/CBw04v7/home.jpg" alt="Family Hub home page on all major screen sizes" >
</div>

---

#### Activities page

<div align="center">
<img src="https://i.ibb.co/yN750bS/activities.jpg" alt="Family Hub activities page on all major screen sizes" >
</div>

---

#### Listing page

<div align="center">
<img src="https://i.ibb.co/LpNYVZJ/listing.jpg" alt="Family Hub listing page on all major screen sizes" >
</div>

---

#### Create account page

<div align="center">
<img src="https://i.ibb.co/qkw56D6/createaccount.jpg" alt="Family Hub create account page on all major screen sizes" >
</div>

---

#### log in page

<div align="center">
<img src="https://i.ibb.co/dpzR69j/login.jpg" alt="Family Hub log in page on all major screen sizes" >
</div>

---

#### Account settings page

<div align="center">
<img src="https://i.ibb.co/f4bgHRp/settings.jpg" alt="Family Hub account settings page on all major screen sizes" >
</div>

---

#### Account page

<div align="center">
<img src="https://i.ibb.co/2qfkKFx/account.jpg" alt="Family Hub account page on all major screen sizes" >
</div>

---

#### Add new listing page

<div align="center">
<img src="https://i.ibb.co/t2S8cyr/addnew.jpg" alt="Family Hub add new listing page on all major screen sizes" >
</div>

---

#### Preview listing page

<div align="center">
<img src="https://i.ibb.co/2MTLzKk/preview.jpg" alt="Family Hub preview listing page on all major screen sizes" >
</div>

---

#### Edit listing page

<div align="center">
<img src="https://i.ibb.co/MR6nKp7/edit.jpg" alt="Family Hub edit listing page on all major screen sizes" >
</div>

---

#### Contact page

<div align="center">
<img src="https://i.ibb.co/hFHp8x9/contact.jpg" alt="Family Hub contact page on all major screen sizes" >
</div>

---

#### 404 page

<div align="center">
<img src="https://i.ibb.co/4Kz1Mp7/404.jpg" alt="Family Hub 404 page on all major screen sizes" >
</div>

---

#### Permission Denied page

<div align="center">
<img src="https://i.ibb.co/M6FkQhZ/denied.jpg" alt="Family Hub permission denied page on all major screen sizes" >
</div>

---

### Features Left to Implement

1. Email authentication
    - Implementation of email authentication of user account before registration complete
2. Full text search
    - Attempted this for several days but was unable to get it to work. Rather than dragging out time on this feature when this project is already very large, I made the decision to remove the relevant code to return to at a future date when my understanding is more advanced. 
    - When returning to this feature, the text search related code I was working on  is in the branch `textSearchFix`. 
    - [Research this link](https://docs.mongodb.com/manual/core/index-text/#wildcard-text-indexes)
3. Wire up contact form
4. Admin account 
- Can edit/delete any listing from database
- Can add/remove "recommended" field on any listing from database
5. Expired listings not visible on the site 
- Data filtered by date and only show entries on todays date and later
6. Expired listings still visible in users account page so they can be edited and updated with new dates.
7. Filter by date on activities page
8. Sections on users account page - Published, Saved and Expired.
9. Slug friendly URLs

## Information Architecture

### data storage types

### data structure

### search filters & implementation


## Technologies Used

- This project uses HTML, CSS and JavaScript programming languages.
- [JQuery](https://jquery.com)
    - The project uses JQuery to simplify DOM manipulation.
- [Cloud9](https://c9.io) 
    - Developer used Cloud9 for their IDE while building the website.
- [Bootstrap](https://www.bootstrapcdn.com/)
    - The project uses Bootstrap to simplify the structure of the website and make the website responsive easily.
    - The project also uses Bootstrap to provide icons from [FontAwesome](https://www.bootstrapcdn.com/fontawesome/)
- [Google Fonts](https://fonts.google.com/)
    - The project uses Google fonts to style the website fonts.
- [Imgbb](https://imgbb.com)
    - All external images for this project are stored on Imgbb.com.
- [Jasmine](https://jasmine.github.io/)
    - This project used Jasmine to automatically test all JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery)
    - This project used Jasmine-jQuery CDN to make it possible to test jQuery code using Jasmine.
- [GitHub](https://github.com/)
    - This project uses GitHub to store and share all project code remotely. 
    - The new GitHub Projects planner was utilised to plan and keep track of this project. This project plan can be viewed [here](https://github.com/AJGreaves/picflip/projects/1).
- [Photoshop](www.adobe.com/Photoshop)
    - This project used tools in Photohshop to edit, crop and save images as well as ulitising the colour picker to ensure color consistency over the entire project.
- [Browserstack](https://www.browserstack.com/)
    - The project used Browserstack to test functionality on all browsers and devices.
- [AutoPrefixer](https://autoprefixer.github.io/)
    - The project used AutoPrefixer to make sure all css prefixes were the most up to date versions. 
- https://gijgo.com/ date and time pickers
- pylint-flask to fix pylint issues in vscode

## Testing 

Testing information can be found in separate [testing.md](testing.md) file

## Deployment

This project was developed using the [Cloud9 IDE](https://c9.io), committed to git and pushed to GitHub and Heroku using the built in function within cloud9.

- more deployment info here for heroku

### How to run this project locally

To clone this project from GitHub:
1. Follow this link to the [FamilyHub GitHub repository](https://github.com/AJGreaves/familyhub).
2. Under the repository name, click "Clone or download".
3. In the Clone with HTTPs section, copy the clone URL for the repository. 
4. In your local IDE open Git Bash.
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type ```git clone```, and then paste the URL you copied in Step 3.
```console
git clone https://github.com/USERNAME/REPOSITORY
```
7. Press Enter. Your local clone will be created.

Further reading and troubleshooting on cloning a repository from GitHub [here](https://help.github.com/en/articles/cloning-a-repository).

## Credits

### Content

- text in this project was written by...
- privacy policy https://www.cleverbox.co.uk/example-privacy-policy/
- cookies policy https://www.cleverbox.co.uk/cookies/


### Media
#### Animations
- Spinner https://icons8.com/preloaders/en/circular
- Hide and seek bot for 404 page: https://dribbble.com/shots/3480375-Stealth-Bot
- gif editor for readme gifs: https://ezgif.com
- image hosting: https://imgbb.com/

#### Images
- The FamilyHub logo was created using [Hatchful](https://hatchful.shopify.com).
- The photographs for the hero images were sourced from [Pexels](https://www.pexels.com/)


### Code
- Template code for multi-card carousel using bootstrap classes taken from [MDBootstrap](https://mdbootstrap.com/docs/jquery/javascript/carousel/) and heavily modified to suit the sites needs.
- Text shadow generated using [CSS3 Text Shadow Generator](https://css3gen.com/text-shadow/)
- Code for floating buttons taken from this [W3Schools post](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp)
- Box shadow codes were taken from [Material Design Box Shadows](https://codepen.io/sdthornton/pen/wBZdXq).
- Code for adding the correct prefixes to css was created using [AutoPrefixer](https://autoprefixer.github.io/).
- Hex to RGBA colour converter: http://hex2rgba.devoth.com/
- function to capitalize first letter of username: https://paulund.co.uk/how-to-capitalize-the-first-letter-of-a-string-in-javascript
- code to make sticky footer: https://css-tricks.com/couple-takes-sticky-footer/
- Code for animated side-nav taken from https://www.w3schools.com/howto/howto_js_sidenav.asp
- Code to generate slug-friendly-urls in python: http://flask.pocoo.org/snippets/5/
- Code to generate slug-friendly-urls in javascript: https://medium.com/@mhagemann/the-ultimate-way-to-slugify-a-url-string-in-javascript-b8e4a0d849e1

### Acknowledgements

Special thanks to: 
- list items here

#### Disclaimer
The content of this website is educational purposes only.
