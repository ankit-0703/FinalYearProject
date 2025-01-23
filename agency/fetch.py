from django.db import models
from models import User  # Replace 'your_app' with your app name

def get_user_name(user_id):
    """
    Fetches and prints the username from the database based on the provided user ID.

    Args:
        user_id (int): The ID of the user.

    Returns:
        None
    """

    try:
        user = User.objects.get(pk=user_id)
        print(user.username)  # Replace 'username' with the actual field name
    except User.DoesNotExist:
        print("User not found.")

# Example usage:
name=GodXThor  # Replace with the actual user ID
getattr(email_address)