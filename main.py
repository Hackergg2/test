from flask import Flask

app = Flask(__name__)

@app.route('/')
def show_profiles():
    return '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8" />
        <title>TikTok Профили</title>
        <style>
            body {
                margin: 0;
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                color: #f0f0f0;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-wrap: wrap;
                padding: 40px;
                gap: 30px;
            }
            .card {
                background: rgba(0, 0, 0, 0.7);
                padding: 30px 25px;
                border-radius: 15px;
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
                max-width: 280px;
                width: 100%;
                text-align: center;
            }
            .avatar {
                width: 100px;
                height: 100px;
                border-radius: 50%;
                border: 3px solid #ff4c4c;
                margin: 0 auto 15px auto;
                background-size: cover;
                background-position: center;
            }
            h2 {
                margin: 0;
                font-size: 1.8em;
                font-weight: 700;
            }
            .username {
                color: #ff4c4c;
                font-weight: 600;
                margin: 5px 0 20px 0;
                font-size: 1.1em;
            }
            .stats {
                display: flex;
                justify-content: space-around;
                font-size: 0.95em;
                font-weight: 600;
            }
            .stat {
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            .stat-number {
                font-size: 1.4em;
                font-weight: 700;
                color: #ff4c4c;
            }
            .stat-label {
                color: #ccc;
                font-size: 0.85em;
            }
            a {
                text-decoration: none;
                color: inherit;
            }
        </style>
    </head>
    <body>

        <!-- Profile 1: فيس -->
        <a href="https://www.tiktok.com/@zunii.real" target="_blank">
            <div class="card">
                <div class="avatar" style="background-image: url('https://p16-sign-va.tiktokcdn.com/tos-useast5-avt-0068-tx/daef5d7a0fb06c1305b98~c5_100x100.jpeg');"></div>
                <h2>فيس</h2>
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
        </a>

        <!-- Profile 2: Kornelia -->
        <a href="https://www.tiktok.com/@kornelia1234975" target="_blank">
            <div class="card">
                <div class="avatar" style="background-image: url('https://p16-sign-va.tiktokcdn.com/tos-useast5-avt-0068-tx/2b35483bbf41b1894377f~c5_100x100.jpeg');"></div>
                <h2>Kornelia</h2>
                <div class="username">@kornelia1234975</div>
                <div class="stats">
                    <div class="stat">
                        <div class="stat-number">245</div>
                        <div class="stat-label">Подписки</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">295</div>
                        <div class="stat-label">Подписчики</div>
                    </div>
                    <div class="stat">
                        <div class="stat-number">6912</div>
                        <div class="stat-label">Лайки</div>
                    </div>
                </div>
            </div>
        </a>

    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
