## 1.Naming convention 
### 1.1 Bubble
#### 1.1 General Rules
a)Use descriptive names: Element names should clearly describe the purpose of the element. Keep it unique for quick reference.

b)Consistency: Maintain a similar pattern throughout.

c)If an element is duplicated, make sure to rename the new element. Don’t leave it as copy.



#### 1.2 Data Types

a) Name data types in singular form and in camel 
case. For example, ‘user’, ‘product’, ‘order’.

b) Name option sets as OS_{{optionset_name}}.

c) For fields within data types, give descriptive names according to their data type and purpose.

d) Custom States: CS_states.

#### 1.3 Page Elements

Name the elements by their acronym followed by the name.

a)Groups: G:{{group_name}}.

b)Repeating Groups: RG:{{repeating_group_name}}.

c)Focus Groups: FG:{{floating_group_name}}.

d)Popup P:{{popup_name}}.

e)Reusable Elements RE:{{reusable_element_name}}.

#### 1.4 Styles

a)Buttons & Groups-> {{style_name}} e.g rejected, accepted, popup.

b)Fonts → {{font_name}}{{font_colour}}{{font_alignment}}{{font_size}}{{font_width}} e.g Arial_blue_left_18_500.

#### 1.5 Pages

When creating a clone, mention the current date against it. {{page_name}}{{current_date}}. This will help us find the relevance of the clone page, especially when there are multiple clones. Or the purpose of clone {{page_name}}{{purpose}} E.g main_clone_110823 or main_ai_test.

This convention will provide a good understanding and an organize project.

### 2. Github Repository

#### 2.1 Repository names
The repository names will be in kebab case : {{kebab_case}}.

#### 2.2 Folder names
The folder names will be in pascal case : {{PascalCase}}.

#### 2.3 File names
The file names will be in camel case : {{camelCase}}.