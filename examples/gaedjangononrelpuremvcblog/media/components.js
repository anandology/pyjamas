/* start module: components */
var components;
$pyjs.loaded_modules['components'] = function (__mod_name__) {
	if($pyjs.loaded_modules['components'].__was_initialized__) return $pyjs.loaded_modules['components'];
	var $m = components = $pyjs.loaded_modules["components"];
	components.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'components';
	var __name__ = components.__name__ = __mod_name__;


	$m['Hidden'] = $p['___import___']('pyjamas.ui.Hidden.Hidden', null, null, false);
	$m['TextArea'] = $p['___import___']('pyjamas.ui.TextArea.TextArea', null, null, false);
	$m['TextBox'] = $p['___import___']('pyjamas.ui.TextBox.TextBox', null, null, false);
	$m['AbsolutePanel'] = $p['___import___']('pyjamas.ui.AbsolutePanel.AbsolutePanel', null, null, false);
	$m['DialogBox'] = $p['___import___']('pyjamas.ui.DialogBox.DialogBox', null, null, false);
	$m['RootPanel'] = $p['___import___']('pyjamas.ui.RootPanel.RootPanel', null, null, false);
	$m['Button'] = $p['___import___']('pyjamas.ui.Button.Button', null, null, false);
	$m['Label'] = $p['___import___']('pyjamas.ui.Label.Label', null, null, false);
	$m['HorizontalPanel'] = $p['___import___']('pyjamas.ui.HorizontalPanel.HorizontalPanel', null, null, false);
	$m['VerticalPanel'] = $p['___import___']('pyjamas.ui.VerticalPanel.VerticalPanel', null, null, false);
	$m['HTML'] = $p['___import___']('pyjamas.ui.HTML.HTML', null, null, false);
	$m['Window'] = $p['___import___']('pyjamas.Window', null, null, false);
	$m['PyJsApp'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'components';
		$cls_definition['app_frame'] = null;
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			$p['setattr'](self, 'app_frame', $m.AppFrame());
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('PyJsApp', $p['tuple']($bases), $data);
	})();
	$m['AppFrame'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'components';
		$cls_definition['edit_panel'] = null;
		$cls_definition['home_panel'] = null;
		$cls_definition['write_panel'] = null;
		$method = $pyjs__bind_method2('__init__', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr8,$attr1,$attr2,$attr5,$attr4,$attr7,$attr6,$attr3;
			$p['setattr'](self, 'panel', $m['AbsolutePanel']());
			$p['setattr'](self, 'edit_panel', $m.EditPanel(self));
			$p['setattr'](self, 'home_panel', $m.HomePanel(self));
			$p['setattr'](self, 'write_panel', $m.WritePanel(self));
			self['panel']['add']((($attr1=($attr2=self)['edit_panel']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
						$p['getattr']($attr2, 'edit_panel'):
						self['edit_panel']));
			self['panel']['add']((($attr3=($attr4=self)['home_panel']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'home_panel'):
						self['home_panel']));
			self['panel']['add']((($attr5=($attr6=self)['write_panel']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'write_panel'):
						self['write_panel']));
			$m['RootPanel']()['add']((($attr7=($attr8=self)['panel']) == null || (($attr8.__is_instance__) && typeof $attr7 == 'function') || (typeof $attr7['__get__'] == 'function')?
						$p['getattr']($attr8, 'panel'):
						self['panel']));
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['__init__'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('AppFrame', $p['tuple']($bases), $data);
	})();
	$m['EditPanel'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'components';
		$method = $pyjs__bind_method2('__init__', function(key, title, content) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				key = arguments[1];
				title = arguments[2];
				content = arguments[3];
			}
			var $div2,$attr20,$attr21,$attr22,$attr23,$attr24,$div3,$div1,$div4,$sub3,$sub2,$sub1,$sub4,$attr9,$attr19,$attr18,$attr15,$attr14,$attr17,$attr16,$attr11,$attr10,$attr13,$attr12,$add2,$add3,$add1,$add4,edit_contents,top,left;
			$m['AbsolutePanel']['__init__'](self);
			$p['setattr'](self, 'edit_header', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'header_label'}, 'Edit a Post']));
			$p['setattr'](self, 'edit_title_label', $m['Label']('Title:'));
			$p['setattr'](self, 'edit_title', $m['TextBox']());
			self['edit_title']['setMaxLength'](255);
			$p['setattr'](self, 'edit_content', $m['TextArea']());
			self['edit_content']['setVisibleLines'](2);
			$p['setattr'](self, 'edit_button', $m['Button']('Save'));
			$p['setattr'](self, 'edit_cancel_button', $m['Button']('Cancel'));
			$p['setattr'](self, 'edit_hidden_key', $m['Hidden']());
			$p['setattr'](self, 'error_message_label', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'error_message_label'}, '']));
			edit_contents = $pyjs_kwargs_call(null, $m['VerticalPanel'], null, null, [{StyleName:'Contents', Spacing:4}]);
			edit_contents['add']((($attr9=($attr10=self)['edit_header']) == null || (($attr10.__is_instance__) && typeof $attr9 == 'function') || (typeof $attr9['__get__'] == 'function')?
						$p['getattr']($attr10, 'edit_header'):
						self['edit_header']));
			edit_contents['add']((($attr11=($attr12=self)['edit_title_label']) == null || (($attr12.__is_instance__) && typeof $attr11 == 'function') || (typeof $attr11['__get__'] == 'function')?
						$p['getattr']($attr12, 'edit_title_label'):
						self['edit_title_label']));
			edit_contents['add']((($attr13=($attr14=self)['edit_title']) == null || (($attr14.__is_instance__) && typeof $attr13 == 'function') || (typeof $attr13['__get__'] == 'function')?
						$p['getattr']($attr14, 'edit_title'):
						self['edit_title']));
			edit_contents['add']((($attr15=($attr16=self)['edit_content']) == null || (($attr16.__is_instance__) && typeof $attr15 == 'function') || (typeof $attr15['__get__'] == 'function')?
						$p['getattr']($attr16, 'edit_content'):
						self['edit_content']));
			edit_contents['add']((($attr17=($attr18=self)['edit_button']) == null || (($attr18.__is_instance__) && typeof $attr17 == 'function') || (typeof $attr17['__get__'] == 'function')?
						$p['getattr']($attr18, 'edit_button'):
						self['edit_button']));
			edit_contents['add']((($attr19=($attr20=self)['edit_cancel_button']) == null || (($attr20.__is_instance__) && typeof $attr19 == 'function') || (typeof $attr19['__get__'] == 'function')?
						$p['getattr']($attr20, 'edit_cancel_button'):
						self['edit_cancel_button']));
			edit_contents['add']((($attr21=($attr22=self)['error_message_label']) == null || (($attr22.__is_instance__) && typeof $attr21 == 'function') || (typeof $attr21['__get__'] == 'function')?
						$p['getattr']($attr22, 'error_message_label'):
						self['error_message_label']));
			edit_contents['add']((($attr23=($attr24=self)['edit_hidden_key']) == null || (($attr24.__is_instance__) && typeof $attr23 == 'function') || (typeof $attr23['__get__'] == 'function')?
						$p['getattr']($attr24, 'edit_hidden_key'):
						self['edit_hidden_key']));
			$p['setattr'](self, 'edit_dialog', $pyjs_kwargs_call(null, $m['DialogBox'], null, null, [{glass:true}]));
			self['edit_dialog']['setHTML']('\x3Cb\x3EBlog Post Form\x3C/b\x3E');
			self['edit_dialog']['setWidget'](edit_contents);
			left = $p['__op_add']($add1=(typeof ($div1=$p['__op_sub']($sub1=$m['Window']['getClientWidth'](),$sub2=900))==typeof ($div2=2) && typeof $div1=='number' && $div2 !== 0?
				$div1/$div2:
				$p['op_div']($div1,$div2)),$add2=$m['Window']['getScrollLeft']());
			top = $p['__op_add']($add3=(typeof ($div3=$p['__op_sub']($sub3=$m['Window']['getClientHeight'](),$sub4=600))==typeof ($div4=2) && typeof $div3=='number' && $div4 !== 0?
				$div3/$div4:
				$p['op_div']($div3,$div4)),$add4=$m['Window']['getScrollTop']());
			self['edit_dialog']['setPopupPosition'](left, top);
			self['edit_dialog']['hide']();
			return null;
		}
	, 1, [null,null,['self'],['key'],['title'],['content']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('clear_edit_panel', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['edit_title']['setText']('');
			self['edit_content']['setText']('');
			self['error_message_label']['setText']('');
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clear_edit_panel'] = $method;
		var $bases = new Array($m['AbsolutePanel']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('EditPanel', $p['tuple']($bases), $data);
	})();
	$m['HomePanel'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'components';
		$method = $pyjs__bind_method2('__init__', function(parent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				parent = arguments[1];
			}
			var $attr32,$attr31,$attr30,$attr25,$attr26,$attr27,$attr28,$attr29;
			$m['AbsolutePanel']['__init__'](self);
			$p['setattr'](self, 'home_header', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'header_label'}, 'Blogjamas']));
			$p['setattr'](self, 'write_button', $m['Button']('Write a Post'));
			$p['setattr'](self, 'edit_hidden_button', $pyjs_kwargs_call(null, $m['Button'], null, null, [{StyleName:'hidden_button'}, '']));
			$p['setattr'](self, 'delete_hidden_button', $pyjs_kwargs_call(null, $m['Button'], null, null, [{StyleName:'hidden_button'}, '']));
			self['add']((($attr25=($attr26=self)['home_header']) == null || (($attr26.__is_instance__) && typeof $attr25 == 'function') || (typeof $attr25['__get__'] == 'function')?
						$p['getattr']($attr26, 'home_header'):
						self['home_header']));
			self['add']((($attr27=($attr28=self)['write_button']) == null || (($attr28.__is_instance__) && typeof $attr27 == 'function') || (typeof $attr27['__get__'] == 'function')?
						$p['getattr']($attr28, 'write_button'):
						self['write_button']));
			self['add']((($attr29=($attr30=self)['edit_hidden_button']) == null || (($attr30.__is_instance__) && typeof $attr29 == 'function') || (typeof $attr29['__get__'] == 'function')?
						$p['getattr']($attr30, 'edit_hidden_button'):
						self['edit_hidden_button']));
			self['add']((($attr31=($attr32=self)['delete_hidden_button']) == null || (($attr32.__is_instance__) && typeof $attr31 == 'function') || (typeof $attr31['__get__'] == 'function')?
						$p['getattr']($attr32, 'delete_hidden_button'):
						self['delete_hidden_button']));
			return null;
		}
	, 1, [null,null,['self'],['parent']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('update_posts', function(posts) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				posts = arguments[1];
			}
			var $attr55,$iter1_iter,$attr46,$attr47,$attr44,$attr45,$attr42,$attr43,$attr40,$attr41,$attr48,$attr49,$iter1_array,$add7,$iter1_nextval,$attr33,$attr37,$attr36,$attr35,$attr34,$attr39,$attr38,$iter1_type,i,$attr50,$attr53,$attr52,$attr54,$attr56,$attr51,$add6,$iter1_idx,$add5,$add8;
			$p['setattr'](self, 'contents', $pyjs_kwargs_call(null, $m['VerticalPanel'], null, null, [{Spacing:1}]));
			$iter1_iter = $p['range']($p['len'](posts));
			$iter1_nextval=$p['__iter_prepare']($iter1_iter,false);
			while (typeof($p['__wrapped_next']($iter1_nextval).$nextval) != 'undefined') {
				i = $iter1_nextval.$nextval;
				$p['setattr'](self, 'divider', $m['HTML']('----------------------------------------------------'));
				self['contents']['add']((($attr33=($attr34=self)['divider']) == null || (($attr34.__is_instance__) && typeof $attr33 == 'function') || (typeof $attr33['__get__'] == 'function')?
							$p['getattr']($attr34, 'divider'):
							self['divider']));
				$p['setattr'](self, 'post_title', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'title_label'}, (($attr35=($attr36=posts.__getitem__(i))['title']) == null || (($attr36.__is_instance__) && typeof $attr35 == 'function') || (typeof $attr35['__get__'] == 'function')?
							$p['getattr']($attr36, 'title'):
							posts.__getitem__(i)['title'])]));
				self['contents']['add']((($attr37=($attr38=self)['post_title']) == null || (($attr38.__is_instance__) && typeof $attr37 == 'function') || (typeof $attr37['__get__'] == 'function')?
							$p['getattr']($attr38, 'post_title'):
							self['post_title']));
				$p['setattr'](self, 'post_content', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'content_label'}, (($attr39=($attr40=posts.__getitem__(i))['content']) == null || (($attr40.__is_instance__) && typeof $attr39 == 'function') || (typeof $attr39['__get__'] == 'function')?
							$p['getattr']($attr40, 'content'):
							posts.__getitem__(i)['content'])]));
				self['contents']['add']((($attr41=($attr42=self)['post_content']) == null || (($attr42.__is_instance__) && typeof $attr41 == 'function') || (typeof $attr41['__get__'] == 'function')?
							$p['getattr']($attr42, 'post_content'):
							self['post_content']));
				$p['setattr'](self, 'edit_button', $m['Button']('Edit'));
				self['edit_button']['setID']($p['__op_add']($add5='edit_',$add6=(($attr43=($attr44=posts.__getitem__(i))['post_id']) == null || (($attr44.__is_instance__) && typeof $attr43 == 'function') || (typeof $attr43['__get__'] == 'function')?
							$p['getattr']($attr44, 'post_id'):
							posts.__getitem__(i)['post_id'])));
				self['edit_button']['addClickListener']((($attr45=($attr46=self)['show_edit_box']) == null || (($attr46.__is_instance__) && typeof $attr45 == 'function') || (typeof $attr45['__get__'] == 'function')?
							$p['getattr']($attr46, 'show_edit_box'):
							self['show_edit_box']));
				self['contents']['add']((($attr47=($attr48=self)['edit_button']) == null || (($attr48.__is_instance__) && typeof $attr47 == 'function') || (typeof $attr47['__get__'] == 'function')?
							$p['getattr']($attr48, 'edit_button'):
							self['edit_button']));
				$p['setattr'](self, 'delete_button', $m['Button']('Delete'));
				self['delete_button']['setID']($p['__op_add']($add7='delete_',$add8=(($attr49=($attr50=posts.__getitem__(i))['post_id']) == null || (($attr50.__is_instance__) && typeof $attr49 == 'function') || (typeof $attr49['__get__'] == 'function')?
							$p['getattr']($attr50, 'post_id'):
							posts.__getitem__(i)['post_id'])));
				self['delete_button']['addClickListener']((($attr51=($attr52=self)['delete_post']) == null || (($attr52.__is_instance__) && typeof $attr51 == 'function') || (typeof $attr51['__get__'] == 'function')?
							$p['getattr']($attr52, 'delete_post'):
							self['delete_post']));
				self['contents']['add']((($attr53=($attr54=self)['delete_button']) == null || (($attr54.__is_instance__) && typeof $attr53 == 'function') || (typeof $attr53['__get__'] == 'function')?
							$p['getattr']($attr54, 'delete_button'):
							self['delete_button']));
			}
			self['add']((($attr55=($attr56=self)['contents']) == null || (($attr56.__is_instance__) && typeof $attr55 == 'function') || (typeof $attr55['__get__'] == 'function')?
						$p['getattr']($attr56, 'contents'):
						self['contents']));
			return null;
		}
	, 1, [null,null,['self'],['posts']]);
		$cls_definition['update_posts'] = $method;
		$method = $pyjs__bind_method2('show_edit_box', function(sender) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}

			self['edit_hidden_button']['setID'](sender['getID']());
			self['edit_hidden_button']['click'](self);
			return null;
		}
	, 1, [null,null,['self'],['sender']]);
		$cls_definition['show_edit_box'] = $method;
		$method = $pyjs__bind_method2('delete_post', function(sender) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				sender = arguments[1];
			}

			self['delete_hidden_button']['setID'](sender['getID']());
			self['delete_hidden_button']['click'](self);
			return null;
		}
	, 1, [null,null,['self'],['sender']]);
		$cls_definition['delete_post'] = $method;
		var $bases = new Array($m['AbsolutePanel']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('HomePanel', $p['tuple']($bases), $data);
	})();
	$m['WritePanel'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'components';
		$method = $pyjs__bind_method2('__init__', function(parent) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				parent = arguments[1];
			}
			var top,contents,$attr68,$attr69,$attr64,$attr65,$attr67,$attr60,$attr61,$attr62,$attr63,$sub8,$sub7,$sub6,$sub5,$div8,$add10,$add11,$add12,$div6,$div7,$div5,$attr59,$attr58,$attr57,$attr70,$add9,$attr66,left;
			$m['AbsolutePanel']['__init__'](self);
			$p['setattr'](self, 'post_header', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'header_label'}, 'Write a Post']));
			$p['setattr'](self, 'post_write_title_label', $m['Label']('Title:'));
			$p['setattr'](self, 'post_title', $m['TextBox']());
			$p['setattr'](self, 'post_content', $m['TextArea']());
			$p['setattr'](self, 'post_button', $m['Button']('Post'));
			$p['setattr'](self, 'cancel_button', $m['Button']('Cancel'));
			$p['setattr'](self, 'error_message_label', $pyjs_kwargs_call(null, $m['Label'], null, null, [{StyleName:'error_message_label'}, '']));
			contents = $pyjs_kwargs_call(null, $m['VerticalPanel'], null, null, [{StyleName:'Contents', Spacing:4}]);
			contents['add']((($attr57=($attr58=self)['post_header']) == null || (($attr58.__is_instance__) && typeof $attr57 == 'function') || (typeof $attr57['__get__'] == 'function')?
						$p['getattr']($attr58, 'post_header'):
						self['post_header']));
			contents['add']((($attr59=($attr60=self)['post_write_title_label']) == null || (($attr60.__is_instance__) && typeof $attr59 == 'function') || (typeof $attr59['__get__'] == 'function')?
						$p['getattr']($attr60, 'post_write_title_label'):
						self['post_write_title_label']));
			contents['add']((($attr61=($attr62=self)['post_title']) == null || (($attr62.__is_instance__) && typeof $attr61 == 'function') || (typeof $attr61['__get__'] == 'function')?
						$p['getattr']($attr62, 'post_title'):
						self['post_title']));
			contents['add']((($attr63=($attr64=self)['post_content']) == null || (($attr64.__is_instance__) && typeof $attr63 == 'function') || (typeof $attr63['__get__'] == 'function')?
						$p['getattr']($attr64, 'post_content'):
						self['post_content']));
			contents['add']((($attr65=($attr66=self)['post_button']) == null || (($attr66.__is_instance__) && typeof $attr65 == 'function') || (typeof $attr65['__get__'] == 'function')?
						$p['getattr']($attr66, 'post_button'):
						self['post_button']));
			contents['add']((($attr67=($attr68=self)['cancel_button']) == null || (($attr68.__is_instance__) && typeof $attr67 == 'function') || (typeof $attr67['__get__'] == 'function')?
						$p['getattr']($attr68, 'cancel_button'):
						self['cancel_button']));
			contents['add']((($attr69=($attr70=self)['error_message_label']) == null || (($attr70.__is_instance__) && typeof $attr69 == 'function') || (typeof $attr69['__get__'] == 'function')?
						$p['getattr']($attr70, 'error_message_label'):
						self['error_message_label']));
			$p['setattr'](self, 'dialog', $pyjs_kwargs_call(null, $m['DialogBox'], null, null, [{glass:true}]));
			self['dialog']['setHTML']('\x3Cb\x3EBlog Post Form\x3C/b\x3E');
			self['dialog']['setWidget'](contents);
			left = $p['__op_add']($add9=(typeof ($div5=$p['__op_sub']($sub5=$m['Window']['getClientWidth'](),$sub6=900))==typeof ($div6=2) && typeof $div5=='number' && $div6 !== 0?
				$div5/$div6:
				$p['op_div']($div5,$div6)),$add10=$m['Window']['getScrollLeft']());
			top = $p['__op_add']($add11=(typeof ($div7=$p['__op_sub']($sub7=$m['Window']['getClientHeight'](),$sub8=600))==typeof ($div8=2) && typeof $div7=='number' && $div8 !== 0?
				$div7/$div8:
				$p['op_div']($div7,$div8)),$add12=$m['Window']['getScrollTop']());
			self['dialog']['setPopupPosition'](left, top);
			self['dialog']['hide']();
			return null;
		}
	, 1, [null,null,['self'],['parent']]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('clear_write_panel', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}

			self['post_title']['setText']('');
			self['post_content']['setText']('');
			self['error_message_label']['setText']('');
			return null;
		}
	, 1, [null,null,['self']]);
		$cls_definition['clear_write_panel'] = $method;
		var $bases = new Array($m['AbsolutePanel']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('WritePanel', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end components */


/* end module: components */


/*
PYJS_DEPS: ['pyjamas.ui.Hidden.Hidden', 'pyjamas', 'pyjamas.ui', 'pyjamas.ui.Hidden', 'pyjamas.ui.TextArea.TextArea', 'pyjamas.ui.TextArea', 'pyjamas.ui.TextBox.TextBox', 'pyjamas.ui.TextBox', 'pyjamas.ui.AbsolutePanel.AbsolutePanel', 'pyjamas.ui.AbsolutePanel', 'pyjamas.ui.DialogBox.DialogBox', 'pyjamas.ui.DialogBox', 'pyjamas.ui.RootPanel.RootPanel', 'pyjamas.ui.RootPanel', 'pyjamas.ui.Button.Button', 'pyjamas.ui.Button', 'pyjamas.ui.Label.Label', 'pyjamas.ui.Label', 'pyjamas.ui.HorizontalPanel.HorizontalPanel', 'pyjamas.ui.HorizontalPanel', 'pyjamas.ui.VerticalPanel.VerticalPanel', 'pyjamas.ui.VerticalPanel', 'pyjamas.ui.HTML.HTML', 'pyjamas.ui.HTML', 'pyjamas.Window']
*/
