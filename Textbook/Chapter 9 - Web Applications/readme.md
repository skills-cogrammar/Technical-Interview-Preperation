# Chapter 10 - Web Applications 
In the modern day, presentation is a very important part of what we do as software engineers and data scientists. As a data scientist, you need to represent your data in a way that is easy to extract important information, and as a software engineer, you need to create systems that are easy for users to navigate.

You could say that tools like Tableau offer a good enough interface for showing your data visualizations and CLI applications can be made easy to work with, the problem with these sources is that they are not exactly the most accessible way of doing things.

Everything these days is web based, people are slowly moving away from native development in favour of easily accessible web based tools. 

If you wanted to build a tool that converted converted PDFs into audiobooks, you can imagine the difference in users between having to tool be only available on desktop compared to having a web version.

Having a basic understanding of how to build web applications is beneficial as it allows you to independently build tools that are easily accessible even if you don't consider yourself a frontend developer. 

In this chapter, we will start at the basics of web development and take a look at HTML and CSS. These two tools will allow us to create the skeleton of a web page and add some polish to the way that it looks.

# 1 Introduction to HTML
HyperText Markup Language (HTML) is behind everything that we can view on the web, it provides the structure that we see on all web pages. 

## 1.1 Basic Structure 
```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
</body>
</html>
```
- Like other markup languages, HTML stores items based on relationships
	- Elements are made up of open and close tags.
	- Elements that are defined within other elements are considered child elements 
	- Changes to parent elements directly affect child elements 
	- The hierachy is important to how we structure the pages and implement our styling.
- Within our open tags, we can add additional information known as attributes,
	- Attributes allow us to change the functionality of the default elements 
	- Attributes allow us to like back to specific elements or a group of similar elements 
	- Attributes allow us to add some metadata to our elements.


### 1.1.1 `<html>`
The `<html> </html>` element is the root element for our entire web page, without it, we don't have an HTML page as all of the additional components we want to work with are children of this element.

### 1.1.2 `<head>`
The `<head></head>` element is used to store metadata about the webpage, this information can inlude details like the encoding of the web page as shown by the `<meta charset="UTF-8">` which states that the content of the page will be `UTF-8` characters.

In the head element, we can also include links to external sources like stylesheets that will allow us to add either our own custom styling to the page, or styling from external sources.

### 1.1.3 `<body>`
The `<body></body>` element is where all of the visible content for the page will be shown, any custom HTML that you would like to display must be put inside the body element.

## 1.2 Key Components 

### 1.2.1 Tags and Elements
An often confusing aspect of HTML is being able to tell the difference between a tag and an element, people often use the terms incorrectly which can lead to some confusion when trying to perform certain operations in the backend.

A tag is used to define the start and the end of an element, when working with HTML, we will in most situations have an open and close tag to define the start and end of an element, but in some cases we have what is known as a self closing tag which is an element that just requires a single tag with a special symbol at the end to show that the tag will self close.

Tags are really important in HTML as they define the scope of our element, if you forget to close a tag, you will have a lot of styling issues, missing closing tags are the cause of many styling errors that you will encounter when working with HTML.

```
<div>
    <input/>
</div>
```

**Open Close Tags**
As we can see in the code, the `div` element is made up of open and close tags, the open tags wrap the name of the element like `<tagname>`, this shows that this is the start of the element, to close the element, a `/` needs to be added in the close tag like `</tagname>`

The open and close tags are commonly used for elements that can be parts to other elements, for example, the `div` element is what we call a container, it's primary purpose is to store other HTML components. 

Open close tags are also used for text elements, for example, when we want to create a paragraph, we use the `<p></p>` element which needs to have opening and closing tags to show where the text will be contained.

**Self Closing**
The code example shows the `input` element which does not contain a regular open or close tag, this is is considered a self closing tag where we open and close the element on the same line.

Self closing tags are used when the element cannot take or does not need to take in any children, these types of elements usually make use of attributes to perform their desired operations.

A self closing element is defined by having the name of the element within `<>` and having a `/` after the name of the element like this `<input />`


