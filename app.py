import Flask import flask , render_template, request, redirect, url_for

app=flask(__name__)

@app.route('/')
def inicio():

    return  render_template('base.html')
   
@app.route('/cadastro')
def cadastro():

    return render_template('cadastro.html')

@app.route('/login')
def login():
    return  render_template('login.html')
    

@app.route('/livro')
def livro():

    return  render_template('livro.html')
    
@app.route('/route_name')
def method_name():
    pass



if __name__ == "__main__":
    app.run(debug=True)