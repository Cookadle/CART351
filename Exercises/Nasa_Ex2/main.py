from flask import Flask, render_template, request, url_for
import requests

app = Flask(__name__)

#show the search page form
@app.route("/")
@app.route("/search")

def search_page():
    return render_template("nasa_search.html")

#handle GET request/////query the NASA API/////return results
@app.route("/results")

def nasa_search_results():
    #GET(HIHI) user search input from GET 
    user_query = request.args.get("query", "")
    
    items = []
    if user_query:
        #nasa image+api url 
        nasa_api_url = f"https://images-api.nasa.gov/search?q={user_query}&media_type=image"
        try:
            response = requests.get(nasa_api_url)
            #if request ok
            if response.status_code == 200:
                data = response.json()
                items = data.get("collection", {}).get("items", [])
        except Exception as e:
            app.logger.error(f"Error fetching data from NASA API: {e}")

    return render_template("nasa_results.html", search_term=user_query, items=items)


#webstolencode if credits asked geek handle error didnt use but keeping templates
#@app.errorhandler(404)
#def page_not_found(e):
#    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)