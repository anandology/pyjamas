/* start module: puremvc.patterns.command */
$pyjs.loaded_modules['puremvc.patterns.command'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.patterns.command'].__was_initialized__) return $pyjs.loaded_modules['puremvc.patterns.command'];
	if(typeof $pyjs.loaded_modules['puremvc.patterns'] == 'undefined' || !$pyjs.loaded_modules['puremvc.patterns'].__was_initialized__) $p['___import___']('puremvc.patterns', null);
	var $m = puremvc['patterns']['command'] = $pyjs.loaded_modules["puremvc.patterns.command"];
	puremvc['patterns']['command'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.patterns.command';
	var __name__ = puremvc['patterns']['command'].__name__ = __mod_name__;
	var command = puremvc['patterns']['command'];
	var $attr9,$attr1,$attr3,$attr2,$attr5,$attr4,$attr6,$attr14,$attr11,$attr10,$attr13,$attr12;

	$m['puremvc'] = $p['___import___']('puremvc.interfaces', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.observer', 'puremvc.patterns');
	$m['MacroCommand'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.command';
		$cls_definition['subCommands'] = null;
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'subCommands', $p['list']([]));
			self['initializeMacroCommand']();
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('initializeMacroCommand', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

 			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeMacroCommand'] = $method;
		$method = $pyjs__bind_method2('addSubCommand', function(commandClassRef) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				commandClassRef = arguments[1];
			}

			self['subCommands']['append'](commandClassRef);
			return null;
		}
	, 1, [null,null,['self'],['commandClassRef']]);
		$cls_definition['addSubCommand'] = $method;
		$method = $pyjs__bind_method2('execute', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}
			var $attr8,commandClassRef,$attr7,commandInstance;
			while ($p['bool'](($p['cmp']($p['len']((($attr7=($attr8=self)['subCommands']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'subCommands'):
						self['subCommands'])), 0) == 1))) {
				commandClassRef = self['subCommands']['pop'](0);
				commandInstance = commandClassRef();
				commandInstance['execute'](notification);
			}
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['execute'] = $method;
		var $bases = new Array((($attr1=($attr2=$m['puremvc']['patterns']['observer'])['Notifier']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
				$p['getattr']($attr2, 'Notifier'):
				$m['puremvc']['patterns']['observer']['Notifier']),(($attr3=($attr4=$m['puremvc']['interfaces'])['ICommand']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
				$p['getattr']($attr4, 'ICommand'):
				$m['puremvc']['interfaces']['ICommand']),(($attr5=($attr6=$m['puremvc']['interfaces'])['INotifier']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
				$p['getattr']($attr6, 'INotifier'):
				$m['puremvc']['interfaces']['INotifier']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('MacroCommand', $p['tuple']($bases), $data);
	})();
	$m['SimpleCommand'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.command';
		$method = $pyjs__bind_method2('execute', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

 			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['execute'] = $method;
		var $bases = new Array((($attr9=($attr10=$m['puremvc']['patterns']['observer'])['Notifier']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
				$p['getattr']($attr10, 'Notifier'):
				$m['puremvc']['patterns']['observer']['Notifier']),(($attr11=($attr12=$m['puremvc']['interfaces'])['ICommand']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
				$p['getattr']($attr12, 'ICommand'):
				$m['puremvc']['interfaces']['ICommand']),(($attr13=($attr14=$m['puremvc']['interfaces'])['INotifier']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
				$p['getattr']($attr14, 'INotifier'):
				$m['puremvc']['interfaces']['INotifier']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('SimpleCommand', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.patterns.command */


/* end module: puremvc.patterns.command */


/*
PYJS_DEPS: ['puremvc.interfaces', 'puremvc', 'puremvc.patterns.observer', 'puremvc.patterns']
*/
