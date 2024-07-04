from tests.test_users import create_unique_user
import requests
API_URL = "http://127.0.0.1:5000/"

def login_user():
    user = create_unique_user()
    login_info = {
                "email": user.get("user_dictionary")["email"],
                "password": user.get("non_crypted_passwd")
                }
    
    response = requests.post(f"{API_URL}/login", json=login_info)
    json_obj = response.json()
    jwt_token = json_obj.get("access_token")
    
    return jwt_token