# MngScripts.py	, 	in
#	/home/pydsuperu/Projets/tuto_flask_blog2/ProjectMngmnt_Ignor
import sqlite3, os
import shutil

print(2==2)

def get_db_connection():
    conn = sqlite3.connect('cabwill.db')
    conn.row_factory = sqlite3.Row
    return conn

#==========================================================================
# long SQL strings
#==================
# PageTreeTT1_Vw11
ListPgDescr="""
SELECT
	PagesTreeTT1.ID_Page AS id, 
	PagesTreeTT1.PgSlug AS slug, 
	PagesTreeTT1.PgDescr AS titre, 
	PagesTreeTT1.TxtID_Page AS short
FROM
	PagesTreeTT1
ORDER BY
	PagesTreeTT1.ID_Page ASC
;
"""

def ChooseTplModelForPages(s1):
# _LTF_PageModel_GEN.htm
# in 		/home/pydsuperu/Projets/tuto_flask_blog2/templates/cabwill/TplModels
	relModelPath='../templates/cabwill/TplModels/'
#	ModelFName='LTF_PageModel_GEN.htm'
	ModelFName=s1
	ModelFpath= '%s/%s' %(relModelPath, ModelFName)
	return ModelFpath

def CreateNeededPage_1(s1):
# shutil.copy('/etc/hostname', '/var/tmp/testhostname')
	relNwPgPath='../templates/cabwill/pages/'
	NwPgFName=s1
	NwPgFpath= '%s/%s' %(relNwPgPath, NwPgFName)
#	shutil.copy(ChooseTplModelForPages('LTF_PageModel_GEN.htm'),NwPgFpath)
	if not os.path.exists(NwPgFpath):
		f = open(NwPgFpath, "w")
		with f:
#			os.system(' cp %s %s' %  (ChooseTplModelForPages('LTF_PageModel_GEN.htm'), f)
			os.system(' cp src.txt tgt.txt')

def MakePagesList_1():
	conn = get_db_connection()
	cur = conn.cursor()
	cur.execute(ListPgDescr)
	pages=cur.fetchall()
	for pg in pages:
		print(pg['titre'])
		fname= '%s.htm' % pg['titre']
		print(fname)

	print("list")
	#		END of		MakePagesList_1()




print("end")