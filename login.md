{% include navigation.html %}

## Code Snippets:

### Phone Number

``` 
def authorize(name, email, password, phone):
    if is_user(email, password):
        return False
    else:
        auth_user = Users(
            name=name,
            email=email,
            password=password,
            phone=phone,  
        )
        auth_user.create()
        return True
```

```
<tr><th><label for="phone">Phone Number</label></th></tr>
                        <tr><td><input type="phone" id="phone" name="phone" size="20" required></td></tr>
```

```
phone = request.form.get("phone")
```

### Logout

```
@app_crud.route('/logout')
@login_required
def crud_logout():
    logout()
    return redirect(url_for('crud.crud_login'))

    return render_template("login.html")
```

```
<div style="margin-left:10px;">
            <a href = {{ url_for('crud.crud_logout')}}, style="color:black;">Log Out</a>
            <a href = {{ url_for('crud.crud_login')}}, style="color:black;">Login</a>
        </div>
```

### Password Protect a Page

```
@app_crud.route('/search/')
@login_required
def search():
    """obtains all Users from table and loads Admin Form"""
    return render_template("search.html", table=users_all())

@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('crud.crud_login'))

@app_crud.route('/login/', methods=["GET", "POST"])
def crud_login():
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):     
            return redirect(url_for('crud.search'))

    return render_template("login.html")
```

## Screenshots

### Phone Number

<img width="751" alt="phone crud" src="https://user-images.githubusercontent.com/89223557/162538590-09c96af5-8e6c-4ae3-b406-e4c9f8cc22dc.PNG">
<img width="841" alt="login page" src="https://user-images.githubusercontent.com/89223557/162538595-1668593c-381b-4d62-8ba2-fac54202710b.PNG">
<img width="855" alt="phone sign up" src="https://user-images.githubusercontent.com/89223557/162538597-9393b004-c304-48a8-a8d7-db201ce69ce1.PNG">

### Login/Logout

![login logout](https://user-images.githubusercontent.com/89223557/162538839-60ef712c-649d-4bde-a657-d9d665c1417f.png)

