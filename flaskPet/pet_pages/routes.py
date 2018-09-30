from . import pet_pages

@pet_pages.route('/pet/<pet_id>')
@login_required
def pet(pet_id):
	pet = Pet.query.filter_by(pet_id=pet_id).first_or_404()
	owner = pet.find_owner();
    return render_template('pet.html', pet=pet, owner=owner)
	
@pet_pages.route('/edit_petpage', methods=['GET', 'POST'])
@login_required
def edit_petpage():
	form = EditPetPageForm(current_user.username)
    if form.validate_on_submit():
        pet.petname = form.petname.data
        pet.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('edit_petpage'))
    elif request.method == 'GET':
        form.petname.data = pet.petname
        form.about_me.data = pet.about_me
    return render_template('edit_petpage.html', title='Edit Pet Page',
                           form=form)
						   
@pet_pages.route('/cave')
@login_required
def cave():
	return render_template('cave.html')