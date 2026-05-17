
---

# EXAM 1 – Unit 1: Introduction to the WWW

## Section A – Concepts (short answer)

1. **Define what the World Wide Web is.**  
   The World Wide Web is a system of interlinked hypertext documents and resources accessed through the Internet using web browsers.

2. **Explain in your own words what characterizes Web 1.0.**  
   Web 1.0 refers to the early Web, characterized by static pages, limited interaction, and content that users could only read, not modify.

3. **What is the main difference between Web 2.0 and the Semantic Web?**  
   Web 2.0 focuses on user-generated content and interaction, while the Semantic Web focuses on giving data structure and meaning so machines can understand and automate tasks.

4. **What is a client within web architecture?**  
   A client is a device or application that sends requests to a server to access resources or services.

5. **Mention two functions of the W3C.**  
   - Developing and maintaining web standards (HTML, CSS, etc.).  
   - Ensuring interoperability and accessibility across the Web.

---

## Section B – Development

1. **Describe the general functioning of the HTTP protocol in a typical request.**  
   A client sends an HTTP request specifying a method (GET, POST, etc.). The server processes it and returns a response containing a status code, headers, and optionally a body with the requested resource.

2. **Explain the client–server architecture using a real example.**  
   When a user opens YouTube, the browser (client) requests video data from YouTube’s servers. The server processes the request and sends back the video stream for playback.

3. **Compare Web 1.0 and Web 2.0 in a table.**

   | Web 1.0 | Web 2.0 |
   |---------|---------|
   | Static content | Dynamic, user‑generated content |
   | Read‑only | Interactive and collaborative |
   | Limited user participation | Users create, share, and modify content |

4. **Explain what a URL is and break down its main components.**  
   A URL (Uniform Resource Locator) is the address used to locate a resource on the Web.  
   Components:  
   - Protocol (https://)  
   - Domain name (example.com)  
   - Path (/products/item)  
   - Optional: port, query parameters, fragment

5. **Describe three examples of modern web applications and classify them.**  
   - **Static:** Portfolio websites, documentation pages  
   - **Dynamic:** Wikipedia, online stores  
   - **Interactive:** Social networks, real‑time chat apps

---

## Section C – Analysis / Application

1. **Analyze how Web 2.0 transformed the role of the user.**  
   Web 2.0 turned users from passive consumers into active participants who create, share, and interact with content and with other users.

2. **Explain why the Semantic Web is important for automation and AI.**  
   It provides structured, machine‑readable data that allows software agents and AI systems to understand relationships, automate tasks, and perform more accurate reasoning.

3. **Evaluate the impact of standardization organizations on current web development.**  
   They ensure interoperability, accessibility, and consistency across browsers and devices, enabling developers to build reliable and universal web experiences.

4. **Describe a case where poor client–server implementation affects user experience.**  
   Slow server responses or incorrect API endpoints can cause pages to load incorrectly, fail to display data, or become unusable.

5. **Explain how a browser interprets and displays a web page.**  
   The browser resolves the domain via DNS, establishes an HTTP/HTTPS connection, downloads HTML/CSS/JS files, parses them, builds the DOM and CSSOM, executes scripts, and renders the page.

---

# EXAM 2 – Unit 1: Introduction to the WWW

## Section A – Concepts

1. **Define Semantic Web.**  
   The Semantic Web is an extension of the Web that structures data so machines can understand meaning, relationships, and context.

2. **What is a web server?**  
   A web server is a system that stores, processes, and delivers web pages to clients upon request.

3. **Mention two organizations that regulate Internet standards.**  
   - W3C  
   - IETF

4. **What is an HTTP status code?**  
   A numerical code returned by a server indicating the result of a request (e.g., 200 OK, 404 Not Found).

5. **Define the term “hyperlink.”**  
   A hyperlink is a clickable reference that links one resource to another using a URL.

---

## Section B – Development

1. **Explain the historical evolution of the Web from Web 1.0 to the Semantic Web.**  
   Web 1.0 offered static content. Web 2.0 introduced dynamic pages, user interaction, and social platforms. The Semantic Web adds structured data and machine‑readable meaning to enable automation and intelligent processing.

2. **Describe the complete cycle of an HTTP GET request.**  
   The client sends a GET request → the server receives it → processes it → returns a response with a status code and the requested resource → the browser renders it.

3. **Explain the difference between HTTP and HTTPS.**  
   HTTPS encrypts communication using SSL/TLS certificates, providing confidentiality and authentication.

4. **Describe the role of the browser in web architecture.**  
   The browser sends requests, interprets responses, executes scripts, and renders web pages for the user.

5. **Explain what a web resource is and give three examples.**  
   A web resource is any identifiable item on the Web. Examples:  
   - An HTML page  
   - An image  
   - An API endpoint

---

## Section C – Analysis / Application

1. **How client–server architecture enables scalability.**  
   Workloads can be distributed across multiple servers, allowing applications to handle more users and requests efficiently.

2. **Why W3C standards are fundamental for interoperability.**  
   They ensure that web content behaves consistently across browsers, devices, and platforms.

3. **Advantages and disadvantages of Web 2.0 regarding privacy.**  
   **Advantages:** personalization, collaboration, user‑generated content.  
   **Disadvantages:** data collection, tracking, risk of misuse of personal information.

4. **Scenario where a 404 error affects navigation.**  
   A user clicks a link to a product page that no longer exists, preventing access and causing frustration.

5. **How the Semantic Web could improve search engines.**  
   By providing structured meaning, search engines can understand context, relationships, and intent, producing more accurate results.

---

# EXAM 3 – Unit 1: Introduction to the WWW

## Section A – Concepts

1. **Define the term “WWW.”**  
   The World Wide Web is a system of interlinked hypertext documents accessed through the Internet.

2. **What is an application server?**  
   A server that runs application logic and delivers dynamic content or services to clients.

3. **Explain what a protocol is.**  
   A protocol is a set of rules that define how data is transmitted and communicated between systems.

4. **Define Web 2.0.**  
   Web 2.0 refers to the interactive, collaborative Web where users generate and share content.

5. **What is a static resource?**  
   A resource that does not change unless manually updated, such as images, CSS files, or static HTML pages.

---

## Section B – Development

1. **Explain the client–server model using a diagram (textual).**  
   Client → sends request → Server  
   Server → processes request → sends response → Client

2. **Describe the main characteristics of the Semantic Web.**  
   - Machine‑readable data  
   - Structured meaning  
   - Ontologies and metadata  
   - Automation and intelligent processing

3. **Explain the role of the IETF in the development of the Internet.**  
   The IETF develops and maintains Internet protocols such as TCP/IP, DNS, and HTTP.

4. **Describe how a browser resolves a domain name (DNS).**  
   The browser queries a DNS resolver → resolver checks cache or contacts DNS servers → obtains the IP address → returns it to the browser.

5. **Explain what hypermedia is and how it relates to the Web.**  
   Hypermedia is media linked through hyperlinks (text, images, video). The Web is a hypermedia system enabling navigation between resources.

---

## Section C – Analysis / Application

1. **How Web 1.0 limited user interaction.**  
   Users could only read content; they could not comment, modify, or contribute.

2. **Impact of Web 2.0 on modern education.**  
   Enabled collaborative learning, online courses, shared resources, and interactive platforms.

3. **How the Semantic Web could improve accessibility.**  
   Structured data helps assistive technologies interpret content more accurately.

4. **Case where lack of standards affects visualization.**  
   A website built without standards may render differently or break across browsers.

5. **Importance of HTTP in distributed systems.**  
   HTTP provides a universal communication protocol enabling interoperability between services and systems.

---