/* start module: puremvc.patterns.proxy */
$pyjs.loaded_modules['puremvc.patterns.proxy'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.patterns.proxy'].__was_initialized__) return $pyjs.loaded_modules['puremvc.patterns.proxy'];
	if(typeof $pyjs.loaded_modules['puremvc.patterns'] == 'undefined' || !$pyjs.loaded_modules['puremvc.patterns'].__was_initialized__) $p['___import___']('puremvc.patterns', null);
	var $m = puremvc['patterns']['proxy'] = $pyjs.loaded_modules["puremvc.patterns.proxy"];
	puremvc['patterns']['proxy'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.patterns.proxy';
	var __name__ = puremvc['patterns']['proxy'].__name__ = __mod_name__;
	var proxy = puremvc['patterns']['proxy'];
	var $attr1,$attr3,$attr2,$attr5,$attr4,$attr6;

	$m['puremvc'] = $p['___import___']('puremvc.interfaces', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.observer', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.facade', 'puremvc.patterns');
	$m['Proxy'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.proxy';
		$cls_definition['NAME'] = 'Proxy';
		$cls_definition['facade'] = null;
		$cls_definition['proxyName'] = null;
		$cls_definition['data'] = null;
		$method = $pyjs__bind_method2('__init__', function(proxyName, data) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
				data = arguments[2];
			}
			if (typeof proxyName == 'undefined') proxyName=arguments.callee.__args__[3][1];
			if (typeof data == 'undefined') data=arguments.callee.__args__[4][1];
			var $attr8,$attr7;
			$p['setattr'](self, 'facade', $m['puremvc']['patterns']['facade']['Facade']['getInstance']());
			if ($p['bool'](proxyName)) {
				$p['setattr'](self, 'proxyName', proxyName);
			}
			else {
				$p['setattr'](self, 'proxyName', (($attr7=($attr8=self)['NAME']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
							$p['getattr']($attr8, 'NAME'):
							self['NAME']));
			}
			if ($p['bool'](data)) {
				self['setData'](data);
			}
			return null;
		}
	, 1, [null,null,['self'],['proxyName', null],['data', null]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('getProxyName', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr9,$attr10;
			return (($attr9=($attr10=self)['proxyName']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'proxyName'):
						self['proxyName']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getProxyName'] = $method;
		$method = $pyjs__bind_method2('setData', function(data) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				data = arguments[1];
			}

			$p['setattr'](self, 'data', data);
			return null;
		}
	, 1, [null,null,['self'],['data']]);
		$cls_definition['setData'] = $method;
		$method = $pyjs__bind_method2('getData', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr11,$attr12;
			return (($attr11=($attr12=self)['data']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
						$p['getattr']($attr12, 'data'):
						self['data']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getData'] = $method;
		$method = $pyjs__bind_method2('onRegister', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

 			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['onRegister'] = $method;
		$method = $pyjs__bind_method2('onRemove', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

 			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['onRemove'] = $method;
		var $bases = new Array((($attr1=($attr2=$m['puremvc']['patterns']['observer'])['Notifier']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
				$p['getattr']($attr2, 'Notifier'):
				$m['puremvc']['patterns']['observer']['Notifier']),(($attr3=($attr4=$m['puremvc']['interfaces'])['IProxy']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
				$p['getattr']($attr4, 'IProxy'):
				$m['puremvc']['interfaces']['IProxy']),(($attr5=($attr6=$m['puremvc']['interfaces'])['INotifier']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
				$p['getattr']($attr6, 'INotifier'):
				$m['puremvc']['interfaces']['INotifier']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Proxy', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.patterns.proxy */


/* end module: puremvc.patterns.proxy */


/*
PYJS_DEPS: ['puremvc.interfaces', 'puremvc', 'puremvc.patterns.observer', 'puremvc.patterns', 'puremvc.patterns.facade']
*/
