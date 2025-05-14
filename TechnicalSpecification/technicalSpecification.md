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
      - [4.4.1 Why This Matters](#441-why-this-matters)
      - [4.4.2How It Works](#442how-it-works)
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
      - [**EAN Code**](#ean-code)
      - [**ITM8**](#itm8)
      - [**BarCode Scanner Plugin**](#barcode-scanner-plugin)
      - [**Magic Link**](#magic-link)
      - [**Local Data**](#local-data)
      - [**Pairing**](#pairing)
      - [**Responsive Design**](#responsive-design)
      - [**Product Database**](#product-database)
      - [**User Preferences**](#user-preferences)
  
</details>

## 1.Project Summary
__Conseil Intermarché__ is a web app solution for customers, it help them by giving recommendation for now only on cheese and wine. It will also allow product to be scan, multiple language will be supported by the wep app and the web app provides a personalized experience for users. We will use Bubble to make Conseil Intermarché.
## 2.Technical Requirements
__Programing Language__ : NoCode will be use for this project.

__Supported Devices__ : The devices that will be supported will mostly be the smartphone and also computers.

__Supported Languages__ : The two most important one are French and English.

__An Easy Access And Interface__ : To access the web app, there will be a QR code at the entry of the store. Also the interface will be very intuitive using blocks and sections like (wine, cheese etc).

__Products__ All the products of the web app has been given by the client with the __ITM8__ and the __EAN__. There is also the prices, the quantities and the price/kg.
**Project:** Wine & Cheese Recommendation Web App  

**Client:** Intermarché Saint-Rémy-de-Provence  

**Target Users:** General public, including foreign tourists  
## 3 Styles
The style we will use are mainly the __red__,__black__ and __white__.
Because they are the main colors of the intermarché logo and theme.
## 4.Features 
### 4.1 Language Selection
You will be able to choose between __French__ and __English__

### 4.2 Personalized Interface
#### 4.2.1 Preferences of users
There will be a total of 3 to 5 questions about what the customer likes about wine tastes, cheese texture etc. The user have the prossibilty to skip those questions if he want to directly access the web app. The answer will be saved in the local data.
Also the questions will be like a popup when you first open the web app
#### 4.2.2 Dynamic Interface
The web app will give the user an __unique interface__ based on the local data of the user. Each web app interface will be different if the answers are not the same.

### 4.3 Scan
You will be able to scan the barcode of the product. The web app will shows the description and recommend other merchandise that is good with the scanned product. To make it work, we will use a pluging called __BarCode Scanner__ that we can add on Bubble

### 4.4 Superlink
To allow occasional follow-up, promotions, or sending pairing guides via email, we’re adding a __Magic Link__ system. This feature lets users input their name and email or phone number, and receive a personal link to revisit their wine/cheese suggestions or pairing history.

#### 4.4.1 Why This Matters
It avoids logins or account creation — frictionless and GDPR-conscious.Also it re-engages interested customers with minimal tech. This can be used in future campaigns, especially during wine & cheese events.

#### 4.4.2How It Works
User browses the app normally. At any point, they can tap “Save and Send Link”, after a short form appears to collect name and contact (email or phone). Bubble generates a unique URL tied to their browsing session or preferences. Finnaly this link is sent to them automatically. When they reopen it, their saved pairings are restored instantly.

## 5.DataBase
### 5.1 Product

#### 5.1.1 Data Management Of Products

The core dataset includes two main categories of products: wines and cheeses. Each product has a name, description in both French and English, a price (sourced either from Intermarché’s internal base or direct suppliers), and a classification into subcategories such as "red wine", "soft cheese", etc. Fromages often have pricing by weight (per kilogram), and units sold may vary significantly (e.g., full wheels vs. small portions), so this distinction must be managed clearly in the database.

Each product also includes a reference code (ITM8), a barcode (EAN), and a location tag to reflect its physical placement in the store’s layout. The store uses Zebra devices to track barcode positioning, which can be used to support future in-store geolocation features.

The product database will be imported from curated Excel files for best-selling wines and cheeses, cleaned and structured in Bubble’s database. Pairing data between wine and cheese will be managed separately and can be generated manually or algorithmically based on sales data and predefined flavor compatibility rules.

| Field Name          | Type   |
| ------------------- | ------ |
| name\_fr            | text   |
| name\_en            | text   |
| description\_fr     | text   |
| description\_en     | text   |
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

| Field Name | Type    |
| ---------- | ------- |
| wine       | Product |
| cheese     | Product |
| score      | number  |
| notes\_fr  | text    |
| notes\_en  | text    |


### 5.4 User
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

The app will be built entirely on Bubble.io, with structured data types including `Product`, `Pairing`, and `UserSession`. The system must not rely on native mobile installation. The application should function in a browser environment using responsive design principles, and should preload essential data to ensure it functions offline. All media (images, labels) should be optimized for performance. Bubble's built-in logic and plugin ecosystem (such as barcode scanning support) will be leveraged to handle product recognition and conditional recommendations.

## 7. Integration
Photos and product descriptions may be sourced directly from Intermarché’s public product catalog. The Champagne and cider categories may be added as an extension of the wine dataset if required.

## 8. Supported Browsers
### 8.1 Browser Support Summary
Base on the __Bubble docs__, it is supported on:
- Safari
- Edge
- Firefox
- Chrome
- Brave

Also we encourage the users to update their browsers to the lastest version.

### 8.2 Edit-Mode
The __edit-mode__ is the developer interface to make apps or webapp
Also base on the __Bubble docs__, it is supported on:
- Safari
- Edge
- Firefox
- Chrome
- Brave

## 9. Future Improvement 
If the demo proves successful and has a measurable impact on sales, the project may be expanded to other Intermarche locations. Also we can add more type products like beef, fish, bakery and more.
Maybe the fact to add some client's feedbacks on certain product to have more accurate pairing options.

## 10. Glossary 

#### **Bubble.io**
A no-code platform used to build the web app without traditional programming.

#### **NoCode**
A development method using visual tools instead of code to create apps.

#### **Web App**
An application accessed via a browser on phones or computers — no installation needed.

#### **QR Code**
A scannable code placed at the store entrance to quickly access the app.

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
Taste or texture options selected by users to generate custom recommendations.
















