<div align="center">
    <img src="https://i.ibb.co/Pm36prG/fh-logo-readme.png" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Family Hub Logo" aria-label="Family Hub Logo" />
    <img src="https://i.ibb.co/Pj9RZW5/tagline.png" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Family events and activities for kids in Haarlemmermeer" aria-label="Family events and activities for kids in Haarlemmermeer" />
</div> 

## Introduction

<div align="center">
    <img src="https://i.ibb.co/CBw04v7/home.jpg" href="http://family-hub-nl.herokuapp.com" target="_blank" rel="noopener" alt="Image of how home page looks on all screen sizes" aria-label="Image of how home page looks on all screen sizes" />
</div>
<br>

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
        - [Elements on every Page](#elements-on-every-page)
        - [Home Page](#home-page)
        - [Activities Page](#activities-page)
        - [Listing Page](#listing-page)
        - [Create Account Page](#create-account-page)
        - [Log In Page](#log-in-page)
        - [Account Settings Page](#account-settings-page)
        - [Account Page](#account-page)
        - [Add new Listing Page](#add-new-listing-page)
        - [Preview Listing Page](#preview-listing-page)
        - [Edit Listing Page](#edit-listing-page)
        - [Contact Page](#contact-page)
        - [404 Page](#404-page)
        - [Permission Denied Page](#permission-denied-page)
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

# UX

## Goals

### Visitor Goals

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

### Business Goals

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

### Family Hub Goals

- Provide an effective, easy to use site for English speaking international families to search and filter through entries to find the listings that suit their needs.

- So that I can learn and practice frontend and backend programming together for the first time. To combine the use of HTML, CSS, Bootstrap and JavaScript with Python, MongoDB, Flask and Jinja.

- While this is currently a student project, the future goal of Family Hub to monetise the website to charge businesses for advertising their events and activities on it. This will come later once the site has a few more features to offer those who use it (see [Features Left to Implement](#features-left-to-implement)).

## User Stories

### Visitor Stories

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

### Business Stories

As a Business advertising on FamilyHub I expect/want/need:
1. To see that the information other businesses have put on the site are being displayed in an attractive and useful way for the user. 

2. To see that various methods of contacting my business are available to users using Family Hub. 

3. To be able to log in to access my existing entries, and for my data to only be editable with my account.

4. To create, edit and delete entries in my account.

5. A user interface that is simple and easy to use, that is laid out in a logical way with clear indications where necessary about the type and format of the data I need to provide. 

6. Forms for inputting my data to make the process easy, that there is no wasting my time or making the process difficult or slow. 

## Design Choices

The Family Hub website has an overall family friendly feel, with emphasis on providing complex information in a bite size, learnable format. The following design choices were made with this in mind:

### Fonts

- The primary font `News Cycle` was chosen for the main text of the site because it is easy to read and complements the fonts chosen for titles very well. A extra reason for picking this font is that it is still easy to read when printed small, and as this site provides a large amount of information, using a smaller font is occasionally necessary.

- The secondary font `Delius` was chosen for the main headings because it resembles simple clear handwriting that a parent or teacher might use when teaching a child. The font has a personal feel to it, and when combined with the colours chosen for this project, refers well to families. Being a cursive font it complements in the main sans-serif type font very well from a design perspective

- The tertiary font `Patrick Hand SC` was chosen for its contrast with the two main fonts. Only used in a handful of places across the site, it brings a little extra flavour to the fonts while not overwhelming the user with too many. 

### Icons

![Example listing page with icons](https://i.ibb.co/hXkxsM1/Clipboard01.jpg)

- It is important to use icons on the Family Hub website for three main reasons:

    1. The site provides a lot of different information about each activity. Icons help to break up this information in a way that helps the user to identify the parts of the information that is relevant to their needs. 

    2. Icons break up the information visually, creating space for the user and not overwhelming them with too much info at once. 

    3. The international community in The Netherlands is made up of people from many other countries, and often English is their 2nd or 3rd language. Providing information to them in a visual way as well as in English enhances these users ability to understand the site even when their English is not very strong (though likely stronger than their Dutch).

- Each icon was chosen for it's clarity in quickly explaining the relevant meaning with an image. 

- Icons are most used on the individual listing pages for each activity. And were also added to the navigation bar as well. 

- Social media icons for facebook, instagram and twitter are used in 3 places on the site. 

    1. In the footer, to link to the social media outlets for Family Hub. these links do not yet exits, so currently the icons link to the main pages for each social media network.

    2. On each listing page for any links provided by the organizers to their events and activities. 

    3. At the bottom of each activity page with a link to share that page on each of the social media platforms. (does not include instagram, but does include an icon to email the page instead).

### Colours
<div align="center">
    <img src="https://i.ibb.co/d2qQzsP/colours.jpg" alt="Family Hub Brand Colours" aria-label="Family Hub Brand colours" />
</div>

- The brand colours for this project were chosen because they are colorful, which references to family well, while still choosing tones and shades that worked well together without overwhelming the eyes. 

- Colorful highlights that draw the eye to headings are provided by the terracotta colour, which is accented with the light blues in horizontal lines and links. 

- A dark navy blue was chosen for the main text as it contrasts with the white background clearly. 

- The navbar background colour is a clean platinum colour, light enough to provide contrast with the navy blue headings, while still setting itself apart from the white background in the main content.

- In the footer a darker shade of greenish-blue provides the background colour, setting the footer apart from the rest of the content and making it dark enough that the text can be in white and still have enough contrast to be easily readable. 

- The same darker green-blue is used for the filters bar on the activities page. Green-blue is a colour for outdoors, adventure and learning, so was a good choice for the feeling of this website. 

### Styling

- A **loading spinner** was added to Family hub, to run while the page or data loads. The spinner chosen resembles a wind spinner toy. I picked it because it is colorful and fits well with the overall feel and demographic for the site.

- All **buttons** on the site fit the same bootstrap button styling in size and shape, but I added my own brand colours to them so they fit in with the rest of the content. 

- Bootstrap **cards** were utilized on Family Hub to display short information about each activity and event, with a link to each listing page on it. The cards were styled with **curved corners**, a theme repeated around the entire website in images, input boxes, buttons, pagination links etc. 

- A bootstrap **table** has been utilized for displaying opening times on listing pages, the clean bootstrap styling was perfect for the design of this page.

- Movement on the **carousels** has been slowed long enough for the user to be able to read more of the content before moving on again. If the user hovers over the carousel then the movement stops completely. 

- hover effects
    - Some subtle **shadows** have been added to listing cards, modals and smaller form boxes, to give them depth on the page. This shadow is made larger on hover, giving the user a positive user experience in highlighting the section of the site they are hovering over.

    - Css effects on buttons cause them to animate to a darker shade when hovered over, this same effect is also applied to all text links on the site. 

## Wireframes

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

### Flowcharts 

- [Account and login pages flowchart](https://i.ibb.co/x1wxDsZ/flowchart.jpg). 

This flowchart was created using [draw.io](https://www.draw.io) to plan and explain the flow of behavior between the user, javascript, data and the modal messages the user sees based on their interactions.

# Features
 
## Existing Features

### Elements on every page
- Navbar
    - The navigation bar features the Family Hub logo in the top left corner.

    - For visitors to the site who are not logged in, list items links are available for them to use.
        1. Home
        2. Activities
        3. Create Account
        4. Log in 
        5. Contact

    - For users who are logged in, the list items are as follows: 
        1. Home
        2. Activities
        3. Contact
        4. My account (this option is a dropdown menu)
            - My listings
            - Add new
            - Settings
            - Log out

    - Python determines if the user is logged in or not by checking `if 'user' in session` and passes this data to Jinja to display the correct navbar for the user.

    - The navbar is collapsed into a burger icon on small screens. On the activities page, where the activities filter takes up some of the width of the screen, the navbar is collapsed on medium screens as well, so that menu items did not start overlapping content. 

    - The practical design choice was made not to fix the navbar to the top of the page as the user scrolls. This was because I wanted as much screen height as possible to display the website information on and I did not want to take up precious space with a fixed navbar. To get around the problem of having to scroll up a long way to reach the navigation, I added a scroll to top button and essential links in the footer as well.

- Footer
    - The footer features:
        - Contact information for Family hub, including the address which is linked to google maps, an email address and Chamber of Commerce number (currently a fake number, but will be registered before launching this as a real site.)
        - A profile photo of the website creator as well as a brief description of the purpose and mission for the site. 
        - A list of useful links users might need when viewing the footer. 
        - Copyright information.
        - Links to social media locations (Which will eventually be linked up to the Family Hub social media platforms, once they exist).

- Floating to top button:
    - A floating button appears on the lower right of the screen when the user starts to scroll downwards. Clicking this moves the view back up to the top of the page. I added this feature because some pages can be quite long and the navbar is not fixed to the top of the page.
    - Adding the class `.active` to the `#to-top-button` changes it's `opacity` from `0` to `0.5`, which gave me the ability to animate the change gently. The opacity is increased again to `1` on hover. 

```javascript
function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        $("#to-top-btn").addClass('active');
    } else {
        $("#to-top-btn").removeClass('active');
    }
}
```

### Home Page

<div align="center">
<img src="https://i.ibb.co/CBw04v7/home.jpg" alt="Family Hub home page on all major screen sizes" >
</div>

**hero image**
- The Family Hub home page features a colorful hero image of a child with paint on their hands. I chose this image because it is eye catching and striking, and it features a child doing an activity. The tagline for the website is laid over the image. This image was coded as a background-image in css and set to `background-size: cover;` so that it is responsive while never getting stretched or distorted. 

**Event cards**

- Each event card on the home page gives the user some brief and useful information about each of the listings displayed. The activity image, town name, title and 100 character string introduces the activity to the user. Every card is clickable to go to the main listing page for that activity, so that if the user wishes to learn more the information is only one click away. 

- The images on the cards are set to background-image using css, which ensures that no matter what dimensions the original image provided was, all card images have equal size, making for a much more attractive site and user experience.

**Carousels**

- The home page features 3 carousels in total. Each carousel has a heading on the left and a "search more" button on the right that leads to the Activities page

- **Recommended Carousel** features a random selection of 12 activities that have `{ "recommended": true }` in their data. At the moment this value has been set manually in MongoDB. However eventually this setting will be set using an Admin account accessible only by the website administrator. A place on the "recommended" carousel will be a paid for feature for businesses advertising on the site.

- **Seasonal Carousel** features events and activities for upcoming school holidays, which is a particular pain point for most parents, and something that would draw them to search for things for their children to do. The results for this carousel are pulled from entries in the database that have `{ "holidays": { "summer": true } }` in them. This can easily be switched for one of the other seasons in the `holidays` object as the year goes by. 

- At the moment of submitting this project for my course the summer school holidays have just begun, this part of the site would change depending on the year, so would feature activities and events for Autumn break, Christmas holidays, Easter vacation etc as the year goes on. 

- **Sports Carousel**. Dutch culture is very sporty and the number of sports activities available for kids is vast, so a carousel offering some highlights from the choices in this category was also created for the home page. 12 random results from entries in the database with `{ "category": { "sports": true } }` are pulled for this carousel when the home page is loaded. 

**Top Tip Feature box**

- A feature box, placed just below the first recommended carousel breaks up the rest of the content on the home page and offers a prime position on the home page for a top paying business to advertise their activity or event. 

### Activities Page

<div align="center">
<img src="https://i.ibb.co/yN750bS/activities.jpg" alt="Family Hub activities page on all major screen sizes" >
</div>

- For the average visitor to Family Hub the Activities page is the main purpose of the site. This is where the user can use the filters to find the activities that suit their needs. 

**Activity Cards**
- Actiivity cards are displayed in exactly the same format as the ones in the carousels on the home page. Providing the user with a short introduction to each activity, and a link to read more about the ones they are most interested in.

**Filters**

- At the moment the filters available are: 
    - Location
    - Category
    - Days of the week
    - Indoor or Outdoor
    - Age range
    - Other details
- (see [Features Left to Implement](#features-left-to-implement) for filters to be included in future releases)

- As soon as the user clicks on one of these options JavaScrip sends a fetch request to pull the relevant data and display it for the user, without having to reload the page. 

- The user is also provided with a clear filters button if they wish to return to looking at all the available listings. 

**Pagination**

Pagination is included on the activities page when the number of results to display is over 12. Each page contains up to 12 listings. This was done to make loading times faster and a smoother experience for the user. 

### Listing Page

<div align="center">
<img src="https://i.ibb.co/LpNYVZJ/listing.jpg" alt="Family Hub listing page on all major screen sizes" >
</div>

Each listing page for an entry in the database displays that information in clearly laid out and easy to digest way. Utilizing icons to make locating and assimilating information faster for the user.

- The **image** for the listing, in the listing page the dimensions of this image are not altered, so that the business listing can have their entire picture on the website.
- On large size screens and up the image takes up 50% width of it's container. On medium and small size screens it takes up 100% width and the other content is displayed below it. 

- The **open times** for the activity are displayed in a table that is easy to read and understand.

- The **dates** section is visible for activities and events that have a start and end date. If the business has selected "ongoing" when creating the entry then the dates section does not appear in the listing page.

- The **ages** section of the listing page is a simple table with the age groups listed down on column and a row of green check marks and terracotta crosses to mark which ages the activity is for. This provides clear visual information for the user.  

- On the listing page the **Address** has been linked to google maps so that the location of the event can be easily found with one click. 

- The **social links** available for the activity page are Facebook, Instagram and Twitter. They appear on the listings page only when the business has provided links for the platform.

- A list of **categories** that the activity applies to are provided above the description. Icons have been added to make assimilating this information faster for the user.

- The **more info** section includes a list of other important aspects that user might need to know or filter their searches by. Such as "Free entrance" "Catering available" or "Suitable for bad weather". These items hare also displayed with relevant icons.

- The activity **description** is displayed underneath all the other information, for the user who has already scanned all the relevant data and wants to know more. 

- The **contact link buttons** from the business include a link to their website, a phone number (optional), and an email business button. 

- The email business button opens a modal with an **email form** to send to the business directly from the Family Hub website. This feature was chosen to protect the businesses email addresses from being scraped from the website if they were set to `mailto:`. The email address is inserted from the data into the the contact html using JavaScript. The email form is sent using [EmailJS](http://www.emailjs.com/).

- Each listing page contains **share this page icons** with links to share the url from the page on Facebook, Twitter or by sending an email. A popular feature on websites that want to maximize social media impact for their site. 

- At the bottom of the listing pages there is a **search more activities button**, which takes the user (back) to the activities page.

### Create Account Page

- The create account page features a simple form, where the user can input an account name, email address and password. The form was kept deliberately simple so that signup has minimum barriers. 

- Once the form is complete the data is sent to the backend using javascript `fetch()` and then a request is made to MongoDB to check if the user name or email address already exists in the the database.

- If it does then a response is returned to javascript so that a response can be given to the user via modal. 

- If the user does not already exist in the database then the account is created, and a modal informing the user of successful creation of their account appears. In the modal a button link to the log in page is provided.

- This [Account and login pages flowchart](https://i.ibb.co/x1wxDsZ/flowchart.jpg) fully explains the behavior of the forms, data checks and modal messages on this page and the [Log In Page](#log-in-page).

- (see [Features Left to Implement](#features-left-to-implement) for additional features to be included on this page in future releases)

### log In Page

- The log in page also features a simple **form** where the user can enter either their username or their email address, and their password. 

- This form also uses JavaScript `fetch()` to pass the input data from the user to Python. The reason for this use is that I wanted to provide the user with a modal once they were logged in, rather than reloading the page. 

- If the user inputs incorrect data a **modal** responds with various messages depending on what was incorrect. 

- When the user logs in with a correct email and password a **success modal** appears with links to their personal account page and editor page to add a new activity to the database.

- This [Account and login pages flowchart](https://i.ibb.co/x1wxDsZ/flowchart.jpg) fully explains the behavior of the forms, data checks and modal messages on this page and the [Account Page](#account-page).

### Account settings page

- The account settings page includes two small forms for the user to update their email address or password. 

- Each form requires the user to input their current email/password and then their new one. 

- If the current data is not correct the user is informed of this via modal. 

### Account page

<div align="center">
<img src="https://i.ibb.co/2qfkKFx/account.jpg" alt="Family Hub account page on all major screen sizes" >
</div>

- The user account page displays a card for each of the listings in the database that they have created. 

- Each card has three buttons underneath it: View, Edit and Delete.

- The **view** button takes the user to the listing on Family Hub as visitors to the site see it.

- The **edit** button takes the user to the [Edit Listing Page](#edit-listing-page) where they can update the data for this listing in the database. 

- The **delete** button activates a modal, asking the user to confirm that they want to delete this listing by typing "DELETE" into an input field. 

    - Once the field value is equal to "DELETE" the **confirm delete** button on the modal can be clicked to remove the activity entry from the database. 

    - This feature was included to prevent accidental deletion of a complex data entry. 

### Add new listing page

<div align="center">
<img src="https://i.ibb.co/t2S8cyr/addnew.jpg" alt="Family Hub add new listing page on all major screen sizes" >
</div>

### Preview listing page

<div align="center">
<img src="https://i.ibb.co/2MTLzKk/preview.jpg" alt="Family Hub preview listing page on all major screen sizes" >
</div>

### Edit listing page

<div align="center">
<img src="https://i.ibb.co/MR6nKp7/edit.jpg" alt="Family Hub edit listing page on all major screen sizes" >
</div>

### Contact page

<div align="center">
<img src="https://i.ibb.co/hFHp8x9/contact.jpg" alt="Family Hub contact page on all major screen sizes" >
</div>

### 404 page

<div align="center">
<img src="https://i.ibb.co/4Kz1Mp7/404.jpg" alt="Family Hub 404 page on all major screen sizes" >
</div>

### Permission Denied page

<div align="center">
<img src="https://i.ibb.co/M6FkQhZ/denied.jpg" alt="Family Hub permission denied page on all major screen sizes" >
</div>

## Features Left to Implement

1. Email authentication
    - Implementation of email authentication of user account before registration is complete.
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

# Information Architecture

### data storage types

### data structure

### search filters & implementation


# Technologies Used

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

# Testing 

Testing information can be found in separate [testing.md](testing.md) file

# Deployment

## Heroku deployment

This project was developed using the [Cloud9 IDE](https://c9.io), committed to git and pushed to GitHub and Heroku using the built in function within cloud9.

- more deployment info here for heroku

## How to run this project locally

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

# Credits

## Content

- text in this project was written by...
- privacy policy https://www.cleverbox.co.uk/example-privacy-policy/
- cookies policy https://www.cleverbox.co.uk/cookies/


## Media
### Animations
- Spinner https://icons8.com/preloaders/en/circular
- Hide and seek bot for 404 page: https://dribbble.com/shots/3480375-Stealth-Bot
- gif editor for readme gifs: https://ezgif.com
- image hosting: https://imgbb.com/

### Images
- The FamilyHub logo was created using [Hatchful](https://hatchful.shopify.com).
- The photographs for the hero images were sourced from [Pexels](https://www.pexels.com/)


## Code
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

## Acknowledgements

Special thanks to: 
- list items here

# Contact

## Disclaimer
The content of this website is educational purposes only.
