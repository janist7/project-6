from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_required
from flask_login import current_user
from sqlalchemy import asc
from app.categories.models import Category
from ..categories import categories

@categories.route('/categories', methods=['GET'])
def showCategories():
    categories = Category.query.order_by(asc(Category.name))
    return render_template('categories.html', categories=categories)

@categories.route('/categories/new/', methods=['GET', 'POST'])
@login_required
def newCategory():
    if request.method == 'POST':
        newCategory = Category.create(
            name=request.form['name'],
            user_id=current_user.get_id()
        )
        flash('New Category %s Successfully Created' % newCategory.name)
        return redirect(url_for('categories.showCategories'))
    else:
        return render_template('newCategory.html')

@categories.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
@login_required
def editCategory(category_id):
    editedCategory = Category.query.filter_by(id=category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)


# Delete a restaurant
@categories.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
@login_required
def deleteCategory(category_id):
    categoryToDelete = Category.query.filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)
