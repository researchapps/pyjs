

link_subs = {}

ofile = open("tmp.txt", "w+")

with open("index.rst") as infile:

  for line in infile:
    line = line.rstrip("\n").rstrip()
    if(line.startswith(".. ")):
      if(line.startswith(".. note::")):
        print(line, file=ofile)
        continue

      pos = line.find(":")
      if(pos < 3): continue

      if(line[3] == "_"):
        toks = line[4:].split(":")

        link_subs["`%s`_" % line[4:pos]] = \
          '<a href="%s">%s</a>' % (toks[1] + "\:" + toks[2].strip(), toks[0])
#          "[[%s|%s]]" % (toks[1] + "\:" + toks[2].strip(), toks[0])

    else:
      if(line.startswith("  * ")):
        print("** " + line[4:], file=ofile)
      else:
        print(line, file=ofile)

ofile.close()


with open("sed_it.sed", "w+") as sed_file:
  print("#!/usr/bin/sed -f", file=sed_file)
  for k,v in link_subs.items():
    print("s:%s:%s:g" % (k, v), file=sed_file)



#.. Documentation master file to be processed using sphinx
#
#.. _Flask: http://flask.pocoo.org/
#.. _Pyjamas: http://pyjs.org/
#.. _CORS: http://www.w3.org/TR/cors/
#.. _HTTP access control: https://developer.mozilla.org/En/HTTP_access_control/
#.. _XHR: http://www.w3.org/TR/XMLHttpRequest/
#.. _Celery: http://celeryproject.org/
#.. _RabbitMQ: http://www.rabbitmq.com/