### 1.2.2 Attributes 
Attributes in HTML can be thought of the same way as attributes in a class, they are used to define the characteristics of a given HTML element. Attributes are defined in the opening tag of our element and each HTML element will have it's own unqiue set of attributes to choose from, but there are a few attributes that can be used with all HTML elements, like the `style`, `class` and `id` which we will take a look at a bit later.

When you start working with HTML elements, it's worth doing some research online to find the element specific attributes that can be used. [mdn web docs](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)

```html
<div class="container" id="root">
    <a href="https://www.google.com">
	Click Here
    </a>
</div>
```
- The attributes are added to the opening tag of the element 
- We can have as many attributes as we want, but only one of each 
- Different elements have special attributes that's can't be used by all elements like the `href` for the `a` element.

## 1.3 Hierarchy
The structure of HTML pages is based on hierarchy, this hierarchy is important to the way that content is styled. Good UI design is based on grouping items together so that common styles can be applied. It also allows us to create component based designs where each small group is styled individually and put together to make up a whole page.

The concept of component based design is better described when working with libraries like React, but we can still encorparate element of component based design to plain HTML.

```html 
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>

<body>
</body>
</html>
```
- The first hierarchy that we can observe is the one between the `html` element:
	- We can't have the `head` and `body` without the `html`
	- The `head` and `body` elements are logically grouped within the same `html` element

*Zooming into the body section*
```html 
<body>
    <div style="margin-left: 50px">
	<div>
	    DIV GROUP 1
	</div>		
	<div>
            DIV GROUP 1
	</div>
    </div>

    <div style="background-color: brown">
	<div>
            DIV GROUP 2
	</div>		
	<div>
            DIV GROUP 2
	</div>
    </div>	
</body>
```

<body>
	<div style="margin-left: 50px">
		<div>
			DIV GROUP 1
		</div>		
		<div>
			DIV GROUP 1
		</div>
	</div>

	<div style="background-color: brown">
		<div>
			DIV GROUP 2
		</div>		
		<div>
			DIV GROUP 2
		</div>
	</div>	
</body>

- Contained in our `body` we have two `div` elements 
- Each `div` is a child of the `body` so any changes to `body` will affect both `div` elements 
- Each `div` has two children, when a style is applied to the parent `div` elements, the child elements are affected 
	- The first div is being moved to the right
	- The second div has changed it's colour.


### 1.3.1 Containers 
In order to implement hierarchy, knowing the elements that can be used to implement it is important.

Even though HTML allows us to add child components to any element with opening and closing tags, it's important to leave text elements to only storing text and container elements for containing other HTML elements.

Here is a list of the common container elements.

**Generic**

| Element | Description                                                              |
| ------- | ------------------------------------------------------------------------ |
| div     | Most versatile container, used for generic grouping of content           |
| span    | Inline container that can wrap a small amount of text or inline elements |
|         |                                                                          |
**Structural**

| Element | Description                                                                             |
| ------- | --------------------------------------------------------------------------------------- |
| header  | Defines the header section of a webpage that usually contains the navigation, logos etc |
| nav     | Contains the links to different parts of the website                                    |
| main    | The primary content area of the webpage                                                 |
| section | Defines thematic sections within a webpage, usually groups related content              |
| footer  | Contains the footer information for a page                                              |

**List**

| Element | Description                                           |
| ------- | ----------------------------------------------------- |
| ul      | Unordered list, makes use of bullet points by default |
| ol      | Ordered list, makes use of numbers by default         |

**Table**

| Element | Description                                            |
| ------- | ------------------------------------------------------ |
| table   | Defines a tabular data structure with rows and columns |

**Form**

| Element | Description                                                              |
| ------- | ------------------------------------------------------------------------ |
| form    | Creates forms for grouping input fields and submitting all input at once |

## 1.4 Identifying Elements 
Being able to identify your elements is very important when you want to add some functionality or styling to your elements.

### 1.4.1 Class Attribute
Class attributes are used to identify a group of elements that require some common action to be performed on them, this can either be a common style through CSS or common logic through JavaScript.

