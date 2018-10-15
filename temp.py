from  flask  import  Flask , render_template
app = Flask(__name__)

#Testing Page
@app.route('/hello/')
@app.route('/hello/<name>')
def  namefun(name=None):
	return  render_template('conditional.html', name=name)
#Home Page
@app.route('/ccg-collectable-card-games')
def  HomepageSlected(name=None):
	return  render_template('home.html')
#Item Selected Page
@app.route('/ccg-collectable-card-games/CCG')
@app.route('/ccg-collectable-card-games/CCG/<ccg>')
def  CCGSlected(name=None):
	return  render_template('item.html', name=name)
#Serch Selected Page
@app.route('/ccg-collectable-card-games/Serch')
@app.route('/ccg-collectable-card-games/Serch/<item>')
def  SearchSelected(name=None):
	return  render_template('search.html', name=name)

if  __name__  == "__main__":
	app.run(host='0.0.0.0', debug=True)
