from flask import (
    current_app, request, redirect, url_for, render_template, flash, abort,
)
from flask_babel import gettext
from flask_login import login_required
from app.recipes.models import Recipe
from ..recipes import recipes

@recipes.route('/category/<int:category_id>/')
@recipes.route('/category/<int:category_id>/recipe/')
def showRecipe(category_id):
    category = Recipe.query.filter_by(id=category_id).one()
    creator = getUserInfo(category.user_id)
    items = Recipe.query.filter_by(category_id=category_id).all()
    return render_template('showRecipe.html', items=items, category=category, creator=creator)

@recipes.route('/category/<int:category_id>/recipe/new/', methods=['GET', 'POST'])
def newMenuItem(category_id):
    category = Recipe.query.filter_by(id=category_id).one()
    if request.method == 'POST':
        newRecipe = Recipe.create(
            name=request.form['name'],
            description=request.form['description'],
            image_url="test",
            restaurant_id=restaurant_id,
            user_id=restaurant.user_id
        )
        flash('New Menu %s Item Successfully Created' % (newRecipe.name))
        return redirect(url_for('showRecipe', category_id=category_id))
    else:
        return render_template('newRecipe.html', category_id=category_id)

@recipes.route('/category/<int:category_id>/recipe/<int:recipe_id>/edit', methods=['GET', 'POST'])
def editMenuItem(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(MenuItem).filter_by(id=menu_id).one()
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit menu items to this restaurant. Please create your own restaurant in order to edit items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['course']:
            editedItem.course = request.form['course']
        session.add(editedItem)
        session.commit()
        flash('Menu Item Successfully Edited')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('editmenuitem.html', restaurant_id=restaurant_id, menu_id=menu_id, item=editedItem)


# Delete a restaurant
@recipes.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def deleteMenuItem(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    itemToDelete = session.query(MenuItem).filter_by(id=menu_id).one()
    if login_session['user_id'] != restaurant.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete menu items to this restaurant. Please create your own restaurant in order to delete items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('deleteMenuItem.html', item=itemToDelete)
