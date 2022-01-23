#! pip install -U googlemaps
## FOR THIS TO WORK YOU MUST HAVE A GOOGLE API

import googlemaps
import requests

G_API = ''

gmaps = googlemaps.Client(key=G_API)

#input city string
def city_to_coord(city):
    pass

#keyword is a string, coord is a list of strings for ['latitude', 'longitude']
def maps_query(place_name, coord):
    places_result = gmaps.places_nearby(keyword = place_name, location = coord, radius = 50000) #gives places result 
    
    names = []
    reviews = []
    times = []
    #print(len(places_result['results']))
   
    for j in range (len(places_result['results'])):
        place_id = places_result['results'][j]['place_id']
        #print(place_id)
        review_text = []
        review_time = []
        place = gmaps.place(place_id = place_id) #now only looking at one place 
        #print(place)
        i = 0;
        try:
            for r_i in place['result']['reviews']:
                #print(r_i, "\n")
                review_text.append(r_i.get('text'));
                review_time.append(r_i.get('relative_time_description'));
               # print(review_text[:-1])
                i += 1
        except(TypeError):
            return (['no reviews'],[],[])
        reviews.append(review_text) #returns tuple
        times.append(review_time)
        names.append(place['result']['name'])
    #print(reviews)
    return (names, reviews, times)

names, reviews, times = maps_query('sobeys', [43.6532, -79.3832]);
output_str = ""
for i in range (len(names)):
   output_str = output_str + names[i] + "\n"
   for j in range(len(reviews[i])):
       output_str = output_str + str(times[i][j]) +  "\n"
       output_str = output_str + reviews[i][j] +  "\n\n ######################################### \n"

