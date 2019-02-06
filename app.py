from flask import Flask, request, jsonify, make_response
import DatabaseManager as DBManager
import RobotProcess as RP

# Create the Flask app
app = Flask(__name__)

# Initialise the database
DBManager.initDB()


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
    # Return with an error and its reason if validation unsuccessful
    validation = robot.validate()
    if not validation[0]:
        return make_response(jsonify({'error': validation[1]}), 404)

    # Add input to database
    DBManager.insertInput(robot.roomSize, robot.coords, robot.patches, robot.instructions)

    # Carry out navigation process
    robot.navigate()

    # Populate output payload and return
    output = {'coords': robot.getPosition(),
              'patches': robot.getNoOfPatchesCleaned()}

    # Add output to database
    DBManager.insertOutput(output['coords'], output['patches'])

    # Return output as json to service call
    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)
