from flask import Flask

app = Flask(__name__)

@app.route('/')
def important():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <title>Важное сообщение</title>
        <style>
            body {
                margin: 0;
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                text-align: center;
            }
            .container {
                background: rgba(0, 0, 0, 0.6);
                padding: 40px 60px;
                border-radius: 15px;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.8);
                max-width: 500px;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 0.3em;
                letter-spacing: 2px;
                text-transform: uppercase;
                font-weight: 700;
            }
            p {
                font-size: 1.2em;
                margin-bottom: 1.5em;
                line-height: 1.5;
                color: #ccc;
            }
            .btn {
                background-color: #ff4c4c;
                border: none;
                padding: 15px 35px;
                font-size: 1.2em;
                color: white;
                border-radius: 50px;
                cursor: pointer;
                box-shadow: 0 5px 15px rgba(255, 76, 76, 0.6);
                transition: background-color 0.3s ease;
                text-decoration: none;
                display: inline-block;
            }
            .btn:hover {
                background-color: #e03b3b;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Внимание!</h1>
            <p>Это важное сообщение, которое требует вашего внимания. Пожалуйста, не игнорируйте его.</p>
            <a href="https://example.com" class="btn" target="_blank" rel="noopener noreferrer">Узнать больше</a>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
