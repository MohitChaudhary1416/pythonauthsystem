def login(db, username, password):
    user = db.get_user(username)
    if not user:
        print("User not registered")
        return
 
    if password == user[1]:
        print("login success")
    else:
        print("Invalid password")
   
    return
 