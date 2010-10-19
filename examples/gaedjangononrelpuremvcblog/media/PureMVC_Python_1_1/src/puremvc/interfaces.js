/* start module: puremvc.interfaces */
$pyjs.loaded_modules['puremvc.interfaces'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.interfaces'].__was_initialized__) return $pyjs.loaded_modules['puremvc.interfaces'];
	if(typeof $pyjs.loaded_modules['puremvc'] == 'undefined' || !$pyjs.loaded_modules['puremvc'].__was_initialized__) $p['___import___']('puremvc', null);
	var $m = puremvc['interfaces'] = $pyjs.loaded_modules["puremvc.interfaces"];
	puremvc['interfaces'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.interfaces';
	var __name__ = puremvc['interfaces'].__name__ = __mod_name__;
	var interfaces = puremvc['interfaces'];


	$m['ICommand'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('execute', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['execute'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('ICommand', $p['tuple']($bases), $data);
	})();
	$m['IController'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('registerCommand', function(notificationName, commandClassRef) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				commandClassRef = arguments[2];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['commandClassRef']]);
		$cls_definition['registerCommand'] = $method;
		$method = $pyjs__bind_method2('executeCommand', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['executeCommand'] = $method;
		$method = $pyjs__bind_method2('removeCommand', function(notificationName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
			}

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notificationName']]);
		$cls_definition['hasCommand'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IController', $p['tuple']($bases), $data);
	})();
	$m['IFacade'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('notifyObservers', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['notifyObservers'] = $method;
		$method = $pyjs__bind_method2('registerProxy', function(proxy) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxy = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['proxy']]);
		$cls_definition['registerProxy'] = $method;
		$method = $pyjs__bind_method2('retreieveProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['retreieveProxy'] = $method;
		$method = $pyjs__bind_method2('removeProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['hasProxy'] = $method;
		$method = $pyjs__bind_method2('registerCommand', function(noteName, commandClassRef) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				noteName = arguments[1];
				commandClassRef = arguments[2];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['noteName'],['commandClassRef']]);
		$cls_definition['registerCommand'] = $method;
		$method = $pyjs__bind_method2('removeCommand', function(notificationName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
			}

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notificationName']]);
		$cls_definition['hasCommand'] = $method;
		$method = $pyjs__bind_method2('registerMediator', function(mediator) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediator = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['mediator']]);
		$cls_definition['registerMediator'] = $method;
		$method = $pyjs__bind_method2('retreieveMediator', function(mediatorName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediatorName = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['retreieveMediator'] = $method;
		$method = $pyjs__bind_method2('removeMediator', function(mediatorName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediatorName = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['removeMediator'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IFacade', $p['tuple']($bases), $data);
	})();
	$m['IMediator'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('getMediatorName', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['getMediatorName'] = $method;
		$method = $pyjs__bind_method2('getViewComponent', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['getViewComponent'] = $method;
		$method = $pyjs__bind_method2('setViewComponent', function(viewComponent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				viewComponent = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['viewComponent']]);
		$cls_definition['setViewComponent'] = $method;
		$method = $pyjs__bind_method2('listNotificationInterests', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['onRemove'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IMediator', $p['tuple']($bases), $data);
	})();
	$m['IModel'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('registerProxy', function(proxy) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxy = arguments[1];
			}

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['hasProxy'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IModel', $p['tuple']($bases), $data);
	})();
	$m['INotification'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('getName', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['str'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('INotification', $p['tuple']($bases), $data);
	})();
	$m['INotifier'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['body', null],['type', null]]);
		$cls_definition['sendNotification'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('INotifier', $p['tuple']($bases), $data);
	})();
	$m['IObserver'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('setNotifyMethod', function(notifyMethod) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notifyMethod = arguments[1];
			}

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notifyContext']]);
		$cls_definition['setNotifyContext'] = $method;
		$method = $pyjs__bind_method2('notifyObserver', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['notifyObserver'] = $method;
		$method = $pyjs__bind_method2('compareNotifyContext', function(object) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				object = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['object']]);
		$cls_definition['compareNotifyContext'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IObserver', $p['tuple']($bases), $data);
	})();
	$m['IProxy'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('getProxyName', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['getProxyName'] = $method;
		$method = $pyjs__bind_method2('setData', function() {
			if (this.__is_instance__ === true) {
				var data = this;
			} else {
				var data = arguments[0];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['data']]);
		$cls_definition['setData'] = $method;
		$method = $pyjs__bind_method2('getData', function() {
			if (this.__is_instance__ === true) {
			} else {
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null]);
		$cls_definition['getData'] = $method;
		$method = $pyjs__bind_method2('onRegister', function() {
			if (this.__is_instance__ === true) {
			} else {
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null]);
		$cls_definition['onRegister'] = $method;
		$method = $pyjs__bind_method2('onRemove', function() {
			if (this.__is_instance__ === true) {
			} else {
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null]);
		$cls_definition['onRemove'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IProxy', $p['tuple']($bases), $data);
	})();
	$m['IView'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.interfaces';
		$method = $pyjs__bind_method2('registerObserver', function(notificationName, observer) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				observer = arguments[2];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['observer']]);
		$cls_definition['registerObserver'] = $method;
		$method = $pyjs__bind_method2('notifyObservers', function(notification) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notification = arguments[1];
			}

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['notifyObservers'] = $method;
		$method = $pyjs__bind_method2('registerMediator', function(mediator) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediator = arguments[1];
			}

			throw ($p['NotImplemented']);
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

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
			return null;
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

			throw ($p['NotImplemented']);
			return null;
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['hasMediator'] = $method;
		var $bases = new Array(pyjslib.object);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('IView', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.interfaces */


/* end module: puremvc.interfaces */


