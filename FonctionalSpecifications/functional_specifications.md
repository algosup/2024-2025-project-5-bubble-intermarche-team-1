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
    - [5.2.1 Actors](#5-2-1-actors)  
    - [5.2.2 Preconditions](#5-2-2-preconditions)  
    - [5.2.3 Trigger](#5-2-3-trigger)  
    - [5.2.4 Main Flow](#5-2-4-main-flow)  
    - [5.2.5 Alternate Flows](#5-2-5-alternate-flows)  
    - [5.2.6 Postconditions](#5-2-6-postconditions)  

- [6. Functional Requirements](#6-functional-requirements)  
  - [6.1 Overview & Prioritization](#6-1-overview--prioritization)  
  - [6.2 Module A: Feature Name](#6-2-module-a-feature-name)  
  - [6.3 Module B: Feature Name](#6-3-module-b-feature-name)  
  - [6.4 Traceability Matrix](#6-4-traceability-matrix)  

- [7. User Interface Overview](#7-user-interface-overview)  
  - [7.1 Navigation Flow](#7-1-navigation-flow)  
  - [7.2 Wireframe References](#7-2-wireframe-references)  

- [8. Privacy & Security Considerations](#8-privacy--security-considerations)

- [9. Business Rules](#9-business-rules)  

- [10. Non-Functional Considerations](#10-non-functional-considerations)  
  - [10.1 Performance Expectations](#10-1-performance-expectations)  
  - [10.2 Compliance & Regulations](#10-2-compliance--regulations)  

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

#### Out-Scope Features

  - Barcode/EAN scanning via device camera that will redirect on the page of the product.
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

  - Shopper views product details and images 
  - Shopper applies filter preferences
  - Shopper views recommended pairings
  - Shopper scans a product barcode (Out Of Scope)
  - Staff updates top-100 via Admin Panel (Out Of Scope)

### 5.2 Detailed Use Cases

#### 5.2.1 Actors

 -

#### 5.2.2 Preconditions

 -

#### 5.2.3 Trigger

 -

#### 5.2.4 Main Flow

 -

#### 5.2.5 Alternate Flows

 -

#### 5.2.6 Postconditions

 -

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

### 6.2 Module A: Feature Name

 -

### 6.3 Module B: Feature Name

 -

## 7. User Interface Overview

### 7.1 Navigation Flow

 -

### 7.2 Wireframe References

 -

## 8. Privacy & Security Considerations

 -

## 9. Business Rules

 -

## 10. Non-Functional Considerations

### 10.1 Performance Expectations

 -

### 10.2 Compliance & Regulations

 -