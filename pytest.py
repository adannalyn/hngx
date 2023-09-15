import requests

# Base URL for the API
base_url = "http://localhost:3000/api/people"

# Function to create a new person
def create_person(name, age, email):
    url = base_url
    data = {
        "name": name,
        "age": age,
        "email": email
    }
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())

# Function to fetch details of a person
def fetch_person(person_id):
    url = f"{base_url}/{person_id}"
    response = requests.get(url)
    print(response.status_code)
    print(response.json())

# Function to update details of an existing person
def update_person(person_id, age, email):
    url = f"{base_url}/{person_id}"
    data = {
        "age": age,
        "email": email
    }
    response = requests.put(url, json=data)
    print(response.status_code)
    print(response.json())

# Function to delete a person
def delete_person(person_id):
    url = f"{base_url}/{person_id}"
    response = requests.delete(url)
    print(response.status_code)

# Test the API
def run_tests():
    # Test data
    name = "Mark Essien"
    age = 30
    email = "mark@example.com"

    # Create a new person
    create_person(name, age, email)

    # Fetch person details
    fetch_person(name)

    # Update person details
    new_age = 31
    new_email = "mark.updated@example.com"
    update_person(name, new_age, new_email)

    # Fetch updated person details
    fetch_person(name)

    # Delete the person
    delete_person(name)

    # Fetch person details after deletion
    fetch_person(name)


# Run the tests
run_tests()
