from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_required
from app.utils import babel_flash_message
from .forms import NewRecipe, EditRecipe, DeleteRecipe
from ..recipes import recipes, controller

@recipes.route('/category/<int:category_id>/', methods=['GET'])
@recipes.route('/category/<int:category_id>/recipe/', methods=['GET'])
def showRecipe(category_id):
    try:
        category = controller.currentCategory(category_id)
        creator = controller.categoryCreator(category)
        recipes = controller.recipeList(category_id)
    except:
        abort(404)
    return render_template('showRecipe.html', recipes=recipes, category=category, creator=creator)

@recipes.route('/category/<int:category_id>/recipe/new/', methods=['GET', 'POST'])
@login_required
def newRecipe(category_id):
    try:
        category = controller.currentCategory(category_id)
        creator = controller.categoryCreator(category)
    except:
        abort(404)
    try:
        form = NewRecipe()
    except:
        abort(500)
    if form.validate_on_submit():
        controller.createNewRecipe(form.data['name'], form.data['description'], "test", category_id, category.user_id)
        babel_flash_message('Recipe "{data}" successfully created', form.data['name'])
        return redirect(url_for('recipes.showRecipe', category_id=category_id))
    else:
        return render_template('forms/newRecipe.html', category_id=category_id, creator=creator, form=form)

@recipes.route('/category/<int:category_id>/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
@login_required
def editRecipe(category_id, recipe_id):
    try:
        editedRecipe = controller.currentRecipe(recipe_id)
        category = controller.currentCategory(category_id)
        creator = controller.categoryCreator(category)
    except:
        pass
    try:
        form = EditRecipe()
    except:
        abort(500)
    if form.validate_on_submit():
        controller.updateRecipe(editedRecipe, form.data['name'], form.data['description'])
        babel_flash_message('Recipe "{data}" successfully edited', form.data['name'])
        return redirect(url_for('recipes.showRecipe', category_id=category_id))
    else:
        return render_template('forms/editRecipe.html', category_id=category_id, recipe_id=recipe_id, recipe=editedRecipe, creator=creator, form=form)


# Delete a restaurant
@recipes.route('/category/<int:category_id>/menu/<int:recipe_id>/delete', methods=['GET', 'POST'])
@login_required
def deleteRecipe(category_id, recipe_id):
    try:
        category = controller.currentCategory(category_id)
        creator = controller.categoryCreator(category)
        recipeToDelete = controller.currentRecipe(recipe_id)
    except:
        abort(404)
    try:
        form = DeleteRecipe()
    except:
        abort(500)
    if form.validate_on_submit():
        controller.deleteRecipe(recipeToDelete)
        babel_flash_message('Recipe "{data}" Successfully Deleted', recipeToDelete.name)
        return redirect(url_for('recipes.showRecipe', category_id=category_id))
    else:
        return render_template('forms/deleteRecipe.html', recipe=recipeToDelete, creator=creator, form=form, category_id=category_id)
