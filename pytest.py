import requests

# Define the API base URL
base_url = 'http://localhost:3000/api/people'  # Replace with your API endpoint

# Initialize person_id to None
person_id = None

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
    if create_response.status_code == 201:
        person_id = create_response.json().get('_id')
        if person_id:
            print(f"Person created with ID: {person_id}")
        else:
            print("Response did not contain '_id' field.")
    else:
        print(f"Failed to create person. Status code: {create_response.status_code}")

    # Fetch details of the created person
    if person_id:
        fetch_response = fetch_person(person_id)
        if fetch_response.status_code == 200:
            person_data = fetch_response.json()
            print("Fetch Response:", person_data)
        else:
            print(f"Failed to fetch person details. Status code: {fetch_response.status_code}")

        # Modify the person's details
        if person_data:
            update_data = {"name": "Updated Name"}
            update_response = update_person(person_id, update_data)
            if update_response.status_code == 200:
                print("Update Response:", update_response.json())
            else:
                print(f"Failed to update person details. Status code: {update_response.status_code}")

            # Remove the person
            delete_response = delete_person(person_id)
            if delete_response.status_code == 204:
                print("Person removed successfully.")
            else:
                print(f"Failed to remove person. Status code: {delete_response.status_code}")
