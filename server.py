# Launch with
#
# python app.py

from flask import Flask, render_template
import sys
import pickle

app = Flask(__name__)

@app.route("/")
def articles():
    """Show a list of article titles"""
    ## YOUR CODE HERE
    topics=[(a[0],a[1],a[2]) for a in article_data]
    return render_template('articles.html', topics=topics)


@app.route("/article/<topic>/<filename>")
def article(topic, filename):
    """
    Show an article with relative path filename. Assumes the BBC structure of
    topic/filename.txt so our URLs follow that.
    """
    ## YOUR CODE HERE
    recommended_articles=recommended[(topic,filename)]
    text=''
    title=''
    for art in article_data:
        if art[0] == topic and art[1] == filename :
            title= art[2]
            text=art[3]
            break
        else:
            pass
    return render_template("article.html", topic=topic, title=title,text=text, recommended_articles=recommended_articles)


f = open('articles.pkl', 'rb')
article_data = pickle.load(f)
f.close()

f = open('recommended.pkl', 'rb')
recommended = pickle.load(f)
f.close()

# you may need more code here or not


# for local debug
if __name__ == '__main__':
    app.run(debug=True)

