import json
from app import db
from app.models import User


def adduser(data, su=False):

    if data:
        username = data['username']
        password = data['password']
        for user in User.query.all():
            if user.username == username:
                #Username exists
                return False
        user = User()
        user.username = username
        user.set_password(password)
    else:
        return False

    if su:
        for user in User.query.all():
            if user.is_superuser: return False
        user.is_superuser = True
        db.session.add(user)
        db.session.commit()
        return True

    user.is_superuser = False
    db.session.add(user)
    db.session.commit()
    return True