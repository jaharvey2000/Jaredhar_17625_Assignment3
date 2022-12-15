# 17-625 API Design

## Assignment 3: gRPC API

**TO START SERVER:** `python .\service\inventory_server.py`

**TO EXECUTE TESTS:** `python .\service\inventory_client.py`

-----

### Assignment Description

This assignment is meant to introduce students to the design and implementation of protocol buffers and gRPC APIs. In this assignment, students must implement a simple book inventory API, which can store and retrieve book objects. Students must use protocol buffers and gRPC to implement this API, utilizing the *protoc* compiler and Python to implement the API.

Students follow a [tutorial]() to learn how to implement their API. However, their API must meet the following specifications:

* Protocol buffers for "Book" and "InventoryItem" class of objects must be implemented,
* An "InventoryService" must be implemented, which supports the two following RPCs:
  * **CreateBook:** A new book is added to the database, and
  * **GetBook:** An existing book is fetched from the database.
* The RPCs must be implemented in a server using Python.

Students should implement their API by following gRPC best practices.

As an optional extra credit, students can test their APIs using a query tool such as Postman, Kreya, etc.

### Design Choices

Since the specifications are fairly clear in the assignment description, I did not take many liberties with this assignment. I have made the following choices and assumptions:

* I have used **optional** parameters for my protocol buffers, as this is generally preferred for future flexibility.
* To ensure that a book cannot be added which doesn't have all fields populated, I have added requirements to this in my server. These errors will be returned when the API is called with an incomplete Book object.
* I have added additional checks for whether a book exists in the database. When a book is being added with *CreateBook*, then that book's ISBN should not exist in the database. Conversely, if a book is being fetched with *GetBook*, that book must exist in the database. If either of these conditions fail to hold, the server returns an error.
