# vim:sw=3:ts=3:fileencoding=utf-8:list:listchars=tab\:»·,trail\:·:noexpandtab:
# :encoding=utf-8:indentSize=3:tabSize=3:noTabs=false:

from functools import wraps

from django.utils.decorators import available_attrs

from http_responses import HttpResponseUnauthorized

def require_login ( view_func ):
	@wraps(view_func, assigned=available_attrs(view_func))
	def inner ( req, *args, **kwargs ):
		if req.user.is_authenticated():
			return view_func( req, *args, **kwargs )

		msg = 'Only authenticated users may perform this action.'
		res = HttpResponseUnauthorized( msg )
		res['Content-Length'] = len( msg )
		return res
	return inner
