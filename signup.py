def signup(db, username, password):
    user = db.get_user(username)
    if user:
        print("User Already register")
        return
    
    db.add_user(username, password)
    print("Signup Sucessfully")

