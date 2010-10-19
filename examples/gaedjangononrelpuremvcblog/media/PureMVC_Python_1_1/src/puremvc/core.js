/* start module: puremvc.core */
$pyjs.loaded_modules['puremvc.core'] = function (__mod_name__) {
	if($pyjs.loaded_modules['puremvc.core'].__was_initialized__) return $pyjs.loaded_modules['puremvc.core'];
	if(typeof $pyjs.loaded_modules['puremvc'] == 'undefined' || !$pyjs.loaded_modules['puremvc'].__was_initialized__) $p['___import___']('puremvc', null);
	var $m = puremvc['core'] = $pyjs.loaded_modules["puremvc.core"];
	puremvc['core'].__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'puremvc.core';
	var __name__ = puremvc['core'].__name__ = __mod_name__;
	var core = puremvc['core'];
	var $attr28,$attr1,$attr2,$attr27,$attr15,$attr16;

	$m['puremvc'] = $p['___import___']('puremvc.interfaces', 'puremvc');
	$m['puremvc'] = $p['___import___']('puremvc.patterns.observer', 'puremvc');
	$m['Controller'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.core';
		$cls_definition['instance'] = null;
		$cls_definition['view'] = null;
		$cls_definition['commandMap'] = null;
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
				$p['setattr'](cls, 'instance', $pyjs_kwargs_call($p['$$super']($m['Controller'], cls), '__new__', args, kwargs, [{}, cls]));
				cls['instance']['initializeController']();
			}
			return (($attr7=($attr8=cls)['instance']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'instance'):
						cls['instance']);
		}
	, 3, ['args',['kwargs'],['cls']]);
		$cls_definition['__new__'] = $method;
		$method = $pyjs__bind_method2('getInstance', function() {

			return $m['Controller']();
		}
	, 3, [null,null]);
		$cls_definition['getInstance'] = $method;
		$method = $pyjs__bind_method2('initializeController', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'view', $m.View['getInstance']());
			$p['setattr'](self, 'commandMap', $p['dict']([]));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeController'] = $method;
		$method = $pyjs__bind_method2('executeCommand', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}
			var commandClassRef,commandInstance;
			commandClassRef = self['commandMap']['get'](note['getName'](), null);
			if ($p['bool']($p['op_eq'](commandClassRef, null))) {
				return null;
			}
			commandInstance = commandClassRef();
			commandInstance['execute'](note);
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['executeCommand'] = $method;
		$method = $pyjs__bind_method2('registerCommand', function(notificationName, commandClassRef) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				commandClassRef = arguments[2];
			}
			var $attr9,$attr11,$attr10,$attr12;
			if ($p['bool']($p['op_eq'](self['commandMap']['get'](notificationName, null), null))) {
				self['view']['registerObserver'](notificationName, $m['puremvc']['patterns']['observer']['Observer']((($attr9=($attr10=self)['executeCommand']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
							$p['getattr']($attr10, 'executeCommand'):
							self['executeCommand']), self));
			}
			(($attr11=($attr12=self)['commandMap']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
						$p['getattr']($attr12, 'commandMap'):
						self['commandMap']).__setitem__(notificationName, commandClassRef);
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['commandClassRef']]);
		$cls_definition['registerCommand'] = $method;
		$method = $pyjs__bind_method2('hasCommand', function(notificationName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
			}

			return (self['commandMap']['get'](notificationName, null) !== null);
		}
	, 1, [null,null,['self'],['notificationName']]);
		$cls_definition['hasCommand'] = $method;
		$method = $pyjs__bind_method2('removeCommand', function(notificationName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
			}
			var $attr14,$attr13;
			if ($p['bool'](self['hasCommand'](notificationName))) {
				self['view']['removeObserver'](notificationName, self);
				(($attr13=($attr14=self)['commandMap']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
							$p['getattr']($attr14, 'commandMap'):
							self['commandMap']).__delitem__(notificationName);
			}
			return null;
		}
	, 1, [null,null,['self'],['notificationName']]);
		$cls_definition['removeCommand'] = $method;
		var $bases = new Array($p['object'],(($attr1=($attr2=$m['puremvc']['interfaces'])['IController']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
				$p['getattr']($attr2, 'IController'):
				$m['puremvc']['interfaces']['IController']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Controller', $p['tuple']($bases), $data);
	})();
	$m['Model'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.core';
		$cls_definition['instance'] = null;
		$cls_definition['proxyMap'] = null;
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
			var $or4,$or3,$attr20,$attr21,$attr22,$attr19,$attr18,$attr17;
			if ($p['bool'](($p['bool']($or3=!$p['bool']((($attr17=($attr18=cls)['instance']) == null || (($attr18.__is_instance__) && typeof $attr17 == 'function') || (typeof $attr17['__get__'] == 'function')?
						$p['getattr']($attr18, 'instance'):
						cls['instance'])))?$or3:!$p['bool']($p['isinstance']((($attr19=($attr20=cls)['instance']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
						$p['getattr']($attr20, 'instance'):
						cls['instance']), cls))))) {
				$p['setattr'](cls, 'instance', $pyjs_kwargs_call($p['$$super']($m['Model'], cls), '__new__', args, kwargs, [{}, cls]));
				cls['instance']['initializeModel']();
			}
			return (($attr21=($attr22=cls)['instance']) == null || (($attr22.__is_instance__) && typeof $attr21 == 'function') || (typeof $attr21['__get__'] == 'function')?
						$p['getattr']($attr22, 'instance'):
						cls['instance']);
		}
	, 3, ['args',['kwargs'],['cls']]);
		$cls_definition['__new__'] = $method;
		$method = $pyjs__bind_method2('getInstance', function() {

			return $m['Model']();
		}
	, 3, [null,null]);
		$cls_definition['getInstance'] = $method;
		$method = $pyjs__bind_method2('initializeModel', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'proxyMap', $p['dict']([]));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeModel'] = $method;
		$method = $pyjs__bind_method2('registerProxy', function(proxy) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxy = arguments[1];
			}
			var $attr23,$attr24;
			(($attr23=($attr24=self)['proxyMap']) == null || (($attr24.__is_instance__) && typeof $attr23 == 'function') || (typeof $attr23['__get__'] == 'function')?
						$p['getattr']($attr24, 'proxyMap'):
						self['proxyMap']).__setitem__(proxy['getProxyName'](), proxy);
			proxy['onRegister']();
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

			return self['proxyMap']['get'](proxyName, null);
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['retrieveProxy'] = $method;
		$method = $pyjs__bind_method2('hasProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}

			return (self['proxyMap']['get'](proxyName, null) !== null);
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['hasProxy'] = $method;
		$method = $pyjs__bind_method2('removeProxy', function(proxyName) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				proxyName = arguments[1];
			}
			var proxy,$attr26,$attr25;
			proxy = self['proxyMap']['get'](proxyName, null);
			if ($p['bool'](proxy)) {
				(($attr25=($attr26=self)['proxyMap']) == null || (($attr26.__is_instance__) && typeof $attr25 == 'function') || (typeof $attr25['__get__'] == 'function')?
							$p['getattr']($attr26, 'proxyMap'):
							self['proxyMap']).__delitem__(proxyName);
				proxy['onRemove']();
			}
			return proxy;
		}
	, 1, [null,null,['self'],['proxyName']]);
		$cls_definition['removeProxy'] = $method;
		var $bases = new Array($p['object'],(($attr15=($attr16=$m['puremvc']['interfaces'])['IModel']) == null || (($attr16.__is_instance__) && typeof $attr15 == 'function') || (typeof $attr15['__get__'] == 'function')?
				$p['getattr']($attr16, 'IModel'):
				$m['puremvc']['interfaces']['IModel']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('Model', $p['tuple']($bases), $data);
	})();
	$m['View'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'puremvc.core';
		$cls_definition['instance'] = null;
		$cls_definition['observerMap'] = null;
		$cls_definition['mediatorMap'] = null;
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
			var $or5,$or6,$attr33,$attr32,$attr31,$attr30,$attr34,$attr29;
			if ($p['bool'](($p['bool']($or5=!$p['bool']((($attr29=($attr30=cls)['instance']) == null || (($attr30.__is_instance__) && typeof $attr29 == 'function') || (typeof $attr29['__get__'] == 'function')?
						$p['getattr']($attr30, 'instance'):
						cls['instance'])))?$or5:!$p['bool']($p['isinstance']((($attr31=($attr32=cls)['instance']) == null || (($attr32.__is_instance__) && typeof $attr31 == 'function') || (typeof $attr31['__get__'] == 'function')?
						$p['getattr']($attr32, 'instance'):
						cls['instance']), cls))))) {
				$p['setattr'](cls, 'instance', $pyjs_kwargs_call($p['$$super']($m['View'], cls), '__new__', args, kwargs, [{}, cls]));
				cls['instance']['initializeView']();
			}
			return (($attr33=($attr34=cls)['instance']) == null || (($attr34.__is_instance__) && typeof $attr33 == 'function') || (typeof $attr33['__get__'] == 'function')?
						$p['getattr']($attr34, 'instance'):
						cls['instance']);
		}
	, 3, ['args',['kwargs'],['cls']]);
		$cls_definition['__new__'] = $method;
		$method = $pyjs__bind_method2('getInstance', function() {

			return $m['View']();
		}
	, 3, [null,null]);
		$cls_definition['getInstance'] = $method;
		$method = $pyjs__bind_method2('initializeView', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'observerMap', $p['dict']([]));
			$p['setattr'](self, 'mediatorMap', $p['dict']([]));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['initializeView'] = $method;
		$method = $pyjs__bind_method2('registerObserver', function(notificationName, observer) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				observer = arguments[2];
			}
			var $attr37,$attr36,$attr35,$attr38;
			if ($p['bool']($p['op_eq'](self['observerMap']['get'](notificationName, null), null))) {
				(($attr35=($attr36=self)['observerMap']) == null || (($attr36.__is_instance__) && typeof $attr35 == 'function') || (typeof $attr35['__get__'] == 'function')?
							$p['getattr']($attr36, 'observerMap'):
							self['observerMap']).__setitem__(notificationName, $p['list']([]));
			}
			(($attr37=($attr38=self)['observerMap']) == null || (($attr38.__is_instance__) && typeof $attr37 == 'function') || (typeof $attr37['__get__'] == 'function')?
						$p['getattr']($attr38, 'observerMap'):
						self['observerMap']).__getitem__(notificationName)['append'](observer);
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
			var $iter1_nextval,$iter1_type,i,$iter1_iter,observers,obsvr,$iter1_array,$attr40,$attr39,$iter1_idx;
			if ($p['bool']((self['observerMap']['get'](notification['getName'](), null) !== null))) {
				observers = (($attr39=($attr40=self)['observerMap']) == null || (($attr40.__is_instance__) && typeof $attr39 == 'function') || (typeof $attr39['__get__'] == 'function')?
							$p['getattr']($attr40, 'observerMap'):
							self['observerMap']).__getitem__(notification['getName']());
				$iter1_iter = $p['range'](0, $p['len'](observers));
				$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
				while (typeof($p['__wrapped_next']($iter1_nextval).$nextval) != 'undefined') {
					i = $iter1_nextval.$nextval;
					obsvr = observers.__getitem__(i);
					obsvr['notifyObserver'](notification);
				}
			}
			return null;
		}
	, 1, [null,null,['self'],['notification']]);
		$cls_definition['notifyObservers'] = $method;
		$method = $pyjs__bind_method2('removeObserver', function(notificationName, notifyContext) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				notificationName = arguments[1];
				notifyContext = arguments[2];
			}
			var $iter2_nextval,$iter2_type,$iter2_iter,i,$attr44,observers,$iter2_idx,$attr42,$attr43,$attr41,$iter2_array;
			observers = (($attr41=($attr42=self)['observerMap']) == null || (($attr42.__is_instance__) && typeof $attr41 == 'function') || (typeof $attr41['__get__'] == 'function')?
						$p['getattr']($attr42, 'observerMap'):
						self['observerMap']).__getitem__(notificationName);
			$iter2_iter = $p['range']($p['len'](observers));
			$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
			while (typeof($p['__wrapped_next']($iter2_nextval).$nextval) != 'undefined') {
				i = $iter2_nextval.$nextval;
				if ($p['bool'](observers.__getitem__(i)['compareNotifyContext'](notifyContext))) {
					observers['pop'](i);
					break;
				}
			}
			if ($p['bool']($p['op_eq']($p['len'](observers), 0))) {
				(($attr43=($attr44=self)['observerMap']) == null || (($attr44.__is_instance__) && typeof $attr43 == 'function') || (typeof $attr43['__get__'] == 'function')?
							$p['getattr']($attr44, 'observerMap'):
							self['observerMap']).__delitem__(notificationName);
			}
			return null;
		}
	, 1, [null,null,['self'],['notificationName'],['notifyContext']]);
		$cls_definition['removeObserver'] = $method;
		$method = $pyjs__bind_method2('registerMediator', function(mediator) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				mediator = arguments[1];
			}
			var interests,$iter3_idx,i,$iter3_array,$attr46,$attr47,$attr45,$iter3_iter,$iter3_type,obsvr,$iter3_nextval,$attr48;
			if ($p['bool'](self['mediatorMap']['keys']().__contains__(mediator['getMediatorName']()))) {
				return null;
			}
			(($attr45=($attr46=self)['mediatorMap']) == null || (($attr46.__is_instance__) && typeof $attr45 == 'function') || (typeof $attr45['__get__'] == 'function')?
						$p['getattr']($attr46, 'mediatorMap'):
						self['mediatorMap']).__setitem__(mediator['getMediatorName'](), mediator);
			interests = mediator['listNotificationInterests']();
			if ($p['bool'](($p['cmp']($p['len'](interests), 0) == 1))) {
				obsvr = $m['puremvc']['patterns']['observer']['Observer']((($attr47=($attr48=mediator)['handleNotification']) == null || (($attr48.__is_instance__) && typeof $attr47 == 'function') || (typeof $attr47['__get__'] == 'function')?
							$p['getattr']($attr48, 'handleNotification'):
							mediator['handleNotification']), mediator);
				$iter3_iter = $p['range'](0, $p['len'](interests));
				$iter3_nextval=$p['__iter_prepare']($iter3_iter,false);
				while (typeof($p['__wrapped_next']($iter3_nextval).$nextval) != 'undefined') {
					i = $iter3_nextval.$nextval;
					self['registerObserver'](interests.__getitem__(i), obsvr);
				}
			}
			mediator['onRegister']();
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

			return self['mediatorMap']['get'](mediatorName, null);
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
			var $iter5_nextval,mediator,$iter6_type,$iter5_idx,$iter5_iter,$iter4_type,$iter5_type,$iter6_iter,$iter4_iter,$attr49,$iter5_array,$iter6_nextval,removalTargets,interests,$iter6_idx,observers,$iter6_array,$attr58,target,$attr51,$iter4_nextval,$attr53,$attr52,$attr55,$attr54,$attr57,$attr56,$iter4_idx,i,notificationName,$attr50,$iter4_array;
			$iter4_iter = self['observerMap']['keys']();
			$iter4_nextval=$p['__iter_prepare']($iter4_iter,false);
			while (typeof($p['__wrapped_next']($iter4_nextval).$nextval) != 'undefined') {
				notificationName = $iter4_nextval.$nextval;
				observers = (($attr49=($attr50=self)['observerMap']) == null || (($attr50.__is_instance__) && typeof $attr49 == 'function') || (typeof $attr49['__get__'] == 'function')?
							$p['getattr']($attr50, 'observerMap'):
							self['observerMap']).__getitem__(notificationName);
				removalTargets = $p['list']([]);
				$iter5_iter = $p['range'](0, $p['len'](observers));
				$iter5_nextval=$p['__iter_prepare']($iter5_iter,false);
				while (typeof($p['__wrapped_next']($iter5_nextval).$nextval) != 'undefined') {
					i = $iter5_nextval.$nextval;
					if ($p['bool']($p['op_eq'](observers.__getitem__(i)['compareNotifyContext'](self['retrieveMediator'](mediatorName)), true))) {
						removalTargets['append'](i);
					}
				}
				target = 0;
				while ($p['bool'](($p['cmp']($p['len'](removalTargets), 0) == 1))) {
					target = removalTargets['pop']();
					observers.__delitem__(target);
				}
				if ($p['bool']($p['op_eq']($p['len'](observers), 0))) {
					(($attr51=($attr52=self)['observerMap']) == null || (($attr52.__is_instance__) && typeof $attr51 == 'function') || (typeof $attr51['__get__'] == 'function')?
								$p['getattr']($attr52, 'observerMap'):
								self['observerMap']).__delitem__(notificationName);
				}
				else {
					(($attr53=($attr54=self)['observerMap']) == null || (($attr54.__is_instance__) && typeof $attr53 == 'function') || (typeof $attr53['__get__'] == 'function')?
								$p['getattr']($attr54, 'observerMap'):
								self['observerMap']).__setitem__(notificationName, observers);
				}
			}
			mediator = self['mediatorMap']['get'](mediatorName, null);
			if ($p['bool']((mediator !== null))) {
				(($attr55=($attr56=self)['mediatorMap']) == null || (($attr56.__is_instance__) && typeof $attr55 == 'function') || (typeof $attr55['__get__'] == 'function')?
							$p['getattr']($attr56, 'mediatorMap'):
							self['mediatorMap']).__delitem__(mediatorName);
				mediator['onRemove']();
			}
			return mediator;
			mediator = self['mediatorMap']['get'](mediatorName, null);
			if ($p['bool'](mediator)) {
				interests = mediator['listNotificationInterests']();
				$iter6_iter = $p['range']($p['len'](interests));
				$iter6_nextval=$p['__iter_prepare']($iter6_iter,false);
				while (typeof($p['__wrapped_next']($iter6_nextval).$nextval) != 'undefined') {
					i = $iter6_nextval.$nextval;
					$m.removeObserver(interests.__getitem__(i), mediator);
				}
				(($attr57=($attr58=self)['mediatorMap']) == null || (($attr58.__is_instance__) && typeof $attr57 == 'function') || (typeof $attr57['__get__'] == 'function')?
							$p['getattr']($attr58, 'mediatorMap'):
							self['mediatorMap']).__delitem__(mediatorName);
				mediator['onRemove']();
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

			return (self['mediatorMap']['get'](mediatorName, null) !== null);
		}
	, 1, [null,null,['self'],['mediatorName']]);
		$cls_definition['hasMediator'] = $method;
		var $bases = new Array($p['object'],(($attr27=($attr28=$m['puremvc']['interfaces'])['IView']) == null || (($attr28.__is_instance__) && typeof $attr27 == 'function') || (typeof $attr27['__get__'] == 'function')?
				$p['getattr']($attr28, 'IView'):
				$m['puremvc']['interfaces']['IView']));
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('View', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end puremvc.core */


/* end module: puremvc.core */


/*
PYJS_DEPS: ['puremvc.interfaces', 'puremvc', 'puremvc.patterns.observer', 'puremvc.patterns']
*/
