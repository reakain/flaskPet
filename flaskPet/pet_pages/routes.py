from . import pet_pages

@pet_pages.route('/pet/<pet_id>')
@login_required
def pet(pet_id):
	pet = Pet.query.filter_by(pet_id=pet_id).first_or_404()
	owner = pet.find_owner();
    return render_template('pet.html', pet=pet, owner=owner)