We can assign an element to as many classes as we need, but it's important to make sure that the classes you apply do not have conflicts as it's hard to predict which implementation will take preference.

```html 
<div class="container">        
    <div class="left child">
	LEFT
    </div>
    <div class="right child">
	RIGHT
    </div>
</div>
```
- The first div is of the `container` class 
- The left element has the `left` and `child` classes
	- When any actions are applied to either the `left` or `child` class group, the left element will be affected 

To reference a class directly in CSS or JavaScript, we will use the full stop before the class name to indicate that we are looking for a class. `.class-name`

Classes play a key role when working with styling libraries like bootstrap or tailwind as they have styles defined using class names and require you to assign the pre-written styles to an element by referencing the class name.


### 1.4.2 Id Attribute 
the id is used to uniquely identify an element, there can only be one element with a given id and each element can only have one id.

Id's are most important when working with JavaScript as they allow us to make changes to a specific element without the potential risk of changing more than 1 element like a class would.

```html 
<div id="container">        
    <div id="left-child">
	LEFT
    </div>
    <div id="right-child">
	RIGHT
    </div>
</div>
```

To reference an id in CSS or JavaScript, we need to use the hash before the id name. `#element-id`

### 1.4.3 Tag Name
When working with CSS and JavaScript, we can us the tag name almost like a class to reference all elements of a certain type.


# 2 Creating a Basic HTML Page
Once you understand the structure of components in HTML, you are good to go and start building out some basic web pages.

Using the knowledge from the last section, we are going to create a simple webpage and introduce some other tags that you might use regularly.

## 2.1 Simple Portfolio Page
```html 
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Resume</title>
</head>

<body>
    <section>
        <h1>
            Resume
        </h1>

        <h3>
            John Doe
        </h3>
    </section>

    <hr>

    <section>
        <h4>Experience</h4>
        <ul>
            <li>
                Software Architect - Facebook
            </li>

            <li>
                Technical Lead - Amazon
            </li>

            <li>
                Senior Software Engineer - Apple
            </li>

            <li>
                Mid-Level Software Engineer - Netflix
            </li>

            <li>
                Junior Software Engineer - Google
            </li>
        </ul>
    </section>

    <section>
        <h4>Skills</h4>
        <ul>
            <li>
                Golang
            </li>
            <li>
                Kafka
            </li>
            <li>
                Kubernetes
            </li>
            <li>
                Docker
            </li>
            <li>
                Flink
            </li>
            <li>
                Snowflake
            </li>
        </ul>
    </section>
</body>
</html>
```

- The `h1` tag is used to create a big heading, the heading sizes decrease as we increase the number that comes after `h`, eg `h3` is smaller than `h2`
	- headings are an example of text elements that are used for containing text values 
- The `<hr/>` is used to draw a line on the screen, it can not contain any elements, so it's self-closing
- The `section` as a container to break up each section in the resume 
	- Within the section, we have a heading and a list 
	- Using the container allows us to show the direct relationship between each heading and list 
	- The layout without styling would be the same if we left the section out, but the section allows us to add a component based design 
	- When working with dynamic websites, the container usage will allow us to reuse a single container to display multiple times.
- The `ul` container is used to state that an unordered list is being created 
	- list items must be included for the `ul` styling to take effect
	- we use the `li` to indicate a new time in our list.
**OUTPUT**

<body>
    <section>
        <h1>
            Resume
        </h1>

        <h3>
            John Doe
        </h3>
    </section>

    <hr>

    <section>
        <h4>Experience</h4>
        <ul>
            <li>
                Software Architect - Facebook
            </li>

            <li>
                Technical Lead - Amazon
            </li>

            <li>
                Senior Software Engineer - Apple
            </li>

            <li>
                Mid-Level Software Engineer - Netflix
            </li>

            <li>
                Junior Software Engineer - Google
            </li>
        </ul>
    </section>

    <section>
        <h4>Skills</h4>
        <ul>
            <li>
                Golang
            </li>
            <li>
                Kafka
            </li>
            <li>
                Kubernetes
            </li>
            <li>
                Docker
            </li>
            <li>
                Flink
            </li>
            <li>
                Snowflake
            </li>
        </ul>
    </section>
