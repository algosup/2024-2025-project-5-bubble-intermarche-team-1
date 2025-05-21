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
  - [3 Styles](#3-styles)
  - [4.Features](#4features)
    - [4.1 Language Selection](#41-language-selection)
    - [4.2 Personalized Interface](#42-personalized-interface)
      - [4.2.1 Preferences of users](#421-preferences-of-users)
      - [4.2.2 Dynamic Interface](#422-dynamic-interface)
    - [4.3 Scan](#43-scan)
    - [4.4 Superlink](#44-superlink)
      - [4.4.1 How It Works](#441-how-it-works)
  - [5.DataBase](#5database)
    - [5.1 Product](#51-product)
      - [5.1.1 Data Management Of Products](#511-data-management-of-products)
    - [5.3 Pairing](#53-pairing)
    - [5.4 User](#54-user)
  - [6.Technical Constraints](#6technical-constraints)
  - [7. Integration](#7-integration)
  - [8. Supported Browsers](#8-supported-browsers)
    - [8.1 Browser Support Summary](#81-browser-support-summary)
    - [8.2 Edit-Mode](#82-edit-mode)
  - [9. Future Improvement](#9-future-improvement)
  - [10. Glossary](#10-glossary)
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

## 3 Styles
The style we will use are mainly the __red__, __black__ and __white__.
Because they are the main colors of the Intermarché logo and theme.
![](images/Logo.jpg)
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

## 5.DataBase
### 5.1 Product

#### 5.1.1 Data Management Of Products

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
| is\_direct\_sale    | yes/no |
| photo               | image  |
| unit\_type          | text   |
| average\_weight\_kg | number |
| geo\_location       | text   |
| popularity\_score   | number |
| added\_date         | date   |


### 5.3 Pairing 

This database will also be done on the site __Firebase__

The __Pairing__ database will be use for a certain product page. It will be done with looking up what's a good pairing or not. The recommandation will be done by also "likes" but also "dislike".

| Field Name      | Type    |
| --------------- | ------- |
| wine\_ITM8      | Product |
| cheese \_ITM8   | Product |
| description\_fr | text    |
| description\_en | text    |
| score           | number  |

### 5.4 User

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
 
 ## 6.Technical Constraints

The database will be created on __Bubble.io__ and __FireBase__ with structured data types including `Product`, `Pairing`, and `User`. The system must not rely on native mobile installation. The application should function in a browser environment using responsive design principles and should preload essential data to ensure it functions offline. All media (images, labels) should be optimized for performance. Bubble's built-in logic and plugin ecosystem (such as barcode scanning support) will be leveraged to handle product recognition and conditional recommendations.

## 7. Integration
Photos, product descriptions, and the price will be sourced directly from the document that Intermarché sends us. The Champagne and cider categories may be added as an extension of the wine dataset if required.

## 8. Supported Browsers
### 8.1 Browser Support Summary
Base on the __Bubble documention__, supported browsers will be :
- Safari
- Edge
- Firefox
- Chrome
- Brave

Also, they advise to always keep those browsers updated to dodge problems with the user usage of a bubble web app.

### 8.2 Edit-Mode
The __edit-mode__ is the developer interface to make apps or webapps.
Also base on the __Bubble documetion__, the browses are also supported on:
- Safari
- Edge
- Firefox
- Chrome
- Brave
  
Again, we will have to keep the browser updated so as not to encounter problems with the saving of our modifications for the product.


## 9. Future Improvement 
If the demo proves successful and has a measurable impact on sales, the project may be expanded to other Intermarche locations. Also, we can add more types of products like beef, fish, bakery, and more.
Maybe the fact of adding some client feedback on a certain product to have a more accurate pairing option. There is a Bubble functionality that can convert the webapp into an app that is on the __App Store__ for Apple phones or on __Google Play__ for Android phones. Finally of other languages can be added for the future for more people who are visiting the webapp in France.


## 10. Glossary 

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
