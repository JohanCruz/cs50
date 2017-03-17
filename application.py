from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from passlib.apps import custom_app_context as pwd_context
from tempfile import gettempdir
from urllib.request import urlopen
import http.client
import sqlite3
from sqlite3 import OperationalError

from helpers import *
dbname="0.db"
su=0


# configure application    heyjuan   pass: juan.com  en:   http://pset7.cs50.net/
app = Flask(__name__)

# ensure responses aren't cached
if app.config["DEBUG"]:
    @app.after_request
    def after_request(response):
        response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        response.headers["Expires"] = 0
        response.headers["Pragma"] = "no-cache"
        return response

# custom filter
app.jinja_env.filters["usd"] = usd

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = gettempdir()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

@app.route("/")
@login_required
def index():
    global su
    if su==0:
        su2=0
    else:
        su2=1
        su=0
    if request.method == "POST":
        if not request.form.get("simbolo"):
            return apology("must provide quote")
        simbolo=request.form["simbolo"]
        pagina1="https://finance.yahoo.com/quote/"+simbolo+"?p="+simbolo
        pagina="http://download.finance.yahoo.com/d/quotes.csv?s="+simbolo+"&f=sl1d1t1c1ohgv&e=.csv"
        codigoFuente = urlopen(pagina).readline()
        su=codigoFuente.decode()
        su = su.split()
        we=urlopen(pagina1).readline()
        we=we.decode()
        we=we.split()

        lk=we[30]+" "+we[31]+" "+we[32]+" "
            
        
        du=""
        fr=""
        count = 0;
        for n in su:
            for i in n:
                if i==",":
                    count=count+1
                
                #if ord(i) > 64 and ord(i)<123 and count>0 and i!=",":
                    #fr=fr+i
                    
                if count<2 and count>0 and i!=",":
                    du=du+i
                    #print(i)
                
        print (du)
        if du=="N/A":
            print("invalid sYmbol")
            return apology("INVALID SYMBOL")
        du=float(du)
        #print(du+1)
        global dbname
        db2 = SQL("sqlite:///"+dbname)
        
        
        print(dbname)
        db2.execute("INSERT INTO TRANSACTIONS (SYMBOL,NAME,SHARES,PRICE) VALUES (:SYMBOL,:NAME,:SHARES,:PRICE)",SYMBOL=request.form["simbolo"], NAME=lk,SHARES=-1*int(request.form["shares"]),PRICE=du)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")
        dicc = dict()
        dicc2= dict()
        dicc3=dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            h=h.upper()
            r=b['SHARES']
            m=b['NAME']
            p=b['PRICE']
            if (h in dicc):
                dicc[h]=r+dicc[h]
                dicc2[h]=dicc2[h]+p*r
            else:
                dicc[h] = r
                dicc2[h] = p*r
                dicc3[h] =m
            #print(f,h,r)

        f=dicc.keys()
        f2=dicc.values()
        #print(f,f2)
        return render_template("index.html",lk=lk,sim= simbolo.upper()+" : $",du=du, transa=rows,d=1,dicc=dicc,dicc2=dicc2, dicc3=dicc3,su2=su2)
    else:
        global dbname
        dbname=str(session.get("user_id"))+".db"
        idu= dbname.replace(".", "")
        idu= idu.replace("d", "")
        idu= idu.replace("b", "")
        rows1 = db.execute("SELECT * FROM users WHERE ID = :ID", ID=idu)
        #print(rows1[0]['cash'])
        tt=rows1[0]['cash']
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")
        dicc = dict()
        dicc2 = dict()
        dicc3 = dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            h=h.upper()
            r=b['SHARES']
            m=b['NAME']
            p=b['PRICE']
            if (h in dicc):
                dicc[h]=r+dicc[h]
                dicc2[h]=dicc2[h]+p*r
            else:
                dicc[h] = r
                dicc2[h] = p*r
                dicc3[h] = m
            print(f,h,r)
            print(dicc2.keys(),dicc2.values())
        return render_template("index.html",sim="",du="",transa="",d=1,dicc=dicc,dicc2=dicc2,dicc3=dicc3,su2=su2,tt=tt)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock."""
    if request.method == "POST":
        if not request.form.get("simbolo"):
            return apology("must provide quote")
        simbolo=request.form["simbolo"]
        pagina1="https://finance.yahoo.com/quote/"+simbolo+"?p="+simbolo
        pagina="http://download.finance.yahoo.com/d/quotes.csv?s="+simbolo+"&f=sl1d1t1c1ohgv&e=.csv"
        codigoFuente = urlopen(pagina).readline()
        su=codigoFuente.decode()
        su = su.split()
        we=urlopen(pagina1).readline()
        we=we.decode()
        we=we.split()

        lk=we[30]+" "+we[31]+" "+we[32]+" "
        gp=lookup(simbolo)
        print (gp) 
        lk=gp['name']
        du=""
        fr=""
        count = 0;
        for n in su:
            for i in n:
                if i==",":
                    count=count+1
                
                #if ord(i) > 64 and ord(i)<123 and count>0 and i!=",":
                    #fr=fr+i
                    
                if count<2 and count>0 and i!=",":
                    du=du+i
                    #print(i)
                
        #print (du)
        if du=="N/A":
            print("invalid sYmbol")
            return apology("INVALID SYMBOL")
        du=float(du)
        #print(du+1)
        global dbname
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        
        idu= dbname.replace(".", "")
        idu= idu.replace("d", "")
        idu= idu.replace("b", "")
        total=float(request.form["shares"])*float(du)
        rows1 = db.execute("SELECT * FROM users WHERE ID = :ID", ID=idu)
        #print(rows1[0]['cash'])
        if (float(rows1[0]['cash'])<total):
            return apology("Invalid Buy, insufficient funds")
        tt=rows1[0]['cash']-total
        sql11 = "UPDATE users SET cash="+str(tt)+" WHERE id="+str(idu)
        data = (str(total), str(idu))
        db.execute(sql11)
        #db.execute("UPDATE users SET cash = %s WHERE id = %s",(total, idu))     
        #print(rows1)
        #print("compra total",total)
        #print(dbname)
        db2.execute("INSERT INTO TRANSACTIONS (SYMBOL,NAME,SHARES,PRICE) VALUES (:SYMBOL,:NAME,:SHARES,:PRICE)",SYMBOL=request.form["simbolo"], NAME=lk,SHARES=request.form["shares"],PRICE=du)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")
        dicc = dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            r=b['SHARES']
            if (h in dicc):
                dicc[h]=r+dicc[h]
            else:
                dicc[h] = r
            #print(f,h,r)
        
        f=dicc.keys()
        f2=dicc.values()
        #print(f,f2)
        global su
        su=1

        return redirect(url_for("index"))
        return render_template("buy.html",lk=lk,sim= simbolo.upper()+" : $",du=du, transa=rows,d=1,dicc=dicc)
    else:
        global dbname
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")
        dicc = dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            r=b['SHARES']
            if (h in dicc):
                dicc[h]=r+dicc[h]
            else:
                dicc[h] = r
            print(f,h,r)
        return render_template("buy.html",sim="",du="",transa="",d=0,dicc=dicc)
    

@app.route("/history")
@login_required
def history():
    """Show history of transactions."""
    if request.method == "POST":
        if not request.form.get("simbolo"):
            return apology("must provide quote")
        simbolo=request.form["simbolo"]
        pagina1="https://finance.yahoo.com/quote/"+simbolo+"?p="+simbolo
        pagina="http://download.finance.yahoo.com/d/quotes.csv?s="+simbolo+"&f=sl1d1t1c1ohgv&e=.csv"
        codigoFuente = urlopen(pagina).readline()
        su=codigoFuente.decode()
        su = su.split()
        we=urlopen(pagina1).readline()
        we=we.decode()
        we=we.split()

        lk=we[30]+" "+we[31]+" "+we[32]+" "
        gp=lookup(simbolo)
        print (gp) 
        lk=gp['name'] 
        
        du=""
        fr=""
        count = 0;
        for n in su:
            for i in n:
                if i==",":
                    count=count+1
                
                #if ord(i) > 64 and ord(i)<123 and count>0 and i!=",":
                    #fr=fr+i
                    
                if count<2 and count>0 and i!=",":
                    du=du+i
                    #print(i)
                
        print (du)
        if du=="N/A":
            print("invalid sYmbol")
            return apology("INVALID SYMBOL")
        du=float(du)
        #print(du+1)
        global dbname
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        
        
        print(dbname)
        db2.execute("INSERT INTO TRANSACTIONS (SYMBOL,NAME,SHARES,PRICE) VALUES (:SYMBOL,:NAME,:SHARES,:PRICE)",SYMBOL=request.form["simbolo"], NAME=lk,SHARES=-1*int(request.form["shares"]),PRICE=du)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")
        dicc = dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            r=b['SHARES']
            if (h in dicc):
                dicc[h]=r+dicc[h]
            else:
                dicc[h] = r
            #print(f,h,r)
        
        f=dicc.keys()
        f2=dicc.values()
        #print(f,f2)
        
        return render_template("history.html",lk=lk,sim= simbolo.upper()+" : $",du=du, transa=rows,d=1,dicc=dicc,wi=0)
    else:
        global dbname
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")
        dicc = dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            h=h.upper()
            r=b['SHARES']
            if (h in dicc):
                dicc[h]=r+dicc[h]
            else:
                dicc[h] = r
            #print(f,h,r)
        return render_template("history.html",sim="",du="",transa=rows,d=1,dicc=dicc,wi=1)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in."""

    # forget any user_id
    session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")

        # query database for username
        global rows
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]
        global dbname
        dbname=str(rows[0]["id"])+".db"

        # redirect user to home page
        return redirect(url_for("index"))

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    """Log user out."""

    # forget any user_id
    session.clear()

    # redirect user to login form
    return redirect(url_for("login"))