</body>

## 2.2 Simple Contact Us Page 

*Zoom into the body element*
```html
<body>
    <header>
        <h2>Contact Us</h2>
    </header>

    <form action="" method="post">
        <input 
	        id="name" 
	        name="name" 
	        placeholder="Your Name" 
	        type="text" 
	        maxlength="30"
	        >

		<input 
			id="surname" 
			name="surname" 
			placeholder="Your Last Name" 
			type="text" 
			maxlength="30"
			>
        
        <input 
	        type="number" 
	        name="age" 
	        placeholder="age" 
	        min="0"
	        >

        <textarea 
	        name="message" 
	        id="message" 
	        placeholder="Your message"
	        >
	        </textarea>

		<button type="submit"> Send </button>
    </form>
</body>
```
- Attributes in the `input` element can be used to add some constraints to the input
	- The `maxlength` restricts the input to a specified about of characters for text inputs
	- The `min` sets the lowest value that can be entered for numeric fields
	- The `type` states the type of input that can be accepted 
- The attributes in the `input` can add some additional information to the element 
	- `name` will be used to reference a specific input within the form 
	- `id` is used to reference a specific element in the whole HTML page 
	- `placeholder` will be the test that is shown if there is no data entered
- The `textarea` can be used for storing larger inputs 
- Having all of the inputs as part of the `form` container will allow us to submit all of the values together 
	- Within the form a `button` element that has a `type="submit"` will take all of the input that has been passed and return it all at once.
	- The `action=""` indicates the API that will take our data, each input field will be passed as a query in our API call 
	- the `method="post"` indicates that we want to make a post request to the API

**OUTPUT**

<body>
    <header>
        <h2>Contact Us</h2>
    </header>
    <form action="" method="post">
        <input id="name" name="name" placeholder="Your Name" type="text" maxlength="30">
        <input id="surname" name="surname" placeholder="Your Last Name" type="text" maxlength="30">
        <input type="number" name="age" placeholder="age" min="0">
        <textarea name="message" id="message" placeholder="Your message"></textarea>
        <button type="submit"> Send </button>
    </form>
</body>


## 2.2.1 Simple Contact Us Page More Structure 

```html
<body>
    <header>
      <h2>Contact Us</h2>
    </header>

    <form action="" method="post">
    
      <div>
        <label for="name">Name</label>
        <input
          id="name"
          name="name"
          placeholder="Your Name"
          type="text"
          maxlength="30"
        />
      </div>

      <div>
        <label for="surname">Surname</label>
        <input
          id="surname"
          name="surname"
          placeholder="Your Last Name"
          type="text"
          maxlength="30"
        />
      </div>

      <div>
        <label for="age">Age</label>
        <input type="number" name="age" placeholder="age" min="0" />
      </div>

      <div>
        <label for="message">Message</label>
        <textarea
          name="message"
          id="message"
          placeholder="Your message"
        ></textarea>
      </div>

      <button type="submit">Send</button>
      
    </form>
</body>
```
- The `label` element can be used to add a label to a specified input 
	- The `for` attribute is used by several elements to link a specific element to another 
		- When using a label, it states that the label is "for" a specific element 
- The `div` is used to couple the label and the input, this will ensure that styling can be applied to each related component.
- Using the `div` will result in the components being place one on top of the other.

<body>
    <header>
      <h2>Contact Us</h2>
    </header>

    <form action="" method="post">
    
      <div>
        <label for="name">Name</label>
        <input
          id="name"
          name="name"
          placeholder="Your Name"
          type="text"
          maxlength="30"
        />
      </div>

      <div>
        <label for="surname">Surname</label>
        <input
          id="surname"
          name="surname"
          placeholder="Your Last Name"
          type="text"
          maxlength="30"
        />
      </div>

      <div>
        <label for="age">Age</label>
        <input type="number" name="age" placeholder="age" min="0" />
      </div>

      <div>
        <label for="message">Message</label>
        <textarea
          name="message"
          id="message"
          placeholder="Your message"
        ></textarea>
      </div>

      <button type="submit">Send</button>
      
    </form>
