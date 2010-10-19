/* start module: vo */
var vo;
$pyjs.loaded_modules['vo'] = function (__mod_name__) {
	if($pyjs.loaded_modules['vo'].__was_initialized__) return $pyjs.loaded_modules['vo'];
	var $m = vo = $pyjs.loaded_modules["vo"];
	vo.__was_initialized__ = true;
	if ((__mod_name__ === null) || (typeof __mod_name__ == 'undefined')) __mod_name__ = 'vo';
	var __name__ = vo.__name__ = __mod_name__;


	$m['PostVO'] = (function(){
		var $cls_definition = new Object();
		var $method;
		$cls_definition.__module__ = 'vo';
		$cls_definition['post_id'] = null;
		$cls_definition['title'] = null;
		$cls_definition['content'] = null;
		$method = $pyjs__bind_method2('__init__', function(post_id, title, content) {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
				post_id = arguments[1];
				title = arguments[2];
				content = arguments[3];
			}
			if (typeof post_id == 'undefined') post_id=arguments.callee.__args__[3][1];
			if (typeof title == 'undefined') title=arguments.callee.__args__[4][1];
			if (typeof content == 'undefined') content=arguments.callee.__args__[5][1];

			if ($p['bool'](post_id)) {
				$p['setattr'](self, 'post_id', post_id);
			}
			if ($p['bool'](title)) {
				$p['setattr'](self, 'title', title);
			}
			if ($p['bool'](content)) {
				$p['setattr'](self, 'content', content);
			}
			return null;
		}
	, 1, [null,null,['self'],['post_id', null],['title', null],['content', null]]);
		$cls_definition['__init__'] = $method;
		$method = $pyjs__bind_method2('is_empty', function() {
			if (this.__is_instance__ === true) {
				var self = this;
			} else {
				var self = arguments[0];
			}
			var $attr1,$attr2,$attr5,$attr4,$attr6,$attr3;
			if ($p['bool']((($attr1=($attr2=self)['post_id']) == null || (($attr2.__is_instance__) && typeof $attr1 == 'function') || (typeof $attr1['__get__'] == 'function')?
						$p['getattr']($attr2, 'post_id'):
						self['post_id']))) {
				return false;
			}
			if ($p['bool']((($attr3=($attr4=self)['title']) == null || (($attr4.__is_instance__) && typeof $attr3 == 'function') || (typeof $attr3['__get__'] == 'function')?
						$p['getattr']($attr4, 'title'):
						self['title']))) {
				return false;
			}
			if ($p['bool']((($attr5=($attr6=self)['content']) == null || (($attr6.__is_instance__) && typeof $attr5 == 'function') || (typeof $attr5['__get__'] == 'function')?
						$p['getattr']($attr6, 'content'):
						self['content']))) {
				return false;
			}
			return true;
		}
	, 1, [null,null,['self']]);
		$cls_definition['is_empty'] = $method;
		var $bases = new Array($p['object']);
		var $data = $p['dict']();
		for (var $item in $cls_definition) { $data.__setitem__($item, $cls_definition[$item]); }
		return $p['_create_class']('PostVO', $p['tuple']($bases), $data);
	})();
	return this;
}; /* end vo */


/* end module: vo */


