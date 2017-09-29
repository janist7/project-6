from app.user.models import User

# Returns user info
def getUser(id):
    return User.getUserInfo(id)
