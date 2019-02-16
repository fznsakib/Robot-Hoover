# Robot-Hoover
A web service that emulates a robot processing grid based instructions. Made using Python with Flask as web framework and sqlite3 for the database.

### Running the server

Enter the directory and then initialise the local server by running:

```
python app.py
```

### Requests
Once the server is running, you may make a request to

```
http://127.0.0.1:5000/navigate
```

with input as a json in the form:

```javascript
{
  "roomSize" : [5, 5],
  "coords" : [1, 2],
  "patches" : [
    [1, 0],
    [2, 2],
    [2, 3]
  ],
  "instructions" : "NNESEESWNWW"
}
```

An example request using the input above can also be made running the client file:

```
python client.py
```

The output will be return as a json in the form:

```javascript
{
  "coords" : [1, 3],
  "patches" : 1
}
```
where ```coords``` are the final coordinates of the hoover and ```patches``` is the number of cleaned patches.

### Database

In order to view the database, you can visit

```
http://127.0.0.1:5000/
```

Note: A new instance of the database is created everytime the server is initialised.

### Other

Testing:

```
pytest test.py
```

If you are getting module errors, create a virtualenv and install any required module using:

```
pip -r requirements.txt
```
