from flask import Flask
import googlemaps
import requests
from flask import request
from flask_cors import CORS, cross_origin
from google_places_reviews import maps_query
from google_places_reviews import google_parse


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
    coord = [43.6532, -79.3832]
    names, reviews, times = maps_query(input_str, coord)
    output_str = ""
    for i in range (len(names)):
        output_str = output_str + "<b>"+names[i] + "</b>" + "<br>"
        for j in range(len(reviews[i])):
            output_str = output_str + times[i][j] +  "<br>"
            output_str = output_str + reviews[i][j] +  "<br><br> ######################################################### <br>"
    
    str_out2 = google_parse("homophobic", input_str)
    return {'method':request.method, 'output': output_str, 'queer': str_out2, 'score': '<b>F</b><br><br>'}
    S#return {'method':coord, 'names': input_str}
    


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    #local host = computer

#post request - get inputs to server
#front end: javascript for search code (get the string, pass string into a post request, send to server)
#(get response from server, show up on front end)

#back end:
