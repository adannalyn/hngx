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
        print(response.text)

# Function to fetch details of a person
def fetch_person(person_id):
    url = f"{base_url}/{person_id}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Person details fetched successfully.")
        print(response.json())
    else:
        print("Failed to fetch person details.")
        print(response.text)

# Function to update details of an existing person
def update_person(person_id, age, email):
    url = f"{base_url}/{person_id}"
    data = {
        "age": age,
        "email": email
    }
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Person details updated successfully.")
        print(response.json())
    else:
        print("Failed to update person details.")
        print(response.text)

# Function to delete a person
def delete_person(person_id):
    url = f"{base_url}/{person_id}"
    response = requests.delete(url)
    if response.status_code == 204:
        print("Person deleted successfully.")
    else:
        print("Failed to delete person.")
        print(response.text)

# Test the API
def run_tests():
    # Test data
    name = "Mark Essien"
    age = 30
    email = "mark@example.com"

    # Create a new person
    create_person(name, age, email)

    # Fetch person details
    fetch_person(1)  # Assuming the ID is 1

    # Update person details
    new_age = 31
    new_email = "mark.updated@example.com"
    update_person(1, new_age, new_email)  # Assuming the ID is 1

    # Fetch updated person details
    fetch_person(1)  # Assuming the ID is 1

    # Delete the person
    delete_person(1)  # Assuming the ID is 1

    # Attempt to fetch person details after deletion
    fetch_person(1)  # Assuming the ID is 1


# Run the tests
run_tests()
