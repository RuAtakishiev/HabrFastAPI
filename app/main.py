import os
from typing import Optional

from fastapi import FastAPI

from utils import json_to_dict_list


def get_path_to_json(file_name: str) -> str:
    # Получаем путь к директории текущего скрипта
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Переходим на уровень выше
    parent_dir = os.path.dirname(script_dir)

    # Получаем путь к JSON
    path_to_json = os.path.join(parent_dir, file_name)

    return path_to_json


def get_users_from_role(searching_data: list, value: Optional[str] = None):
    result_list = searching_data

    path_to_json_user_types = get_path_to_json("./json/user_type.json")
    user_types = json_to_dict_list(path_to_json_user_types)

    for i_user_type in user_types:
        if value == i_user_type["name"]:
            result_list = [i for i in searching_data if i["user_type"] == i_user_type["id"]]
            break
    
    else:
        raise ValueError("Пользователя с такой ролью не существует!")
    
    return result_list


def get_users_status(searching_data: list, value: Optional[bool] = None):    
    return [user for user in searching_data if value == user["not_banned"]]
    

def get_users_by_parameters(searching_data: list, **kwargs) -> list:    
    result_list = searching_data

    for key, value in kwargs.items():
        if key == "user_type":
            result_list = get_users_from_role(result_list, value)
        
        if key == "not_banned":
            result_list = get_users_status(result_list, value)

    return result_list


app = FastAPI()


@app.get("/")
def home_page():
    return {"message": "Привет, Хабр!"}


@app.get("/users")
def get_users(user_type: Optional[str] = None, not_banned: Optional[bool] = None) -> list:
    path_to_json_users = get_path_to_json("./json/user.json")
    users = json_to_dict_list(path_to_json_users)

    result_list = users

    if user_type is not None:
        result_list = get_users_by_parameters(result_list, user_type=user_type)

    if not_banned is not None:
        result_list = get_users_by_parameters(result_list, not_banned=not_banned)
    
    return result_list


@app.get("/users/{user_type}")
def get_users_specified_type(user_type: str, not_banned: Optional[bool] = None) -> list:
    path_to_json_users = get_path_to_json("./json/user.json")
    users = json_to_dict_list(path_to_json_users)

    result_list = users

    if user_type is not None:
        result_list = get_users_by_parameters(result_list, user_type=user_type)

    if not_banned is not None:
        result_list = get_users_by_parameters(result_list, not_banned=not_banned)

    return result_list

