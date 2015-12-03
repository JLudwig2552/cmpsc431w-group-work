from django.shortcuts import render

# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse

import itertools
import MySQLdb as mdb
import sys

def index(request):
    try:
        con = mdb.connect('localhost', 'Admin1', 'Admin1', 'Inceptionists');

        cur = con.cursor()
        cur.execute("SELECT name FROM categories")

        #categories = cur.fetchall()
        categories = list(itertools.chain.from_iterable(cur))

    except mdb.Error, e:

        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    finally:

        if con:
            con.close()

    template = loader.get_template('Main/index.html')
    context = RequestContext(request, {
        'categories': categories,
    })
    #return render(request, 'Main/index.html')
    #return HttpResponse("Database version : %s " % ver)
    return HttpResponse(template.render(context))


def about(request):
    return HttpResponse("Programmed by Fliu and Rcamp")