from app.user.models import User

def getUser(id):
    return User.getUserInfo(id)