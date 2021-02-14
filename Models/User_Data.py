import uuid


class UserData:

    def user_data_generator(self):
        valid_password = "1" * 8
        email = f"{uuid.uuid4().hex}@gmail.com"

        return {
            "email": email,
            "password": f"{valid_password}",
            "passwordRepeat": f"{valid_password}",
            "securityQuestion": {
                "id": 12,
                "question": "Your favorite movie?",
                "createdAt": "2020-05-28T15:35:07.379Z",
                "updatedAt": "2020-05-28T15:35:07.379Z"
            },
            "securityAnswer": "movie"
        }