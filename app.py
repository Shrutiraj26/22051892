from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize sliding window variables
window_size = 10
window_prev_state = []
window_curr_state = []

@app.route('/numbers/e', methods=['GET'])
def handle_request():
    global window_prev_state, window_curr_state

    # Simulate receiving numbers from a 3rd party server
    # For the sake of demonstration, we'll use hardcoded numbers
    if not window_curr_state:  # First request
        numbers = [2, 4, 6, 8]
    else:  # Second request
        numbers = [6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

    # Update previous state and current state
    window_prev_state = window_curr_state[:]
    window_curr_state = (window_curr_state + numbers)[-window_size:]

    # Calculate average of the current state
    avg = sum(window_curr_state) / len(window_curr_state)

    # Prepare response
    response = {
        "windowPrevState": window_prev_state,
        "windowCurrState": window_curr_state,
        "numbers": numbers,
        "avg": round(avg, 2)
    }

    return jsonify(response)

if __name__ == '_main_':
    app.run(port=9876)