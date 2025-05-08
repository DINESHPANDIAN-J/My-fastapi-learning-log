from fastapi import Depends
def get_user_name():
    return "Dinesh J" # This function returns a hardcoded username "user_one". It can be used to fetch the username from a database or any other source in a real-world application.

def get_prefix():
    return "Mr." # This function returns a hardcoded prefix "Mr.

def get_suffix():
    return "J" # This function returns a hardcoded suffix "J".

def get_full_name(prefix:str =Depends(get_prefix), name:str = Depends(get_user_name), suffix:str =Depends(get_suffix)):
    return "{}{}{}".format(prefix, name, suffix) # This function returns the full name by combining the prefix, name, and suffix. It uses FastAPI's Depends to inject the dependencies.

class UserService:
    def __init__(self):
        self.users = ["Dinesh J", "J D Pandian", "Arohara Velan"] # This is a list of hardcoded usernames. In a real-world application, this could be replaced with a database or any other data source.

    def get_users(self):
        return self.users
    
def get_user_service():
    return UserService() # This function returns an instance of the UserService class. It can be used to access user-related services in a FastAPI application.