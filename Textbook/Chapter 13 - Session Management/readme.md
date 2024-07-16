# Chapter 13 - Session Management

Nearly every application now requires you to create an account to access the service, this feature allows for the application experience to be more personalized and/or prevent unauthorised access to sensitive information. 

The distributed nature of modern software presents a few challenges when it comes to ensuring that the interaction between a client and a server is handled correctly. When applications mostly ran natively, the application would only communicate with the server at the initial login and the rest of the operations would be carried out natively, but now, we need constant communication with the server and with each request, the server needs to be aware of who it’s communicating with.

Session management is responsible for ensuring that the communication between the client and the server is only between specific parties, it ensures that the server is able to identify who is making a request and act accordingly.

In this chapter, we will take a look at how we can secure the communication between a client application and a server.

# 13.1 Client Side Rendering

Client-side rendering is the process of a browser creating HTML elements from JavaScript code. To have client-side rendering, we need to send all of the required code and files from our server to the client-side application.

Understanding how client-side rendering works allows us to make a few assumptions about the security of our applications.

Since all of the code that is required for our user-facing application has to be sent to the user's browser we can safely assume that having sensitive connection details like database connections would be a pretty bad idea since anyone who has access to the application would have access to those details.

To solve the problem, we usually make use of a server for handling all sensitive operations, our servers can securely connect to our databases, internal systems and anything else that we wouldn’t want a user to have access to or knowledge of.

# 13.2 Access Control

When building applications that have personalization features or handle sensitive information, it’s important to make sure that there are measures in place that prevent unwanted access to certain resources.

The two main concepts of access control are **Authentication** and **Authorization.** These two concepts are often used interchangeably, but the truth is that these are two completely different concepts that are concerned with different aspects of what a user can do with a system.

Authentication is implemented as the first step before the user can access the system, this usually involves some sort of interface where the user enters credentials to gain access to the system.

Authorization on the other hand is an “invisible” force, the user shouldn’t be able to make changes to their level of access, this is usually done by a third party and the information is stored internally, the user only knows their level of authorization based on how much of the system they can access.

## 13.2.1 Authentication

*Who are you?*

Authentication is concerned with knowing who the client/user is. We can set restrictions on our application that ensure that only authenticated users can access our platforms, you would be familiar with this when logging into a social media platform, or your company/school's system.

Authentication is a key part of many modern applications that focus on custom user experiences, this could be social media applications where each user will have their own posts and follow a unique set of people. Authentication is also important for productivity tools like Notion where each person needs to log in to access their notes which are isolated from other users.

Some common authentication techniques include

- Password-based authentication
    - Most common
    - Requires a password and a uniquely identifying field
- Multi-factor authentication
    - Built on password-based authentication and requires another thing
        - One-time password (OTP)
        - Biometric
        - Security Question
- Token-based Authentication
    - A unique sequence of characters that link to a specific user
    - Typically used for HTTP communications
    - Common when connecting to APIs (API Keys)

## 13.2.2 Authorization

*What can you do?*

Authorization as the name implies, is focused on keeping track of what a user is authorized to do.

Authorization builds on authentication and specifies what each authenticated user can do within the system.

If you think of a company system, all users can authenticate (log in) the same way, but some users can access more parts of the system than others.

Authorization is not only important when it comes to setting up your applications, but it’s important for all of the services that you work with, this includes your database services and the operating systems that your application is running on.

There are a few different approaches to authorization:

- **Role-based Access Control** (RBAC)
    - This is the most popular approach
    - Users are broken up into different groups
    - Each group will have access to certain features, a user in a group will inherit all of the access while they are part of that group.
- **Discretionary Access Control (DAC)**
    - Allows the owner of a resource to grant access to other users
    - The owner can grant access to different users or groups
- **Mandatory Access Control (MAC)**
    - Access is controlled by a central authority based on pre-defined security labels
    - Users and resources are assigned security labels and access is granted based on the label
- **Attribute-Based Access Control (ABAC)**
    - Granular approach
    - Allows for fine-grained access control based on attributes, resources and environments

When setting authorization rules, it’s important to be as restrictive as possible, each user/group should only have access to the things that they need, for example, if you are building a database for a business, the sales team would not need to have access to anything other than the sales data and maybe certain parts of the user data, but they would not need to have access to employee details or company revenue data. 

# 13.3 Session Management

Circling back to the discussion on client-side rendered applications, we know that we can’t have direct access to our databases or other sensitive services from our client application.

Session management is responsible for ensuring that a client application can let the server know who is trying to access certain resources and it allows the server to send information that is relevant based on the user's identity and authorization.

### 13.3.1 HTTP

HTTP is the most common approach for communication between the client and the server, but it’s important to keep in mind that HTTP is a stateless protocol, this means that every request that is made to a server should be independent of any prior requests, as long as a user include all of the required data for a call, they should get a consistent result.

Keeping in mind that our server is responsible for all private operations, one would assume that session management would be handled on the server where we can keep track of all of the active users in some sort of database, the problem is that this approach violates the statelessness principle since the server has to store some sort of state that indicates which users are having a session.

### 13.3.2 Session Token

Session tokens are a good tool for keeping track of a user. Session tokens are generated on the server once the user has been authenticated, the process would look something like this:

1. The user sends their credentials (email+password, access token, etc)
2. The server verifies that the details are correct (looking into the database, using a third-party tool)
3. A token containing identifying information about the user is generated 
4. The token is returned to the client
5. The client stores the token and sends the token with each request 
6. The server verifies the token is correct and valid before making a response. 

The token-based approach requires the client to store the token in a manner that is both easy to access throughout the application, but also secure, here are a few common places where tokens can be stored on the client side.

