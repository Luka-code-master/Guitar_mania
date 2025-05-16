from flask import Flask, render_template

app = Flask(__name__)

guitars = [
    {
        "name": "King V",
        "image": "https://www.fmicassets.com/Damroot/eCommPNG/10002/2914413503_gtr_frt_001_rr.png",
        "des": "High-performance guitar with excellent playability and stage performance.",
        "link": "https://intl.jacksonguitars.com/products/pro-series-king-v-kv"
    },
    {
        "name": "Pro Plus Soloist",
        "image": "https://www.fmicassets.com/Damroot/eCommPNG/10004/2914327580_jac_ins_frt_1_rr.png",
        "des": "High-performance guitar with excellent playability and stage performance.",
        "link": "https://intl.jacksonguitars.com/products/pro-plus-series-soloist-sla3q"
    },
    {
        "name": "MF-1",
        "image": "https://www.fmicassets.com/Damroot/eCommPNG/10001/2919904552_jac_ins_frt_01_rr.png",
        "des": "High-performance guitar with excellent playability and stage performance.",
        "link": "https://intl.jacksonguitars.com/products/pro-series-signature-marty-friedman-mf-1-purple-mirror"
    },
    {
        "name": "Soloist Camo",
        "image": "https://www.fmicassets.com/Damroot/eCommPNG/10019/2916942598_jac_ins_frt_1_rr.png",
        "des": "High-performance guitar with excellent playability and stage performance.",
        "link": "https://intl.jacksonguitars.com/products/x-series-soloist-slx-dx-camo"
    }
]

@app.route('/')
def index():
    return render_template('index.html', guitars=guitars)

@app.route('/amps')
def amps():
    return render_template('amps.html')

@app.route('/form')
def form():
    conn = sqlite3.connect('guitar.db')
    c = conn.cursor()
    c.execute('SELECT name, question FROM form')
    rows = c.fetchall()
    conn.close()

    questions = [{'name': row[0], 'question': row[1]} for row in rows]
    return render_template('form.html', questions=questions)

if __name__ == '__main__':
    app.run(debug=True)




