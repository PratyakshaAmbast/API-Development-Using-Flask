from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/fact/<int:num>')
def fact(num):
	#num = int(input("Enter a number: "))

	factorial = 1
	copy_num=num

	# check if the number is negative, positive or zero
	if num < 0:
	   print("Sorry, {copy_num} factorial does not exist for negative numbers")
	   result = {
	   		"Number" : copy_num,
	   		"Result" : False,
	   		"Factorial" : "Does Not Exist",
	   	}
	elif num == 0:
	   print("The factorial of 0 is 1")
	   result = {
	   		"Number" : copy_num,
	   		"Result" : True,
	   		"Factorial" : copy_factorial,
	   	}
	else:
	   for i in range(1,num + 1):
	       factorial = factorial*i
	       copy_factorial = factorial
	   print("The factorial of",{copy_num},"is",{copy_factorial})
	   result = {
	   		"Number" : copy_num,
	   		"Result" : True,
	   		"Factorial" : copy_factorial,
	   	}

	return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)