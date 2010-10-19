/* start module: view */
var view;
$pyjs.loaded_modules['view'] = function (__mod_name__) {
	if($pyjs.loaded_modules['view'].__was_initialized__) return $pyjs.loaded_modules['view'];
	var $m = view = $pyjs.loaded_modules["view"];
	view.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'view';
	var __name__ = view.__name__ = __mod_name__;


	$m['Mediator'] = $p['___import___']('puremvc.patterns.mediator.Mediator', null, null, false);
	$m['model'] = $p['___import___']('model', null);
	$m['Blog'] = $p['___import___']('Blog', null);
	$m['HomeMediator'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'view';
		$cls_definition['NAME'] = 'HomeMediator';
		$cls_definition['post_remote_proxy'] = null;
		$method = $pyjs__bind_method2('__init__', function(viewComponent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				viewComponent = arguments[1];
			}
			var $attr9,$attr8,$attr1,$attr2,$attr5,$attr4,$attr7,$attr6,$attr10,$attr3;
			$p['$$super']($m['HomeMediator'], self)['__init__']((($attr1=($attr2=$m['HomeMediator'])['NAME']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
						$p['getattr']($attr2, 'NAME'):
						$m['HomeMediator']['NAME']), viewComponent);
			$p['setattr'](self['viewComponent'], 'mediator', self);
			$p['setattr'](self, 'post_remote_proxy', self['facade']['retrieveProxy']((($attr3=($attr4=$m['model']['PostRemoteProxy'])['NAME']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'NAME'):
						$m['model']['PostRemoteProxy']['NAME'])));
			self['viewComponent']['write_button']['addClickListener']((($attr5=($attr6=self)['on_write_click']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'on_write_click'):
						self['on_write_click']));
			self['viewComponent']['edit_hidden_button']['addClickListener']((($attr7=($attr8=self)['on_edit_click']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'on_edit_click'):
						self['on_edit_click']));
			self['viewComponent']['delete_hidden_button']['addClickListener']((($attr9=($attr10=self)['on_delete_click']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'on_delete_click'):
						self['on_delete_click']));
			return null;
		}
	, 1, [null,null,['self'],['viewComponent']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('listNotificationInterests', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr20,$attr19,$attr18,$attr15,$attr14,$attr17,$attr16,$attr11,$attr13,$attr12;
			return $p['list']([(($attr11=($attr12=$m['Blog']['AppFacade'])['POSTS_RETRIEVED']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
						$p['getattr']($attr12, 'POSTS_RETRIEVED'):
						$m['Blog']['AppFacade']['POSTS_RETRIEVED']), (($attr13=($attr14=$m['Blog']['AppFacade'])['POST_ADDED']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
						$p['getattr']($attr14, 'POST_ADDED'):
						$m['Blog']['AppFacade']['POST_ADDED']), (($attr15=($attr16=$m['Blog']['AppFacade'])['POST_EDITED']) == null || (($attr16.__is_instance__) && typeof $attr15 == 'function') || (typeof $attr15['__get__'] == 'function')?
						$p['getattr']($attr16, 'POST_EDITED'):
						$m['Blog']['AppFacade']['POST_EDITED']), (($attr17=($attr18=$m['Blog']['AppFacade'])['POST_DELETED']) == null || (($attr18.__is_instance__) && typeof $attr17 == 'function') || (typeof $attr17['__get__'] == 'function')?
						$p['getattr']($attr18, 'POST_DELETED'):
						$m['Blog']['AppFacade']['POST_DELETED']), (($attr19=($attr20=$m['Blog']['AppFacade'])['EDIT_CANCELED']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
						$p['getattr']($attr20, 'EDIT_CANCELED'):
						$m['Blog']['AppFacade']['EDIT_CANCELED'])]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['listNotificationInterests'] = $method;
		$method = $pyjs__bind_method2('handleNotification', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}
			var $attr21,$attr22,$attr23,$attr24,$attr25,$attr26,$attr27,$attr28,$attr29,$attr30,note_name;
			note_name = note['getName']();
			if ($p['bool']($p['op_eq'](note_name, (($attr21=($attr22=$m['Blog']['AppFacade'])['POSTS_RETRIEVED']) == null || (($attr22.__is_instance__) && typeof $attr21 == 'function') || (typeof $attr21['__get__'] == 'function')?
						$p['getattr']($attr22, 'POSTS_RETRIEVED'):
						$m['Blog']['AppFacade']['POSTS_RETRIEVED'])))) {
				self['update_posts']();
			}
			if ($p['bool']($p['op_eq'](note_name, (($attr23=($attr24=$m['Blog']['AppFacade'])['POST_ADDED']) == null || (($attr24.__is_instance__) && typeof $attr23 == 'function') || (typeof $attr23['__get__'] == 'function')?
						$p['getattr']($attr24, 'POST_ADDED'):
						$m['Blog']['AppFacade']['POST_ADDED'])))) {
				self['clear_update_posts']();
			}
			if ($p['bool']($p['op_eq'](note_name, (($attr25=($attr26=$m['Blog']['AppFacade'])['POST_EDITED']) == null || (($attr26.__is_instance__) && typeof $attr25 == 'function') || (typeof $attr25['__get__'] == 'function')?
						$p['getattr']($attr26, 'POST_EDITED'):
						$m['Blog']['AppFacade']['POST_EDITED'])))) {
				self['clear_update_posts']();
			}
			if ($p['bool']($p['op_eq'](note_name, (($attr27=($attr28=$m['Blog']['AppFacade'])['POST_DELETED']) == null || (($attr28.__is_instance__) && typeof $attr27 == 'function') || (typeof $attr27['__get__'] == 'function')?
						$p['getattr']($attr28, 'POST_DELETED'):
						$m['Blog']['AppFacade']['POST_DELETED'])))) {
				self['clear_update_posts']();
			}
			if ($p['bool']($p['op_eq'](note_name, (($attr29=($attr30=$m['Blog']['AppFacade'])['EDIT_CANCELED']) == null || (($attr30.__is_instance__) && typeof $attr29 == 'function') || (typeof $attr29['__get__'] == 'function')?
						$p['getattr']($attr30, 'EDIT_CANCELED'):
						$m['Blog']['AppFacade']['EDIT_CANCELED'])))) {
				self['clear_hidden_id']();
			}
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['handleNotification'] = $method;
		$method = $pyjs__bind_method2('clear_update_posts', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['clear_posts']();
			self['clear_hidden_id']();
			self['update_posts']();
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clear_update_posts'] = $method;
		$method = $pyjs__bind_method2('clear_posts', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr32,$attr31;
			self['viewComponent']['remove']((($attr31=($attr32=self['viewComponent'])['contents']) == null || (($attr32.__is_instance__) && typeof $attr31 == 'function') || (typeof $attr31['__get__'] == 'function')?
						$p['getattr']($attr32, 'contents'):
						self['viewComponent']['contents']));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clear_posts'] = $method;
		$method = $pyjs__bind_method2('clear_hidden_id', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['viewComponent']['edit_hidden_button']['setID']('');
			self['viewComponent']['delete_hidden_button']['setID']('');
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clear_hidden_id'] = $method;
		$method = $pyjs__bind_method2('update_posts', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var posts;
			posts = self['post_remote_proxy']['get_reversed_posts']();
			self['viewComponent']['update_posts'](posts);
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['update_posts'] = $method;
		$method = $pyjs__bind_method2('on_write_click', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr33,$attr34;
			self['sendNotification']((($attr33=($attr34=$m['Blog']['AppFacade'])['VIEW_WRITE_POST']) == null || (($attr34.__is_instance__) && typeof $attr33 == 'function') || (typeof $attr33['__get__'] == 'function')?
						$p['getattr']($attr34, 'VIEW_WRITE_POST'):
						$m['Blog']['AppFacade']['VIEW_WRITE_POST']));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['on_write_click'] = $method;
		$method = $pyjs__bind_method2('is_click_id_set', function(sender_id) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender_id = arguments[1];
			}
			var $or1,$or2;
			if ($p['bool'](($p['bool']($or1=$p['op_eq'](sender_id, ''))?$or1:$p['op_eq'](sender_id, null)))) {
				return false;
			}
			return true;
		}
	, 1, [null,null,['self'],['sender_id']]);
		$cls_definition['is_click_id_set'] = $method;
		$method = $pyjs__bind_method2('on_edit_click', function(sender) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}
			if (typeof sender == 'undefined') sender=arguments.callee.__args__[3][1];
			var $attr35,$attr36;
			if ($p['bool'](self['is_click_id_set'](sender['getID']()))) {
				self['sendNotification']((($attr35=($attr36=$m['Blog']['AppFacade'])['VIEW_EDIT_POST']) == null || (($attr36.__is_instance__) && typeof $attr35 == 'function') || (typeof $attr35['__get__'] == 'function')?
							$p['getattr']($attr36, 'VIEW_EDIT_POST'):
							$m['Blog']['AppFacade']['VIEW_EDIT_POST']), sender['getID']());
			}
			return null;
		}
	, 1, [null,null,['self'],['sender', null]]);
		$cls_definition['on_edit_click'] = $method;
		$method = $pyjs__bind_method2('on_delete_click', function(sender) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}
			if (typeof sender == 'undefined') sender=arguments.callee.__args__[3][1];
			var post_id,key;
			if ($p['bool'](self['is_click_id_set'](sender['getID']()))) {
				key = sender['getID']();
				post_id = key['$$replace']('delete_', '');
				self['post_remote_proxy']['delete_remote_post'](post_id);
			}
			return null;
		}
	, 1, [null,null,['self'],['sender', null]]);
		$cls_definition['on_delete_click'] = $method;
		var $bases = new Array($m['Mediator']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('HomeMediator', $p['tuple']($bases), $data);
	})();
	$m['WriteMediator'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'view';
		$cls_definition['NAME'] = 'WriteMediator';
		$cls_definition['post_remote_proxy'] = null;
		$method = $pyjs__bind_method2('__init__', function(viewComponent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				viewComponent = arguments[1];
			}
			var $attr42,$attr44,$attr37,$attr43,$attr40,$attr41,$attr39,$attr38;
			$p['$$super']($m['WriteMediator'], self)['__init__']((($attr37=($attr38=$m['WriteMediator'])['NAME']) == null || (($attr38.__is_instance__) && typeof $attr37 == 'function') || (typeof $attr37['__get__'] == 'function')?
						$p['getattr']($attr38, 'NAME'):
						$m['WriteMediator']['NAME']), viewComponent);
			$p['setattr'](self['viewComponent'], 'mediator', self);
			$p['setattr'](self, 'post_remote_proxy', self['facade']['retrieveProxy']((($attr39=($attr40=$m['model']['PostRemoteProxy'])['NAME']) == null || (($attr40.__is_instance__) && typeof $attr39 == 'function') || (typeof $attr39['__get__'] == 'function')?
						$p['getattr']($attr40, 'NAME'):
						$m['model']['PostRemoteProxy']['NAME'])));
			self['viewComponent']['post_button']['addClickListener']((($attr41=($attr42=self)['add_post']) == null || (($attr42.__is_instance__) && typeof $attr41 == 'function') || (typeof $attr41['__get__'] == 'function')?
						$p['getattr']($attr42, 'add_post'):
						self['add_post']));
			self['viewComponent']['cancel_button']['addClickListener']((($attr43=($attr44=self)['on_close']) == null || (($attr44.__is_instance__) && typeof $attr43 == 'function') || (typeof $attr43['__get__'] == 'function')?
						$p['getattr']($attr44, 'on_close'):
						self['on_close']));
			return null;
		}
	, 1, [null,null,['self'],['viewComponent']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('listNotificationInterests', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr46,$attr45;
			return $p['list']([(($attr45=($attr46=$m['Blog']['AppFacade'])['VIEW_WRITE_POST']) == null || (($attr46.__is_instance__) && typeof $attr45 == 'function') || (typeof $attr45['__get__'] == 'function')?
						$p['getattr']($attr46, 'VIEW_WRITE_POST'):
						$m['Blog']['AppFacade']['VIEW_WRITE_POST'])]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['listNotificationInterests'] = $method;
		$method = $pyjs__bind_method2('handleNotification', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}
			var $attr47,$attr48,note_name;
			note_name = note['getName']();
			if ($p['bool']($p['op_eq'](note_name, (($attr47=($attr48=$m['Blog']['AppFacade'])['VIEW_WRITE_POST']) == null || (($attr48.__is_instance__) && typeof $attr47 == 'function') || (typeof $attr47['__get__'] == 'function')?
						$p['getattr']($attr48, 'VIEW_WRITE_POST'):
						$m['Blog']['AppFacade']['VIEW_WRITE_POST'])))) {
				self['view_write_post'](self);
			}
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['handleNotification'] = $method;
		$method = $pyjs__bind_method2('view_write_post', function(event) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				event = arguments[1];
			}

			self['viewComponent']['clear_write_panel']();
			self['viewComponent']['dialog']['show']();
			self['viewComponent']['post_title']['setFocus'](true);
			return null;
		}
	, 1, [null,null,['self'],['event']]);
		$cls_definition['view_write_post'] = $method;
		$method = $pyjs__bind_method2('on_close', function(event) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				event = arguments[1];
			}

			self['viewComponent']['dialog']['hide']();
			return null;
		}
	, 1, [null,null,['self'],['event']]);
		$cls_definition['on_close'] = $method;
		$method = $pyjs__bind_method2('validate_add', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $add2,title,error_message,content,$add1;
			error_message = '';
			title = self['viewComponent']['post_title']['getText']();
			if ($p['bool']($p['op_eq'](title, ''))) {
				self['viewComponent']['post_title']['setFocus'](true);
				return $p['tuple'](['Title is a required field', title, $m.content]);
			}
			content = self['viewComponent']['post_content']['getText']();
			if ($p['bool']($p['op_eq'](content, ''))) {
				self['viewComponent']['post_content']['setFocus'](true);
				return $p['tuple'](['Content is a required field', title, content]);
			}
			if ($p['bool'](($p['cmp']($p['len'](content), 255) == 1))) {
				self['viewComponent']['post_content']['setFocus'](true);
				return $p['tuple']([$p['__op_add']($add1='Post body must be less than 256 characters. It is ',$add2=$p['str']($p['len'](content))), title, content]);
			}
			return $p['tuple']([error_message, title, content]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['validate_add'] = $method;
		$method = $pyjs__bind_method2('add_post', function(event) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				event = arguments[1];
			}
			var content,error_message,title;
			var $tupleassign1 = self['validate_add']();
			error_message = $tupleassign1.__getitem__(0);
			title = $tupleassign1.__getitem__(1);
			content = $tupleassign1.__getitem__(2);
			if ($p['bool'](($p['cmp']($p['len'](error_message), 0) == 1))) {
				self['viewComponent']['error_message_label']['setText'](error_message);
				return null;
			}
			title = self['viewComponent']['post_title']['getText']();
			content = self['viewComponent']['post_content']['getText']();
			self['post_remote_proxy']['add_remote_blog_post'](title, content);
			self['on_close']();
			return null;
		}
	, 1, [null,null,['self'],['event']]);
		$cls_definition['add_post'] = $method;
		var $bases = new Array($m['Mediator']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('WriteMediator', $p['tuple']($bases), $data);
	})();
	$m['EditMediator'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'view';
		$cls_definition['NAME'] = 'EditMediator';
		$cls_definition['edit_remote_proxy'] = null;
		$method = $pyjs__bind_method2('__init__', function(viewComponent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				viewComponent = arguments[1];
			}
			var $attr51,$attr50,$attr52,$attr55,$attr54,$attr56,$attr53,$attr49;
			$p['$$super']($m['EditMediator'], self)['__init__']((($attr49=($attr50=$m['EditMediator'])['NAME']) == null || (($attr50.__is_instance__) && typeof $attr49 == 'function') || (typeof $attr49['__get__'] == 'function')?
						$p['getattr']($attr50, 'NAME'):
						$m['EditMediator']['NAME']), viewComponent);
			$p['setattr'](self['viewComponent'], 'mediator', self);
			$p['setattr'](self, 'edit_remote_proxy', self['facade']['retrieveProxy']((($attr51=($attr52=$m['model']['PostRemoteProxy'])['NAME']) == null || (($attr52.__is_instance__) && typeof $attr51 == 'function') || (typeof $attr51['__get__'] == 'function')?
						$p['getattr']($attr52, 'NAME'):
						$m['model']['PostRemoteProxy']['NAME'])));
			self['viewComponent']['edit_button']['addClickListener']((($attr53=($attr54=self)['edit_post']) == null || (($attr54.__is_instance__) && typeof $attr53 == 'function') || (typeof $attr53['__get__'] == 'function')?
						$p['getattr']($attr54, 'edit_post'):
						self['edit_post']));
			self['viewComponent']['edit_cancel_button']['addClickListener']((($attr55=($attr56=self)['on_edit_close']) == null || (($attr56.__is_instance__) && typeof $attr55 == 'function') || (typeof $attr55['__get__'] == 'function')?
						$p['getattr']($attr56, 'on_edit_close'):
						self['on_edit_close']));
			return null;
		}
	, 1, [null,null,['self'],['viewComponent']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('listNotificationInterests', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr58,$attr57;
			return $p['list']([(($attr57=($attr58=$m['Blog']['AppFacade'])['VIEW_EDIT_POST']) == null || (($attr58.__is_instance__) && typeof $attr57 == 'function') || (typeof $attr57['__get__'] == 'function')?
						$p['getattr']($attr58, 'VIEW_EDIT_POST'):
						$m['Blog']['AppFacade']['VIEW_EDIT_POST'])]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['listNotificationInterests'] = $method;
		$method = $pyjs__bind_method2('handleNotification', function(note) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				note = arguments[1];
			}
			var $attr59,$attr60,note_body,note_name;
			note_name = note['getName']();
			note_body = note['getBody']();
			if ($p['bool']($p['op_eq'](note_name, (($attr59=($attr60=$m['Blog']['AppFacade'])['VIEW_EDIT_POST']) == null || (($attr60.__is_instance__) && typeof $attr59 == 'function') || (typeof $attr59['__get__'] == 'function')?
						$p['getattr']($attr60, 'VIEW_EDIT_POST'):
						$m['Blog']['AppFacade']['VIEW_EDIT_POST'])))) {
				self['view_edit_post'](note_body);
			}
			return null;
		}
	, 1, [null,null,['self'],['note']]);
		$cls_definition['handleNotification'] = $method;
		$method = $pyjs__bind_method2('view_edit_post', function(post_key) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				post_key = arguments[1];
			}
			var $attr64,$attr61,$attr62,$attr63,post_id,post;
			self['viewComponent']['clear_edit_panel']();
			self['viewComponent']['edit_dialog']['show']();
			post_id = post_key['$$replace']('edit_', '');
			post = self['edit_remote_proxy']['get_post'](post_id);
			self['viewComponent']['edit_title']['setText']((($attr61=($attr62=post)['title']) == null || (($attr62.__is_instance__) && typeof $attr61 == 'function') || (typeof $attr61['__get__'] == 'function')?
						$p['getattr']($attr62, 'title'):
						post['title']));
			self['viewComponent']['edit_title']['setFocus'](true);
			self['viewComponent']['edit_content']['setText']((($attr63=($attr64=post)['content']) == null || (($attr64.__is_instance__) && typeof $attr63 == 'function') || (typeof $attr63['__get__'] == 'function')?
						$p['getattr']($attr64, 'content'):
						post['content']));
			self['viewComponent']['edit_hidden_key']['setValue'](post_id);
			return null;
		}
	, 1, [null,null,['self'],['post_key']]);
		$cls_definition['view_edit_post'] = $method;
		$method = $pyjs__bind_method2('validate_edit', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $add4,title,error_message,content,$add3,key;
			error_message = '';
			key = self['viewComponent']['edit_hidden_key']['getValue']();
			if ($p['bool']($p['op_eq'](key, ''))) {
				return $p['tuple'](['Cannot update without a post identifier', key, $m.title, $m.content]);
			}
			title = self['viewComponent']['edit_title']['getText']();
			if ($p['bool']($p['op_eq'](title, ''))) {
				self['viewComponent']['edit_title']['setFocus'](true);
				return $p['tuple'](['Title is a required field', key, title, $m.content]);
			}
			content = self['viewComponent']['edit_content']['getText']();
			if ($p['bool']($p['op_eq'](content, ''))) {
				self['viewComponent']['edit_content']['setFocus'](true);
				return $p['tuple'](['Content is a required field', key, title, content]);
			}
			if ($p['bool'](($p['cmp']($p['len'](content), 255) == 1))) {
				self['viewComponent']['edit_content']['setFocus'](true);
				return $p['tuple']([$p['__op_add']($add3='Post body must be less than 255 characters. It is ',$add4=$p['str']($p['len'](content))), key, title, content]);
			}
			return $p['tuple']([error_message, key, title, content]);
		}
	, 1, [null,null,['self']]);
		$cls_definition['validate_edit'] = $method;
		$method = $pyjs__bind_method2('on_edit_close', function(event) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				event = arguments[1];
			}
			var $attr65,$attr66;
			self['viewComponent']['edit_dialog']['hide']();
			self['sendNotification']((($attr65=($attr66=$m['Blog']['AppFacade'])['EDIT_CANCELED']) == null || (($attr66.__is_instance__) && typeof $attr65 == 'function') || (typeof $attr65['__get__'] == 'function')?
						$p['getattr']($attr66, 'EDIT_CANCELED'):
						$m['Blog']['AppFacade']['EDIT_CANCELED']));
			return null;
		}
	, 1, [null,null,['self'],['event']]);
		$cls_definition['on_edit_close'] = $method;
		$method = $pyjs__bind_method2('edit_post', function(event) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				event = arguments[1];
			}
			var title,error_message,content,key;
			var $tupleassign2 = self['validate_edit']();
			error_message = $tupleassign2.__getitem__(0);
			key = $tupleassign2.__getitem__(1);
			title = $tupleassign2.__getitem__(2);
			content = $tupleassign2.__getitem__(3);
			if ($p['bool'](($p['cmp']($p['len'](error_message), 0) == 1))) {
				self['viewComponent']['error_message_label']['setText'](error_message);
				return null;
			}
			self['edit_remote_proxy']['edit_remote_blog_post'](key, title, content);
			self['on_edit_close']();
			return null;
		}
	, 1, [null,null,['self'],['event']]);
		$cls_definition['edit_post'] = $method;
		var $bases = new Array($m['Mediator']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('EditMediator', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end view */


/* end module: view */


/*
PYJS_DEPS: ['puremvc.patterns.mediator.Mediator', 'puremvc', 'puremvc.patterns', 'puremvc.patterns.mediator', 'model', 'Blog']
*/
