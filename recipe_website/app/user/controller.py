from .models import User

# Returns user info
def getUser(id):
    return User.getUserInfo(id)
