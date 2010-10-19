/* start module: puremvc.patterns.facade */
$pyjs.loaded_modules['puremvc.patterns.facade'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.patterns.facade'].__was_initialized__) return $pyjs.loaded_modules['puremvc.patterns.facade'];
	if(typeof $pyjs.loaded_modules['puremvc.patterns'] == 'undefined' || !$pyjs.loaded_modules['puremvc.patterns'].__was_initialized__) $p['___import___']('puremvc.patterns', null);
	var $m = puremvc['patterns']['facade'] = $pyjs.loaded_modules["puremvc.patterns.facade"];
	puremvc['patterns']['facade'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.patterns.facade';
	var __name__ = puremvc['patterns']['facade'].__name__ = __mod_name__;
	var facade = puremvc['patterns']['facade'];
	var $attr1,$attr2;

	$m['puremvc'] = $p['___import___']('puremvc.core', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.interfaces', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.observer', 'puremvc.patterns');
	$m['Facade'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.facade';
		$cls_definition['instance'] = null;
		$cls_definition['controller'] = null;
		$cls_definition['model'] = null;
		$cls_definition['view'] = null;
		$method = $pyjs__bind_method2('__new__', function(cls) {
			var args = $p['tuple']($pyjs_array_slice.call(arguments,1,arguments.length-1));

			var kwargs = arguments.length >= 2 ? arguments[arguments.length-1] : arguments[arguments.length];
			if (typeof kwargs != 'object' || kwargs.__name__ != 'dict' || typeof kwargs.$pyjs_is_kwarg == 'undefined') {
				if (typeof kwargs != 'undefined') args.__array.push(kwargs);
				kwargs = arguments[arguments.length+1];
			} else {
				delete kwargs['$pyjs_is_kwarg'];
			}
			if (typeof kwargs == 'undefined') {
				kwargs = $p['__empty_dict']();
				if (typeof cls != 'undefined') {
					if (cls !== null && typeof cls['$pyjs_is_kwarg'] != 'undefined') {
						kwargs = cls;
						cls = arguments[1];
					}
				} else {
				}
			}
			var $attr8,$or1,$or2,$attr3,$attr5,$attr4,$attr7,$attr6;
			if ($p['bool'](($p['bool']($or1=!$p['bool']((($attr3=($attr4=cls)['instance']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'instance'):
						cls['instance'])))?$or1:!$p['bool']($p['isinstance']((($attr5=($attr6=cls)['instance']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'instance'):
						cls['instance']), cls))))) {
				$p['setattr'](cls, 'instance', $pyjs_kwargs_call($p['$$super']($m['Facade'], cls), '__new__', args, kwargs, [{}, cls]));
				cls['instance']['initializeFacade']();
			}
			return (($attr7=($attr8=cls)['instance']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'instance'):
						cls['instance']);
		}
	, 3, ['args',['kwargs'],['cls']]);
		$cls_definition['__new__'] = $method;
		$method = $pyjs__bind_method2('getInstance', function() {

			return $m['Facade']();
		}
	, 3, [null,null]);
		$cls_definition['getInstance'] = $method;
		$method = $pyjs__bind_method2('initializeFacade', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['initializeController']();
			self['initializeModel']();
			self['initializeView']();
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
			var $attr9,$attr10;
			if ($p['bool'](((($attr9=($attr10=self)['controller']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'controller'):
						self['controller']) !== null))) {
				return null;
			}
			$p['setattr'](self, 'controller', $m['puremvc']['core']['Controller']['getInstance']());
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeController'] = $method;
		$method = $pyjs__bind_method2('initializeModel', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr11,$attr12;
			if ($p['bool'](((($attr11=($attr12=self)['model']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
						$p['getattr']($attr12, 'model'):
						self['model']) !== null))) {
				return null;
			}
			$p['setattr'](self, 'model', $m['puremvc']['core']['Model']['getInstance']());
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeModel'] = $method;
		$method = $pyjs__bind_method2('initializeView', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr14,$attr13;
			if ($p['bool'](((($attr13=($attr14=self)['view']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
						$p['getattr']($attr14, 'view'):
						self['view']) !== null))) {
				return null;
			}
			$p['setattr'](self, 'view', $m['puremvc']['core']['View']['getInstance']());
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeView'] = $method;
		$method = $pyjs__bind_method2('registerCommand', function(notificationName, commandClassRef) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				commandClassRef = arguments[2];
			}

			self['controller']['registerCommand'](notificationName, commandClassRef);
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['commandClassRef']]);
		$cls_definition['registerCommand'] = $method;
		$method = $pyjs__bind_method2('removeCommand', function(notificationName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
			}

			self['controller']['removeCommand'](notificationName);
			return null;
		}
	, 1, [null,null,['self'],['notificationName']]);
		$cls_definition['removeCommand'] = $method;
		$method = $pyjs__bind_method2('hasCommand', function(notificationName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
			}

			return self['controller']['hasCommand'](notificationName);
		}
	, 1, [null,null,['self'],['notificationName']]);
		$cls_definition['hasCommand'] = $method;
		$method = $pyjs__bind_method2('registerProxy', function(proxy) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxy = arguments[1];
			}

			self['model']['registerProxy'](proxy);
			return null;
		}
	, 1, [null,null,['self'],['proxy']]);
		$cls_definition['registerProxy'] = $method;
		$method = $pyjs__bind_method2('retrieveProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}

			return self['model']['retrieveProxy'](proxyName);
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['retrieveProxy'] = $method;
		$method = $pyjs__bind_method2('removeProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}
			var $attr15,$attr16,proxy;
			proxy = null;
			if ($p['bool'](((($attr15=($attr16=self)['model']) == null || (($attr16.__is_instance__) && typeof $attr15 == 'function') || (typeof $attr15['__get__'] == 'function')?
						$p['getattr']($attr16, 'model'):
						self['model']) !== null))) {
				proxy = self['model']['removeProxy'](proxyName);
			}
			return proxy;
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['removeProxy'] = $method;
		$method = $pyjs__bind_method2('hasProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}

			return self['model']['hasProxy'](proxyName);
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['hasProxy'] = $method;
		$method = $pyjs__bind_method2('registerMediator', function(mediator) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediator = arguments[1];
			}
			var $attr18,$attr17;
			if ($p['bool'](((($attr17=($attr18=self)['view']) == null || (($attr18.__is_instance__) && typeof $attr17 == 'function') || (typeof $attr17['__get__'] == 'function')?
						$p['getattr']($attr18, 'view'):
						self['view']) !== null))) {
				self['view']['registerMediator'](mediator);
			}
			return null;
		}
	, 1, [null,null,['self'],['mediator']]);
		$cls_definition['registerMediator'] = $method;
		$method = $pyjs__bind_method2('retrieveMediator', function(mediatorName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediatorName = arguments[1];
			}

			return self['view']['retrieveMediator'](mediatorName);
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['retrieveMediator'] = $method;
		$method = $pyjs__bind_method2('removeMediator', function(mediatorName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediatorName = arguments[1];
			}
			var $attr20,$attr19,mediator;
			mediator = null;
			if ($p['bool'](((($attr19=($attr20=self)['view']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
						$p['getattr']($attr20, 'view'):
						self['view']) !== null))) {
				mediator = self['view']['removeMediator'](mediatorName);
			}
			return mediator;
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['removeMediator'] = $method;
		$method = $pyjs__bind_method2('hasMediator', function(mediatorName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediatorName = arguments[1];
			}

			return self['view']['hasMediator'](mediatorName);
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['hasMediator'] = $method;
		$method = $pyjs__bind_method2('sendNotification', function(notificationName, body, type) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				body = arguments[2];
				type = arguments[3];
			}
			if (typeof body == 'undefined') body=arguments.callee.__args__[4][1];
			if (typeof type == 'undefined') type=arguments.callee.__args__[5][1];

			self['notifyObservers']($m['puremvc']['patterns']['observer']['Notification'](notificationName, body, type));
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['body', null],['type', null]]);
		$cls_definition['sendNotification'] = $method;
		$method = $pyjs__bind_method2('notifyObservers', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}
			var $attr22,$attr21;
			if ($p['bool'](((($attr21=($attr22=self)['view']) == null || (($attr22.__is_instance__) && typeof $attr21 == 'function') || (typeof $attr21['__get__'] == 'function')?
						$p['getattr']($attr22, 'view'):
						self['view']) !== null))) {
				self['view']['notifyObservers'](notification);
			}
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['notifyObservers'] = $method;
		var $bases = new Array($p['object'],(($attr1=($attr2=$m['puremvc']['interfaces'])['IFacade']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
				$p['getattr']($attr2, 'IFacade'):
				$m['puremvc']['interfaces']['IFacade']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Facade', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.patterns.facade */


/* end module: puremvc.patterns.facade */


/*
PYJS_DEPS: ['puremvc.core', 'puremvc', 'puremvc.interfaces', 'puremvc.patterns.observer', 'puremvc.patterns']
*/
