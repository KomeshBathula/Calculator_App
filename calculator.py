from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route("/math", methods=['POST'])
def calculator_test():
    ops = request.form['operation']
    try:
        # Convert inputs to float for handling both integers and decimals
        first_num = float(request.form['num1'])
        second_num = float(request.form['num2'])
    except ValueError:
        return "Invalid input. Please enter numeric values."

    # Perform the selected operation
    if ops == 'add':
        result = first_num + second_num
        return f"Addition of {first_num} and {second_num} is {result}"
    elif ops == 'subtract':
        result = first_num - second_num
        return f"Subtraction of {first_num} and {second_num} is {result}"
    elif ops == 'multiply':
        result = first_num * second_num
        return f"Multiplication of {first_num} and {second_num} is {result}"
    elif ops == 'divide':
        if second_num == 0:
            return "Error: Division by zero is not allowed."
        result = first_num / second_num
        return f"Division of {first_num} and {second_num} is {result}"
    else:
        return "Invalid operation selected."

if __name__ == '__main__':
    app.run(port=5006)
