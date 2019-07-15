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
    - [Flowchart](#flowchart)
    - [PDF](#pdf)

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
    - [Database choice](#database-choice)
    - [Data Storage Types](#data-storage-types)
    - [Collections Data Structure](#collections-data-structure)
        - [Users Collection](#users-collection)
        - [Activities Collection](#activities-collection)

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

4. To filter the events and activities to find the entries that are best for the age(s) of my child(ren).

5. As a user who does not want to travel far for the activity I am looking for, I want to search for activities in my town.

6. The site to provide easy access to the contact information, phone number, email, website, social media links, and a google map link for an activity or event I am interested in attending. 

7. As a user on a budget, I want to be able to filter results by free entry. I also want to know at which events I am allowed to bring my own food to.

8. As a user searching for things to do on a rainy day, I want to be able to filter results for ones suitable for poor weather.

9. As a parent planning a birthday party, I am looking for ideas on places to hold it. I want to be able to filter results by those that run birthday parties. 

10. As a parent looking for something to do on a certain day of the week, I want to be able to filter results for which days of the week they are open.

11. As a user accessing this site from a mobile phone or tablet, I want the site to have been designed responsively so that it is still easy to navigate and use on my smaller devices. 

12. As a parent searching for ideas for things for my child(ren) to do, I want to be able to filter activities by categories they are interested in. 

13. As a regular user of the Family Hub website, I expect to be able to connect to their social media channels, to keep up to date with new entries on the site. 

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

### Flowchart

- [Account and login pages flowchart](https://i.ibb.co/x1wxDsZ/flowchart.jpg). 

This flowchart was created using [draw.io](https://www.draw.io) to plan and explain the flow of behavior between the user, JavaScript, data and the modal messages the user sees based on their interactions.

### PDF

- [Family Hub development planes PDF](static/pdf/family-hub-development-planes.pdf)

This document was created during the planning phase of this project. The final website has some slight differences from what was planned. But I included this document in the project to provide insight into the original planning and direction of the site during the planning stages.  

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

- As soon as the user clicks on one of these options JavaScript sends a fetch request to pull the relevant data and display it for the user, without having to reload the page. 

- The user is also provided with a clear filters button if they wish to return to looking at all the available listings. 

- On tablet and desktop size screens the filters navbar sits in a fixed position on the left side of the screen. 

- To save space on mobile devices, the filters navbar can be slid out by pressing a **show filters** button.

<div align="center">
<img src="https://i.ibb.co/3YWBHpJ/ezgif-com-video-to-gif.gif" alt="Filters navbar on mobile gif" >
</div>

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

- The **social links** available for the activity page are Facebook, Instagram and Twitter. They appear on the listing page only when the business has provided links for the platform.

- A list of **categories** that the activity applies to are provided above the description. Icons have been added to make assimilating this information faster for the user.

- The **more info** section includes a list of other important aspects that user might need to know or filter their searches by. Such as "Free entrance" "Catering available" or "Suitable for bad weather". These items are also displayed with relevant icons.

- The activity **description** is displayed underneath all the other information, for the user who has already scanned all the relevant data and wants to know more. 

- The **contact link buttons** from the business include a link to their website, a phone number (optional), and an email business button. 

- The email business button opens a modal with an **email form** to send to the business directly from the Family Hub website. This feature was chosen to protect the businesses email addresses from being scraped from the website if they were set to `mailto:`. The email address is inserted from the data into the the contact html using JavaScript. The email form is sent using [EmailJS](http://www.emailjs.com/).

- Each listing page contains **share this page icons** with links to share the url from the page on Facebook, Twitter or by sending an email. A popular feature on websites that want to maximize social media impact for their site. 

- At the bottom of the listing pages there is a **search more activities button**, which takes the user (back) to the activities page.

### Create Account Page

- The create account page features a simple form, where the user can input an account name, email address and password. The form was kept deliberately simple so that signup has minimum barriers. 

- Once the form is complete the data is sent to the backend using JavaScript `fetch()` and then a request is made to MongoDB to check if the user name or email address already exists in the the database.

- If it does then a response is returned to JavaScript so that a response can be given to the user via modal. 

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

- At the top right of the account page a cog icon for access to the [Account Settings Page](#account-settings-page) is displayed. The positioning of this is the convention for links to settings, which is why it was chosen for this page as well. 

- Underneath the cog icon on the account page a clearly visible green **Add New button** has been added so that the user can easily access the [Edit Listing Page](#edit-listing-page).

- The user account page displays a card for each of the listings in the database that they have created. 

- Each card has three buttons underneath it: View, Edit and Delete.

- The **view** button takes the user to the listing on Family Hub as visitors to the site see it.

- The **edit** button takes the user to the [Edit Listing Page](#edit-listing-page) where they can update the data for this listing in the database. 

- The **delete** button activates a modal, asking the user to confirm that they want to delete this listing by typing "DELETE" into an input field. 

    - Once the field value is equal to "DELETE" the **confirm delete button** on the modal becomes active to the user can click it to remove the activity entry from the database. 

    - This feature was included to prevent accidental deletion of a complex data entry. 

### Add new listing page

<div align="center">
<img src="https://i.ibb.co/t2S8cyr/addnew.jpg" alt="Family Hub add new listing page on all major screen sizes" >
</div>

- The **Add New Listing Page** is where the business user provides the data for the Family Hub activities database. 

- The form is broken into sections, and laid out on a clean white background

- The business user is asked to enter the following data for their activity:
    - Title.
    - Location.
        - Street name and number.
        - Postcode.
        - Town/City (dropdown menu).
    - Contact info.
        - Phone number (optional).
        - Email address.
        - Website url.
        - Facebook link (optional).
        - Twitter link (optional).
        - Instagram link (optional).
    - Start date and End date (datepicker) **or** click switch to say the activity is ongoing.
    - Which days of the week they are open.
    - Opening and Closing times (time picker).
    - Check-boxes to indicate if they are open during the school holidays (optional).
        - Spring
        - Summer
        - Autumn
        - Winter
    - Categories check-boxes to indicate what categories the activity applies to.
        - Sports
        - Swimming
        - Creative
        - Science & Tech
        - Cultural & Music
        - Drama & Dance
        - Yoga & Mindfulnes
        - Museums & Exhibitions
        - Parks & playgrounds
        - Nature
        - Animals
        - Clubs
        - Kids Parties 
    - Age range check-boxes.
        - Under 4 yrs
        - 4 - 6 yrs
        - 6 - 8 yrs
        - 8 - 10 yrs
        - 10 - 12 yrs
        - 12 yrs + 
    - Indoor and Outdoor check-boxes.
    - Other details check-boxes.
        - Free entrance
        - Bringing own food permitted
        - Catering available
        - Suitable for good weather
        - Suitable for bad weather
        - Suitable for groups
    - Image link to use with the listing.
    - Description.

- Validation of the `<input>` fields is handled in variety of ways.

    - The input `type` attributes are set to `text`, `email`, `url` and `number` where appropriate. 

    - A dropdown menu is provided so that the town inputs match others in the database, this avoids spelling mistakes and businesses from outside of the area that Family Hub serves from entering their data into the site.

    - Datepickers and Timepickers have been combined with `pointer-events: none` css on the actual input fields, to force the user to use the Date and Timepickers to input this data and give the program the information in the correct format.

    - Check-boxes for much of the data to be stored as simply `true` or `false` in the database. 

    - Limits are placed on the length of input accepted, in order to protect from buffer overflows (hacking attempts).

    - At the bottom of the page the user is given a button to preview their data in the listing page, before it is published to the website. When this button is pushed the data is put into the database with the additional key value pair of `{"published": false}` applied to it. Then the preview page is loaded.

### Preview listing page

- The preview listing page is where the business user can preview their activity listing and see what it will look like on the Family Hub website. 

- The page is identical to the [Listing Page](#listing-page), except for three changes:

    - A preview bar along the top reminds the user that they are in preview mode, and need to click the publish button at the bottom of the page in order to make the listing live on the Family Hub website. 

    - At the bottom left of the page the "share this page" icons do not work, as we do not want the user to accidentally share the preview page. If these icons are clicked a modal pops up to inform the user of this and tell them they can share the page once the listing has been published. 

    - On the bottom right of the page, the "search more activities" button has been replaced with **Edit** and **Publish** buttons. 

        - The Edit button takes the user to the [Edit listing Page](#edit-listing-page).

        - The Publish button updates the listing with `{"published": false}` so that the data can now be displayed on the Family Hub home page and activities page.

### Edit listing Page

- The Edit Listing Page is identical to the [Add New Page](#add-new-page), except that the heading on the page says "Edit" and data for the activity to be edited has been pulled from the database and each `<input>`, `<select>`, `<checkbox>` and `<textarea>` values have been populated with the correct data.

### Contact Page

- The Contact Page features an **email contact form**, which is wired up to my email address with [EmailJS](http://www.emailjs.com/). 

- The contact page also features the contact information for Family Hub as displayed in the footer, with a link to google maps for the location.

### Privacy and Cookies Policy Page

- Features a dummy privacy and cookies policy (to be updated and checked for legality before the site is launched for real).

### 404 Page

- The custom 404 Page contains a fun animation of a robot playing hide and seek, and two buttons to return the user back to the Family Hub **home page** or **activities page**. 

### Permission Denied page

- The custom permission denied page features a humorous surprise for the user who attempts to access pages you must be logged in to access, while being logged out. 

- Two buttons on this page give the user a choice to either go to the **log in** page or **go back** one item in their browser history to whatever page they were on before this one.

## Features Left to Implement

1. Email authentication

    - Implementation of email authentication of user account before registration is complete.

2. On Create Account Page, add confirm password field or ability to see the password that was typed in, to avoid accidental typos.

3. Full text search

    - Attempted this for several days but was unable to get it to work. Rather than dragging out time on this feature when this project is already very large, I made the decision to remove the relevant code to return to at a future date when my understanding is more advanced. 

    - When returning to this feature, the text search related code I was working on  is in the branch `textSearchFix`. 

    - [Research this link](https://docs.mongodb.com/manual/core/index-text/#wildcard-text-indexes)

4. Admin account 

    - Give myself (or any other administrator of Family Hub) special permissions to access / change data in the database from a Family Hub interface, rather than having to access the data directly in MongoDB.

    - Give admin the ability to view, edit and delete any listing from database.

    - Give admin the ability to add/remove "recommended" field on any listing from database, so that only businesses that have paid for this feature will see it effected on the site.

5. Expired listings not visible on the site.
    - Add a filter to home page and activities page to not show any expired listings for events that have already taken place. 

6. Sections on users account page - Published, Saved and Expired.

    - Have separate sections on the users account page so they can see which of their activities/events are published, which are saved (but not published) and which have expired.

7. Filter by date on activities page.

    - So that the events closest to the current date are displayed first.

This section will continue to grow as the site is deployed to it's own domain and implemented in the real word. New issues and needs will become apparent as the site is used.

# Information Architecture

### Database choice

A SQL database structure would have suited this project better, however this website is a student project and the current point that I am in the course is my only opportunity to use NoSQL as the final piece of coursework (the next one) required SQL. In order to get experience with using NoSQL this project utilizes the NoSQL database MongoDB. 

To have easy access to relational data, inner objects were used inside the data structure so that they could be accessed and looped through where needed.

### Data Storage Types

The types of data stored in MongoDB for this project are:
- ObjectId
- String
- Boolean
- DateTime
- Object

### Collections Data Structure

The Family Hub website relies on two database collections:

#### Users Collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account ID | _id | None | ObjectId 
Name | username | text, `maxlength="40"` | string
Email Address | email | email, `maxlength="40"` | string
Password | password | text, `maxlength="15"` | string

[Example JSON from the users collection](familyhubapp\data\schemas\users.json)


#### Activities Collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Activity ID | _id | None | ObjectId 
Username | username |text, `maxlength="40"` | string
Title | title | text, `maxlength="50"` | string
Activity image | imgUrl | url, `maxlength="200"` | string
Indoor | indoor | checkbox | boolean
Outdoor | outdoor | checkbox | boolean
Description | description | textarea | string
Short Description | shortDescription | automatically generated | string
Published | published | User click "publish" button | boolean
Recommended | recommended | checkbox (admin only) | boolean
  |   |   |   
 **Dates** | dates |  | **object** 
 Start Date | start | datepicker | datetime
 End Date | end | datepicker | datetime
 Ongoing (no start/end) | ongoing | custom switch | boolean
  |   |   | 
**Days** | days |  | **object** 
Monday | mon | custom switch | boolean
Tuesday | tue | custom switch | boolean
Wednesday | wed | custom switch | boolean
Thursday | thu | custom switch | boolean
Friday | fri | custom switch | boolean
Saturday | sat | custom switch | boolean
Sunday | sun | custom switch | boolean
  |   |   | 
**Open times** | times |  | **object** 
Monday open time | monStart | timepicker | datetime
Monday close time | monEnd | timepicker | datetime
Tuesday open time | tueStart | timepicker | datetime
Tuesday close time | tueEnd | timepicker | datetime
Wednesday open time | wedStart | timepicker | datetime
Wednesday close time | wedEnd | timepicker | datetime
Thursday open time | thuStart | timepicker | datetime
Thursday close time | thuEnd | timepicker | datetime
Friday open time | friStart | timepicker | datetime
Friday close time | friEnd | timepicker | datetime
Saturday open time | satStart | timepicker | datetime
Saturday close time | satEnd | timepicker | datetime
Sunday open time | sunStart | timepicker | datetime
Sunday close time | sunEnd | timepicker | datetime
  |   |   | 
**School holidays** | holidays | | **object**
Spring vacation | spring | checkbox | boolean
Summer vacation | summer | checkbox | boolean
Autumn vacation | autumn | checkbox | boolean
Christmas vacation | christmas | checkbox | boolean
  |   |   | 
**Categories** | categories | | **object**
Sports | sports | checkbox | boolean
Swimming | swimming | checkbox | boolean
Creative | creative | checkbox | boolean
Science & Tech | scienceTech | checkbox | boolean
Culture & Music | cultureMusic | checkbox | boolean
Drama & Dance | dramaDance | checkbox | boolean
Yoga & Mindfulness | yogaMindfulness | checkbox | boolean
Museums & Exhibitions | museumsExhibitions | checkbox | boolean
Parks & Playgrounds | parksPlaygrounds | checkbox | boolean
Playgrounds | playgrounds | checkbox | boolean
Nature | nature | checkbox | boolean
Animals | animals | checkbox | boolean
Clubs | clubs | checkbox | boolean
Parties | parties | checkbox | boolean
  |   |   | 
**Address** | address | | **object**
Street name & number | addressLine1 | text, `maxlength="50"` | string
Postcode | postcode | text, maxlength 7 chars | string
Town/City | town | dropdown menu | string
  |   |   | 
**Age Range** | ageRange | | **object**
Under 4 years | under4 | checkbox | boolean
4 to 6 years | age4to6 | checkbox | boolean
6 to 8 years | age6to8 | checkbox | boolean
8 to 10 years | age6to10 | checkbox | boolean
10 to 12 years | age10to12 | checkbox | boolean
12 years and up | age12up | checkbox | boolean
  |   |   | 
**Contact** | contact | | **object**
Phone number | phone | tel, `pattern="[0-9]{10}"`, `maxlength="100"` | string
Website | url | url, `maxlength="100"` | string
Email | email | email, `maxlength="100"` | string
Facebook | facebook | url, `maxlength="100"` | string
Twitter | twitter | url, `maxlength="100"` | string
Instagram | instagram | url, `maxlength="100"` | string
  |   |   | 
**Other Details** | otherDetails | | **object**
Free entrance  | free | checkbox | boolean
Bringing own food permitted | bringFood | checkbox | boolean
Catering available | catering | checkbox | boolean
Suitable for good weather | goodWeather | checkbox | boolean
Suitable for bad weather | badWeather | checkbox | boolean
Suitable for groups | groups | checkbox | boolean

- The users `username` is added to each activity database entry automatically to match the user who created it. This links the two database collections together.

- The `shortDescription` in the database is generated using Python, taking the first 100 characters from the description provided by the user. This short description is displayed on the activity cards on the home page and search results.

[Example JSON from the activities collection](familyhubapp\data\schemas\activities.json)


# Technologies Used

- [Visual Studio Code](https://code.visualstudio.com/) is the IDE used for developing this project. 
- [JQuery](https://jquery.com) to simplify DOM manipulation.
- [Bootstrap](https://www.bootstrapcdn.com/) to simplify the structure of the website and make the website responsive easily.
- [FontAwesome](https://www.bootstrapcdn.com/fontawesome/) to provide icons for Family Hub.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Imgbb](https://imgbb.com) to store all external images for this project.
- [Jasmine](https://jasmine.github.io/) to run automated tests on JavaScript and jQuery code.
- [Jasmine-jQuery](https://github.com/velesin/jasmine-jquery) to make it possible to test jQuery code using Jasmine.
- [PyMongo](https://api.mongodb.com/python/current/) to make communication between Python and MongoDB possible.
- [Flask](https://flask.palletsprojects.com/en/1.0.x/) to construct and render pages.
- [Jinja](http://jinja.pocoo.org/docs/2.10/) to simplify displaying data from the backend of this project smoothly and effectively in html.
- [PIP](https://pip.pypa.io/en/stable/installing/) for installation of tools needed in this project.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) to handle version control.
- [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) is the database for this project
- [GitHub](https://github.com/) to store and share all project code remotely. 
- [Photoshop](www.adobe.com/Photoshop) to edit, crop and save images as well as ulitizing the colour picker to ensure color consistency over the entire project.
- [Browserstack](https://www.browserstack.com/) to test functionality on all browsers and devices.
- [Gijgo](https://gijgo.com/) provided bootstrap styled date and time pickers.
- [Am I Responsive](http://ami.responsivedesign.is/) to create the images in this readme file of each page displayed on different screen sizes.
- [EZgif](https://ezgif.com/video-to-gif) provided gif editing software for the gif in this readme file. 
- This project uses HTML, CSS, JavaScript and Python programming languages.

# Testing 

Testing information can be found in separate [testing.md](testing.md) file

# Deployment

## Heroku deployment

To deploy Family Hub to heroku, the following steps were taken:

1. Created a `requirements.txt` file using the terminal command `pip freeze > requirements.txt`.

2. Created a `Procfile` with the terminal command `echo web: python app.py > Procfile`.

3. `git add` and `git commit` the new requirements and Procfile and then `git push` the project to GitHub.

3. Created a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the "New" button in my dashboard. Gave it a  name and set the region to Europe.

4. From the heroku dashboard of my newly created applicaiton, clicked on "Deploy" > "Deployment method" and selected GitHub.

5. Confirmed the linking of my heroku app to the correct GitHub repository.

6. In the heroku dashboard for my application, clicked on "Settings" > "Reveal Config Vars".

7. Set the following config vars:

| Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<not_my_actual_secret_key>`

8. In the heroku dashboard, clicked "Deploy".

9. In the "Manual Deployment" section of this page, made sure the master branch was selected and then clicked "Deploy Branch".

10. The site was successfully deployed.

## How to run this project locally

To run this project on your own IDE follow the instructions below:

Ensure you have the following tools: 
- An IDE such as [Visual Studio Code](https://code.visualstudio.com/)

The following must be installed on your machine:
- [PIP](https://pip.pypa.io/en/stable/installing/) installed on your machine.
- [Python 3](https://www.python.org/downloads/) installed on your machine.
- [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03) installed on your machine.
- An account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas) or MongoDB running locally on your machine.

### Instructions
1. Save a copy of the github repository located at https://github.com/AJGreaves/familyhub by clicking the "download zip" button at the top of the page and extracting the zip file to your chosen folder. If you have Git installed on your system, you can clone the repository with the following command.
```
git clone https://github.com/AJGreaves/familyhub
```

2. If possible open a terminal session in the unzip folder or cd to the correct location.

3. A virtual environment is recommended for the Python interpreter, I recommend using Pythons built in virtual environment. Enter the command:
```
python -m .venv venv
```  
_NOTE: Your Python command may differ, such as python3 or py_

4. Activate the .venv with the command:
```
.venv\Scripts\activate 
```
_Again this may differ depending on your operating system, please check the [Python Documentation on virtual environments](https://docs.python.org/3/library/venv.html) for further instructions._

4. If needed, Upgrade pip locally with
```
pip install --upgrade pip.
```

5. Install all required modules with the command 
```
pip -r requirements.txt.
```

6. In your local IDE create a file called `.flaskenv`.

7. Inside the .flaskenv file, create a SECRET_KEY variable and a MONGO_URI to link to your own database. Please make sure to call your database `familyHub`, with 2 collections called `users` and `activities`. You will find example json structures for these collections in the [schemas](familyhubapp/data/schemas) folder.

8. You can now run the application with the command
```
python app.py
```

9. You can visit the website at `http://127.0.0.1:5000`

# Credits

## Content

- The text, images, links and other data in the database was sourced from various local websites including but not limited to

    - [Amsterdam Mamas](http://amsterdam-mamas.nl/)
    - [Kidsproof Haarlem](https://www.kidsproof.nl/Haarlem)
    - [Go-Kids Haarlem](https://go-kids.nl/haarlem)
    - [Uit in Haarlemmermeer](https://www.uitinhaarlemmermeer.nl/nl/agenda)
    - [Pier-K](https://www.pier-k.nl)

- The data from these other websites was translated into english using [Google Translate](https://translate.google.com/) and inserted into the database to populate it with real local activities and events.

- Text for the Family Hub website privacy and cookies policy were heavily influenced by the [cleverbox privacy policy](https://www.cleverbox.co.uk/example-privacy-policy/) and [Cleverbox cookies policy](https://www.cleverbox.co.uk/cookies/)

- All other text on Family Hub was written by me.

## Media
### Animations
- Animated spinner was provided by [icons8](https://icons8.com/preloaders/en/circular)
- Hide and seek bot for 404 page was provided by [dribbble.com](https://dribbble.com/shots/3480375-Stealth-Bot)

### Images
- The FamilyHub logo was created using [Hatchful](https://hatchful.shopify.com).

- The photographs for the hero images were sourced from [Pexels](https://www.pexels.com/)

- Where possible the links to the images for the events were taken directly from the source images url in the activity listings I sourced the data from. 

- On occasion when this did not work the image was copied to my local machine and then uploaded to my [imgBB](https://anna-gilhespy.imgbb.com/) account, where I took the link from instead.

## Code

- Template code for multi-card carousel using bootstrap classes taken from [MDBootstrap](https://mdbootstrap.com/docs/jquery/javascript/carousel/) and heavily modified to suit the sites needs.

- Code for floating buttons taken from this [W3Schools](https://www.w3schools.com/howto/howto_js_scroll_to_top.asp) post.

- Box shadow codes were taken from [Material Design Box Shadows](https://codepen.io/sdthornton/pen/wBZdXq).

- Code for adding the correct prefixes to css was created using [AutoPrefixer](https://autoprefixer.github.io/).

- [Hex2rgba](http://hex2rgba.devoth.com/) was used to convert hex colours to rgba when I needed transparent background colours without using opacity css.

- code for function to capitalize first letter of username was taken from this [paulund.co.uk](https://paulund.co.uk/how-to-capitalize-the-first-letter-of-a-string-in-javascript) post.

- Code to make sticky footer was taken from this [css-tricks.com](https://css-tricks.com/couple-takes-sticky-footer/) post.

- Code for animated side-nav taken from this [w3schools.com](https://www.w3schools.com/howto/howto_js_sidenav.asp) post.

- Code to generate slug-friendly-urls in Python taken from this [Flask](http://flask.pocoo.org/snippets/5/) post

- Code to generate slug-friendly-urls in JavaScript was taken from this [medium.com](https://medium.com/@mhagemann/the-ultimate-way-to-slugify-a-url-string-in-javascript-b8e4a0d849e1) post.

## Acknowledgements

Special thanks to my mentor Simen Daehlin for his never-ending patience and willingness to teach me not only what code works, but what is expected of my websites and code in industry.

# Contact
To contact me feel free to email

 `gilhespy (dot) anna (at) gmail (dot) com`

## Disclaimer
The content of this website is educational purposes only.
