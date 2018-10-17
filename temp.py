
from  flask  import  Flask , render_template
app = Flask(__name__)

#Testing Page
@app.route('/hello/')
@app.route('/hello/<name>')
def  namefun(name=None):
	return  render_template('conditional.html', name=name)
#Home Page
@app.route('/ccg_index')
def  HomepageSlected(name=None):
	return  render_template('home.html')
#Item Selected Page
@app.route('/ccg_index/ccg')
@app.route('/ccg_index/ccg/<ccg>')
def  CCGSlected(ccg=None):
	return  render_template('item.html', ccg=ccg)
#Serch Selected Page
@app.route('/ccg_index/search')
@app.route('/ccg_index/serch/<item>')
def  SearchSelected(name=None):
	return  render_template('search.html', name=name)

if  __name__  == "__main__":
	app.run(host='0.0.0.0', debug=True)