</body>


## 2.3 Simple Table

*Zoom into body*
```html
<body>

    <table>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
        <tr>
            <td> Jimmy </td>
            <td>30</td>                        
            <td>
                <button>Delete</button>
            </td>
        </tr>
        <tr>
            <td> Garry </td>
            <td>40</td>       
            <td>
                <button>Delete</button>
            </td>                 
        </tr>
        <tr>
            <td> Sam </td>
            <td>50</td>
            <td>
                <button>Delete</button>
            </td>
        </tr>
    </table>
</body>
```
- The `table` element is used to contain elements that make us the different components of a table 
- The `tr` is used to specify a row in the table 
	- The first row will contain the headings denotated by the `th` element
	- Rows below will be dimensions of the tables denoted by the `td` element 
- Table rows aren't limited to only storing text values, we can add other components based on the types of interactions that our tables might require 
	- We can add buttons for adding CRUD functionality 
- The number of headings don't affect the number of columns that each row can have, 
	- Each `tr` is independent, the `table` element just contains all of the `tr` elements so that they are logically connected.

**OUTPUT**

<body>

    <table>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
        <tr>
            <td> Jimmy </td>
            <td>30</td>                        
            <td>
                <button>Delete</button>
            </td>
        </tr>
        <tr>
            <td> Garry </td>
            <td>40</td>       
            <td>
                <button>Delete</button>
            </td>                 
        </tr>
        <tr>
            <td> Sam </td>
            <td>50</td>
            <td>
                <button>Delete</button>
            </td>
        </tr>
    </table>
</body>


# 3 Styling
In modern day application development, just having plain HTML just isn't enough to captivate an audience. The visual appeal of an application is as important as the actual functionality. 

In this chapter, we will be taking a look at CSS, this is the primary way for adding styling to an HTML page, all other styling tools be it libraries like Bootstrap or Tailwind, or other languages like SCSS will translate their code back to CSS so that it can be applied to the HTML.

In future chapters, we will be implementing Tailwind CSS for styling, but to understand how the libraries work, it's important to understand how CSS works. If you are looking to get into a full-stack or frontend role, a deeper understanding of CSS is important and it's encouraged to work through some CSS content before fully transitioning into CSS libraries, but if you are looking to build frontend applications infrequently, then libraries will be your bestfriend.

## 3.1 CSS
Cascading Style Sheet (CSS) is styling language that is applied to markup languages like HTML and XML, it allows us to add custom layouts and additional flavour to our pages making them more appealing.

```css
h2 {
margin: 0;
font-size: 5em;            
}

.container {
width: 100vw;
background-color: brown;            
display: flex;
justify-content: space-evenly;
}

.child {
width: 100%;
}

#left-child{
background-color: aqua;
}

.container .right{
background-color: blue;
}

.container h2 {
font-size: 1em;
}
```
- To identify class elements a full stop is added before the name `.class-name`
- to identify id elements a hash is added before the name `#element-id`
- To implement a style, you need to identify the element or group of elements being worked with 
	- Using the element name will change the styling for all elements of the same type, eg, all `h2` elements will have the defined styling applied to them 
	- Using the class will change the styling for all elements with the specified class, this will overwrite any element level styling that has been applied 
	- Using the id will style a specific element and overwrite any class level styling
- To style elements of a specific class that are children of another element of a specific class, the class names can be stated one after the other based on their hierarchy 
	- `.container .left` - styles all `.left` elements contained within a `.container` element
	- `.container h2` - styles all `h2`'s inside a `.container` element 

CSS has a lot of styling options available per component, it's important to take a look at the different values and units that can be applied. [Resource](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Values_and_Units)

### 3.1.1 Layout
Laying out your components is the most important part to making good use of CSS, if the page isn't well laid out, there is no point in applying any fancy styling.

#### 3.1.1.2 Flexbox
Flexbox is a good approach for layout your page, as the name implies, it offers a flexible way for laying out your page.

