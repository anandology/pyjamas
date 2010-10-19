/* start module: controller */
var controller;
$pyjs.loaded_modules['controller'] = function (__mod_name__) {
	if($pyjs.loaded_modules['controller'].__was_initialized__) return $pyjs.loaded_modules['controller'];
	var $m = controller = $pyjs.loaded_modules["controller"];
	controller.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'controller';
	var __name__ = controller.__name__ = __mod_name__;


	$m['SimpleCommand'] = $p['___import___']('puremvc.patterns.command.SimpleCommand', null, null, false);
	$m['PostRemoteProxy'] = $p['___import___']('model.PostRemoteProxy', null, null, false);
	$m['HomeMediator'] = $p['___import___']('view.HomeMediator', null, null, false);
	$m['WriteMediator'] = $p['___import___']('view.WriteMediator', null, null, false);
	$m['EditMediator'] = $p['___import___']('view.EditMediator', null, null, false);
	$m['StartupCommand'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'controller';
		$method = $pyjs__bind_method2('execute', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}
			var $attr1,$attr2,$attr5,$attr4,$attr6,main_panel,$attr3;
			self['facade']['registerProxy']($m['PostRemoteProxy']());
			main_panel = note['getBody']();
			self['facade']['registerMediator']($m['HomeMediator']((($attr1=($attr2=main_panel)['home_panel']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
						$p['getattr']($attr2, 'home_panel'):
						main_panel['home_panel'])));
			self['facade']['registerMediator']($m['WriteMediator']((($attr3=($attr4=main_panel)['write_panel']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'write_panel'):
						main_panel['write_panel'])));
			self['facade']['registerMediator']($m['EditMediator']((($attr5=($attr6=main_panel)['edit_panel']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'edit_panel'):
						main_panel['edit_panel'])));
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['execute'] = $method;
		var $bases = new Array($m['SimpleCommand']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('StartupCommand', $p['tuple']($bases), $data);
	})();
	$m['GetPostsCommand'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'controller';
		$method = $pyjs__bind_method2('execute', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}
			var $attr9,$attr8,$attr7,facade,postProxy,$attr10;
			facade = (($attr7=($attr8=self)['facade']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'facade'):
						self['facade']);
			postProxy = facade['retrieveProxy']((($attr9=($attr10=$m['PostRemoteProxy'])['NAME']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'NAME'):
						$m['PostRemoteProxy']['NAME']));
			postProxy['retrieve_posts']();
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['execute'] = $method;
		var $bases = new Array($m['SimpleCommand']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('GetPostsCommand', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end controller */


/* end module: controller */


/*
PYJS_DEPS: ['puremvc.patterns.command.SimpleCommand', 'puremvc', 'puremvc.patterns', 'puremvc.patterns.command', 'model.PostRemoteProxy', 'model', 'view.HomeMediator', 'view', 'view.WriteMediator', 'view.EditMediator']
*/
