import simplejson
import web

class JsonHandler:
  def POST(self):
    args = simplejson.loads(web.data())
    json_func = getattr(self, args["method"])
    json_params = args["params"]
    json_method_id = args["id"]
    result = json_func(*json_params)
    # reuse args to send result back
    args.pop("method")
    args["result"] = result
    args["error"] = None # IMPORTANT!!
    web.header("Content-Type","text/html; charset=utf-8")
    return simplejson.dumps(args)
