import requests


def get_all_users():
    url = "http://127.0.0.1:8000/users"
    response = requests.get(url)
    return response.json()


def get_users_with_param_requests(user_id: str, user_type: str, not_banned: bool):
    url = "http://127.0.0.1:8000/users"
    response = requests.get(url, params={"user_id": user_id, "user_type": user_type, "not_banned": not_banned})
    return response.json()


def get_users_with_param_path(user_param: str):
    url = f"http://127.0.0.1:8000/users/{user_param}"
    response = requests.get(url)
    return response.json()


def get_users_with_param_mix(user_type: str, user_id: str, not_banned: bool):
    url = f"http://127.0.0.1:8000/users/{user_type}/q"
    response = requests.get(url, params={"user_id": user_id, "not_banned": not_banned})
    return response.json()


users = get_all_users()
for user in users:
    print(user)

print("done")

users = get_users_with_param_requests(user_id="4922ecb5-d927-40e1-a8e6-54cb4dd81965", user_type="applicant", not_banned=True)
for user in users:
    print(user)

print("done")

users = get_users_with_param_path("applicant")
for user in users:
    print(user)

print("done")

users = get_users_with_param_mix("applicant", user_id="ca13068b-8ba9-4966-9cda-8edf3bb85e1b", not_banned=False)
print(users)
