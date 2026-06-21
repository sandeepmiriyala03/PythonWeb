from repository.user_repository import userRepository

class userService:

    @staticmethod
    def create_user(user):

        userRepository.create_user(user)

        return {
            "message": user.username + " Created"
        }

    @staticmethod
    def get_users():
        user_list = userRepository.get_users()
        # Implement the logic to retrieve users from the database
        # For now, returning a placeholder response
        return {
            "message": "List of users",
            "users": user_list
        }
