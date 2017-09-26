from flask import abort
from user.models import User


def createNewUser(name, email, password, remote_addr):
    user = User.create(
        username=name,
        email=email,
        password=password,
        remote_addr=remote_addr,
    )
    return user


def getUser(id):
    return User.getUserInfo(id)