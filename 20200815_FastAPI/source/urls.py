from controllers import *

# urlのルーティング定義
app.add_api_route('/', index)
app.add_api_route('/admin', admin)
app.add_api_route('/register', register, methods=['GET', 'POST'])  # new