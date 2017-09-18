""" All Category related views """

from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_required
from flask_login import current_user
from app.utils import babel_flash_message
from .forms import NewCategory, EditCategory, DeleteCategory
from ..categories import categories, controller


@categories.route('/categories', methods=['GET'])
def showCategories():
    return render_template('categories.html', categories=controller.categoryList())


@categories.route('/categories/new/', methods=['GET', 'POST'])
@login_required
def newCategory():
    try:
        form = NewCategory()
    except:
        abort(500)
    if form.validate_on_submit():
        controller.createNewCategory(form.data['name'], current_user.get_id())
        babel_flash_message('Category "{data}" successfully created', form.data['name'])
        return redirect(url_for('categories.showCategories'))
    else:
        return render_template('forms/newCategory.html', form=form)


@categories.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
@login_required
def editCategory(category_id):
    try:
        editedCategory = controller.currentCategory(category_id)
        creator = controller.categoryCreator(editedCategory)
    except:
        abort(404)
    try:
        form = EditCategory()
    except:
        abort(500)
    if form.validate_on_submit():
        if form.data['name']:
            controller.updateCategory(editedCategory, form.data['name'])
            babel_flash_message('Category "{data}" successfully edited', form.data['name'])
            return redirect(url_for('categories.showCategories'))
    else:
        return render_template('forms/editCategory.html', category=editedCategory,
                               creator=creator, category_id=category_id, form=form)


# Delete a restaurant
@categories.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteCategory(category_id):
    try:
        categoryToDelete = controller.currentCategory(category_id)
        creator = controller.categoryCreator(categoryToDelete)
    except:
        abort(404)
    try:
        form = DeleteCategory()
    except:
        abort(500)
    if form.validate_on_submit():
        controller.deleteCategory(categoryToDelete, category_id)
        babel_flash_message('Category "{data}" successfully deleted', categoryToDelete.name)
        return redirect(url_for('categories.showCategories', category_id=category_id))
    else:
        return render_template('forms/deleteCategory.html', category=categoryToDelete,
                               creator=creator, category_id=category_id, form=form)
