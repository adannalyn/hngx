import requests

# Define the API base URL
base_url = 'http://localhost:3000/api/people'  # Replace with your API endpoint

# Function to create a new person
def create_person(name):
    data = {"name": name}
    response = requests.post(base_url, json=data)
    return response

# Function to fetch details of a person
def fetch_person(person_id):
    url = f'{base_url}/{person_id}'
    response = requests.get(url)
    return response

# Function to modify details of an existing person
def update_person(person_id, updated_data):
    url = f'{base_url}/{person_id}'
    response = requests.put(url, json=updated_data)
    return response

# Function to remove a person
def delete_person(person_id):
    url = f'{base_url}/{person_id}'
    response = requests.delete(url)
    return response

# Example usage
if __name__ == "__main__":
    # Create a new person
    create_response = create_person("Mark Essien")
    print("Create Response:", create_response.json())

    # Fetch details of the created person
    person_id = create_response.json()['_id']
    fetch_response = fetch_person(person_id)
    print("Fetch Response:", fetch_response.json())

    # Modify the person's details
    update_data = {"name": "Updated Name"}
    update_response = update_person(person_id, update_data)
    print("Update Response:", update_response.json())

    # Remove the person
    delete_response = delete_person(person_id)
    print("Delete Response:", delete_response.status_code)
