/* start module: puremvc.patterns.mediator */
$pyjs.loaded_modules['puremvc.patterns.mediator'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.patterns.mediator'].__was_initialized__) return $pyjs.loaded_modules['puremvc.patterns.mediator'];
	if(typeof $pyjs.loaded_modules['puremvc.patterns'] == 'undefined' || !$pyjs.loaded_modules['puremvc.patterns'].__was_initialized__) $p['___import___']('puremvc.patterns', null);
	var $m = puremvc['patterns']['mediator'] = $pyjs.loaded_modules["puremvc.patterns.mediator"];
	puremvc['patterns']['mediator'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.patterns.mediator';
	var __name__ = puremvc['patterns']['mediator'].__name__ = __mod_name__;
	var mediator = puremvc['patterns']['mediator'];
	var $attr1,$attr3,$attr2,$attr5,$attr4,$attr6;

	$m['puremvc'] = $p['___import___']('puremvc.interfaces', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.observer', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.facade', 'puremvc.patterns');
	$m['Mediator'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.mediator';
		$cls_definition['NAME'] = 'Mediator';
		$cls_definition['facade'] = null;
		$cls_definition['viewComponent'] = null;
		$cls_definition['mediatorName'] = null;
		$method = $pyjs__bind_method2('__init__', function(mediatorName, viewComponent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediatorName = arguments[1];
				viewComponent = arguments[2];
			}
			if (typeof mediatorName == 'undefined') mediatorName=arguments.callee.__args__[3][1];
			if (typeof viewComponent == 'undefined') viewComponent=arguments.callee.__args__[4][1];
			var $attr7,$attr8;
			$p['setattr'](self, 'facade', $m['puremvc']['patterns']['facade']['Facade']['getInstance']());
			if ($p['bool'](mediatorName)) {
				$p['setattr'](self, 'mediatorName', mediatorName);
			}
			else {
				$p['setattr'](self, 'mediatorName', (($attr7=($attr8=self)['NAME']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
							$p['getattr']($attr8, 'NAME'):
							self['NAME']));
			}
			$p['setattr'](self, 'viewComponent', viewComponent);
			return null;
		}
	, 1, [null,null,['self'],['mediatorName', null],['viewComponent', null]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('getMediatorName', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr9,$attr10;
			return (($attr9=($attr10=self)['mediatorName']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'mediatorName'):
						self['mediatorName']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getMediatorName'] = $method;
		$method = $pyjs__bind_method2('setViewComponent', function(viewComponent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				viewComponent = arguments[1];
			}

			$p['setattr'](self, 'viewComponent', viewComponent);
			return null;
		}
	, 1, [null,null,['self'],['viewComponent']]);
		$cls_definition['setViewComponent'] = $method;
		$method = $pyjs__bind_method2('getViewComponent', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr11,$attr12;
			return (($attr11=($attr12=self)['viewComponent']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
						$p['getattr']($attr12, 'viewComponent'):
						self['viewComponent']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getViewComponent'] = $method;
		$method = $pyjs__bind_method2('listNotificationInterests', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			return $p['list']([]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['listNotificationInterests'] = $method;
		$method = $pyjs__bind_method2('handleNotification', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

 			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['handleNotification'] = $method;
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
				$m['puremvc']['patterns']['observer']['Notifier']),(($attr3=($attr4=$m['puremvc']['interfaces'])['IMediator']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
				$p['getattr']($attr4, 'IMediator'):
				$m['puremvc']['interfaces']['IMediator']),(($attr5=($attr6=$m['puremvc']['interfaces'])['INotifier']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
				$p['getattr']($attr6, 'INotifier'):
				$m['puremvc']['interfaces']['INotifier']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Mediator', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.patterns.mediator */


/* end module: puremvc.patterns.mediator */


/*
PYJS_DEPS: ['puremvc.interfaces', 'puremvc', 'puremvc.patterns.observer', 'puremvc.patterns', 'puremvc.patterns.facade']
*/