'''
console format
names, reviews, times = maps_query('sobeys', [43.6532, -79.3832]);

names = ['Sobeys South Ajax',
 'Sobeys Ajax',
 'Sobeys Whitby',
 'Sobeys Oshawa',
 'Sobeys Danforth',
 'Sobeys Laird & Wicksteed',
 'Sobeys Clark & Hilda',
 'Sobeys Todmorden',
 'Sobeys Jefferson Square',
 'Sobeys Urban Fresh Balliol',
 'Sobeys Urban Fresh Rosebury Square',
 'Sobeys Urban Fresh Spadina',
 'Sobeys Pharmacy Ajax',
 'Sobeys Urban Fresh High Park',
 'Sobeys Aurora Bayview',
 'Sobeys Queensway',
 'Sobeys Urban Fresh Bloor & Islington',
 'Sobeys Kipling',
 'Sobeys North Park',
 'Sobeys Mississauga']

times =
[[1637115963, 1642780422, 1607407744, 1603630398, 1640278730],
 [1642609138, 1639536324, 1640995847, 1639140063, 1640196492],
 [1640998138, 1641088686, 1640316738, 1600564108, 1637869101],
 [1641328519, 1641606098, 1638811803, 1634512425, 1641337008],
 [1599415906, 1637075153, 1640895685, 1637670879, 1599870741],
 [1631760561, 1630629035, 1641412589, 1639148186, 1642017630],
 [1640556752, 1600385913, 1641171103, 1639189054, 1633293970],
 [1636456757, 1642140623, 1641790926, 1640883083, 1634493826],
 [1637708365, 1598791889, 1603675131, 1639673031, 1639967191],
 [1642189097, 1637691505, 1638999409, 1614813981, 1614689275],
 [1599364389, 1640721281, 1633745469, 1631811970, 1635908445],
 [1599916110, 1599847709, 1641858579, 1638806963, 1596667593],
 [1597528493, 1605705736, 1604249551, 1588632900, 1489116181],
 [1642169869, 1639356592, 1635443558, 1633199057, 1630119926],
 [1641695708, 1641506938, 1599521105, 1617723836, 1639350592],
 [1642418821, 1637714355, 1638837784, 1642888519, 1638646843],
 [1642211262, 1641565953, 1630111152, 1634226211, 1632592481],
 [1639363737, 1642289871, 1638906739, 1639211189, 1635288125],
 [1637335283, 1640189701, 1622798278, 1626871261, 1631291695],
 [1641948090, 1642613850, 1641266290, 1601235929, 1633377691]]

reviews =
[["The location is convenient being right in the heart of the city, and the fact it's relatively new is quite evident. It's clean and comfortable. The staff do a great job serving their customers including myself. Now as far as the food is concerned, this is literally one of the best chicken sandwich places in the city. Obviously that's subjective but I've lived in the city long enough to know what a truly good chicken sandwich tastes like and when you come here you won't be disappointed. Just keep in mind due to its location and popularity it gets a little busy around lunch time so be prepared to wait a few minutes but it's definitely worth it.",
  'Bit of a line-up, but very COVID-Friendly.',
  'relly lik the chimken but they dont say my pelsur anymore',
  "Recently visited this restaurant and location finally as I haven't been able to since it first opened in 2019. I have to say it was worth the wait. The burger and fries were so good. I love how you can cater the burger to your own liking with any of the sauces that they have to offer. The fries were by far the best fries I have ever had - I wish they had a larger size option as I would have definitely ordered it. The cookies and cream milkshake was amazing and way worth the extra $2. The ordering process was so quick and efficient. Highly recommend and way better than any fast food joint. You get what you pay for and the quality is really good.",
  "Waited months to try this after opening due to the crazy lines. It's always exciting when a big American chain expands into Canada with a flagship location in Toronto. The space is nice, they do a great job at managing the lines by taking orders while you wait. The food itself is standard fast food quality. Waffle fries are a nice option. While the sandwiches don't disappoint, they don't impress either. I can name a dozen places in the city with a better chicken sandwich."],
 ['The spicy chicken sandwich was great. It was crispy, fresh, had good sauce, sandwiched between a soft, buttery bun. Waffle fries were decent.\n\nAt first glance, you\'d think "it\'s not worth waiting half an hour just to get a sandwich and fries." But it wasn\'t like that at all. There\'s an effective ordering and pickup system in place and in the end it only took ~10 minutes to get my food. Good training = good customer service...the employees were kind and knowledgeable.\n\nDefinitely coming back. Delicious!',
  'The portion size is pretty good, service is also very nice. Friendly staff with tasty food is an amazing combo. I did a mobile order and it was super fast and convenient. I scanned the QR code and within 10mins I had my food despite the rush. Chicken is so tender and juicy too.',
  "I ordered a large order but I didn't get my 12 piece nuggets. It was so busy you couldn't even check your order. Not happy.\n\nEdit: The customer service regarding this was amazing! The team got back to me promptly and was able to resolve my issue. Very happy now :)",
  'The chicken sandwich is great. The waffle fries could be crisper but, were fine. The staff are courteous and efficient.  They line up  goes quickly and is monitored for people who forget to stay 6 feet apart. Two thumbs up.',
  "Line up was crazy long but their spicy chicken is actually good because it's breaded and marinated spicy. Not like every other place giving you a regular chicken sandwich with spicy mayo. Plus waffle fries."],
 ['Lived up to the hype. The deluxe spicy sandwich was delicious with pepper jack cheese, the chicken was meaty and had just the right amount of spice. The regular sandwich was also good, but I recommend trying it with their dipping sauce. The waffles fries were my favourite, crispy on the outside yet airy and not overly salty. The sweet tea was yummy (tasted like a bbt flavour to me) and the lemonade was sour but refreshing. It was a long line, so I highly recommend ordering ahead online. Either way it’s worth the wait!',
  'This restaurant is relatively new in the yorkdale food court , there is always a line but the',
  "If you're out and about, this is a great spot to pickup some delicious food. Their menu is short and sweet, but still has great options. Would definitely recommend waffle fries, and would overall recommend this place!",
  "Very fast service. Tasty chicken. Great waffle fries. Nice selection of sauces to put on the chicken or to dunk your fries. Reasonable prices. Tried the cherry coke, but wouldn't get again...would rather have Dr. Pepper.",
  'Just to be clear, I am not giving  “5” because of the food quality.  There was a couple of other issues.  The food was great, unarguably! The two issue were:\n1- Although they have a dedicated space for them, but management decided not to use it, rather just use the common area at the food court, which is quite crowded!  A Sushi bar in the same location decided to take the lead and better serve there customers and use their dedicated area.  I wonder why can’t Chick Fil A do the same.\n2- my order was late getting out of the kitchen (around 15 minutes after I paid), and the excuse was that salad preparation take long time!  Unfortunately, the order was missing two sandwiches; luckily I was dining in so I could go back and get the missing sandwiches!'],
 ['Truly one of the best fast foods out there, high quality food as well!',
  'Some of the best chicken in the city comes from Chick-fil-A, the next closet location to this one is at Yonge & Bloor St and also a location at Yorkdale Mall.',
  '']]
'''

