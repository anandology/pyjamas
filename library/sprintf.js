
// args is a pyjslib.List
// str is a String
function sprintf2(str, args)
{
   if(args)
         alert(args.__class__);
   if(args && args.__class__ != "pyjslib.List")
      args = new pyjslib.List([args]);
   if (!args || pyjslib.len(args) < 1 || !RegExp)
   {
      return;
   }
   var re = /([^%]*)%('.|0|\x20)?(-)?(\d+)?(\.\d+)?(%|b|c|d|u|f|o|s|x|X)(.*)/;
   var a = b = [], numSubstitutions = 0, numMatches = 0;
   while (a = re.exec(str))
   {
      var leftpart = a[1], pPad = a[2], pJustify = a[3], pMinLength = a[4];
      var pPrecision = a[5], pType = a[6], rightPart = a[7];
      
      //alert(a + '\n' + [a[0], leftpart, pPad, pJustify, pMinLength, pPrecision);

      numMatches++;
      if (pType == '%')
      {
         subst = '%';
      }
      else
      {
         if (numSubstitutions >= args.length)
         {
            alert('Error! Not enough function args (' + (args.length - 1) + ', excluding the string)\nfor the number of substitution parameters in string (' + numSubstitutions + ' so far).');
         }
         var param = args.__getitem__(numSubstitutions);
         var pad = '';
                if (pPad && pPad.substr(0,1) == "'") pad = leftpart.substr(1,1);
           else if (pPad) pad = pPad;
         var justifyRight = true;
                if (pJustify && pJustify === "-") justifyRight = false;
         var minLength = -1;
                if (pMinLength) minLength = parseInt(pMinLength);
         var precision = -1;
                if (pPrecision && pType == 'f') precision = parseInt(pPrecision.substring(1));
         var subst = param;
                if (pType == 'b') subst = parseInt(param).toString(2);
           else if (pType == 'c') subst = String.fromCharCode(parseInt(param));
           else if (pType == 'd') subst = parseInt(param) ? parseInt(param) : 0;
           else if (pType == 'u') subst = Math.abs(param);
           else if (pType == 'f') subst = (precision > -1) ? Math.round(parseFloat(param) * Math.pow(10, precision)) / Math.pow(10, precision): parseFloat(param);
           else if (pType == 'o') subst = parseInt(param).toString(8);
           else if (pType == 's') subst = param;
           else if (pType == 'x') subst = ('' + parseInt(param).toString(16)).toLowerCase();
           else if (pType == 'X') subst = ('' + parseInt(param).toString(16)).toUpperCase();
         numSubstitutions++;
      }
      str = leftpart + subst + rightPart;
   }
   return str;
}

/**
*
*  Javascript sprintf
*  http://www.webtoolkit.info/
*
*
**/

// str is a String
// args is a pyjslib.List or pyjslib.Tuple
sprintfWrapper = {

	init : function (str, args) {

        if (args === undefined)
        {
            return null;
        }
        constructor = null;
        if (!pyjslib.is_basetype(args))
            constructor = pyjslib.get_pyjs_classtype(args);

        if(constructor != "pyjslib.List" && constructor != "pyjslib.Tuple")
        {
            args = new pyjslib.List([args]);
        }

       if (pyjslib.len(args) < 1 || !RegExp)
       {
          return null;
       }

		var exp = new RegExp(/(%([%]|(\-)?(\+|\x20)?(0)?(\d+)?(\.(\d)?)?([bcdfosxX])))/g);
		var matches = new Array();
		var strings = new Array();
		var convCount = 0;
		var stringPosStart = 0;
		var stringPosEnd = 0;
		var matchPosEnd = 0;
		var newString = '';
		var match = null;

		while (match = exp.exec(str)) {
			if (match[9]) { convCount += 1; }

			stringPosStart = matchPosEnd;
			stringPosEnd = exp.lastIndex - match[0].length;
			strings[strings.length] = str.substring(stringPosStart, stringPosEnd);
         var param = args.__getitem__(convCount-1);

			matchPosEnd = exp.lastIndex;
			matches[matches.length] = {
				match: match[0],
				left: match[3] ? true : false,
				sign: match[4] || '',
				pad: match[5] || ' ',
				min: match[6] || 0,
				precision: match[8],
				code: match[9] || '%',
				negative: parseInt(param) < 0 ? true : false,
				argument: String(param)
			};
		}
		strings[strings.length] = str.substring(matchPosEnd);

		if (matches.length == 0) { return str; }
		if ((args.length - 1) < convCount) { return null; }

		var code = null;
		var match = null;
		var i = null;

		for (i=0; i<matches.length; i++) {

			if (matches[i].code == '%') { substitution = '%' }
			else if (matches[i].code == 'b') {
				matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(2));
				substitution = sprintfWrapper.convert(matches[i], true);
			}
			else if (matches[i].code == 'c') {
				matches[i].argument = String(String.fromCharCode(parseInt(Math.abs(parseInt(matches[i].argument)))));
				substitution = sprintfWrapper.convert(matches[i], true);
			}
			else if (matches[i].code == 'd') {
				matches[i].argument = String(Math.abs(parseInt(matches[i].argument)));
				substitution = sprintfWrapper.convert(matches[i]);
			}
			else if (matches[i].code == 'f') {
				matches[i].argument = String(Math.abs(parseFloat(matches[i].argument)).toFixed(matches[i].precision ? matches[i].precision : 6));
				substitution = sprintfWrapper.convert(matches[i]);
			}
			else if (matches[i].code == 'o') {
				matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(8));
				substitution = sprintfWrapper.convert(matches[i]);
			}
			else if (matches[i].code == 's') {
				matches[i].argument = String(matches[i].argument)
				matches[i].argument = matches[i].argument.substring(0, matches[i].precision ? matches[i].precision : matches[i].argument.length)
				substitution = sprintfWrapper.convert(matches[i], true);
			}
			else if (matches[i].code == 'x') {
				matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(16));
				substitution = sprintfWrapper.convert(matches[i]);
			}
			else if (matches[i].code == 'X') {
				matches[i].argument = String(Math.abs(parseInt(matches[i].argument)).toString(16));
				substitution = sprintfWrapper.convert(matches[i]).toUpperCase();
			}
			else {
				substitution = matches[i].match;
			}

			newString += strings[i];
			newString += substitution;

		}
		newString += strings[i];

		return newString;

	},

	convert : function(match, nosign){
		if (nosign) {
			match.sign = '';
		} else {
			match.sign = match.negative ? '-' : match.sign;
		}
		var l = match.min - match.argument.length + 1 - match.sign.length;
		var pad = new Array(l < 0 ? 0 : l).join(match.pad);
		if (!match.left) {
			if (match.pad == "0" || nosign) {
				return match.sign + pad + match.argument;
			} else {
				return pad + match.sign + match.argument;
			}
		} else {
			if (match.pad == "0" || nosign) {
				return match.sign + match.argument + pad.replace(/0/g, ' ');
			} else {
				return match.sign + match.argument + pad;
			}
		}
	}
}

sprintf = sprintfWrapper.init;