- Cookies
    - The server creates a cookie that is sent out to the client, the client application automatically saves this cookie and automatically sends it with every request that is made
    - Pros
        - Simple to implement
        - Widely supported by browsers
        - Accessible by client-side JavaScript
    - Cons
        - Accessible by client-side JavaScript
        - Normal cookies can be stolen by Cross Site Scripting (XSS) attacks or when sending through HTTP
- HttpOnly Cookies
    - Ensures the normal cookies are secure
    - Pros
        - Can’t be accessed by client-side JavaScript removing the risk of XSS
        - Most secure approach
    - Cons
        - Requires HTTPS (which isn’t really a con)
- LocalStorage
    - Stores information in the memory of the browser and can be accessed by the specific website that stores the data
    - Pros
        - Able to store a lot of data
        - More control over when data is sent since it’s not sent automatically with each request
    - Cons
        - Requires JavaScript to access making it vulnerable to XSS
        - Data is persisted until manually cleaned, when you leave a site and come back, the local storage will still be there.
- Session Storage
    - A temporary version of local storage, it only persists the data for a single tab of a given website and clears when that browser tab is closed
    - Pros
        - Same control of local storage
        - The data is cleared once the session ends
    - Cons
        - All the same as local storage.

### 13.3.2 Securing a Session Token

Whenever data is being transferred over the internet, there are risks, this is true for our session tokens since they need to be passed between the client and the server.

It’s very important to make sure that our session tokens are kept securely as they determine who a user is and what they can do. 

If a general user's token is stolen, the person who has this token can impersonate them, if you’re building a banking application, you can imagine the problems this could cause. For a company system, if an admin token is stolen, the person who has this token can access sensitive information about the company and make changes to different things within the system.

### The Token

We can start at the lowest level which would be ensuring that the token itself is safe. We want to make sure that the token that is sent out has safety measures that prevent someone from gaining further information if the token is wrongfully accessed, we can do this by:

- Encrypting the token
    - Using a 128-character token is the recommended approach
        - This can be done through the use of a [JSON Web Token](https://jwt.io/) (JWT)
    - Use a strong `secret` when setting up your JWT
        - The `secret` is the password that will be used to encrypt and decrypt your token
        - A good approach would be to generate a random key and keep this key secure
        - Anyone with the `secret` will be able to decrypt the JWT
    - Set the token to expire
        - The token should expire after a set amount of time, the life of the token depends on the use case
            - Social media login - The token can last for a few months before reauthentication is required
            - Work-related - the token can expire after a day before requiring reauthentication
            - Banking - The token can expire after a few minutes before requiring reauthentication
        - There are more advanced techniques for defining the life of a token
    - Limit the amount of information in the token
        - Although the encryption of the JWT should protect the information, it’s still important to limit the information that is passed in the token
        - Only send
            - User ID - for linking the request to a database user
            - Role - for faster access to what the user is allowed to do
                - Depending on server resources, it would be better to access this through a call to the database, but to reduce the number of calls made to the server, it can be stored in the token.

### The communication

A well-defined token does not mean that the communication is completely safe, even if someone is not able to decrypt the token, it can still be stolen and used allowing the person to make requests as if they are the rightful recipient.

Session jacking happens when an attacker obtains a user's session token and makes requests to the server pretending to be the original owner of the session. This is one of the reasons why expiring session tokens are important as the attacker will have limited time to do what they want to do before the session expires.

Like all communication, we need to make sure that an attacker is not able to steal information or add their own information that would undermine the client-server communication.

Here is how we can secure a user session 

- Force **HTTPS (TLS)** - All communication should be sent through secure HTTPS, this ensures that all traffic is encrypted preventing hackers from seeing any data that is in transit
- Use **HttpOnly Cookies** - These cookies are attached by the server and automatically attached to every request that the user sends.
    - These types of cookies cannot be accessed by JavaScript preventing any external scripts that run on the application from accessing the tokens.
- Use **SameSite** attribute for cookies - This defines whether a website requesting on behalf of the client application can send cookies with the request
- **Expires and Max-Age** - This will set the life of the cookies, once the cookie reaches its max-age, it will be cleared requiring the user to authenticate since there would be no token sent with the requests.

# 13.4 Conclusion

We have seen how user sessions can be managed and secured, but like all things in tech, the concepts are better understood when seen and done, below are some resources that you can look at for a deeper dive into the security implications as well as some videos that show how these concepts can be applied practically.

It is highly recommended that you take a look at all of the different topics that are covered on OWASP when developing applications as they keep an updated list of vulnerabilities that are common in different types of applications. They also provide some useful tips on how to secure your applications.

# Resources

### Theory and Articles

- [https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [https://www.infosectrain.com/blog/what-is-session-management/](https://www.infosectrain.com/blog/what-is-session-management/)
- [https://www.authgear.com/post/session-management](https://www.authgear.com/post/session-management)

### Practical Implementations

- [**Back to Basics: Managing Your Web Application’s Session**](https://www.youtube.com/watch?v=uRmdTJva7vI)
- [**How Sessions work in Web Servers**](https://www.youtube.com/watch?v=5beyFcuTw20&t=82s)
- [**Session Management Reimagined: What is session management?**](https://www.youtube.com/watch?v=Pjbzvxas4kM)
- [**Web App Pentesting - HTTP Cookies & Sessions**](https://www.youtube.com/watch?v=zHBpJA5XfDk)

### Additional Resources

- [Auth0 - Authentication Service](https://auth0.com/)
- [OAuth](https://oauth.net/2/)
- [JWT](https://jwt.io/)
