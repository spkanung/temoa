# vim:sw=3:ts=3:fileencoding=utf-8:list:listchars=tab\:»·,trail\:·:noexpandtab:
# :encoding=utf-8:indentSize=3:tabSize=3:noTabs=false:

from base64 import b64encode
import json

from django.contrib import messages
from django.http import HttpResponse


def set_cookie ( req, res, **kwargs ):
	cookie = {}
	if req.user.is_authenticated():
		cookie[ 'username' ] = req.user.username
	else:
		cookie[ 'username' ] = None

	for key in ( 'analysis_id', 'process_ids',):
		if key in kwargs:
			cookie[ key ] = kwargs[ key ]

	cookie = b64encode(json.dumps( cookie ))
	res.set_cookie( 'ServerState', value=cookie, max_age=None ) # session only

