""" All Users managment related views """

from flask import request, redirect, url_for, render_template, flash, g, abort
from flask_babel import gettext
from flask_login import login_required
from app.user.models import User
from app.user.forms import EditUserForm
from flask_login import current_user
from app.utils import babel_flash_message
from app.database import DataTable
from ..user import user, controller


@user.route('/list', endpoint='list', methods=['GET', 'POST'])
@login_required
def list():
    if current_user.is_admin:
        datatable = DataTable(
            model=User,
            columns=[User.remote_addr],
            sortable=[User.username, User.email, User.created_ts],
            searchable=[User.username, User.email],
            filterable=[User.active],
            limits=[25, 50, 100],
            request=request
        )

        if g.pjax:
            return render_template(
                'users.html',
                datatable=datatable,
                stats=User.stats()
            )

        return render_template(
            'list.html',
            datatable=datatable,
            stats=User.stats()
        )
    else:
        abort(404)


@user.route('/edit/<int:id>', endpoint='edit', methods=['GET', 'POST'])
@login_required
def edit(id):
    if current_user.is_admin:
        user = controller.getUser(id)
        form = EditUserForm(obj=user)
        if form.validate_on_submit():
            form.populate_obj(user)
            user.update()
            babel_flash_message('User {data} edited', user.username)
        return render_template('edit.html', form=form, user=user)
    else:
        abort(404)


@user.route('/delete/<int:id>', endpoint='delete', methods=['GET'])
@login_required
def delete(id):
    if current_user.is_admin:
        user = controller.getUser(id)
        # Deleteting user breaks any categories that the user created and making the server return 404s.
        # 1) Could delete the category and all recipes asociated, but it doesnt make sense
        # 2) Best option would be to just deacivate the account
        user.delete()
        babel_flash_message('User {data} deleted', user.username)
        return redirect(url_for('.list'))
    else:
        abort(404)
