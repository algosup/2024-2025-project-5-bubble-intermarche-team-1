# Technical Specification
## Author
| Name        | Role             |
| ----------- | ---------------- |
| NOGUES Loic | Technical Leader |
## Table of Contents

<details>

- [Technical Specification](#technical-specification)
  - [Author](#author)
  - [Table of Contents](#table-of-contents)
  - [1.Project Summary](#1project-summary)
  - [2.Technical Requirements](#2technical-requirements)
  - [3 Styles, Pages, Flow.](#3-styles-pages-flow)
    - [3.1 Styles](#31-styles)
    - [3.2 Pages](#32-pages)
    - [3.3 Flow of the Webapp](#33-flow-of-the-webapp)
  - [4.Features](#4features)
    - [4.1 Language Selection](#41-language-selection)
    - [4.2 Personalized Interface](#42-personalized-interface)
      - [4.2.1 Preferences of users](#421-preferences-of-users)
      - [4.2.2 Dynamic Interface](#422-dynamic-interface)
    - [4.3 Scan](#43-scan)
    - [4.4 Superlink](#44-superlink)
      - [4.4.1 How It Works](#441-how-it-works)
  - [5. Reusable Elements](#5-reusable-elements)
  - [6.DataBase](#6database)
    - [6.1 Product](#61-product)
      - [6.1.1 Data Management Of Products](#611-data-management-of-products)
    - [6.2 Pairing](#62-pairing)
    - [6.3 User](#63-user)
  - [7.Technical Constraints](#7technical-constraints)
  - [8. Integration](#8-integration)
  - [9. Supported Browsers](#9-supported-browsers)
    - [9.1 Browser Support Summary](#91-browser-support-summary)
    - [9.2 Edit-Mode](#92-edit-mode)
  - [10. Future Improvement](#10-future-improvement)
  - [11. Glossary](#11-glossary)
      - [**Bubble.io**](#bubbleio)
      - [**NoCode**](#nocode)
      - [**Web App**](#web-app)
      - [**QR Code**](#qr-code)
      - [**FireBase**](#firebase)
      - [**EAN Code**](#ean-code)
      - [**ITM8**](#itm8)
      - [**BarCode Scanner Plugin**](#barcode-scanner-plugin)
      - [**Magic Link**](#magic-link)
      - [**Local Data**](#local-data)
      - [**Pairing**](#pairing)
      - [**Responsive Design**](#responsive-design)
      - [**Product Database**](#product-database)
      - [**User Preferences**](#user-preferences)
      - [**Bubble.io**](#bubbleio-1)
      - [**NoCode**](#nocode-1)
      - [**Web App**](#web-app-1)
      - [**QR Code**](#qr-code-1)
      - [**FireBase**](#firebase-1)
      - [**EAN Code**](#ean-code-1)
      - [**ITM8**](#itm8-1)
      - [**Barcode Scanner Plugin**](#barcode-scanner-plugin-1)
      - [**Magic Link**](#magic-link-1)
      - [**Local Data**](#local-data-1)
      - [**Pairing**](#pairing-1)
      - [**Responsive Design**](#responsive-design-1)
      - [**Product Database**](#product-database-1)
      - [**User Preferences**](#user-preferences-1)

</details>

## 1.Project Summary
__Conseil Intermarché__ is a web app solution for customers, it helps them by giving recommendations for only cheese and wine for now. It will also allow the product to be scanned. Multiple languages will be supported by the web app, and Conseil Intermarché provides a personalized experience for users. We will use __Bubble Editor__ and __Firebase__ for the data to make Conseil Intermarché.
## 2.Technical Requirements
__Programing Language__ : NoCode will be use for this project.

__Supported Devices__ : The devices that will be supported will mostly be the smartphones. It will  also be supported on computers

__Supported Languages__ : Conseil Intermarché will be translated in __English__ and __French__

__An Easy Access And Interface__ : To access the web app, there will be a QR code at the entry of the store. Also the interface will be very intuitive using blocks and sections like (wine, cheese etc).

__Products__: All the products of the web app has been given by the client with the __ITM8__ and the 
__EAN__. There is also the prices, the quantities and the price/kg.

**Project:** Wine & Cheese Recommendation Web App  

**Client:** Intermarché Saint-Rémy-de-Provence  

## 3 Styles, Pages, Flow.
### 3.1 Styles
The style we will use are mainly the __red__, __black__ and __white__.
Because they are the main colors of the Intermarché logo and theme.
![](<images/Logo.jpg>)
### 3.2 Pages
There will be a total 5 pages :
- Index / Menu Page

      This is the menu of the web app. With a button get
      started to start your journey on Conseil Intermaché

- Question page
    
      Right after the Menu Page the user will be answering 
      questions for there preferences. 
      The answers of the users will be on the user Data Base.
      Also there will be a skip button for if the user 
      doesn't want to answers questions. 
- Home Page

      The home of the web app where the user can access.
      everything (Search Page and Product Page).
      Recommandation based on the answers of the 
      Questions Page. There will be a hotbar at the bottom
      of the screen with a barcode, a search button and 
      a possibilty to go back to the Home Page. 
      Also there will be an access to the wines page and 
      the cheese page.
      To access those catalogs pages we will need to make
      a button to go to these pages.

- Wine/Cheese Page

      This page is accessible by clicking on the wine or 
      cheese button. 
      This is made for searching which wine or cheese 
      he wants with a search bar, filters etc.
      To do display the products we will need the product
      Database and repeating groups. To recommand the 
      best wine, all the users can put a like on the 
      products he likes. This will add a +1 on the product 
      score.

- Product Page

      The page is for when the user click on a product or
      scan the barcode of a wine or a cheese.
      This where the user can likes the products.
      Also there will be a pairing recommandation with the
      product clicked. This will be based on the Pairing
      Database and when clicked, a popup will appear
      with the possibilty to like or dislike the pairing. 
      The dislike will remove -1 on the pairing score.

### 3.3 Flow of the Webapp
![](<images/Flow.png>)

      

## 4.Features 
### 4.1 Language Selection
You will be able to choose between __French__ and __English__. We will put new fields in the database to translate into __English__ and into __French__.

### 4.2 Personalized Interface
#### 4.2.1 Preferences of users
There will be a total of 3 to 5 questions about what the customer likes about wine tastes, cheese texture, etc. The user has the possibility to skip those questions if they want to directly access the web app. The answer will be saved in the local data.
Also, there will be a next and previous button, and a skip button if you don't want to respond to the questions.
#### 4.2.2 Dynamic Interface
The web app will give the user an __unique interface__ based on the local data of the user. Each web app interface will be different if the answers are not the same. In the __HomePage__ the preferences will be based on the previous questions the user answered.

### 4.3 Scan
You will be able to scan the barcode of the product. The web app will shows the description and recommend other merchandise that is good with the scanned product. To make it work, we will use a plugin called __BarCode Scanner__ that we can add on Bubble. To add a plugin, you will have on the left tab in the __Edit-Mode__. Click and just search for the plugin that you want. When you find the plugins wanted just click on them and click on add.
The plugin will be added.

### 4.4 Superlink
To allow occasional follow-up, promotions, or sending pairing guides via email, we’re adding a __Magic Link__ system. This feature lets users input their name and email or phone number, and receive a personal link to revisit their wine/cheese suggestions or pairing history.

#### 4.4.1 How It Works
The user browses the app normally. At any point, they can tap the button “Save and Send Link”, after a short form appears to collect name and contact (email). Bubble generates a unique URL tied to their browsing session or preferences. Finally, this link is sent to them automatically. When they reopen it, their saved pairings are restored instantly.

## 5. Reusable Elements
To create a page in Bubble using reusable elements, first open the Bubble editor and navigate to the Design tab. In the left panel, locate the “Reusable elements” section and click “New reusable element.” Name your reusable component, for example “Header,” “Footer,” or “CardComponent,” and then design it using the same tools available for any group. You can add inputs, text, buttons, icons, workflows, or custom states.

Once the reusable element is created, go to the page where you want to use it. In the Design tab for that page, search for the reusable element by name in the elements panel and drag it into the page. The reusable element will appear as a single block that you can position like any other group. If the reusable element includes custom states or workflows, those will work wherever it's placed.

To pass data into a reusable element, use the element's exposed inputs (if you’ve configured any). You can define custom data fields by clicking on the reusable element, going to the property editor, and setting the type of content. Inside the reusable element, you can reference “Parent group's [thing]” to access the passed data.

Reusable elements are useful for maintaining consistency across your app. For example, a reusable header used on all pages can be updated in one place, and the change will propagate everywhere it's used. You can also nest reusable elements inside each other if needed.

Finally, to handle workflows, open the reusable element directly and configure its internal logic as you would with any page or group. You can also trigger custom events inside the reusable element and expose them to be triggered from the main page using the “Trigger a custom event from reusable element” action.
## 6.DataBase
### 6.1 Product

#### 6.1.1 Data Management Of Products

The core dataset includes two main categories of products: wines and cheeses. Each product has a name, description, a price (sourced either from Intermarché’s internal base or direct suppliers), and a classification into categories such as "red wine" and subcategories like "soft cheese", etc. Fromages often have pricing by weight (per kilogram), and units sold may vary significantly (e.g., full wheels vs. small portions), so this distinction must be managed clearly in the database.

Each product also includes a reference code (ITM8), a barcode (EAN), and a location tag to reflect its physical placement in the store. Also, the barcode (EAN) will serve as an ID for products

The product database will be done on a database site named FireBase, there is a plugin that can be used for that. We will use that because it is more efficient than doing it one by one on bubble.

![](<images/API firebase.png>)

The Product database I will be using only for the pages where there is only wine or cheese. The recommendation system will be based on "likes" by the users. The more likes a product has, the more it will be recommended. If there are no "likes," the recommendation will be based at the start with the 10 most sold wines and cheeses.

Finally, the way we will find all the images will be by searching on the internet and finding everything we want.


| Field Name          | Type   |
| ------------------- | ------ |
| name                | text   |
| description_fr      | text   |
| description_en      | text   |
| category            | text   |
| subcategory         | text   |
| itm8\_ref           | text   |
| ean\_code           | text   |
| price               | number |
| photo               | image  |
| unit\_type          | text   |
| average\_weight\_kg | number |  
| popularity\_score   | number |


### 6.2 Pairing 

This database will also be done on the site __Firebase__

The __Pairing__ database will be use for a certain product page. It will be done with looking up what's a good pairing or not. The recommandation will be done by also "likes" but also "dislike".

| Field Name      | Type    |
| --------------- | ------- |
| wine\_ITM8      | Product |
| cheese \_ITM8   | Product |
| description\_fr | text    |
| description\_en | text    |
| score           | number  |

### 6.3 User

The __Question page__ will be use as a base of recommandation of what the user answered. The result will be on the __Home page__ so the first wine and cheese he likes 
will be recommanded on the page.

| Field Name    | Type             |
| ------------- | ---------------- |
| cheesestrengh | list             |
| cheesetexture | list             |
| language      | languageproperty |
| milktype      | list             |
| winestyle     | list             |
| winetype      | list             |
| email         | text             |
| modified date | date             |
| created date  | date             |
| slug          | text             |
 
 ## 7.Technical Constraints

The database will be created on __Bubble.io__ and __FireBase__ with structured data types including `Product`, `Pairing`, and `User`. The system must not rely on native mobile installation. The application should function in a browser environment using responsive design principles and should preload essential data to ensure it functions offline. All media (images, labels) should be optimized for performance. Bubble's built-in logic and plugin ecosystem (such as barcode scanning support) will be leveraged to handle product recognition and conditional recommendations.

## 8. Integration
Photos, product descriptions, and the price will be sourced directly from the document that Intermarché sends us. The Champagne and cider categories may be added as an extension of the wine dataset if required.

## 9. Supported Browsers
### 9.1 Browser Support Summary
Base on the __Bubble documention__, supported browsers will be :
- Safari
- Edge
- Firefox
- Chrome
- Brave

Also, they advise to always keep those browsers updated to dodge problems with the user usage of a bubble web app.

### 9.2 Edit-Mode
The __edit-mode__ is the developer interface to make apps or webapps.
Also base on the __Bubble documetion__, the browses are also supported on:
- Safari
- Edge
- Firefox
- Chrome
- Brave
  
Again, we will have to keep the browser updated so as not to encounter problems with the saving of our modifications for the product.


## 10. Future Improvement 
If the demo proves successful and has a measurable impact on sales, the project may be expanded to other Intermarche locations. Also, we can add more types of products like beef, fish, bakery, and more.
Maybe the fact of adding some client feedback on a certain product to have a more accurate pairing option. There is a Bubble functionality that can convert the webapp into an app that is on the __App Store__ for Apple phones or on __Google Play__ for Android phones. Finally of other languages can be added for the future for more people who are visiting the webapp in France.


## 11. Glossary 

#### **Bubble.io**
A no-code platform used to build the web app without traditional programming.

#### **NoCode**
A development method using visual tools instead of code to create apps.

#### **Web App**
An application accessed via a browser on phones or computers — no installation needed.

#### **QR Code**
A scannable code placed at the store entrance to quickly access the app.

#### **FireBase**
The Firebase Realtime Database is a cloud-hosted NoSQL database that lets organizations store and sync data in real time across all of their users' devices. This makes it easy to build apps that are always up to date, even when users are offline. 

#### **EAN Code**
A barcode used to identify products like cheese or wine.

#### **ITM8**
Intermarché’s internal reference code for product tracking.

#### **BarCode Scanner Plugin**
A plugin used in Bubble to scan product barcodes with a smartphone camera.

#### **Magic Link**
A personal URL sent by email or SMS, allowing users to return to their saved preferences without logging in.

#### **Local Data**
Information (like language or taste preferences) stored in the user’s browser for a personalized experience.

#### **Pairing**
A match between a wine and cheese product, stored in the database with a compatibility score.

#### **Responsive Design**
Design that adapts the app layout for smartphones, tablets, or desktops.

#### **Product Database**
Structured storage of wines and cheeses, including name, price, barcode, category, etc.

#### **User Preferences**
Taste or texture options selected by users to generate custom recommendations. --> ## 10. Glossary 

#### **Bubble.io**
A no-code platform used to build a web app without traditional programming.

#### **NoCode**
A development method using visual tools instead of code to create apps.

#### **Web App**
An application accessed via a browser on phones or computers — no installation needed.

#### **QR Code**
A scannable code is placed at the store entrance to quickly access the app.

#### **FireBase**
The Firebase Realtime Database is a cloud-hosted NoSQL database that lets organizations store and sync data in real time across all of their users' devices. This makes it easy to build apps that are always up to date, even when users are offline. 

#### **EAN Code**
A barcode is used to identify products like cheese or wine.

#### **ITM8**
Intermarché’s internal reference code for product tracking.

#### **Barcode Scanner Plugin**
A plugin used in Bubble to scan product barcodes with a smartphone camera.

#### **Magic Link**
A personal URL sent by email or SMS, allowing users to return to their saved preferences without logging in.

#### **Local Data**
Information (like language or taste preferences) is stored in the user’s browser for a personalized experience.

#### **Pairing**
A match between a wine and a cheese product, stored in the database with a compatibility score.

#### **Responsive Design**
Design that adapts the app layout for smartphones, tablets, or desktops.

#### **Product Database**
Structured storage of wines and cheeses, including name, price, barcode, category, etc.

#### **User Preferences**
Taste or texture options selected by users to generate custom recommendations.


[def]: Flow.png