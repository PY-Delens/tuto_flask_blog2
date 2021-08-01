
import sqlite3
from flask import Flask, render_template, render_template_string, request, url_for, flash, redirect,Markup
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'nobodyknows'

def formattedQuery(q): return " ".join([s.strip() for s in q.splitlines()])


#   === List (Dictionary) of Base Templates  ====
#   in   /home/pydsuperu/Projets/tuto_flask_blog2/templates/cabwill
BaseTemplates={1:'cabwill_base1.htm', 2:'base_cw.htm'}
BaseTemplatesPath='/cabwill/'
#   === List (Dictionary) of _LTF_PageModels  ====
#   in  /home/pydsuperu/Projets/tuto_flask_blog2/templates/cabwill/TplModels
LtfPageModels={1:'_LTF_PageModel_GEN.htm', 2:'_LTF_PageModel_PlainJ2.htm'}
LtfPageModelsPath='/cabwill/TplModels/'



#==========================================================================
# long SQL strings
#==================

# for tree2 : PageTreeTT1_TreeVw02 in cabwill.db
tree2SqlA="""
WITH RECURSIVE
  under_root(ID_Page,level, lbl,slug,OnOff) AS (
    SELECT
	PagesTreeTT1.ID_Page, 0, PagesTreeTT1.PgDescr, PagesTreeTT1.TxtID_Page, PagesTreeTT1.OnOff
FROM 	PagesTreeTT1
WHERE PagesTreeTT1.ParentPage_Id ISNULL  AND PagesTreeTT1.OnOff = 1
    UNION ALL
    SELECT PagesTreeTT1.ID_Page, under_root.level+1, PagesTreeTT1.PgDescr, PagesTreeTT1.TxtID_Page, PagesTreeTT1.OnOff
      FROM PagesTreeTT1 JOIN under_root ON PagesTreeTT1.ParentPage_Id=under_root.ID_Page
			WHERE PagesTreeTT1.OnOff = 1
     ORDER BY 2 DESC
  )
SELECT (substr('..........',1,level*3) || lbl) as BranchString, slug FROM under_root;"""
# SELECT (substr('..........',1,level*3) || ID_Page || '  ' || lbl) as BranchString, slug FROM under_root;
#==========================================================================

from jinja2 import Template

def cleverfunction(): 
    return "HelloGlobalsSoir2"
# str1='astring and the Hello : {{cleverfunction}}'
# template=Template(str1)
# template.globals['cleverfunction']=cleverfunction

app.jinja_env.globals.update(cleverfunction=cleverfunction)

def chooseBase(option=1):
    fpathname= '%s%s' % (BaseTemplatesPath, BaseTemplates[option])
    return fpathname

app.jinja_env.globals.update(chooseBase=chooseBase)

def runchooseBase():
#    option=input("N° du BaseTemplate : ")
    option=1
    st=  chooseBase(int(option))
    print('BaseTPL selected is : %s' % st )
    return st

app.jinja_env.globals.update(runchooseBase=runchooseBase)

runchooseBase()

def get_db_connection():
    conn = sqlite3.connect('cabwill.db')
    conn.row_factory = sqlite3.Row
    return conn


from markupsafe import escape

@app.route('/')
def defaultview():
    return 'Hello, defaultview - from cabwill'


@app.route('/cw')
def hello():
    return 'Hello, World - from cabwill'

#   from https://pythonspot.com/flask-with-static-html-files/
@app.route('/<string:page_name>/')
def render_static(page_name):
   return render_template('/cabwill/pages/%s.htm' % page_name)

@app.route('/tree1')        #       zzzzz , field is missing here
def maketree():
    conn = get_db_connection()
    branches = conn.execute('SELECT * FROM PagesTreeTT1').fetchall()
    conn.close()
#    return 'TreeDone'
    return render_template('cabwill/pagestree.htm', branches=branches)


print ("'TreeDone'")


# tree2Sql=tree2SqlA

@app.route('/tree2')
def maketree2():
    conn = get_db_connection()
    branches = conn.execute(tree2SqlA).fetchall()
    conn.close()
#    return 'TreeDone'
    return render_template('cabwill/pagestree.htm', branches=branches)

app.jinja_env.globals.update(maketree2=maketree2)

@app.route('/tree3')
def maketree3():
    conn = get_db_connection()
    branches = conn.execute(tree2SqlA).fetchall()
    conn.close()
#    return 'TreeDone'
    return render_template('cabwill/JustTheTree.htm', branches=branches)
str2='{{ maketree3 }}'      # u'xxxx'
template=Template(str2)
template.globals['maketree3']=maketree3
app.jinja_env.globals.update(maketree3=maketree3)

def maketree4():
    conn = get_db_connection()
    branches = conn.execute(tree2SqlA).fetchall()
    conn.close()
    return branches
app.jinja_env.globals.update(maketree4=maketree4)


print ("'TreeDone'")


@app.route('/base1')
def base1():
    return render_template('/cabwill/cabwill_base1.htm')





print("endend")