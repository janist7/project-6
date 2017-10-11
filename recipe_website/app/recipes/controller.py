from flask import abort
from sqlalchemy import asc
from app.categories.models import Category
from .models import Recipe
from app.user.models import User


# Returns 1 Recipe
def currentRecipe(recipe_id):
    return Recipe.getCurrentRecipe(recipe_id)


# Returns 1 Category
def currentCategory(category_id):
    return Category.getCurrentCategory(category_id)


# Returns user info that created the category
def categoryCreator(category):
    return User.getUserInfo(category.user_id)


# Returns Recipe list for this category
def recipeList(category_id):
    return Recipe.getRecipeList(category_id)


def createNewRecipe(name, description, img_url, category_id, user_id):
    Recipe.create(
        name=name,
        description=description,
        image_url=img_url,
        category_id=category_id,
        user_id=user_id
    )
    return True


def updateRecipe(recipe, name, description):
    recipe.name = name
    recipe.description = description
    recipe.update()
    return True


def deleteRecipe(recipe):
    recipe.delete()
    return True
