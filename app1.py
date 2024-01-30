from flask import Flask
import telegram
# Create the application instance
app = Flask(__name__)

TOKEN ='6244092180:AAH_10MCMX4wAESk6TTp-iboI1EMSe6FeZ8'
bot = telegram.Bot(TOKEN)
chat_id = '1432402481'

# route for index page
@app.route('/', methods=['POST'])
def index():
    print('index page')
    bot.send_message(chat_id=chat_id, text='Hello World!!!')
    return 'index page'
if __name__=="__main__":
    app.run(debug=True)