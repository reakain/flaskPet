from . import user_pages

@user_pages.route('/user_pages')
def user_pages():
	return 'user_pages'