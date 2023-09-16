import requests

# Base URL for the API
base_url = "http://localhost:3000/api/people"

# Define a class to represent a person
class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def to_json(self):
        return {
            "name": self.name,
            "age": self.age,
            "email": self.email,
        }

# Define a function to create a new person
def create_person(person):
    url = f"{base_url}"
    data = person.to_json()
    headers = {"Content-Type": "application/json"}

    response = requests.post(url, json=data, headers=headers)
    response.raise_for_status()
    # The server should return the created person with an assigned ID
    return Person(**response.json())

# Define a function to fetch a person by ID
def fetch_person(person_id):
    url = f"{base_url}/{person_id}"

    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        return Person(**response.json())
    else:
        return None

# Define a function to update a person by ID
def update_person(person):
    url = f"{base_url}/{person.id}"
    data = person.to_json()
    headers = {"Content-Type": "application/json"}

    response = requests.put(url, json=data, headers=headers)
    response.raise_for_status()
    return True

# Define a function to delete a person by ID
def delete_person(person_id):
    url = f"{base_url}/{person_id}"

    response = requests.delete(url)
    response.raise_for_status()
    return True

# Define a function to test all the CRUD operations
def test_crud_operations():
    # Create a new person
    person = Person("John Doe", 35, "john.doe@example.com")
    created_person = create_person(person)

    # Assert that the created person is a Person object
    assert isinstance(created_person, Person)

    # Fetch the person by ID
    fetched_person = fetch_person(created_person.id)

    # Assert that the fetched person is equal to the created person
    assert fetched_person == created_person

    # Update the person's name
    person.name = "Jane Doe"
    update_person(person)

    # Fetch the person by ID again
    fetched_person = fetch_person(created_person.id)

    # Assert that the fetched person's name has been updated
    assert fetched_person.name == "Jane Doe"

    # Delete the person
    delete_person(created_person.id)

    # Fetch the person by ID again
    fetched_person = fetch_person(created_person.id)

    # Assert that the person does not exist
    assert fetched_person is None

# Example usage:

# Test all the CRUD operations
test_crud_operations()