review = ['gay', 'not', 'Homophobic', 'discrimination', 'is', 'bad', 'be', 'nice', 'to', 'queers', 'not', 'racists']
reviews = [["The location is not homophobic gay convenient being right homophobic homophobic in the heart of the city, and the fact it's relatively new is quite evident. It's clean and comfortable. The staff do a great job serving their customers including myself. Now as far as the food is concerned, this is literally one of the best chicken sandwich places in the city. Obviously that's subjective but I've lived in the city long enough to know what a truly good chicken sandwich tastes like and when you come here you won't be disappointed. Just keep in mind due to its location and popularity it gets a little busy around lunch time so be prepared to wait a few minutes but it's definitely worth it.", 'Bit of a line-up, but very COVID-Friendly.', 'relly lik the chimken but they dont say my pelsur anymore', "Recently visited this restaurant and location finally as I haven't been able to since it first opened in 2019. I have to say it was worth the wait. The burger and fries were so good. I love how you can cater the burger to your own liking with any of the sauces that they have to offer. The fries were by far the best fries I have ever had - I wish they had a larger size option as I would have definitely ordered it. The cookies and cream milkshake was amazing and way worth the extra $2. The ordering process was so quick and efficient. Highly recommend and way better than any fast food joint. You get what you pay for and the quality is really good.", "Waited months to try this after opening due to the crazy lines. It's always exciting when a big American chain expands into Canada with a flagship location in Toronto. The space is nice, they do a great job at managing the lines by taking orders while you wait. The food itself is standard fast food quality. Waffle fries are a nice option. While the sandwiches don't disappoint, they don't impress either. I can name a dozen places in the city with a better chicken sandwich."], ['The spicy chicken sandwich was great. It was crispy, fresh, had good sauce, sandwiched between a soft, buttery bun. Waffle fries were decent.\n\nAt first glance, you\'d think "it\'s not worth waiting half an hour just to get a sandwich and fries." But it wasn\'t like that at all. There\'s an effective ordering and pickup system in place and in the end it only took ~10 minutes to get my food. Good training = good customer service...the employees were kind and knowledgeable.\n\nDefinitely coming back. Delicious!', 'The portion size is pretty good, service is also very nice. Friendly staff with tasty food is an amazing combo. I did a mobile order and it was super fast and convenient. I scanned the QR code and within 10mins I had my food despite the rush. Chicken is so tender and juicy too.', "I ordered a large order but I didn't get my 12 piece nuggets. It was so busy you couldn't even check your order. Not happy.\n\nEdit: The customer service regarding this was amazing! The team got back to me promptly and was able to resolve my issue. Very happy now :)", 'The chicken sandwich is great. The waffle fries could be crisper but, were fine. The staff are courteous and efficient.  They line up  goes quickly and is monitored for people who forget to stay 6 feet apart. Two thumbs up.', "Line up was crazy long but their spicy chicken is actually good because it's breaded and marinated spicy. Not like every other place giving you a regular chicken sandwich with spicy mayo. Plus waffle fries."], ['Lived up to the hype. The deluxe spicy sandwich was delicious with pepper jack cheese, the chicken was meaty and had just the right amount of spice. The regular sandwich was also good, but I recommend trying it with their dipping sauce. The waffles fries were my favourite, crispy on the outside yet airy and not overly salty. The sweet tea was yummy (tasted like a bbt flavour to me) and the lemonade was sour but refreshing. It was a long line, so I highly recommend ordering ahead online. Either way it’s worth the wait!', 'This restaurant is relatively new in the yorkdale food court , there is always a line but the', "If you're out and about, this is a great spot to pickup some delicious food. Their menu is short and sweet, but still has great options. Would definitely recommend waffle fries, and would overall recommend this place!", "Very fast service. Tasty chicken. Great waffle fries. Nice selection of sauces to put on the chicken or to dunk your fries. Reasonable prices. Tried the cherry coke, but wouldn't get again...would rather have Dr. Pepper.", 'Just to be clear, I am not giving  “5” because of the food quality.  There was a couple of other issues.  The food was great, unarguably! The two issue were:\n1- Although they have a dedicated space for them, but management decided not to use it, rather just use the common area at the food court, which is quite crowded!  A Sushi bar in the same location decided to take the lead and better serve there customers and use their dedicated area.  I wonder why can’t Chick Fil A do the same.\n2- my order was late getting out of the kitchen (around 15 minutes after I paid), and the excuse was that salad preparation take long time!  Unfortunately, the order was missing two sandwiches; luckily I was dining in so I could go back and get the missing sandwiches!'], ['Truly one of the best fast foods out there, high quality food as well!', 'Some of the best chicken in the city comes from Chick-fil-A, the next closet location to this one is at Yonge & Bloor St and also a location at Yorkdale Mall.', '']]