```css
#container {
display: flex;
}

#container div{
flex: 1;
}
```

<div id="container" style="display: flex;">
	<div class="one" style="background-color: aqua; flex: 1">
		ONE
	</div >
	<div class="two" style="background-color: blueviolet; flex: 1">   
		TWO
	</div>
	<div class="three" style="background-color: blue; flex: 1">
		THREE
	</div>
</div>

#### 3.1.1.2 Grid

```css
.grid-container {  
display: grid;
grid-template-columns: auto auto auto; 
gap: 20px
}
```
<div id="container" style="display: grid; grid-template-columns: auto auto auto; gap: 20px">
	<div class="one" style="background-color: aqua; flex: 1">
		ONE
	</div >
	<div class="two" style="background-color: blueviolet; flex: 1">   
		TWO
	</div>
	<div class="three" style="background-color: blue; flex: 1">
		THREE
	</div>
	<div class="one" style="background-color: aqua; flex: 1">
		ONE
	</div >
	<div class="two" style="background-color: blueviolet; flex: 1">   
		TWO
	</div>
	<div class="three" style="background-color: blue; flex: 1">
		THREE
	</div>
	<div class="one" style="background-color: aqua; flex: 1">
		ONE
	</div >
	<div class="two" style="background-color: blueviolet; flex: 1">   
		TWO
	</div>
	<div class="three" style="background-color: blue; flex: 1">
		THREE
	</div>
</div>


### 3.1.2 Styling Hierarchy
We can style elements by tags, classes and ids so it's a realistic expectation that some elements might have more than 1 style applied to them.

Although it might sound like a terrible thin , it's actually good that we can apply many styles on a single element as we can create general styles and then drill down as required.

If a certain element has multiple styles applied, the styles for a specific attribute will be considered based on the lowest level of referencing, so if we had a `h2` style, it would be overwritten by a `.headings` and the `.headings` would be overwritten by a `#page-heading`, this is because referencing a class is more specific than referencing a tag and referencing an id is more specific than referencing a class.

**Order**
1. ID
2. Class
3. Tag

Using the order in which styles are applied, we can have a global styling for all components of a certain type, for example, we can set a font for all `h2` tag and then style the colour and size on a class level or id level, if we decide to use a different font for a specific class or id, it will be applied over the global font.

## 3.2 Invisible Styling 
Before we get into the fancy stuff, we need to talk about the "invisible" styling as I have affectionately dubbed it. These dictate the spaces around and within an element and are important to how the element will be displayed within it's parent element.

### 3.2.1 Margin 
When we have a container of any type, we refer to the margin as the space around the container, this is a force that the container will apply on it's parent and result in the position of the component changing within the parent component.

When margin is applied, there is can be no elements within the space, for example, if there are two elements in a parent and margin is applied on one of them, one of two things might happen, the element where the margin is being applied will either shrink, or push the other component.

<body style="margin: 0; padding: 0;">
    <div style="background-color: brown; display: flex; justify-content: space-evenly;">
        <div style="background-color: aqua; width: 100%; margin: 10px; color: black ">
            MARGIN APPLIED
        </div>
        <div style="background-color: blue; width: 100%;  color: black">
            NO MARGIN
        </div>
    </div>
</body>
- The parent containers background has been set the colour brown
	- The `MARGIN APPLIED` and `NO MARGIN` container are both child elements 
	- Both child component have the same amount of space allocated
- The `MARGIN APPLIED` container has a margin set 
	- This leads to the container being squashed within its portion of the parent component
	- We can see that the `NO MARGIN` component is able to take up all of the available space 


### 3.2.2 Padding 
Where margin is an external force, padding is an internal force, this is the force that the parent component applies on its children. When padding is applied, it will exert a force on all of the child components within that element. This is really helpful when you need to enforce certain boundaries within a parent component.

<body style="margin: 0; padding: 0;">
    <div style="background-color: brown; display: flex; justify-content: space-evenly; padding: 5px ">
        <div style="background-color: aqua; width: 100%; margin: 10px; color: black ">
            MARGIN APPLIED
        </div>
        <div style="background-color: blue; width: 100%;  color: black">
            NO MARGIN
        </div>
    </div>
