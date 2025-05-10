# Fonctional Specifications - Intermarché WEB APP

## Author

|       Name       |       Role       |
| ---------------- | ---------------- |
| Yann-Maël Bouton | Program Manager  |

## Modification

|       Date       |    Description    |
| ---------------- | ----------------- |
|    28/04/2025    | Creation of the document |
|    30/04/2025    | Started filling section  |
|    05/05/2025    | Added stackholder & success criteria |
|    11/05/2025    | completed the all document (only mockup need to be finished) |

---

<details>
<summary>Table of content</summary>

- [1. Introduction](#1-introduction)  
  - [1.1 Purpose](#1-1-purpose)  
  - [1.2 Scope of Functional Specifications](#1-2-scope-of-functional-specifications)  
  - [1.3 Definitions & Acronyms](#1-3-definitions--acronyms)  
  - [1.4 Stakeholders](#1-4-stakeholders)  
  - [1.5 References](#1-5-references)  

- [2. Business Context](#2-business-context)  
  - [2.1 Problem Statement](#2-1-problem-statement)  
  - [2.2 Objectives & Goals](#2-2-objectives--goals)  
  - [2.3 Success Criteria](#2-3-success-criteria)  

- [3. Functional Scope](#3-functional-scope)  
  - [3.1 In-Scope Features](#3-1-in-scope-features)  
  - [3.2 Out-of-Scope Items](#3-2-out-of-scope-items)  

- [4. User Roles & Permissions](#4-user-roles--permissions)  
  - [4.1 User Roles](#4-1-user-roles)  
  - [4.2 Permission Matrix](#4-2-permission-matrix)  

- [5. Use Cases & User Stories](#5-use-cases--user-stories)  
  - [5.1 Use Case List](#5-1-use-case-list)  
  - [5.2 Detailed Use Cases](#5-2-detailed-use-cases)

- [6. Functional Requirements](#6-functional-requirements)  
  - [6.1 Overview & Prioritization](#6-1-overview--prioritization)  
  - [6.2 Module A: Feature Name](#6-2-module-a-feature-name)  
  - [6.3 Module B: Feature Name](#6-3-module-b-feature-name)  
  - [6.4 Traceability Matrix](#6-4-traceability-matrix)  

- [7. Wireframe References](#7-wireframe-references)  

- [8. High-level database architecture](#8-high-level-database-architecture)  

- [9. Privacy & Security Considerations](#9-privacy--security-considerations)

- [10. Business Rules](#10-business-rules)  

- [11. Non-Functional Considerations](#11-non-functional-considerations)  
  - [11.1 Performance Expectations](#11-1-performance-expectations)  
  - [11.2 Compliance & Regulations](#11-2-compliance--regulations)  

</details>

---

## 1. Introduction

### 1.1 Purpose

Create and implement a very easy-to-use, bilingual, and progressive online application that can be accessed using a QR code at the store's entry. The objective is to increase sales and improve the shopping experience for visitors in the wine and cheese sections.

### 1.2 Scope of Functional Specifications

Covers all in-scope features including product lookup, recommendations, bilingual UI, and QR-code access. Excludes native apps, full backend/admin interface, offline capability, barcode scanning and integration beyond top-100 products.

### 1.3 Definitions & Acronyms

  - PWA: Progressive Web App
  - QR: Quick Response
  - EAN: European Article Number (barcode standard)
  - ITM8: Intermarché internal barcode prefix
  - Slack: Team collaboration platform

### 1.4 Stakeholders

| Name              | Fonction          |
| ----------------- | ----------------- |
| Yann-Maël BOUTON  | Program Manager   |
| Geoffrey DELRIEU  | Project Manager   |
| Loïc NOGUES       | Technical Lead    |
| Alexis SANTOS     | Software Engineer |
| Salaheddine NAMIR | Quality Insurance |
| Michel RIFF       | Technical Writer  |
| Franck JEANNIN    | Supervisor        |
| Intermarché       | Client            |

## 2. Business Context

### 2.1 Problem Statement

Tourists in the wine & cheese aisles quick product information and pairing guidance, leading to decision delays and missed upsell opportunities.

### 2.2 Objectives & Goals

Reduce product decision time to under 30 seconds, increase cross-sell rate by 15% among scanned items and highlight unknown wines to drive incremental revenue.

### 2.3 Success Criteria

- 20% uplift in average cart size from wine/cheese sections
- Positive user satisfaction feedback ≥4/5

## 3. Functional Scope

#### In-Scope Features

  - Personalized user experiences (UI/UX) throught question list.
  - Display high resolution product images.
  - Hidden feedback to enhance recommandation.
  - Recommended pairings and recipe suggestions.
  - Bilingual UI (minimum language : EN and FR).
  - Search engine for product.
  - User authentification throught SMS/EMAIL magic link.
  - Barcode/EAN scanning via device camera that will redirect on the page of the product.

#### Out-Scope Features

  - Admin panel to add, modify or delete product.
  - Native app (available on play store and apple store) / Shortcut app.
  - Integration beyond top-100 product.

## 4. User Roles & Permissions

### 4.1 User Roles

  - Shopper (anonymous)
  - Shopper (logged in) (* Shopper LI)
  - Store Staff (content update via admin platform) (OUT OF SCOPE)

### 4.2 Permission Matrix

| Role        | Scan Products | View Details | Apply Filters | Update Top-100 List | Save Own Experiences | Give Product Feedback |
|-------------|---------------|--------------|---------------|---------------------|----------------------|-----------------------|
| Shopper     | ✔️            | ✔️           | ✔️            | ✖️                 | ✖️                 | ✖️                   |
| Shopper LI  | ✖️            | ✖️           | ✖️            | ✔️                 | ✔️                 | ✔️                   |
| Store Staff | ✖️            | ✖️           | ✖️            | ✔️                 | ✖️                 | ✖️                   |

## 5. Use Cases & User Stories

### 5.1 Use Case List

  - access app: Scan store QR code → Select language → (Optional) Login → Complete preference quiz → Browse recommendations.
  - view product: Search or browse list → Select item → View images, description, pairings.
  - personalize: Answer up to 5 quick preference questions (wine type, style, cheese texture, milk type, strength).
  - save session: After 5 interactions, prompt magic-link registration for enhanced personalization.
  - barcode scanner: Scan product barcode -> redirect on product page.

### 5.2 Detailed Use Cases

UC1: Access App
- Actors: Guest Shopper, Logged-in Shopper
- Preconditions: User is in-store and scans the QR code displayed in the wine or cheese aisle.
- Main Flow:

  1. User scans QR code with his smartphone, tablet, mobile phone or any other device.
  2. PWA loads and shows a language selector (FR/EN).
  3. User selects preferred language.
  4. The system queries whether the user already has a session token.
     1. In case a token exists, then the execution goes on to step 7.

  5. User is asked to complete a quick preference quiz (optional on first visit).
  6. User may enter email/SMS to receive a magic link for login (optional).
  7. System displays the personalized home screen with product recommendations and catalog access.

- Alternative Flows:
  A1: User skips quiz and magic link entry → System proceeds with default recommendations in guest mode.
- Postconditions: App home screen is rendered with appropriate navigation and recommendations.

UC2: View Product Details

- Actors: Guest Shopper, Logged-in Shopper
- Preconditions: User has successfully accessed the app (UC1 completed).
- Main Flow:

  1. User navigates using search, filters.
  2. User choose a product from the results list.
  3. The system shows the product's details page with the following information:

     - Clear, large images
     - Product name, origin, and description
     - Recommended pairings (wine with cheese and vice versa)

  4. The user can move back for browsing or select other products for viewing.

- Alternative Flows:
  A1: After a user makes a search, and the system does not bring up any results → The system shows 'No matches found' and recommends that the user clears the filters or uses other keywords.
- Postconditions: User has watched detailed info as well as pairing suggestions.

UC3: Get Personalized Recommendations

- Actors: Guest Shopper, Logged-in Shopper
- Preconditions: User is on home or product listing screen and either first-time user or chooses to update preferences.
- Main Flow:

  1. User taps the "Preferences" icon/button.
  2. System presents up to 5 questions on styles and preferences.

    - Preferred wine types (e.g.: red, white)
    - Style preferences (e.g.: full-body, crisp)
    - Cheese texture (e.g.: soft, hard)
    - Milk type (e.g.: cow, goat, sheep)
    - Intensity/strength

  3. User answers the questions, system applies the logic of skipping on the basis of responses of questions.
  4. System recalculates and displays new recommendations.

- Alternative Flows:
  A1: User quits quiz midway → System keeps previous / default preference set and updates only based on completed answers.
- Postconditions: The Recommendations given have to match the user's explicitly stated preferences.

UC4: Save Session & Prompt Registration

- Actors: Guest Shopper
- Preconditions: The current user has at least interacted with five products during the ongoing session.
- Main Flow:

  1. The system track the user's contacts with the products (views, filters applied, quiz participation).
  2. After the fifth interaction, the system gives a one-time registration prompt.
  3. The prompt is telling about the benefits of saving preferences and order history.
  4. User types his email or phone number.
  5. System forwards a magic link for authentication.
  6. User clicks on the magic link and gets logged in.

- Alternative Flows:
  A1: User says no to registration → The system remains in guest mode and reprompts the user again only once per session.
- Postconditions: Registered users have their sessions stored after visits and can store their favorite products and preferences.

UC5: Scan Product Barcode

- Actors: Guest Shopper, Logged-in Shopper
- Preconditions: User is in possession of a physical product with a scannable barcode and is on either the home or the catalog screen.
- Main Flow:

  1. User click on the barcode scanner icon/button.
  2. System turns on the device camera to do the barcode scan.
  3. User positions the barcode in the camera frame.
  4. System reads the barcode and looks for the product in database.
     1. If the product is found, system redirects user to the product detail page (per UC2 flow).

  5. User checks the product detail page or goes back to the scanner.

- Alternative Flows:
  A1: User cancels scan → The system stops the camera and the user is directed to the previous screen.
  A2: Camera access denied → The system shows the permission error and prompts the user to do a manual search.
  A3: Barcode not recognized → The system displays the message 'Product not found' with an option to go to the catalog.
- Postconditions: Product detail page is shown if the product was found, otherwise, the user is still on the scanning interface with an error message.

## 6. Functional Requirements

### 6.1 Overview & Prioritization

| ID   | Feature                                        | Priority |
|------|------------------------------------------------|----------|
| FR1  | QR-code scan entry point                       | Must     |
| FR2  | Barcode/EAN camera scanner                     | Could    |
| FR3  | Product detail page                            | Must     |
| FR6  | Multilingual support                           | Must     |
| FR7  | Offline caching of top-100                     | Should   |
| FR8  | Personalization filters                        | Must     |
| FR9  | Personalized User Experiences (Question List)  | Must     |

## 7. Wireframe References

## 8. High-level database architecture

  **Option Sets:**

  - Category: Wine, Cheese
  - InteractionType: view, filter, quiz, scan, click, like
  - WineType: Red, White, Rosé, Sparkling
  - Style: Full-body, Crisp, Fruity, Earthy
  - CheeseTexture: Soft, Semi-soft, Hard
  - MilkType: Cow, Goat, Sheep
  - Intensity: Mild, Medium, Strong

  **Data Types:**

  | Data Type          | Field                   | Type                               |
  | ------------------ | ----------------------- | ---------------------------------- |
  | User               | Email                   | email (optional)                   |
  |                    | Phone                   | text (optional)                    |
  |                    | PreferredWineTypes      | list of WineType (option set)      |
  |                    | PreferredStyles         | list of Style (option set)         |
  |                    | PreferredCheeseTextures | list of CheeseTexture (option set) |
  |                    | PreferredMilkTypes      | list of MilkType (option set)      |
  |                    | PreferredIntensities    | list of Intensity (option set)     |
  |                    | CreatedAt               | date                               |
  | Session            | User                    | User                               |
  |                    | Token                   | text                               |
  |                    | ExpiresAt               | date                               |
  |                    | CreatedAt               | date                               |
  | Product            | Name                    | text                               |
  |                    | Category                | Category (option set)              |
  |                    | Origin                  | text                               |
  |                    | Description             | text (multiline)                   |
  |                    | Image                   | image                              |
  |                    | RatingAvg               | number                             |
  |                    | WineType                | WineType (option set)              |
  |                    | Style                   | Style (option set)                 |
  |                    | CheeseTexture           | CheeseTexture (option set)         |
  |                    | MilkType                | MilkType (option set)              |
  |                    | Intensity               | Intensity (option set)             |
  | Barcode            | Product                 | Product                            |
  |                    | CodeValue               | text                               |
  | ProductInteraction | Session                 | Session                            |
  |                    | Product                 | Product                            |
  |                    | InteractionType         | InteractionType (option set)       |
  |                    | CreatedAt               | date                               |
  |                    | Details                 | text (optional)                    |
  | Recommendation     | User                    | User (optional)                    |
  |                    | Session                 | Session (optional)                 |
  |                    | Products                | list of Product                    |
  |                    | Scores                  | list of number                     |
  |                    | GeneratedAt             | date                               |

## 9. Privacy & Security Considerations

- HTTPS/TLS for all requests and responses
- Data that is very sensitive should be encrypted e.g. tokens, etc.
- Send out limited-time-use magic-link tokens that are secure and which can only be used once
- Allow access to the system only for users who have the relevant role and make sure that each input is valid

## 10. Business Rules

- Our only concern is the wine and cheese.
- Personalization updates only after user interaction (quiz, click, like)
- Always honor the users selected language for UI and content

## 11. Non-Functional Considerations

### 11.1 Performance Expectations

- Initial PWA load time < 2 seconds on a 3G connection
- Barcode scan → detail page navigation < 1 second
- Average API response time < 1.5 seconds on a 3G connection
- Cache static assets and API responses via Service Worker

### 11.2 Compliance & Regulations

- GDPR: minimal data retention, explicit opt-in for any personal data
- Accessibility: comply with WCAG 2.1 AA for contrast, keyboard navigation, and labels
- Ensure all analytics data is anonymized and stored in accordance with privacy policy