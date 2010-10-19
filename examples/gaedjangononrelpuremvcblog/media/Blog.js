/* start module: Blog */
var Blog;
$pyjs.loaded_modules['Blog'] = function (__mod_name__) {
	if($pyjs.loaded_modules['Blog'].__was_initialized__) return $pyjs.loaded_modules['Blog'];
	var $m = Blog = $pyjs.loaded_modules["Blog"];
	Blog.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'Blog';
	var __name__ = Blog.__name__ = __mod_name__;
	var $attr7,$attr8,$attr12,$attr11,$attr5,$attr10,$attr6,$attr9;

	$m['pyjd'] = $p['___import___']('pyjd', null);
	$m['Facade'] = $p['___import___']('puremvc.patterns.facade.Facade', null, null, false);
	$m['StartupCommand'] = $p['___import___']('controller.StartupCommand', null, null, false);
	$m['GetPostsCommand'] = $p['___import___']('controller.GetPostsCommand', null, null, false);
	$m['PyJsApp'] = $p['___import___']('components.PyJsApp', null, null, false);
	$m['AppFacade'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'Blog';
		$cls_definition['STARTUP'] = 'startup';
		$cls_definition['ADD_POST'] = 'addPost';
		$cls_definition['EDIT_POST'] = 'editPost';
		$cls_definition['DELETE_POST'] = 'deletePost';
		$cls_definition['GET_POSTS'] = 'getPosts';
		$cls_definition['POSTS_RETRIEVED'] = 'postsRetrieved';
		$cls_definition['EDIT_CANCELED'] = 'editCanceled';
		$cls_definition['VIEW_WRITE_POST'] = 'viewWritePost';
		$cls_definition['VIEW_EDIT_POST'] = 'viewEditPost';
		$cls_definition['POST_REMOTE_FAILURE'] = 'postRemoteFailure';
		$cls_definition['POST_REMOTE_NONE'] = 'postRemoteNone';
		$cls_definition['POST_ADDED'] = 'postAdded';
		$cls_definition['POST_EDITED'] = 'postEdited';
		$cls_definition['POST_DELETED'] = 'postDeleted';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['initializeFacade']();
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('getInstance', function() {

			return $m['AppFacade']();
		}
	, 3, [null,null]);
		$cls_definition['getInstance'] = $method;
		$method = $pyjs__bind_method2('initializeFacade', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['$$super']($m['AppFacade'], self)['initializeFacade']();
			self['initializeController']();
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeFacade'] = $method;
		$method = $pyjs__bind_method2('initializeController', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr1,$attr2,$attr3,$attr4;
			$p['$$super']($m['AppFacade'], self)['initializeController']();
			$p['$$super']($m['AppFacade'], self)['registerCommand']((($attr1=($attr2=$m['AppFacade'])['STARTUP']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
						$p['getattr']($attr2, 'STARTUP'):
						$m['AppFacade']['STARTUP']), $m['StartupCommand']);
			$p['$$super']($m['AppFacade'], self)['registerCommand']((($attr3=($attr4=$m['AppFacade'])['GET_POSTS']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'GET_POSTS'):
						$m['AppFacade']['GET_POSTS']), $m['GetPostsCommand']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeController'] = $method;
		var $bases = new Array($m['Facade']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('AppFacade', $p['tuple']($bases), $data);
	})();
	if ($p['bool']($p['op_eq'](Blog['__name__'], '__main__'))) {
		$m['pyjd']['setup']('./public/Blog.html');
		$m['app'] = $m['AppFacade']['getInstance']();
		$m['pyjs_app'] = $m['PyJsApp']();
		$m['app']['sendNotification']((($attr5=($attr6=$m['AppFacade'])['STARTUP']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
					$p['getattr']($attr6, 'STARTUP'):
					$m['AppFacade']['STARTUP']), (($attr7=($attr8=$m['pyjs_app'])['app_frame']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
					$p['getattr']($attr8, 'app_frame'):
					$m['pyjs_app']['app_frame']));
		$m['app']['sendNotification']((($attr9=($attr10=$m['AppFacade'])['GET_POSTS']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
					$p['getattr']($attr10, 'GET_POSTS'):
					$m['AppFacade']['GET_POSTS']), (($attr11=($attr12=$m['pyjs_app'])['app_frame']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
					$p['getattr']($attr12, 'app_frame'):
					$m['pyjs_app']['app_frame']));
		$m['pyjd']['run']();
	}
	return this;
}; /* end Blog */


/* end module: Blog */


/*
PYJS_DEPS: ['pyjd', 'puremvc.patterns.facade.Facade', 'puremvc', 'puremvc.patterns', 'puremvc.patterns.facade', 'controller.StartupCommand', 'controller', 'controller.GetPostsCommand', 'components.PyJsApp', 'components']
*/
