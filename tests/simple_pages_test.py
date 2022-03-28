"""This test the homepage"""

def test_request_main_menu_links(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b'<a class="nav-link" href="/about">About</a>' in response.data
    assert b'<a class="nav-link" href="/page1">GIT</a>' in response.data
    assert b'<a class="nav-link" href="/page2">Docker</a>' in response.data
    assert b'<a class="nav-link" href="/page3">Python/Flask</a>' in response.data
    assert b'<a class="nav-link" href="/page4">CI/CD</a>' in response.data

def test_request_index(client):
    """This makes the index page"""
    response = client.get("/")
    assert response.status_code == 200
    assert b"Index Page" in response.data

def test_request_about(client):
    """This makes the index page"""
    response = client.get("/about")
    assert response.status_code == 200
    assert b"About Page" in response.data

def test_request_page1(client):
    """This makes the index page"""
    response = client.get("/page1")
    assert response.status_code == 200
    assert b"GIT is a version control system. Git branches are different workspaces where we can work on our code without changing the main branch with the working code. Commits are like saves to our work in the VCS. Repo's are where we can see the different branches with their commits. Finally, merges are when a feature is complete outside of the default branch and they are combined." in response.data

def test_request_page2(client):
    """This makes the index page"""
    response = client.get("/page2")
    assert response.status_code == 200
    assert b"Docker is an open platform for developing, and running applications. It can be compared to having a sterile environment for your code to run in. Commands such as docker run allows us to run a program in a docker container. Docker ps is what allows us to see what is currently running." in response.data

def test_request_page3(client):
    """This makes the index page"""
    response = client.get("/page3")
    assert response.status_code == 200
    assert b"Flask is a micro web framework written in Python. While Python is it's own standalone language. Its design philosophy emphasizes code readability with the use of significant indentation. It's what helps us automate processes in our code." in response.data

def test_request_page4(client):
    """This makes the index page"""
    response = client.get("/page4")
    assert response.status_code == 200
    assert b"CI/CD(Continuous Integration and Continuous Deployment) are what allow us to keep the website or application running while also being stable. There are a series of checks before the application is deployed, making sure it's always stable." in response.data

def test_request_page5(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 200
    assert b"Instantiation mean to call the constructor of a class that creates an instance or object of the type of that class. Object object is a member (also called an instance) of a class. Each object has an identity, a behavior and a state. Class a template used to create objects and to define object data types and methods. Namespaces allow programmers to create small private areas in which to declare classes. Constructor is a special method that is used to initialize objects. The constructor is called when an object of a class is created. Fixture define the steps and data that constitute the arrange phase of a test. Type cast the data types of objects are converted using predefined functions by the user. Unit testing is a technique in which particular module is tested to check by developer himself whether there are any errors. Static means that the member is on a class level rather on the instance level. Instance method are called because they can access unique data of their instance. Instance property is a Python variable belonging to only one object. Static method are methods that are bound to a class rather than its object. Static property means that the member is on a class level rather on the instance level. Encapsulation is the packing of data and functions that work on that data within a single object. Inheritance allows us to define a class that inherits all the methods and properties from another class. Polymorphism defines methods in the child class that have the same name as the methods in the parent class. Abstraction is the process of hiding the real implementation of an application from the user and emphasizing only on usage of it." in response.data

def test_request_page6(client):
    """This makes the index page"""
    response = client.get("/page6")
    assert response.status_code == 200
    assert b"AAA screening can find large bulges that might rupture if they are not repaired. Screening can also find smaller bulges that can be watched carefully over the years." in response.data

def test_request_page7(client):
    """This makes the index page"""
    response = client.get("/page7")
    assert response.status_code == 200
    assert b"The calculator program many OOP principals such as Encapsulation, Inheritance, Polymorphism, and Abstraction. Encapsulation describes the idea of wrapping data and the methods(such as addition and multiplication) that work on data within one unit. Inheritance allows us to define a class that inherits all the methods and properties from another class, such as using different math methods like addition and subtraction. Polymorphism allows the user of the calculator program to use simple calls such as add, or divide followed by numbers to calculate. Abstraction in Python is the process of hiding the real implementation of an application from the user and emphasizing only on how to use the application, which helps us hide data that would be irrelevant to the user." in response.data

def test_request_page8(client):
    """This makes the index page"""
    response = client.get("/page8")
    assert response.status_code == 200
    assert b"CI/CD(Continuous Integration and Continuous Deployment) are what allow us to keep the website or application running while also being stable. There are a series of checks before the application is deployed, making sure it's always stable." in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page9")
    assert response.status_code == 404