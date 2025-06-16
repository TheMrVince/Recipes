import requests

APP_ID = ""
APP_KEY = ""
USER_ID = "your_user_id"  # Only needed if your app requires it

def search_recipes(query):
    url = "https://api.edamam.com/api/recipes/v2"
    params = {
        "type": "public",
        "q": query,
        "app_id": APP_ID,
        "app_key": APP_KEY
    }
    headers = {
        "Edamam-Account-User": USER_ID
    }
    response = requests.get(url, params=params, headers=headers)
    return response.json()

# Example usage:
if __name__ == "__main__":
    result = search_recipes("chicken")
    print("bruh")