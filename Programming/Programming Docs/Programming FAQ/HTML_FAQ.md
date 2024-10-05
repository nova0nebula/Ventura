# **HTML FAQ**

## **Table of Contents**
1. [General Questions](#general-questions)
2. [HTML Basics](#html-basics)
3. [HTML Elements and Attributes](#html-elements-and-attributes)
4. [Forms and Input](#forms-and-input)
5. [Multimedia](#multimedia)
6. [Semantic HTML](#semantic-html)
7. [HTML5 Features](#html5-features)
8. [Common Issues and Troubleshooting](#common-issues-and-troubleshooting)
9. [Resources](#resources)

## **General Questions**

### **1. What is HTML?**
HTML (HyperText Markup Language) is the standard markup language used to create and design web pages. It defines the structure and content of a web page through the use of various tags and attributes. HTML is the backbone of web development, allowing browsers to interpret and display content correctly.

### **2. What are the main components of an HTML document?**
An HTML document is composed of several key components:
- **Document Type Declaration (Doctype)**: Defines the version of HTML being used.
- **HTML Element**: The root element that wraps all content.
- **Head Element**: Contains meta-information, links to stylesheets, and other resources.
- **Body Element**: Contains the visible content of the page.

### **3. How does HTML differ from other web technologies like CSS and JavaScript?**
- **HTML**: Provides the structure and content of web pages.
- **CSS (Cascading Style Sheets)**: Handles the presentation and layout of the HTML content.
- **JavaScript**: Adds interactivity and dynamic functionality to the web pages.

## **HTML Basics**

### **1. What is the basic structure of an HTML document?**

An HTML document follows a standard structure:

```html
<!DOCTYPE html>
<html>
<head>
  <title>Document Title</title>
</head>
<body>
  <h1>Heading</h1>
  <p>This is a paragraph.</p>
</body>
</html>
```

- **`<!DOCTYPE html>`**: Declaration defining the HTML version.
- **`<html>`**: Root element.
- **`<head>`**: Contains metadata and links.
- **`<body>`**: Contains the content displayed on the page.

### **2. How do I create comments in HTML?**

Comments in HTML are added using the `<!-- -->` syntax:

```html
<!-- This is a comment -->
<p>This is visible content.</p>
```

## **HTML Elements and Attributes**

### **1. What are HTML elements and attributes?**

- **HTML Elements**: Basic building blocks of HTML, such as `<p>`, `<a>`, `<div>`, etc. Each element is enclosed in opening and closing tags.
- **Attributes**: Provide additional information about elements, placed within the opening tag. For example, the `href` attribute in an `<a>` tag:

```html
<a href="https://example.com">Visit Example</a>
```

### **2. What are some common HTML elements?**

- **Headings**: `<h1>`, `<h2>`, `<h3>`, etc.
- **Paragraphs**: `<p>`
- **Links**: `<a>`
- **Images**: `<img>`
- **Lists**: `<ul>`, `<ol>`, `<li>`
- **Tables**: `<table>`, `<tr>`, `<td>`, `<th>`
- **Divisions**: `<div>`
- **Spans**: `<span>`

### **3. How do I use attributes in HTML?**

Attributes provide additional information and are included in the opening tag:

```html
<img src="image.jpg" alt="Description" width="300" height="200">
```

- **`src`**: Specifies the image source.
- **`alt`**: Provides alternative text for the image.
- **`width`** and **`height`**: Define the dimensions of the image.

## **Forms and Input**

### **1. How do I create a form in HTML?**

Forms are created using the `<form>` element and can include various input elements:

```html
<form action="/submit" method="post">
  <label for="name">Name:</label>
  <input type="text" id="name" name="name">
  <input type="submit" value="Submit">
</form>
```

- **`action`**: URL where the form data will be sent.
- **`method`**: HTTP method used (e.g., `post` or `get`).

### **2. What are common input types in HTML forms?**

- **Text Input**: `<input type="text">`
- **Password**: `<input type="password">`
- **Radio Buttons**: `<input type="radio">`
- **Checkboxes**: `<input type="checkbox">`
- **Dropdowns**: `<select>` with `<option>`
- **Textareas**: `<textarea>`

### **3. How do I handle form submissions?**

Form submissions are handled by specifying the `action` attribute in the `<form>` tag, which sends the form data to a server-side script or endpoint.

## **Multimedia**

### **1. How do I embed images in an HTML page?**

Use the `<img>` tag to embed images:

```html
<img src="image.jpg" alt="Description" width="500">
```

- **`src`**: Path to the image file.
- **`alt`**: Alternative text for the image.

### **2. How do I include videos and audio in HTML?**

- **Videos**:
  ```html
  <video width="320" height="240" controls>
    <source src="video.mp4" type="video/mp4">
    Your browser does not support the video tag.
  </video>
  ```

- **Audio**:
  ```html
  <audio controls>
    <source src="audio.mp3" type="audio/mpeg">
    Your browser does not support the audio element.
  </audio>
  ```

## **Semantic HTML**

### **1. What is semantic HTML?**

Semantic HTML refers to using HTML elements that convey meaning about the content they enclose. This improves accessibility and SEO.

### **2. What are examples of semantic HTML elements?**

- **`<header>`**: Defines the header section.
- **`<footer>`**: Defines the footer section.
- **`<article>`**: Represents an independent piece of content.
- **`<section>`**: Represents a section of content.
- **`<nav>`**: Defines navigation links.
- **`<aside>`**: Represents content tangentially related to the main content.

## **HTML5 Features**

### **1. What are some key features of HTML5?**

- **New Semantic Elements**: `<header>`, `<footer>`, `<section>`, `<article>`, etc.
- **Enhanced Form Controls**: New input types such as `date`, `email`, and `range`.
- **Audio and Video Support**: `<audio>` and `<video>` elements for multimedia.
- **Canvas API**: `<canvas>` element for drawing graphics.
- **Local Storage**: Mechanism for storing data on the client side using `localStorage` and `sessionStorage`.

### **2. How do I use the Canvas API in HTML5?**

The `<canvas>` element allows for drawing graphics directly in the browser:

```html
<canvas id="myCanvas" width="200" height="100"></canvas>
<script>
  var canvas = document.getElementById('myCanvas');
  var ctx = canvas.getContext('2d');
  ctx.fillStyle = 'blue';
  ctx.fillRect(10, 10, 150, 75);
</script>
```

## **Common Issues and Troubleshooting**

### **1. Why is my HTML not displaying correctly?**

- **Check for Syntax Errors**: Ensure all tags are properly closed.
- **Verify Paths**: Confirm that paths to resources like images and stylesheets are correct.
- **Inspect in Browser**: Use browser developer tools to check for issues.

### **2. How do I ensure my HTML is valid?**

- **Use Validators**: Tools like the [W3C Markup Validation Service](https://validator.w3.org/) can help validate your HTML.
- **Follow Best Practices**: Adhere to HTML standards and semantic practices.

## **Resources**

- [W3C HTML Documentation](https://www.w3.org/TR/html/)
- [MDN Web Docs: HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [HTML5 Rocks](https://www.html5rocks.com/)
- [Can I Use](https://caniuse.com/) - For checking HTML5 feature support