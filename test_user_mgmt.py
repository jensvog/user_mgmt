from user_mgmt import create_html_output


# Test class for creating HTML output
class TestCreateHTMLOutput:
    def test_with_one_user(self):
        users = [{'id': 1,
                  'email': 'george.bluth@reqres.in',
                  'first_name': 'George', 
                  'last_name': 'Bluth',
                  'avatar': 'https://reqres.in/img/faces/1-image.jpg'}]
        assert(create_html_output(users) == '''<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Users of the System</title>
</head>
<body>
    <h1>Users of the System</h1>
    <table>
        <tr>
            <th>Avatar</th><th>ID</th><th>E-Mail</th><th>Name</th>
        </tr>
        
        <tr>
            <td><img src="https://reqres.in/img/faces/1-image.jpg" /></td><td>1</td><td>george.bluth@reqres.in</td><td>George Bluth</td>
        </tr>
        
    </table>
</body>
</html>''')
