from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse

import MySQLdb as mdb
import sys

def index(request):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        cur.execute("SELECT VERSION()")

        ver = cur.fetchone()

        print "Database version : %s " % ver

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()
    #return render(request, 'Main/index.html')
    return HttpResponse("Database version : %s " % ver)