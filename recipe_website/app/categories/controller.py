from flask import abort
from sqlalchemy import asc
from .models import Category
from recipes.models import Recipe
from user.models import User


# Returns all categories
def categoryList():
    return Category.getCategories()


# Returns 1 category
def currentCategory(category_id):
    return Category.getCurrentCategory(category_id)


# Returns user info that created the category
def categoryCreator(category):
    return User.getUserInfo(category.user_id)


# Returns Recipe list for this category
def recipeList(category_id):
    return Recipe.getRecipeList(category_id)


def createNewCategory(name, id):
    Category.create(
        name=name,
        user_id=id
    )
    return True


def updateCategory(category, name):
    category.name = name
    category.update()
    return True


def deleteCategory(category, category_id):
    try:
        recipes = recipeList(category_id)
        recipes.delete()
    except:
        abort(500)
    category.delete()
    return True
