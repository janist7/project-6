from flask import abort
from sqlalchemy import asc
from app.categories.models import Category
from app.recipes.models import Recipe
from app.user.models import User


def categoryList():
    return Category.getCategories()

def currentCategory(category_id):
    return Category.getCurrentCategory(category_id)

def categoryCreator(category):
    return User.getUserInfo(category.user_id)

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
