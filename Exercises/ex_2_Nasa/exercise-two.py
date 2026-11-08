from flask import Flask,render_template,request,redirect,url_for
import requests
app = Flask(__name__)


# the default route
@app.route("/")
def index():
      return render_template("index.html")

#*************************************************
#Task-1: GET REQUEST
@app.route("/t1")
def t1():
     return render_template("t1.html",have_results=False)
#*************************************************
@app.route("/getSearchCriteria")
def getSearchCriteria():
    #user 
    userInput = request.args.get('search')
    #NASA image url 
    url = "https://images-api.nasa.gov/search?q=" + userInput + "&media_type=image"
    
    response = requests.get(url)

    #cjson get result
    data = response.json()

    items = data['collection']['items']

 
    firstItem = items[0]

   
    imgFromNasa = firstItem['links'][0]['href']

    
    description = firstItem['data'][0]['description']

    #rreplace the empty space to be url encoded
    imgFromNasa = imgFromNasa.replace(' ', '%20')
    

    return render_template("t1.html",
    have_results=True,
    description=description,
    imgPath=imgFromNasa)
   
    #fill me in :
    #replace the empty space to be url encoded
                                           
    #                        )


#*************************************************
# #Task-2: GET REQUEST
@app.route("/t2")
def t2():
    return render_template("t2.html")
#*************************************************
@app.route("/getSearchCriteria_adv")
def getSearchCriteria_adv():

    userInput = request.args.get('search')

    url = "https://images-api.nasa.gov/search?q=" + userInput + "&media_type=image"
     
    response = requests.get(url)
 
    #cjson get result
    data = response.json()
 
    items = data['collection']['items']

    encodedImageLinks = []
 #loop 4 elements
    for element in items:
        
        singleImage = element['links'][0]['href']
        
        #replace the empty space to be url encoded
        singleImage = singleImage.replace(' ', '%20')
        
        encodedImageLinks.append(singleImage)

    return render_template("t2.html",images=encodedImageLinks)
   
#*************************************************

#run
app.run(debug=True)