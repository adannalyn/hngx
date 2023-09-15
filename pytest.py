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
    if response.status_code == 201:
        print("Person created successfully.")
        print(response.json())
    else:
        print("Failed to create person.")
        print(response.status_code)
        print(response.text)

# Function to fetch details of a person by name
def fetch_person_by_name(name):
    url = f"{base_url}/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Fetched person details successfully.")
        print(response.json())
    else:
        print("Failed to fetch person details.")
        print(response.status_code)
        print(response.text)

# Function to update details of an existing person by name
def update_person_by_name(name, age, email):
    url = f"{base_url}/{name}"
    data = {
        "age": age,
        "email": email
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Person updated successfully.")
        print(response.json())
    else:
        print("Failed to update person.")
        print(response.status_code)
        print(response.text)

# Function to delete a person by name
def delete_person_by_name(name):
    url = f"{base_url}/{name}"
    response = requests.delete(url)
    if response.status_code == 204:
        print("Person deleted successfully.")
    else:
        print("Failed to delete person.")
        print(response.status_code)
        print(response.text)

# Test the API
def run_tests():
    # Test data
    name = "Mark Essien"
    age = 30
    email = "mark@example.com"

    # Create a new person
    create_person(name, age, email)

    # Fetch person details by name
    fetch_person_by_name(name)

    # Update person details by name
    new_age = 31
    new_email = "mark.updated@example.com"
    update_person_by_name(name, new_age, new_email)

    # Fetch updated person details by name
    fetch_person_by_name(name)

    # Delete the person by name
    delete_person_by_name(name)

# Run the tests
run_tests()
