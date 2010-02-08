import json
import web

class JsonHandler:
  def POST(self):
    args = json.loads(web.data())
    json_func = getattr(self, args[u"method"])
    json_params = args[u"params"]
    json_method_id = args[u"id"]
    result = json_func(*json_params)
    # reuse args to send result back
    args.pop(u"method")
    args["result"] = result
    args["error"] = None # IMPORTANT!!
    web.header("Content-Type","text/html; charset=utf-8")
    return json.dumps(args)
