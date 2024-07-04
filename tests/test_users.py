import requests
import uuid

from tests import test_functions
from flask import jsonify

API_URL = "http://127.0.0.1:5000/"


def create_unique_user():
    """
    Helper function to create a new user with a unique email.
    Sends a POST request to /users with new user data and returns the created user's ID.
    """
    unique_email = f"test.user.{uuid.uuid4()}@example.com"
    new_user = {
        "email": unique_email,
        "first_name": "Test",
        "last_name": "User",
        "password": "password123"
    }
    response = requests.post(f"{API_URL}/users", json=new_user)
    assert (
        response.status_code == 201
    ), f"Expected status code 201 but got {response.status_code}. Response: {response.text}"
    return {"user_dictionary": response.json(), "non_crypted_passwd": new_user.get("password")}


def login_user():
    user = create_unique_user()
    login_info = {
                "email": user.get("user_dictionary")["email"],
                "password": user.get("non_crypted_passwd")
                }
    print(login_info.get("password"))
    print(login_info.get("email"))
    response = requests.post(f"{API_URL}/login", json=login_info)
    json_obj = response.json()
    jwt_token = json_obj.get("access_token")
    #print(jwt_token)
    return jwt_token



    
def test_get_users():
    """
    Test to retrieve all users
    Sends a GET request to /users and checks that the response status is 200
    and the returned data is a list.
    """
    jwt_token = login_user()
    print("my jwt", jwt_token)
    print("The type of the token", type(jwt_token))
    my_header = {"Authorization": f"Bearer {jwt_token}"}
    response = requests.get(f"{API_URL}/users", headers=my_header)
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    assert isinstance(
        response.json(), list
    ), f"Expected response to be a list but got {type(response.json())}"


def test_post_user():
    """
    Test to create a new user
    Sends a POST request to /users with new user data and checks that the
    response status is 201 and the returned data matches the sent data.
    """
    
    unique_email = f"test.user.{uuid.uuid4()}@example.com"
    new_user = {
        "email": unique_email,
        "first_name": "John",
        "last_name": "Doe",
        "password": "password123"
    }
    response = requests.post(f"{API_URL}/users", json=new_user)
    assert (
        response.status_code == 201
    ), f"Expected status code 201 but got {response.status_code}. Response: {response.text}"
    user_data = response.json()
    assert (
        user_data["email"] == new_user["email"]
    ), f"Expected email to be {new_user['email']} but got {user_data['email']}"
    assert (
        user_data["first_name"] == new_user["first_name"]
    ), f"Expected first name to be {new_user['first_name']} but got {user_data['first_name']}"
    assert (
        user_data["last_name"] == new_user["last_name"]
    ), f"Expected last name to be {new_user['last_name']} but got {user_data['last_name']}"
    assert "id" in user_data, "User ID not in response"
    assert "created_at" in user_data, "Created_at not in response"
    assert "updated_at" in user_data, "Updated_at not in response"
    return user_data["id"]  # Return the ID of the created user for further tests


def test_get_user():
    """
    Test to retrieve a specific user by ID
    Creates a new user, then sends a GET request to /users/{id} and checks that the
    response status is 200 and the returned data matches the created user's data.
    """
    jwt_token = login_user()
    my_header = {"Authorization": f"Bearer {jwt_token}"}
    new_user = create_unique_user()
    new_user_id = new_user.get("user_dictionary")["id"]
    # Retrieve the newly created user
    response = requests.get(f"{API_URL}/users/{new_user_id}", headers=my_header)
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    user_data = response.json()
    assert (
        user_data["id"] == new_user_id
    ), f"Expected user ID to be {new_user_id} but got {user_data['id']}"
    assert "email" in user_data, "Email not in response"
    assert "first_name" in user_data, "First name not in response"
    assert "last_name" in user_data, "Last name not in response"
    assert "created_at" in user_data, "Created_at not in response"
    assert "updated_at" in user_data, "Updated_at not in response"


def test_put_user():
    """
    Test to update an existing user
    Creates a new user, then sends a PUT request to /users/{id} with updated user data
    and checks that the response status is 200 and the returned data matches the updated data.
    """
    jwt_token = login_user()
    my_header = {"Authorization": f"Bearer {jwt_token}"}
    user_to_update = create_unique_user()
    user_dict = user_to_update.get("user_dictionary")
    user__id = user_dict.get("id")
    # Update the newly created user
    updated_user = {
        "email": f"updated.user.{uuid.uuid4()}@example.com",
        "first_name": "John",
        "last_name": "Smith",
        "password": "newpassword123"
    }
    response = requests.put(f"{API_URL}/users/{user__id}", json=updated_user, headers=my_header)
    assert (
        response.status_code == 200
    ), f"Expected status code 200 but got {response.status_code}. Response: {response.text}"
    user_data = response.json()
    assert (
        user_data["email"] == updated_user["email"]
    ), f"Expected updated email to be {updated_user['email']} but got {user_data['email']}"
    assert (
        user_data["first_name"] == updated_user["first_name"]
    ), f"Expected updated first name to be {updated_user['first_name']} but got {user_data['first_name']}"
    assert (
        user_data["last_name"] == updated_user["last_name"]
    ), f"Expected updated last name to be {updated_user['last_name']} but got {user_data['last_name']}"
    assert "id" in user_data, "User ID not in response"
    assert "created_at" in user_data, "Created_at not in response"
    assert "updated_at" in user_data, "Updated_at not in response"


def test_delete_user():
    """
    Test to delete an existing user
    Creates a new user, then sends a DELETE request to /users/{id} and checks that the
    response status is 204 indicating successful deletion.
    """
    jwt_token = login_user()
    my_header = {"Authorization": f"Bearer {jwt_token}"}
    user_to_delete = create_unique_user()
    user_dict = user_to_delete.get("user_dictionary")
    user__id = user_dict.get("id")
    # Delete the newly created user
    response = requests.delete(f"{API_URL}/users/{user__id}", headers=my_header)
    assert (
        response.status_code == 204
    ), f"Expected status code 204 but got {response.status_code}. Response: {response.text}"





if __name__ == "__main__":
    # Run the tests
    test_functions(
        [
            
            test_get_users,
            test_post_user,
            test_get_user,
            test_put_user,
            test_delete_user,
        ]
    )
