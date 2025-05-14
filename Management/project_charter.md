
# Project Charter – Bubble PWA for Intermarché Saint-Rémy-de-Provence

<details>
<summary><b>Table Of Contents</b></summary>

  * [Team Members](#team-members)
  * [Scope](#scope)

    * [Project Purpose](#project-purpose)
    * [Target Audience](#target-audience)
    * [Core Features](#core-features)
    * [Out of Scope](#out-of-scope)
  * [Limitations](#limitations)

    * [Constraints](#constraints)
    * [Risks](#risks)
  * [Stakeholders](#stakeholders)
  * [Communication](#communication)
  * [Responsibilities](#responsibilities)
  * [Deadlines](#deadlines)
  * [Resources](#resources)

</details>

---

## Team Members

| Name              | Role              |
| ----------------- | ----------------- |
| Yann-Maël BOUTON  | Program Manager   |
| Geoffrey DELRIEU  | Project Manager   |
| Salaheddine NAMIR | Quality Assurance |
| Alexis SANTOS     | Software Engineer |
| Loïc NOGUES       | Technical Lead    |
| Michel RIFF       | Technical Writer  |

---

## Scope

### Project Purpose

Design and deliver a **bilingual, ultra-simple Progressive Web App (PWA)** accessible via QR code at the store entrance of **Intermarché Saint-Rémy-de-Provence**.
The aim is to **boost wine and cheese sales**, improve user experience for international tourists, and reinforce the store’s innovative and customer-friendly image.

---

### Target Audience

* **Affluent international tourists**
* **Local non-regular customers**
* **Intermarché staff** (to maintain a top-selling product list via Slack)

---

### Core Features

#### 1. Product Discovery via Barcode

* Scan any **wine or cheese product barcode (EAN)** to:

  * Show product photos (fetched online)
  * Display detailed product info (origin, tasting notes)
  * Recommend pairings (wine ↔ cheese)
  * Suggest recipes

#### 2. In-Store Navigation

* Use barcode to **locate the product** in the aisle (using store-provided devices like Zebra)

#### 3. Smart Recommendations

* Recommend complementary items
* Filters: dietary (vegan, halal, alcohol-free), country of origin, etc.

#### 4. Technical Features

* **Progressive Web App** (offline-capable, installable via QR code)
* **Multilingual Interface** (English & French, others if possible)
* **Mobile-first design**, lightweight and fast
* No login or user account required

---

### Out of Scope

* Full back-office admin interface
* Multi-store deployment
* Customer account system

---

## Limitations

### Constraints

* PWA must work offline or in low-connectivity environments
* Compatible with all recent smartphones
* Must integrate Intermarché barcodes (ITM8 / EAN)

### Risks

* Barcode data availability and accuracy
* Limited control over product metadata (external sources)
* Tourist language diversity
* Shelf location data not fully accessible

---

## Stakeholders

| Role              | Representative                     |
| ----------------- | ---------------------------------- |
| Client            | Intermarché Saint-Rémy-de-Provence |
| Technical Contact | Chrys (on-site staff)              |

---

## Communication

* Internal: Slack, GitHub
* External: Meetings with Chrys and store staff
* Testing: Potential user testing with real customers via Chrys

---

## Responsibilities

| Team Member       | Responsibility                                                              |
| ----------------- | --------------------------------------------------------------------------- |
| Yann-Maël BOUTON  | Define project scope and client communication                               |
| Geoffrey DELRIEU  | Task planning, tracking progress, risk management                           |
| Salaheddine NAMIR | Define test plan, run functional tests, ensure client requirements are met  |
| Alexis SANTOS     | Implement core features (barcode scan, pairing system, multilingual UI)     |
| Loïc NOGUES       | Lead technical decisions, ensure code quality, manage development standards |
| Michel RIFF       | Write clear documentation for users and stakeholders                        |

---

## Deadlines

| Date       | Milestone                     |
| ---------- | ----------------------------- |
| 13/05/2025 | Requirements and UX draft     |
| 20/05/2025 | Technical Specification ready |
| 27/05/2025 | First working prototype       |
| 03/06/2025 | Testing phase                 |
| 10/06/2025 | Final version demo            |

---

## Resources

* **Budget:** None (demo only)
* **Team Size:** 6 people



