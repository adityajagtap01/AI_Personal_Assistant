from flask import Flask, jsonify,render_template,request,redirect,url_for
from dotenv import load_dotenv
import os
from groq import Groq


load_dotenv()
api_key=os.getenv("API_KEY")
app = Flask(__name__)
client = Groq(api_key=api_key)

@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/ask",methods=["POST"])
def ask():
    question=request.form["question"]                                                     
    chat1_completion=client.chat.completions.create(
        messages=[
            {
                "role":"system",
                "content":"Act as my helpful personal assistant."
            },
            {
                "role":"user",
                "content":question
            }
        ],

        model="llama-3.3-70b-versatile"


        
        )
  
    ans= chat1_completion.choices[0].message.content
    return jsonify({"response":ans}),200
    

@app.route("/summarize",methods=["POST"])
def summarize():
    email_text=request.form["email_text"]
    prompt=f"summarize the following mail in 2 to 3 sentences :{email_text}"

    chat1_completion=client.chat.completions.create(
            messages=[
                {
                    "role":"system",
                    "content":"Act as my helpful personal assistant."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ],
        
            model="llama-3.3-70b-versatile"
                                                                                     
     )

    summary= chat1_completion.choices[0].message.content
    return jsonify({"response":summary}),200
app.run(debug=True)