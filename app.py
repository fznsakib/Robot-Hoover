from flask import Flask, request, jsonify
import RobotProcess as RP

# create the Flask app
app = Flask(__name__)


# Main navigation service route
@app.route('/navigate', methods=['POST'])
def navigateService():
    # Accept data as json
    data = request.get_json()

    # Initialise RobotProcess object using input parameters
    robot = RP.RobotProcess(data['roomSize'], data['coords'], data['patches'], data['instructions'])

    # Carry out navigation process
    robot.navigate()

    # Populate output payload and rturn
    output = {'coords': robot.getPosition(),
              'patches': robot.getNoOfPatchesCleaned()}

    return jsonify(output)


if __name__ == '__main__':
    app.run(debug=True)  # run app in debug mode on port 5000
