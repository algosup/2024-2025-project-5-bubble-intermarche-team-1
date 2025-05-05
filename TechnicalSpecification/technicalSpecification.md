# Technical Specification
## Author
|Name|Role|
|----|----|
|NOGUES Loic|Technical Leader|
## 1.Project Summary
__Conseil Intermarché__ is a web app solution for customers, it help them by giving recommendation for now only on cheese and wine. It will also allow product to be scan, multiple language will be supported by the wep app and the web app provides a personalized experience for users. We will use Bubble to make Conseil Intermarché.
## 2.Core Requirements
__Programing Language__ : NoCode will be use for this project.

__Supported Devices__ : The devices that will be supported will mostly be the smartphone and also computers.

__Supported Languages__ : The two most to implement is French and English.

__An Easy Access And Interface__ : To access the web app, there will be a QR code at the entry of the store. Also the interface will be very intuitive using blocks and sections like (wine, cheese etc).

__Products__ All the products of the web app has been given by the client with the __ITM8__ and the __EAN__. There is also the prices, the quantities and the price/kg.

## 3.Features 
### 3.1 Language Selection
You will be able to choose between __French__ and __English__

### 3.2 Personalized Interface
#### 3.2.1 Preferences of users
There will be a total of 3 to 5 questions about what the customer likes about wine tastes, cheese texture etc. The user have the prossibilty to skip those questions if he want to directly access the web app. The answer will be saved in the local data.
#### 3.2.2 Dynamic Interface
The web app will give the user an __unique interface__ based on the local data of the user. Each web app interface will be different if the answers are not the same.

### 3.3 Scan
You will be able to scan the barcode of the product. The web app will shows the description and recommend other merchandise that is good with the scanned product. To make it work, we will use a pluging called __BarCode Scanner__ that we can add on Bubble

### 3.4 Superlink
The superlink is basically our way to save the data that the customer put. The data saved will be the questions and their phone number. To receive this superlink, the user will have to enter his phone number.












## 2.Naming convention 
### 2.1 Bubble
#### 2.1.1 General Rules
a)Use descriptive names: Element names should clearly describe the purpose of the element. Keep it unique for quick reference.

b)Consistency: Maintain a similar pattern throughout.

c)If an element is duplicated, make sure to rename the new element. Don’t leave it as copy.



#### 2.1.2 Data Types

a) Name data types in singular form and in camel 
case. For example, ‘user’, ‘product’, ‘order’.

b) Name option sets as OS_{{optionset_name}}.

c) For fields within data types, give descriptive names according to their data type and purpose.

d) Custom States: CS_states.

#### 2.1.3 Page Elements

Name the elements by their acronym followed by the name.

a)Groups: G:{{group_name}}.

b)Repeating Groups: RG:{{repeating_group_name}}.

c)Focus Groups: FG:{{floating_group_name}}.

d)Popup P:{{popup_name}}.

e)Reusable Elements RE:{{reusable_element_name}}.

#### 2.1.4 Styles

a)Buttons & Groups-> {{style_name}} e.g rejected, accepted, popup.

b)Fonts → {{font_name}}{{font_colour}}{{font_alignment}}{{font_size}}{{font_width}} e.g Arial_blue_left_18_500.

#### 2.1.5 Pages

When creating a clone, mention the current date against it. {{page_name}}{{current_date}}. This will help us find the relevance of the clone page, especially when there are multiple clones. Or the purpose of clone {{page_name}}{{purpose}} E.g main_clone_110823 or main_ai_test.

This convention will provide a good understanding and an organize project.

### 2.2 Github Repository

#### 2.2.1 Repository names
The repository names will be in kebab case : {{kebab_case}}.

#### 2.2.2 Folder names
The folder names will be in pascal case : {{PascalCase}}.

#### 2.2.3 File names
The file names will be in camel case : {{camelCase}}.