@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("simbolo"):
            return apology("must provide quote")
        simbolo=request.form["simbolo"]
        pagina1="https://finance.yahoo.com/quote/"+simbolo+"?p="+simbolo
        pagina="http://download.finance.yahoo.com/d/quotes.csv?s="+simbolo+"&f=sl1d1t1c1ohgv&e=.csv"
        codigoFuente = urlopen(pagina).readline()
        
        su=codigoFuente.decode()
        su = su.split()
        

        we=urlopen(pagina1).readline()
        we=we.decode()
        we=we.split()

        
        lk=we[30]+" "+we[31]+" "+we[32]+" "+we[33]+" "+we[34]+" "+we[35]
        gp=lookup(simbolo)
        print (gp) 
        lk=gp['name']  
        du=""
        fr=""
        count = 0;
        for n in su:
            for i in n:
                if i==",":
                    count=count+1
                
                #if ord(i) > 64 and ord(i)<123 and count>0 and i!=",":
                    #fr=fr+i
                    
                if count<2 and count>0 and i!=",":
                    du=du+i
                    #print(i)
                
        print (du)
        if du=="N/A":
            print("invalid sYmbol")
            return apology("INVALID SYMBOL")
        du=float(du)
        #print(du+1)    
        return render_template("quote.html",lk=lk,sim= simbolo.upper()+" : $",du=du,wi=0)
    else:
        return render_template("quote.html",sim="",du="",wi=1)
        
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    """Get stock quote."""
    if request.method == "POST":
        if not request.form.get("simbolo"):
            return apology("invalid")
        add=request.form["simbolo"]
        global dbname
        dbname=str(session.get("user_id"))

        rows1 = db.execute("SELECT * FROM users WHERE ID = :ID", ID=dbname)
        #print(rows1[0]['cash'])
        tt=float(rows1[0]['cash'])+float(add)
        sql11 = "UPDATE users SET cash="+str(tt)+" WHERE id="+dbname
        db.execute(sql11)
        
        return redirect(url_for("index"))
        return render_template("add.html")
    else:
        return render_template("add.html")

