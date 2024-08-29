# **HTML Programming Guide**

## **Introduction**
HTML (HyperText Markup Language) is the standard language used to create and design web pages. Developed by Tim Berners-Lee, HTML provides the basic structure for web content and is essential for building websites. HTML documents consist of elements and attributes that define the structure and content of web pages.

## **Table of Contents**
1. [Getting Started](#getting-started)
2. [HTML Document Structure](#html-document-structure)
3. [HTML Elements and Tags](#html-elements-and-tags)
4. [Attributes](#attributes)
5. [Text Formatting](#text-formatting)
6. [Links and Navigation](#links-and-navigation)
7. [Images and Media](#images-and-media)
8. [Forms and Input](#forms-and-input)
9. [Tables](#tables)
10. [Semantic HTML](#semantic-html)
11. [Conclusion](#conclusion)
12. [Appendix](#appendix)

## **Getting Started**
### Setting Up Your Environment
1. **Text Editor**: Use any text editor to write HTML. Popular choices include Visual Studio Code, Sublime Text, and Notepad++.

2. **Browser**: HTML files can be viewed in any modern web browser such as Google Chrome, Firefox, or Safari.

3. **Creating Your First HTML Document**: Create a file with a `.html` extension and add the following code:

   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>My First HTML Page</title>
   </head>
   <body>
       <h1>Hello, World!</h1>
       <p>This is my first HTML page.</p>
   </body>
   </html>
   ```

   Open the file in a browser to see the result.

## **HTML Document Structure**
### Basic Structure
An HTML document has a basic structure consisting of several elements:

- **`<!DOCTYPE html>`**: Declares the document type and version of HTML.
- **`<html>`**: The root element that contains all HTML content.
- **`<head>`**: Contains meta-information about the document, such as the title and links to stylesheets.
- **`<body>`**: Contains the main content of the document that is displayed in the browser.

### Example
```html
<!DOCTYPE html>
<html>
<head>
    <title>Sample Page</title>
</head>
<body>
    <h1>Welcome to My Website</h1>
    <p>This is a sample paragraph.</p>
</body>
</html>
```

## **HTML Elements and Tags**
### Common Elements
HTML documents are composed of elements enclosed in tags. Common elements include:

- **Headings**: `<h1>` to `<h6>` define headings, with `<h1>` being the highest level.

  ```html
  <h1>Main Heading</h1>
  <h2>Subheading</h2>
  ```

- **Paragraphs**: `<p>` defines a paragraph of text.

  ```html
  <p>This is a paragraph.</p>
  ```

- **Links**: `<a>` defines a hyperlink.

  ```html
  <a href="https://www.example.com">Visit Example</a>
  ```

- **Lists**: `<ul>` for unordered lists and `<ol>` for ordered lists, with `<li>` for list items.

  ```html
  <ul>
      <li>Item 1</li>
      <li>Item 2</li>
  </ul>

  <ol>
      <li>First</li>
      <li>Second</li>
  </ol>
  ```

## **Attributes**
### Common Attributes
Attributes provide additional information about HTML elements. They are added within the opening tag:

- **`href`**: Specifies the URL for hyperlinks.

  ```html
  <a href="https://www.example.com">Example</a>
  ```

- **`src`**: Specifies the source of an image.

  ```html
  <img src="image.jpg" alt="Description">
  ```

- **`alt`**: Provides alternative text for images.

  ```html
  <img src="logo.png" alt="Company Logo">
  ```

- **`id`** and **`class`**: Used for styling and JavaScript interaction.

  ```html
  <div id="main-content" class="container">
      <!-- Content -->
  </div>
  ```

## **Text Formatting**
### Common Tags
HTML provides several tags to format text:

- **Bold**: `<b>` or `<strong>`.

  ```html
  <b>Bold text</b>
  <strong>Strong text</strong>
  ```

- **Italic**: `<i>` or `<em>`.

  ```html
  <i>Italic text</i>
  <em>Emphasized text</em>
  ```

- **Underline**: `<u>`.

  ```html
  <u>Underlined text</u>
  ```

- **Superscript**: `<sup>`.

  ```html
  Chemical formula: H<sub>2</sub>O
  ```

- **Subscript**: `<sub>`.

  ```html
  E = mc<sup>2</sup>
  ```

## **Links and Navigation**
### Creating Links
Use the `<a>` tag to create hyperlinks:

- **External Links**:

  ```html
  <a href="https://www.example.com">Visit Example</a>
  ```

- **Internal Links**:

  ```html
  <a href="#section1">Go to Section 1</a>
  ```

  And target the link with an `id` attribute:

  ```html
  <h2 id="section1">Section 1</h2>
  ```

### Navigation Menus
Create a navigation menu using unordered lists:

```html
<nav>
    <ul>
        <li><a href="index.html">Home</a></li>
        <li><a href="about.html">About</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>
</nav>
```

## **Images and Media**
### Adding Images
Use the `<img>` tag to add images:

```html
<img src="image.jpg" alt="Description">
```

### Embedding Media
Embed videos using the `<video>` tag:

```html
<video width="320" height="240" controls>
    <source src="movie.mp4" type="video/mp4">
    Your browser does not support the video tag.
</video>
```

## **Forms and Input**
### Creating Forms
Forms allow users to submit data. Use the `<form>` tag and various input elements:

```html
<form action="/submit" method="post">
    <label for="name">Name:</label>
    <input type="text" id="name" name="name">
    <br>
    <label for="email">Email:</label>
    <input type="email" id="email" name="email">
    <br>
    <input type="submit" value="Submit">
</form>
```

### Input Types
Different types of inputs include:

- **Text**: `<input type="text">`
- **Password**: `<input type="password">`
- **Checkbox**: `<input type="checkbox">`
- **Radio**: `<input type="radio">`
- **Submit Button**: `<input type="submit">`

## **Tables**
### Creating Tables
Tables are created using the `<table>` tag with rows (`<tr>`) and cells (`<td>` or `<th>`):

```html
<table>
    <thead>
        <tr>
            <th>Name</th>
            <th>Age</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Alice</td>
            <td>30</td>
        </tr>
        <tr>
            <td>Bob</td>
            <td>25</td>
        </tr>
    </tbody>
</table>
```

## **Semantic HTML**
### Importance of Semantics
Semantic HTML uses tags that convey meaning about the content they enclose:

- **`<header>`**: Represents introductory content or navigational links.
- **`<footer>`**: Represents the footer of a section or page.
- **`<article>`**: Represents a self-contained piece of content.
- **`<section>`**: Represents a thematic grouping of content.
- **`<aside>`**: Represents content indirectly related to the main content.

### Example
```html
<header>
    <h1>Website Title</h1>
</header>
<main>
    <section>
        <h2>About Us</h2>
        <p>Information about us.</p>
    </section>
    <aside>
        <h3>Related Links</h3>
        <ul>
            <li><a href="#">Link 1</a></li>
            <li><a href="#">Link 2</a></li>
        </ul>
    </aside>
</main>
<footer>
    <p>&copy; 2024 My Website</p>
</footer>
```

## **Conclusion**
HTML is the backbone of web development, providing the fundamental structure needed to create and format web pages. Its combination of elements, attributes, and tags allows developers to build rich, interactive web experiences. Understanding and mastering HTML is essential for anyone involved in web development.

## **Append

ix**
### Glossary
- **Element**: A component of an HTML document, such as a heading or paragraph.
- **Tag**: The HTML markup that surrounds content, defining its structure and function.
- **Attribute**: Additional information provided in an HTML tag to modify its behavior or appearance.

### Additional Resources
- [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [W3Schools HTML Tutorial](https://www.w3schools.com/html/)
- [HTML Living Standard](https://html.spec.whatwg.org/)