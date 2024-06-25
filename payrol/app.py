from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, FloatField,StringField,SubmitField, DateField, DateTimeField, TimeField
from wtforms.validators import DataRequired, Length

#This will be moved to a separate .py file in the employees folder later
class EmployeeForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(), Length(max=50)])
    lastname = StringField('Last Name', validators=[DataRequired(), Length(max=50)])
    address1 = StringField('Address 1', validators=[DataRequired(), Length(max=50)])
    address2 = StringField('Address 2')
    city = StringField('City', validators=[DataRequired(), Length(max=20)])
    state = StringField('State', validators=[DataRequired(), Length(max=2)])
    zip = StringField('ZIP Code', validators=[DataRequired(), Length(min=5, max=5)])
    hourlyrate = FloatField('Hourly Rate', validators=[DataRequired()])
    age = IntegerField('Age', validators=[])
    submit = SubmitField('Submit')

#This will be moved to a separate .py file in the employeer folder later
class EmployerForm(FlaskForm):
    companyname = StringField('Company Name', validators=[DataRequired(), Length(max=50)])
    industry = StringField('Industry or Business Segment', validators=[Length(max=50)])
    address1 = StringField('Address 1', validators=[DataRequired(), Length(max=50)])
    address2 = StringField('Address 2')
    city = StringField('City', validators=[DataRequired(), Length(max=20)])
    state = StringField('State', validators=[DataRequired(), Length(max=2)])
    zip = StringField('ZIP Code', validators=[DataRequired(), Length(min=5, max=5)])
    overtime_rate = FloatField('Overtime Pay Rate', validators=[DataRequired()])
    fulltime_employees = IntegerField('Full Time Employees', validators=[])
    submit = SubmitField('Submit')

class WorkDayForm(FlaskForm):
    comp_id = IntegerField('Company ID', validators=[DataRequired()])
    emp_id = IntegerField('Employee ID', validators=[DataRequired()])
    work_date = DateField('Date of Work (MM/DD/YYYY)', validators=[DataRequired()])
    clock_in = TimeField('Clock In Time (00:00 AM/PM)', validators=[DataRequired()])
    clock_out = TimeField('Clock Out Time (00:00 AM/PM', validators=[DataRequired()])
    submit = SubmitField('Submit')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user')
def user():
    return render_template('newpage.html')

@app.route('/jinjatest')
def jinjatest():
    message = 'The <strong>sum</strong> of the numbers is: '
    items = ['widget', 'doodad', 'thingie', 'whatsit']
    return render_template('jinjatest.html', message=message, items=items)

@app.route('/employees', methods=['GET', 'POST'])
def employees():
    form = EmployeeForm()
    if form.validate_on_submit():
        # Here, you would typically add code to insert the form data into your database
        flash('User Registered Successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to a different page, e.g., home
    return render_template('employee.html', form=form)

@app.route('/employer', methods=['GET', 'POST'])
def employer():
    form = EmployerForm()
    if form.validate_on_submit():
        # Here, you would typically add code to insert the form data into your database
        flash('Company Registered Successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to a different page, e.g., home
    return render_template('employer.html', form=form)

@app.route('/workday', methods=['GET', 'POST'])
def workday():
    # return '<h2>Hello world</h2>'
    form = WorkDayForm()
    if form.validate_on_submit():
        # Process the data, save to database, etc.
        flash('Data submitted successfully!')
        return redirect(url_for('index'))
    return render_template('workdays.html', form=form)

#Custom Error Handler to avoid some code exception messages on HTML output
#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
#Internal Server Error General Message
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(debug=True, port=5555)