@app.route("/register", methods=["GET","POST"])
def register():
    """Register user."""
    # forget any user_id
    #session.clear()

    # if user reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username")

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password")
            
        db.execute("INSERT INTO users (hash,username) VALUES (:passw,:username)", username=request.form["username"], passw=pwd_context.encrypt(request.form["password"]))

        # query database for username
        global rows
        rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))

        # ensure username exists and password is correct
        if len(rows) != 1 or not pwd_context.verify(request.form.get("password"), rows[0]["hash"]):
            return apology("invalid username and/or password")

        # remember which user has logged in
        session["user_id"] = rows[0]["id"]
        global dbname
        dbname=str(rows[0]["id"])+".db"
         
        conn=sqlite3.connect(dbname)
        cursor=conn.cursor()
        cursor.execute("""CREATE TABLE TRANSACTIONS
                (ID INTEGER PRIMARY KEY    NOT NULL,
                 SYMBOL TEXT           NOT NULL,
                 NAME   TEXT           NOT NULL,
                 SHARES INTEGER        NOT NULL,
                 PRICE  REAL           NOT NULL)""")
        # redirect user to home page
        return redirect(url_for("index"))
        #return render_template("apology.html")

    # else if user reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")
    #return apology("TODO")

@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock."""
    if request.method == "POST":
        if not request.form.get("simbolo"):
            return apology("must provide quote")
        simbolo=request.form["simbolo"]
        pagina1="https://finance.yahoo.com/quote/"+simbolo+"?p="+simbolo
        pagina="http://download.finance.yahoo.com/d/quotes.csv?s="+simbolo+"&f=sl1d1t1c1ohgv&e=.csv"
        codigoFuente = urlopen(pagina).readline()
        su=codigoFuente.decode()
        su = su.split()
        we=urlopen(pagina1).readline()
        we=we.decode()
        we=we.split()

        lk=we[30]+" "+we[31]+" "+we[32]+" "
            
        
        du=""
        fr=""
        count = 0;
        for n in su:
            for i in n:
                if i==",":
                    count=count+1
                
                #if ord(i) > 64 and ord(i)<123 and count>0 and i!=",":
                    #fr=fr+i
                    
                if count<2 and count>0 and i!=",":
                    du=du+i
                    #print(i)
                
        #print (du)
        if du=="N/A":
            print("invalid sYmbol")
            return apology("INVALID SYMBOL")
        du=float(du)
        #print(du+1)
        global dbname
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        
        
        #print(dbname)
        db2.execute("INSERT INTO TRANSACTIONS (SYMBOL,NAME,SHARES,PRICE) VALUES (:SYMBOL,:NAME,:SHARES,:PRICE)",SYMBOL=request.form["simbolo"], NAME=lk,SHARES=-1*int(request.form["shares"]),PRICE=du)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")

        dicc = dict()
        dicc2= dict()
        dicc3=dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            h=h.upper()
            r=b['SHARES']
            m=b['NAME']
            p=b['PRICE']
            if (h in dicc):
                dicc[h]=r+dicc[h]
                dicc2[h]=dicc2[h]+p*r
            else:
                dicc[h] = r
                dicc2[h] = p*r
                dicc3[h] =m
            #print(f,h,r)
        
        f=dicc.keys()
        f2=dicc.values()
        #print(f,f2)
        idu= dbname.replace(".", "")
        idu= idu.replace("d", "")
        idu= idu.replace("b", "")
        rows1 = db.execute("SELECT * FROM users WHERE ID = :ID", ID=idu)
        #print(rows1[0]['cash'])
        tt=rows1[0]['cash']+int(request.form["shares"])*du
        sql11 = "UPDATE users SET cash="+str(tt)+" WHERE id="+str(idu)
        db.execute(sql11)
        return render_template("sell.html",lk=lk,sim= simbolo.upper()+" : $",du=du, transa=rows,d=1,dicc=dicc,dicc2=dicc2, dicc3=dicc3)
    else:
        global dbname
        dbname=str(session.get("user_id"))+".db"
        db2 = SQL("sqlite:///"+dbname)
        rows = db2.execute("SELECT * FROM TRANSACTIONS")

        dicc = dict()
        dicc2 = dict()
        dicc3 = dict()
        for b in rows:
            f=b.keys()
            h=b['SYMBOL']
            h=h.upper()
            r=b['SHARES']
            m=b['NAME']
            p=b['PRICE']
            if (h in dicc):
                dicc[h]=r+dicc[h]
                dicc2[h]=dicc2[h]+p*r
            else:
                dicc[h] = r
                dicc2[h] = p*r
                dicc3[h] = m
            #print(f,h,r)
            #print(dicc2.keys(),dicc2.values())
        return render_template("sell.html",sim="",du="",transa="",d=0,dicc=dicc,dicc2=dicc2,dicc3=dicc3)
