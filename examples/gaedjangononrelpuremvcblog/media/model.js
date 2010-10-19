/* start module: model */
var model;
$pyjs.loaded_modules['model'] = function (__mod_name__) {
	if($pyjs.loaded_modules['model'].__was_initialized__) return $pyjs.loaded_modules['model'];
	var $m = model = $pyjs.loaded_modules["model"];
	model.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'model';
	var __name__ = model.__name__ = __mod_name__;


	$m['JSONProxy'] = $p['___import___']('pyjamas.JSONService.JSONProxy', null, null, false);
	$m['Proxy'] = $p['___import___']('puremvc.patterns.proxy.Proxy', null, null, false);
	$m['vo'] = $p['___import___']('vo', null);
	$m['Blog'] = $p['___import___']('Blog', null);
	$m['PostRemoteProxy'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'model';
		$cls_definition['NAME'] = 'PostRemoteProxy';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr1,$attr2;
			$p['$$super']($m['PostRemoteProxy'], self)['__init__']((($attr1=($attr2=$m['PostRemoteProxy'])['NAME']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
						$p['getattr']($attr2, 'NAME'):
						$m['PostRemoteProxy']['NAME']), $p['list']([]));
			$p['setattr'](self, 'data', $p['list']([]));
			$p['setattr'](self, 'remote', $m.DataService());
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('get_posts', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr3,$attr4;
			return (($attr3=($attr4=self)['data']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'data'):
						self['data']);
		}
	, 1, [null,null,['self']]);
		$cls_definition['get_posts'] = $method;
		$method = $pyjs__bind_method2('get_reversed_posts', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr5,$lambda1,$attr6;
			var 			$lambda1 = function(post) {
				var $attr8,$attr7;
				return (($attr7=($attr8=post)['post_id']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
							$p['getattr']($attr8, 'post_id'):
							post['post_id']);
			};
			$lambda1.__name__ = '$lambda1';

			$lambda1.__bind_type__ = 0;
			$lambda1.__args__ = [null,null,['post']];
			return $pyjs_kwargs_call(null, $p['sorted'], null, null, [{key:$lambda1, reverse:true}, (($attr5=($attr6=self)['data']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'data'):
						self['data'])]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['get_reversed_posts'] = $method;
		$method = $pyjs__bind_method2('get_post', function(post_id) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				post_id = arguments[1];
			}
			var $attr9,$attr16,$iter1_nextval,$iter1_type,i,$iter1_iter,$iter1_array,$attr15,$attr14,$attr12,$attr11,$attr10,$attr13,$iter1_idx;
			$iter1_iter = $p['range']($p['len']((($attr9=($attr10=self)['data']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'data'):
						self['data'])));
			$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
			while (typeof($p['__wrapped_next']($iter1_nextval).$nextval) != 'undefined') {
				i = $iter1_nextval.$nextval;
				if ($p['bool']($p['op_eq']((($attr13=($attr14=(($attr11=($attr12=self)['data']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
							$p['getattr']($attr12, 'data'):
							self['data']).__getitem__(i))['post_id']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
							$p['getattr']($attr14, 'post_id'):
							(($attr11=($attr12=self)['data']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
							$p['getattr']($attr12, 'data'):
							self['data']).__getitem__(i)['post_id']), post_id))) {
					return (($attr15=($attr16=self)['data']) == null || (($attr16.__is_instance__) && typeof $attr15 == 'function') || (typeof $attr15['__get__'] == 'function')?
								$p['getattr']($attr16, 'data'):
								self['data']).__getitem__(i);
				}
			}
			return null;
		}
	, 1, [null,null,['self'],['post_id']]);
		$cls_definition['get_post'] = $method;
		$method = $pyjs__bind_method2('add_blog_post', function(post) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				post = arguments[1];
			}

			self['data']['append'](post);
			return null;
		}
	, 1, [null,null,['self'],['post']]);
		$cls_definition['add_blog_post'] = $method;
		$method = $pyjs__bind_method2('update_blog_post', function(post) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				post = arguments[1];
			}
			var $iter2_nextval,$iter2_type,$iter2_iter,i,$attr22,$attr20,$attr21,$iter2_idx,$attr23,$attr19,$attr18,$attr26,$attr24,$attr17,$iter2_array,$attr25;
			$iter2_iter = $p['range']($p['len']((($attr17=($attr18=self)['data']) == null || (($attr18.__is_instance__) && typeof $attr17 == 'function') || (typeof $attr17['__get__'] == 'function')?
						$p['getattr']($attr18, 'data'):
						self['data'])));
			$iter2_nextval=$p['__iter_prepare']($iter2_iter,false);
			while (typeof($p['__wrapped_next']($iter2_nextval).$nextval) != 'undefined') {
				i = $iter2_nextval.$nextval;
				if ($p['bool']($p['op_eq']((($attr21=($attr22=(($attr19=($attr20=self)['data']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
							$p['getattr']($attr20, 'data'):
							self['data']).__getitem__(i))['post_id']) == null || (($attr22.__is_instance__) && typeof $attr21 == 'function') || (typeof $attr21['__get__'] == 'function')?
							$p['getattr']($attr22, 'post_id'):
							(($attr19=($attr20=self)['data']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
							$p['getattr']($attr20, 'data'):
							self['data']).__getitem__(i)['post_id']), (($attr23=($attr24=post)['post_id']) == null || (($attr24.__is_instance__) && typeof $attr23 == 'function') || (typeof $attr23['__get__'] == 'function')?
							$p['getattr']($attr24, 'post_id'):
							post['post_id'])))) {
					(($attr25=($attr26=self)['data']) == null || (($attr26.__is_instance__) && typeof $attr25 == 'function') || (typeof $attr25['__get__'] == 'function')?
								$p['getattr']($attr26, 'data'):
								self['data']).__setitem__(i, post);
				}
			}
			return null;
		}
	, 1, [null,null,['self'],['post']]);
		$cls_definition['update_blog_post'] = $method;
		$method = $pyjs__bind_method2('delete_post', function(post_id) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				post_id = arguments[1];
			}
			var $iter3_idx,$attr27,$attr35,$attr32,i,$iter3_type,$attr33,$attr31,$attr30,$iter3_iter,$attr34,$iter3_array,$attr28,$attr29,$iter3_nextval,$attr36;
			$iter3_iter = $p['range']($p['len']((($attr27=($attr28=self)['data']) == null || (($attr28.__is_instance__) && typeof $attr27 == 'function') || (typeof $attr27['__get__'] == 'function')?
						$p['getattr']($attr28, 'data'):
						self['data'])));
			$iter3_nextval=$p['__iter_prepare']($iter3_iter,false);
			while (typeof($p['__wrapped_next']($iter3_nextval).$nextval) != 'undefined') {
				i = $iter3_nextval.$nextval;
				if ($p['bool']($p['op_eq']((($attr31=($attr32=(($attr29=($attr30=self)['data']) == null || (($attr30.__is_instance__) && typeof $attr29 == 'function') || (typeof $attr29['__get__'] == 'function')?
							$p['getattr']($attr30, 'data'):
							self['data']).__getitem__(i))['post_id']) == null || (($attr32.__is_instance__) && typeof $attr31 == 'function') || (typeof $attr31['__get__'] == 'function')?
							$p['getattr']($attr32, 'post_id'):
							(($attr29=($attr30=self)['data']) == null || (($attr30.__is_instance__) && typeof $attr29 == 'function') || (typeof $attr29['__get__'] == 'function')?
							$p['getattr']($attr30, 'data'):
							self['data']).__getitem__(i)['post_id']), post_id))) {
					(($attr33=($attr34=self)['data']) == null || (($attr34.__is_instance__) && typeof $attr33 == 'function') || (typeof $attr33['__get__'] == 'function')?
								$p['getattr']($attr34, 'data'):
								self['data']).__delitem__(i);
					self['sendNotification']((($attr35=($attr36=$m['Blog']['AppFacade'])['POST_DELETED']) == null || (($attr36.__is_instance__) && typeof $attr35 == 'function') || (typeof $attr35['__get__'] == 'function')?
								$p['getattr']($attr36, 'POST_DELETED'):
								$m['Blog']['AppFacade']['POST_DELETED']));
					return null;
				}
			}
			return null;
		}
	, 1, [null,null,['self'],['post_id']]);
		$cls_definition['delete_post'] = $method;
		$method = $pyjs__bind_method2('retrieve_posts', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr38,$attr37,id;
			id = self['remote']['get_posts'](self);
			if ($p['bool'](($p['cmp'](id, 0) == -1))) {
				self['sendNotification']((($attr37=($attr38=$m['Blog']['AppFacade'])['POST_REMOTE_FAILURE']) == null || (($attr38.__is_instance__) && typeof $attr37 == 'function') || (typeof $attr37['__get__'] == 'function')?
							$p['getattr']($attr38, 'POST_REMOTE_FAILURE'):
							$m['Blog']['AppFacade']['POST_REMOTE_FAILURE']));
			}
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['retrieve_posts'] = $method;
		$method = $pyjs__bind_method2('add_remote_blog_post', function(title, content) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				title = arguments[1];
				content = arguments[2];
			}
			var $attr40,$attr39,id;
			id = self['remote']['add_post'](title, content, self);
			if ($p['bool'](($p['cmp'](id, 0) == -1))) {
				self['sendNotification']((($attr39=($attr40=$m['Blog']['AppFacade'])['POST_REMOTE_FAILURE']) == null || (($attr40.__is_instance__) && typeof $attr39 == 'function') || (typeof $attr39['__get__'] == 'function')?
							$p['getattr']($attr40, 'POST_REMOTE_FAILURE'):
							$m['Blog']['AppFacade']['POST_REMOTE_FAILURE']));
			}
			return null;
		}
	, 1, [null,null,['self'],['title'],['content']]);
		$cls_definition['add_remote_blog_post'] = $method;
		$method = $pyjs__bind_method2('edit_remote_blog_post', function(key, title, content) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				key = arguments[1];
				title = arguments[2];
				content = arguments[3];
			}
			var $attr42,$attr41,id;
			id = self['remote']['update_post'](key, title, content, self);
			if ($p['bool'](($p['cmp'](id, 0) == -1))) {
				self['sendNotification']((($attr41=($attr42=$m['Blog']['AppFacade'])['POST_REMOTE_FAILURE']) == null || (($attr42.__is_instance__) && typeof $attr41 == 'function') || (typeof $attr41['__get__'] == 'function')?
							$p['getattr']($attr42, 'POST_REMOTE_FAILURE'):
							$m['Blog']['AppFacade']['POST_REMOTE_FAILURE']));
			}
			return null;
		}
	, 1, [null,null,['self'],['key'],['title'],['content']]);
		$cls_definition['edit_remote_blog_post'] = $method;
		$method = $pyjs__bind_method2('delete_remote_post', function(key) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				key = arguments[1];
			}
			var $attr44,id,$attr43;
			id = self['remote']['delete_post'](key, self);
			if ($p['bool'](($p['cmp'](id, 0) == -1))) {
				self['sendNotification']((($attr43=($attr44=$m['Blog']['AppFacade'])['POST_REMOTE_FAILURE']) == null || (($attr44.__is_instance__) && typeof $attr43 == 'function') || (typeof $attr43['__get__'] == 'function')?
							$p['getattr']($attr44, 'POST_REMOTE_FAILURE'):
							$m['Blog']['AppFacade']['POST_REMOTE_FAILURE']));
			}
			return null;
		}
	, 1, [null,null,['self'],['key']]);
		$cls_definition['delete_remote_post'] = $method;
		$method = $pyjs__bind_method2('onRemoteResponse', function(response, request_info) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				response = arguments[1];
				request_info = arguments[2];
			}
			var blog_post,$iter5_nextval,post_number,$iter5_array,$attr46,$attr47,$iter5_iter,$iter4_type,$iter5_type,$iter4_iter,$attr48,$attr49,$attr60,$iter5_idx,post,$attr59,$attr58,$attr51,$iter4_nextval,$attr52,$attr55,$attr54,$attr57,$attr56,$iter4_idx,$attr45,$attr50,$iter4_array,$attr53;
			if ($p['bool']($p['op_eq']((($attr45=($attr46=request_info)['method']) == null || (($attr46.__is_instance__) && typeof $attr45 == 'function') || (typeof $attr45['__get__'] == 'function')?
						$p['getattr']($attr46, 'method'):
						request_info['method']), 'get_posts'))) {
				$iter4_iter = response;
				$iter4_nextval=$p['__iter_prepare']($iter4_iter,false);
				while (typeof($p['__wrapped_next']($iter4_nextval).$nextval) != 'undefined') {
					post = $iter4_nextval.$nextval;
					self['add_blog_post']($m['vo']['PostVO'](post.__getitem__(0), post.__getitem__(1), post.__getitem__(2)));
				}
				self['sendNotification']((($attr47=($attr48=$m['Blog']['AppFacade'])['POSTS_RETRIEVED']) == null || (($attr48.__is_instance__) && typeof $attr47 == 'function') || (typeof $attr47['__get__'] == 'function')?
							$p['getattr']($attr48, 'POSTS_RETRIEVED'):
							$m['Blog']['AppFacade']['POSTS_RETRIEVED']));
			}
			else if ($p['bool']($p['op_eq']((($attr49=($attr50=request_info)['method']) == null || (($attr50.__is_instance__) && typeof $attr49 == 'function') || (typeof $attr49['__get__'] == 'function')?
						$p['getattr']($attr50, 'method'):
						request_info['method']), 'add_post'))) {
				blog_post = $m['vo']['PostVO'](response.__getitem__(0).__getitem__(0), response.__getitem__(0).__getitem__(1), response.__getitem__(0).__getitem__(2));
				self['add_blog_post'](blog_post);
				self['sendNotification']((($attr51=($attr52=$m['Blog']['AppFacade'])['POST_ADDED']) == null || (($attr52.__is_instance__) && typeof $attr51 == 'function') || (typeof $attr51['__get__'] == 'function')?
							$p['getattr']($attr52, 'POST_ADDED'):
							$m['Blog']['AppFacade']['POST_ADDED']), blog_post);
			}
			else if ($p['bool']($p['op_eq']((($attr53=($attr54=request_info)['method']) == null || (($attr54.__is_instance__) && typeof $attr53 == 'function') || (typeof $attr53['__get__'] == 'function')?
						$p['getattr']($attr54, 'method'):
						request_info['method']), 'update_post'))) {
				post = response;
				$iter5_iter = response;
				$iter5_nextval=$p['__iter_prepare']($iter5_iter,false);
				while (typeof($p['__wrapped_next']($iter5_nextval).$nextval) != 'undefined') {
					post = $iter5_nextval.$nextval;
					self['update_blog_post']($m['vo']['PostVO'](post.__getitem__(0), post.__getitem__(1), post.__getitem__(2)));
				}
				self['sendNotification']((($attr55=($attr56=$m['Blog']['AppFacade'])['POST_EDITED']) == null || (($attr56.__is_instance__) && typeof $attr55 == 'function') || (typeof $attr55['__get__'] == 'function')?
							$p['getattr']($attr56, 'POST_EDITED'):
							$m['Blog']['AppFacade']['POST_EDITED']));
			}
			else if ($p['bool']($p['op_eq']((($attr57=($attr58=request_info)['method']) == null || (($attr58.__is_instance__) && typeof $attr57 == 'function') || (typeof $attr57['__get__'] == 'function')?
						$p['getattr']($attr58, 'method'):
						request_info['method']), 'delete_post'))) {
				post_number = response;
				self['delete_post'](post_number);
			}
			else {
				self['sendNotification']((($attr59=($attr60=$m['Blog']['AppFacade'])['POST_REMOTE_NONE']) == null || (($attr60.__is_instance__) && typeof $attr59 == 'function') || (typeof $attr59['__get__'] == 'function')?
							$p['getattr']($attr60, 'POST_REMOTE_NONE'):
							$m['Blog']['AppFacade']['POST_REMOTE_NONE']));
			}
			return null;
		}
	, 1, [null,null,['self'],['response'],['request_info']]);
		$cls_definition['onRemoteResponse'] = $method;
		$method = $pyjs__bind_method2('onRemoteError', function(code, message, request_info) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				code = arguments[1];
				message = arguments[2];
				request_info = arguments[3];
			}
			var $attr61,$attr62;
			self['sendNotification']((($attr61=($attr62=$m['Blog']['AppFacade'])['POST_REMOTE_FAILURE']) == null || (($attr62.__is_instance__) && typeof $attr61 == 'function') || (typeof $attr61['__get__'] == 'function')?
						$p['getattr']($attr62, 'POST_REMOTE_FAILURE'):
						$m['Blog']['AppFacade']['POST_REMOTE_FAILURE']));
			return null;
		}
	, 1, [null,null,['self'],['code'],['message'],['request_info']]);
		$cls_definition['onRemoteError'] = $method;
		var $bases = new Array($m['Proxy']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('PostRemoteProxy', $p['tuple']($bases), $data);
	})();
	$m['DataService'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'model';
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$m['JSONProxy']['__init__'](self, '/services/', $p['list'](['add_post', 'get_posts', 'update_post', 'delete_post']));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		var $bases = new Array($m['JSONProxy']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('DataService', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end model */


/* end module: model */


/*
PYJS_DEPS: ['pyjamas.JSONService.JSONProxy', 'pyjamas', 'pyjamas.JSONService', 'puremvc.patterns.proxy.Proxy', 'puremvc', 'puremvc.patterns', 'puremvc.patterns.proxy', 'vo', 'Blog']
*/
