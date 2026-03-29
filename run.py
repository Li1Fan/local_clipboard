import os
import time

from flask import Flask, request, render_template, render_template_string

app = Flask(__name__)
app.config['FILESHARE_URL'] = os.environ.get('FILESHARE_URL', '')

clipboard_text = ''
history_text = ''


def get_current_time():
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


# 初始页面
@app.route('/')
def index():
    return render_template('index.html', messages=clipboard_text,
                           fileshare_url=app.config['FILESHARE_URL'])


# 处理表单提交
@app.route('/', methods=['POST'])
def add_message():
    global clipboard_text
    global history_text
    if request.form['clear'] == '1':
        clipboard_text = ''
        history_text = ''
    else:
        message = request.form['message']
        clipboard_text = message
        history_text = history_text + get_current_time() + ':\n' + message + '\n\n'
    return index()


@app.route('/text')
def text():
    return render_template_string('<head><meta charset="UTF-8"><title>剪贴板历史</title>'
                                  '<body><pre>{{ message }}</pre></body>', message=history_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
