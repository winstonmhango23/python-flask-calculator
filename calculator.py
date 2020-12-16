from flask import Flask, render_template, request

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def home():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def calculation():
    #Our console input() function has been converted to form inputs!!
    num1 = request.form.get("num1", type=int)
    num2 = request.form.get("num2", type=int)
    #Our choices collected through a drop-down form element in the UI(browser)
    choice = request.form.get("choice")
    if(choice == 'Addition'):
        calculation = num1 + num2
    elif(choice == 'Subtraction'):
        calculation = num1 - num2
    elif(choice == 'Multiplication'):
        calculation = num1 * num2
    elif(choice == 'Division'):
        calculation = num1 / num2
    elif(choice == 'FlatDivision'):
        calculation = num1 // num2
    elif(choice == 'Modulo'):
        calculation = num1 % num2
    else:
        calculation = 'Please enter a valid choice'
    #asign the result of calculation to answer variable
    answer = calculation
    return render_template('form.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)