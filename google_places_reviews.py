#! pip install -U googlemaps
import googlemaps

G_API = 'AIzaSyAa8xObDBanS74duZX7fC1ICmbJUGoG3GU'
gmaps = googlemaps.Client(key=G_API)

#keyword is a string, coord is a list of strings for ['latitude', 'longitude']
def reviews_query(place_name,coord):
    places_result = gmaps.places_nearby(keyword = place_name, location = coord, radius = 50000) #gives places result 

    reviews = []
   
    for j in range (len(places_result['results'])):
        place_id = places_result['results'][j]['place_id']
        print(place_id)
        review_text = []
        place = gmaps.place(place_id = place_id) #now only looking at one place 
        #print(place)
        i = 0;
        for r_i in place['result']['reviews']:
            review_text.append(r_i.get('text'));
            i += 1
        reviews.append(review_text)
        
    return reviews


def parse_reviews(reviews, keyword):
    correlation = 0;
    for j in range (len(reviews)):
        for i in range (len(j)):
            if reviews[j][i] == keyword:
                correlation += 1;
    return correlation 


