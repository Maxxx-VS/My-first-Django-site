import os
def authenticate(username, password):
    # file_path = os.path.join(os.path.dirname(__file__), '..', 'users.json')
    file_path = '/mysite/users.json'
    with open(file_path) as file:
        for i in file:
            i = i.strip()
            if i == f'Username: {username}, Publish: {password}':
                return True
    return False
