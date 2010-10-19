/* start module: puremvc.patterns.observer */
$pyjs.loaded_modules['puremvc.patterns.observer'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.patterns.observer'].__was_initialized__) return $pyjs.loaded_modules['puremvc.patterns.observer'];
	if(typeof $pyjs.loaded_modules['puremvc.patterns'] == 'undefined' || !$pyjs.loaded_modules['puremvc.patterns'].__was_initialized__) $p['___import___']('puremvc.patterns', null);
	var $m = puremvc['patterns']['observer'] = $pyjs.loaded_modules["puremvc.patterns.observer"];
	puremvc['patterns']['observer'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.patterns.observer';
	var __name__ = puremvc['patterns']['observer'].__name__ = __mod_name__;
	var observer = puremvc['patterns']['observer'];
	var $attr9,$attr1,$attr11,$attr2,$attr10,$attr12;

	$m['puremvc'] = $p['___import___']('puremvc.interfaces', 'puremvc.patterns');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.facade', 'puremvc.patterns');
	$m['Observer'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.observer';
		$cls_definition['notify'] = null;
		$cls_definition['context'] = null;
		$method = $pyjs__bind_method2('__init__', function(notifyMethod, notifyContext) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notifyMethod = arguments[1];
				notifyContext = arguments[2];
			}

			self['setNotifyMethod'](notifyMethod);
			self['setNotifyContext'](notifyContext);
			return null;
		}
	, 1, [null,null,['self'],['notifyMethod'],['notifyContext']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('setNotifyMethod', function(notifyMethod) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notifyMethod = arguments[1];
			}

			$p['setattr'](self, 'notify', notifyMethod);
			return null;
		}
	, 1, [null,null,['self'],['notifyMethod']]);
		$cls_definition['setNotifyMethod'] = $method;
		$method = $pyjs__bind_method2('setNotifyContext', function(notifyContext) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notifyContext = arguments[1];
			}

			$p['setattr'](self, 'context', notifyContext);
			return null;
		}
	, 1, [null,null,['self'],['notifyContext']]);
		$cls_definition['setNotifyContext'] = $method;
		$method = $pyjs__bind_method2('getNotifyMethod', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr3,$attr4;
			return (($attr3=($attr4=self)['notify']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'notify'):
						self['notify']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getNotifyMethod'] = $method;
		$method = $pyjs__bind_method2('getNotifyContext', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr5,$attr6;
			return (($attr5=($attr6=self)['context']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'context'):
						self['context']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getNotifyContext'] = $method;
		$method = $pyjs__bind_method2('notifyObserver', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

			self['getNotifyMethod']()(notification);
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['notifyObserver'] = $method;
		$method = $pyjs__bind_method2('compareNotifyContext', function(obj) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				obj = arguments[1];
			}
			var $attr8,$attr7;
			return (obj === (($attr7=($attr8=self)['context']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'context'):
						self['context']));
		}
	, 1, [null,null,['self'],['obj']]);
		$cls_definition['compareNotifyContext'] = $method;
		var $bases = new Array($p['object'],(($attr1=($attr2=$m['puremvc']['interfaces'])['IObserver']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
				$p['getattr']($attr2, 'IObserver'):
				$m['puremvc']['interfaces']['IObserver']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Observer', $p['tuple']($bases), $data);
	})();
	$m['Notifier'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.observer';
		$cls_definition['facade'] = null;
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'facade', $m['puremvc']['patterns']['facade']['Facade']['getInstance']());
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
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

			self['facade']['sendNotification'](notificationName, body, type);
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['body', null],['type', null]]);
		$cls_definition['sendNotification'] = $method;
		var $bases = new Array($p['object'],(($attr9=($attr10=$m['puremvc']['interfaces'])['INotifier']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
				$p['getattr']($attr10, 'INotifier'):
				$m['puremvc']['interfaces']['INotifier']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Notifier', $p['tuple']($bases), $data);
	})();
	$m['Notification'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.patterns.observer';
		$cls_definition['$$name'] = null;
		$cls_definition['body'] = null;
		$cls_definition['type'] = null;
		$method = $pyjs__bind_method2('__init__', function(name, body, type) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				name = arguments[1];
				body = arguments[2];
				type = arguments[3];
			}
			if (typeof body == 'undefined') body=arguments.callee.__args__[4][1];
			if (typeof type == 'undefined') type=arguments.callee.__args__[5][1];

			$p['setattr'](self, '$$name', name);
			$p['setattr'](self, 'body', body);
			$p['setattr'](self, 'type', type);
			return null;
		}
	, 1, [null,null,['self'],['name'],['body', null],['type', null]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('getName', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr14,$attr13;
			return (($attr13=($attr14=self)['$$name']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
						$p['getattr']($attr14, '$$name'):
						self['$$name']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getName'] = $method;
		$method = $pyjs__bind_method2('setBody', function(body) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				body = arguments[1];
			}

			$p['setattr'](self, 'body', body);
			return null;
		}
	, 1, [null,null,['self'],['body']]);
		$cls_definition['setBody'] = $method;
		$method = $pyjs__bind_method2('getBody', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr15,$attr16;
			return (($attr15=($attr16=self)['body']) == null || (($attr16.__is_instance__) && typeof $attr15 == 'function') || (typeof $attr15['__get__'] == 'function')?
						$p['getattr']($attr16, 'body'):
						self['body']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['getBody'] = $method;
		$method = $pyjs__bind_method2('setType', function(type) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				type = arguments[1];
			}

			$p['setattr'](self, 'type', type);
			return null;
		}
	, 1, [null,null,['self'],['type']]);
		$cls_definition['setType'] = $method;
		$method = $pyjs__bind_method2('getType', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr17,$attr18;
			return (($attr17=($attr18=self)['type']) == null || (($attr18.__is_instance__) && typeof $attr17 == 'function') || (typeof $attr17['__get__'] == 'function')?
						$p['getattr']($attr18, 'type'):
						self['type']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['getType'] = $method;
		$method = $pyjs__bind_method2('str', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr20,$attr21,$attr22,$attr23,$attr24,$attr25,$attr26,ty,msg,bd,$attr19,$add2,$add3,$add1,$add6,$add7,$add4,$add5,$add10,$add8,$add9;
			msg = $p['__op_add']($add1='Notification Name: ',$add2=self['getName']());
			bd = 'None';
			if ($p['bool'](((($attr19=($attr20=self)['body']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
						$p['getattr']($attr20, 'body'):
						self['body']) !== null))) {
				bd = $p['str']((($attr21=($attr22=self)['body']) == null || (($attr22.__is_instance__) && typeof $attr21 == 'function') || (typeof $attr21['__get__'] == 'function')?
							$p['getattr']($attr22, 'body'):
							self['body']));
			}
			ty = 'None';
			if ($p['bool'](((($attr23=($attr24=self)['type']) == null || (($attr24.__is_instance__) && typeof $attr23 == 'function') || (typeof $attr23['__get__'] == 'function')?
						$p['getattr']($attr24, 'type'):
						self['type']) !== null))) {
				ty = (($attr25=($attr26=self)['type']) == null || (($attr26.__is_instance__) && typeof $attr25 == 'function') || (typeof $attr25['__get__'] == 'function')?
							$p['getattr']($attr26, 'type'):
							self['type']);
			}
			msg = $p['__op_add']($add5=msg,$add6=$p['__op_add']($add3='\x0ABody:',$add4=bd));
			msg = $p['__op_add']($add9=msg,$add10=$p['__op_add']($add7='\x0AType:',$add8=ty));
			return msg;
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['str'] = $method;
		var $bases = new Array($p['object'],(($attr11=($attr12=$m['puremvc']['interfaces'])['INotification']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
				$p['getattr']($attr12, 'INotification'):
				$m['puremvc']['interfaces']['INotification']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Notification', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.patterns.observer */


/* end module: puremvc.patterns.observer */


/*
PYJS_DEPS: ['puremvc.interfaces', 'puremvc', 'puremvc.patterns.facade', 'puremvc.patterns']
*/
