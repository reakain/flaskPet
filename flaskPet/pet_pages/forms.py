class EditPetPageForm(FlaskForm):
    petname = StringField('Pet Name', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')
	
	def __init__(self, original_petname, *args, **kwargs):
        super(EditPetPageForm, self).__init__(*args, **kwargs)
        self.original_petname = original_petname