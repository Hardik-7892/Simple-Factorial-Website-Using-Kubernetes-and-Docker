from flask import Flask, request, jsonify
 
app = Flask(__name__)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

@app.route('/factorial', methods=['GET'])
def calculate_factorial():
    try:
        num = int(request.args.get('number'))
        result = factorial(num)
        return jsonify({'number': num, 'factorial': result})
    except (ValueError, TypeError):
        return jsonify({'error': 'Please provide a valid integer.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
