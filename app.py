from flask import Flask, render_template
import json
import requests

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.com/gimme/2"
    response=json.loads(requests.request("GET",url).text)
    first_meme = response["memes"][0]

    image_large=first_meme["preview"][-2]
    subreddit=first_meme["subreddit"]
    return image_large, subreddit, response
    
@app.route("/")
def hello():
    return "Welcome to Singularity Box Flask!"

@app.route("/meme")
def meme():
    meme_pic,subreddit,response=get_meme()
    return render_template("index.html", meme_pic=meme_pic, subreddit=subreddit)

@app.route("/response")
def response():
    meme_pic,subreddit,response=get_meme()
    # print("STATUS:", response.status_code)        # check status
    # print("HEADERS:", response.headers.get("content-type"))  # see if it's JSON
    # print("TEXT:", response.text[:500])           # print first 500 chars
    
    try:
        # response = response.json()   # better than json.loads(r.text)
        response = response
    except json.JSONDecodeError:
        print("Response is not JSON!")
        # response = None
        response = "Response is not JSON!"
    return response

if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=80, debug=True)
