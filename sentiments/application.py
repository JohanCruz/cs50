from flask import Flask, redirect, render_template, request, url_for
import sys
import os
from twython import Twython

import helpers
from analyzer import Analyzer

positives = os.path.join(sys.path[0], "positive-words.txt")
negatives = os.path.join(sys.path[0], "negative-words.txt")
analyzer = Analyzer(positives, negatives)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    
def scored(text):
    h= text
    h=h.split()
    points=0
    for d in h:
        score = analyzer.analyze(d)
        #print(d, score)
        points=points+score
    return points

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "").lstrip("@")
    if not screen_name:
        return redirect(url_for("index"))

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name)

    # TODO
    positive, negative, neutral = 0.0, 0.0, 0.0
    twitter = Twython(os.environ.get("API_KEY"), os.environ.get("API_SECRET"))
    #s=twitter.search(tweets)
    s=tweets
    for f in s:
        #print (f)
        #if "text" in f:
           #print("si esta text")
        #print()
        #print(len(f))
        #h=f['text']
        score=scored(f)
        print (f)
        if score > 0.0:
            positive=positive+1
            print("1")
        elif score < 0.0:
            negative=negative+1
            print("-1")
        else:
          neutral=neutral+1
          print("0")
        #print(f['text'])
    #print(s)
    pos=100*positive/(positive+negative+neutral)
    neg=100*negative/(positive+negative+neutral)
    neu=100*neutral/(positive+negative+neutral)
    positive=pos
    negative=neg
    neutral=neu
    

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
