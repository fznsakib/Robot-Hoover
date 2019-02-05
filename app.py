from flask import Flask, request, jsonify, make_response
import RobotProcess as RP

# create the Flask app
app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/')
def index():
    return "Robot ready!"


# Main navigation service route
@app.route('/navigate', methods=['POST'])
def navigateService():
    # Accept data as json
    data = request.get_json()

    # Initialise RobotProcess object using input parameters
    robot = RP.RobotProcess(data['roomSize'], data['coords'], data['patches'], data['instructions'])

    # Validate input
    # if not robot.validate():
    #     return make_response(jsonify({'error': 'Not found'}), 404)

    # Carry out navigation process
    robot.navigate()

    # Populate output payload and return
    output = {'coords': robot.getPosition(),
              'patches': robot.getNoOfPatchesCleaned()}

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
