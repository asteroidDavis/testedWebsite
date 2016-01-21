from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object(__name__)

homePage='home.htm'
homePic='.\\static\\pictures\\profilePic'
homeName='Nate Davis'
sharingOptions=['facebook', 'linkedin', 'twitter']
contactOptions=['email', 'mobile phone']
subscriptionOptions=['email', 'twitter', 'linkedin', 'RSS']

#index has a customizable homeName, pic, and sharing options, contact options, and subscription options
@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'home.html',
        homePage=homePage,
        #TODO: Break this into a navbar and a socbar dictionary
        homePic=homePic,
        homeName=homeName,
        sharingOptions=sharingOptions,
        contactOptions=contactOptions,
        subscriptionOptions=subscriptionOptions
    )
    
    
    
    

if __name__ == "__main__":
    app.run(debug=True)