keyword_list = ['gay', 'homophobic', 'discrimination', 'racist', 'racists', 'gays', 'queers', 'gay','homo','racists','discriminatory','sexist','racist','xenophobic','misogynistic','discrimination','dyke', 'faggot','tranny','sodomite']
Hscore = 0
date = ''


def count_bwords(review_list, keyword_list):
#function returns the number of key words in the review with match the keyword list 
    count = 0
    i = 0
    j = 0
    correlation = 0
    correlation_list = []
    
    #for review in (review_list):
        #for i in range (len(review)):
    #print(review_list)
    for review in review_list:
        #print(review)
        for review_x in review:
            review_lst  = list(review_x.split(" "))
            #print(review_lst)

            while len(review_lst) > j:
                #print(len(review_lst))
                #print(review[j])
                for b_word in keyword_list:
        
                    if b_word == review_lst[j].lower():
                        print("j is ", review_lst[j])
                    #if b_word in review[i]:
                        correlation = correlation + 1
                        #print(review_lst[j-1])
                        if review_lst[j-1].lower() == 'not':
                            correlation -= 1
                j += 1
            correlation_list.append(correlation)
            correlation = 0

                
    print(correlation_list)
    print('correlation is ' + str(correlation))
    return correlation_list

    
def score(correlation_list):
    count_total = 0
    count1 = 0
    count2 = 0
    for correlation_score in correlation_list:
        count1 += correlation_score
        if correlation_score > 0:
            count2 += 1
    count_total = count1 + count2

    if count_total > 50:
        score = 'F'
    elif count_total > 10:
        score = 'D'
    elif count_total > 5:
        score = 'C'
    elif count_total > 1:
        score = 'B'
    else:
        score = 'A'
    print(score)
        
    return score

correlation_list = count_bwords(reviews, keyword_list)
score(correlation_list)


def parse_reviews(reviews, keyword):
    correlation = 0;
    for j in (reviews):
        for i in range (len(j)):
            if keyword in j[i]:
                correlation += 1;
    return correlation 


def google_parse(keyword, company):
    # Copy your credentials from the console
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = G_API
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "ba761ac47ff9a620e"
    query = keyword + " "+ company
    # using the first page
    page = 1
    # constructing the URL
    # doc: https://developers.google.com/custom-search/v1/using_rest
    # calculating start, (page=2) => (start=11), (page=3) => (start=21)
    start = (page - 1) * 10 + 1
    url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
    # make the API request
    data = requests.get(url).json()
    
    print(data)
    # get the result items
    search_items = data.get("items")
    # iterate over 10 results found
    try:
        str_out = ""
        for i, search_item in enumerate(search_items, start=1):
            # get the page title
            title = search_item.get("title")
            # page snippet
            snippet = search_item.get("snippet")
            # alternatively, you can get the HTML snippet (bolded keywords)
            html_snippet = search_item.get("htmlSnippet")
            # extract the page url
            link = search_item.get("link")
            # print the results
            str_out = str_out + "="*10+ f"Result #{i+start-1}"+ "="*10 + "<br>Title:"+ title + "<br>Description:"+ snippet + "<br>URL:" + link + "<br>"
           # print("totalResults:", totalResults)  - use number of search results oto 
       
    except(TypeError):
        pass
    return str_out

def find_lgbt(coord): #input coordinate in list, outputs list of businesses, addresses, and their websites, if available
    places_result = gmaps.places_nearby(keyword = 'lgbtq owned', location = coord, radius = 50000) #gives places result 
    #print(len(places_result['results']))
    lgbt_list = []
    
    for j in range (len(places_result['results'])):
        place_id = places_result['results'][j]['place_id']
        #print(place_id)
        review_text = []
        place = gmaps.place(place_id = place_id) #now only looking at one place 
        #print(place['result'])
        try:
            web_url = (place['result']['website'])
        except (KeyError): 
            web_url = ''
        
        list_j = [place['result']['name'], print(place['result']['formatted_address']), web_url]
        
    return lgbt_list

#listen to requests
#gather and respond --> web server

#can write in whatever language, use a python web server, give a few different questions we can ask


    
    