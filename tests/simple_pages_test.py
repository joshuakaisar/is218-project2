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
    assert b"Page 4" in response.data

def test_request_page_not_found(client):
    """This makes the index page"""
    response = client.get("/page5")
    assert response.status_code == 404