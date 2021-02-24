import requests
import jinja2

# Exception class when no API is available
class ApiError(Exception):
    def __init__(self, message):
        self.expression = expression


# Retrieves information from API
def get_data_from_api(page=1):
    r = requests.get("https://reqres.in/api/users?page=" + str(page))
    if r.status_code == 200:
        return r.json()
    else:
        raise ApiError("API not available")


# Lists all users by calling the API function
def list_users():
    users = []
    page = 1
    total_pages = -1

    while (total_pages == -1 or page <= total_pages):
        data = get_data_from_api(page)
        total_pages = data["total_pages"]
        page += 1
        users_page = data["data"]
        users.extend(users_page)
    return users


# Creates HTML output with a template
def create_html_output(users):
    return jinja2.Environment( 
                loader=jinja2.FileSystemLoader('./')      
                ).get_template('template.html').render(mydata=users) 


# Main application code
if __name__ == "__main__":
    try:
        # Get users
        users = list_users()
        # Create HTML output
        html_page = create_html_output(users)
        # Write to file
        with open('index.html', 'w') as f:
            f.write(html_page)
    except ApiError as ae:
        # Print error message, when API not available
        print(ae.message)