</body>

<body style="margin: 0; padding: 0;">
    <div style="background-color: brown; display: flex; justify-content: space-evenly; padding: 5px ">
        <div style="background-color: aqua; width: 100%; color: black ">
            MARGIN APPLIED
        </div>
        <div style="background-color: blue; width: 100%;  color: black">
            NO MARGIN
        </div>
    </div>
</body>
- Adding padding to the parent will squash both elements the same amount
- Removing the initial margin from the left child, it's clear that the padding only works around the child components.


## 3.3 Applying Style 
There are two main ways of applying style to our components, these are inline styling and through stylesheets.

### 3.3.1 Inline Styling
If you are familiar with how markdown works, you would know that HTML can be rendered using markdown, this is how all of the representations you see in this document have been implemented. To add the structure in the [Invisible styling](#invisible-styling) section, inline styling was used.

To apply inline styling, the `style` attribute needs to be added to the opening tag of the element that is being styled. Inline styling will only affect a single element and it's children.

If you have a few elements that need to be styled exactly the same, this approach would not be the most manageable approach.

Inline styling is the lowest level of styling that can be applied in HTML and as such, it will override any higher level styling.

```html 
<body style="margin: 0; padding: 0;">
    <div style="background-color: brown; display: flex; justify-content: space-evenly;">
        <div style="background-color: aqua; width: 100%; color: black ">
            MARGIN APPLIED
        </div>
        <div style="background-color: blue; width: 100%;  color: black">
            NO MARGIN
        </div>
    </div>
</body>
```
- We can apply styling to every HTML element
- We use the CSS syntax of styling

### 3.3.2 Internal Stylesheets
We can add a style sheet to our HTML head section, this will allow us to style based on the tags, ids and classes of our elements.

```html
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Resume</title>

    <style>

        h2 {
            margin: 0;
            font-size: 5em;            
        }

        .container {
            width: 100vw;
            background-color: brown;            
            display: flex;
            justify-content: space-evenly;
        }

        .child {
            width: f;
        }

        .container .left{
            background-color: aqua;
        }

        .container .right{
            background-color: blue;
        }


    </style>
</head>

<body style="margin: 0; padding: 0;">
    <h2>
        Hello There
    </h2>
    <div class="container">        
        <div class="left child">
            LEFT
        </div>
        <div class="right child">
            RIGHT
        </div>
    </div>
</body>
```



### 3.3.3 External Stylesheets
For better readability and reusability, we can move our style sheets into an external `.css`file and reference the styles in our HTML file. We do this by adding a `<link>` element in our header that contains the information about the style sheet.

```html
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Resume</title>

    <link rel="stylesheet" href="style.css">
</head>

<body style="margin: 0; padding: 0;">
    <h2>
        Hello There
    </h2>
    <div class="container">        
        <div class="left child">
            LEFT
        </div>
        <div class="right child">
            RIGHT
        </div>
    </div>
</body>
```

We are not limited to style sheets that are in our current project, we can make use of style sheets from online sources as well if we need to.



# 4 Conclusion 
Working with web applications is something that almost all technical people will do at some point in their lives, having these skills will be very beneficial in the work environment especially as a junior developer.

To gain a deeper insight, please take a look at the resources section where there are some very good tutorials and website links that will equip you with all of the skills you'll need to create basic websites in no time.

# 5. Resources

## Videos 
- [HTML and CSS Crash Course](https://www.youtube.com/watch?v=HXYZxVbWkjc)
- [HTML Crash Course](https://www.youtube.com/watch?v=qz0aGYrrlhU)
- [CSS Crash Course](https://www.youtube.com/watch?v=r1xBCi5SOjw)
- [JavaScript for Beginners Crash Course](https://www.youtube.com/watch?v=hdI2bqOjy3c)

### Courses
- [Responsive Web Design](https://www.freecodecamp.org/learn/2022/responsive-web-design/)
- [CS50 Web Development](https://pll.harvard.edu/course/cs50s-web-programming-python-and-javascript)







































