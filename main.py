from flask import Flask

app = Flask(__name__)

@app.route('/')
def tiktok_profile():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <title>Профиль TikTok</title>
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
                background: rgba(0, 0, 0, 0.7);
                padding: 40px 50px;
                border-radius: 15px;
                box-shadow: 0 0 25px rgba(0, 0, 0, 0.9);
                max-width: 400px;
                width: 100%;
            }
            .avatar {
                width: 120px;
                height: 120px;
                border-radius: 50%;
                border: 3px solid #ff4c4c;
                margin: 0 auto 20px auto;
                background-size: cover;
                background-position: center;
            }
            h1 {
                margin: 0;
                font-size: 2.5em;
                letter-spacing: 1.5px;
                font-weight: 700;
            }
            .username {
                color: #ff4c4c;
                font-weight: 600;
                margin: 5px 0 25px 0;
                font-size: 1.2em;
            }
            .stats {
                display: flex;
                justify-content: space-around;
                font-size: 1.1em;
                font-weight: 600;
                letter-spacing: 1px;
            }
            .stat {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .stat-number {
                font-size: 1.8em;
                font-weight: 700;
                margin-bottom: 4px;
                color: #ff4c4c;
            }
            .stat-label {
                font-size: 0.9em;
                color: #ccc;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="avatar" style="background-image: url('https://cdn-icons-png.flaticon.com/512/147/147144.png');"></div>
            <h1>فيس</h1>
            <div class="username">@zunii.real</div>
            <div class="stats">
                <div class="stat">
                    <div class="stat-number">24</div>
                    <div class="stat-label">Подписки</div>
                </div>
                <div class="stat">
                    <div class="stat-number">1048</div>
                    <div class="stat-label">Подписчики</div>
                </div>
                <div class="stat">
                    <div class="stat-number">18K</div>
                    <div class="stat-label">Лайки</div>
                </div>
            </div>
        </div>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
