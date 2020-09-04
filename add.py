from app import db
from app.models import User, Post

usernames = ["Mapel", "Mana", "Lick"]
emails = [i + "@123.com" for i in usernames]
data = dict(zip(usernames, emails))
for username, email in data.items():
    u = User(username=username, email=email)
    db.session.add(u)
    db.session.commit()
print("done")
