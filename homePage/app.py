from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin


app = Flask(__name__) #flask constructor, app is how to interact with web server

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#route on webpage returns this function, / is default page
@app.route("/") 
@cross_origin()
def hello_world():
    return {'message':"<p>It's Maggie and Kyla!</p>"}

#get = asking for something (no sub-fields), post = more stuff with the questions
#visiting a webpage is a get request
#to make post requests, may need to use html file 
@app.route("/about", methods = ['POST', 'GET']) 
@cross_origin()
def hello_world2():
    input_str = request.json["company"]
    return {'method':request.method, 'output': request.json["company"] + "maybe!"}
    #return {'method':request.method}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    #local host = computer

#post request - get inputs to server
#front end: javascript for search code (get the string, pass string into a post request, send to server)
#(get response from server, show up on front end)

#back end:
