# Importing flask
"""Creating a flask app"""
from datetime import date
from flask import Flask, render_template, request

# Initialize our application
app = Flask(__name__)    # This line creates the application

def findAge(current_date, current_month, current_year,
            birth_date, birth_month, birth_year):
    """Calculating the age"""
    # if birth_date > current_date:
    #     current_month -= 1
    #     current_date += 30

    # if birth_month > current_month:
    #     current_year -= 1
    #     current_month += 12

    calculated_date = current_date - birth_date
    calculated_month = current_month - birth_month
    calculated_year = current_year - birth_year

    return calculated_date, calculated_month, calculated_year
# Routing
@app.route('/')
# What function do we wanna show
def home():
    """The home page"""
    return render_template('home.html')

@app.route('/calculator',methods=['POST'])
def calculator():
    """The about page"""
    today = date.today()
    current_date = today.day
    current_month = today.month
    current_year = today.year

    birth_date = int(request.form['birth_date'])
    birth_month = int(request.form['birth_month'])
    birth_year = int(request.form['birth_year'])

    calculated_year, calculated_month, calculated_date = findAge(current_date, current_month, current_year,
                                                                 birth_date, birth_month, birth_year)
    return render_template('about.html',
                           calculated_year = calculated_year,
                           calculated_month = calculated_month,
                           calculated_date = calculated_date)


# Running the application
if __name__ == '__main__':
    app.run(debug=True)
