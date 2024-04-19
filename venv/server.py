from flask import Flask, render_template, request, redirect

app= Flask(__name__)
app.debug=True

@app.route('/submit_form', methods =['GET','POST'])
def help():
  if request.method=='POST':
    data = request.form.to_dict()
    return redirect('thankyou.html')
  
@app.route('/', methods =['GET'])
def index():
  return render_template('index.html')



@app.route('/<string:page_name>', methods =['GET'])
def html_page(page_name):
  return render_template(page_name)






if __name__=="__main__":
  app.run()
