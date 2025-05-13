# Naming convention 
## Author
|Name|Role|
|----|----|
|NOGUES Loic|Technical Leader|
## 1. Bubble
### 1.1 General Guidelines
* **Use descriptive names**: Element names should clearly describe their purpose. Make them unique for quick reference.
* **Be consistent**: Apply a consistent naming pattern throughout the app.
* **Avoid default names**: When duplicating elements, rename them. Don’t leave names like “copy of …”.
---
### 1.2 Data Types and Fields
* **Data types**: Use **singular** form and **camelCase** (e.g., `user`, `product`, `order`).
* **Option sets**: Prefix with `OS_`, e.g., `OS_Status`.
* **Fields**: Use descriptive camelCase names relevant to their purpose and type (e.g., `isAdmin`, `orderDate`).
* **Custom states**: Prefix with `CS_`, e.g., `CS_isLoading`.
---
### 1.3 Page Elements
Name elements using the following prefixes, followed by a descriptive name:
| Element Type     | Prefix Format | Example                |
| ---------------- | ------------- | ---------------------- |
| Group            | `G:`          | `G:ProductDetails`     |
| Repeating Group  | `RG:`         | `RG:UserList`          |
| Floating Group   | `FG:`         | `FG:HeaderMenu`        |
| Popup            | `P:`          | `P:DeleteConfirmation` |
| Reusable Element | `RE:`         | `RE:Navbar`            |
---
### 1.4 Styles
* **Buttons / Groups**: Use a descriptive name related to state or context (e.g., `accepted`, `rejected`, `popupPrimary`).
* **Fonts**: Format → `{{fontName}}_{{color}}_{{alignment}}_{{size}}_{{weight}}`
  Example: `Arial_blue_left_18_500`.
---
### 1.5 Pages
* **Clone pages**: Indicate the date or purpose in the name.
  Format: `{{pageName}}_{{YYYYMMDD}}` or `{{pageName}}_{{purpose}}`
  Example: `main_clone_20230811` or `main_ai_test`.
> :coche_blanche: This helps identify the relevance and intent of a clone, especially with multiple versions.
---
## 2. GitHub Repository
### 2.1 Repository Names
* Use **kebab-case**
  Example: `bubble-client-dashboard`
### 2.2 Folder Names
* Use **PascalCase**
  Example: `UserProfile`, `AdminPanel`
### 2.3 File Names
* Use **camelCase**
  Example: `userService.pdf`, `loginModal.md`