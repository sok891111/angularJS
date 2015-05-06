(function($){
	var root = this;
	if(!$) return

	//사용자 validation 정규식
	$.reg = {
		email : /^[0-9a-zA-Z_\-]+@[0-9a-zA-Z_\-]+(\.[0-9a-zA-Z_\-]+){1,2}$/,
		passwd : /^(?=.*[a-zA-Z])((?=.*\d)|(?=.*\W)).{6,20}$/
	}

	var submitPermission = true;
	$.setSubmitPermisstion = function(permisstion){
		submitPermission = permisstion;
	};
	$.getSubmitPermisstion = function(){
		return submitPermission;
	}
	$.fn.extend({
		validate : function(result, text){
			var select = "#validate_"+this.attr("id");
			$(select+"").remove();
			var elm = this;
			if(result){
				submitPermission = true;
				elm.parent().addClass("has-success").removeClass("has-error");
			}else{
				submitPermission = false;
				var errorMsg = '<label class="control-label" id="validate_'+this.attr("id")+'">'+text+'</label>';
				elm.parent().append($(errorMsg))
				elm.parent().addClass("has-error").removeClass("has-success");
			}
		},
		submit: function(){
			if( this[0].tagName.toLowerCase() != 'form')
				return;
			this.find('input').each(function(){
				var obj = $(this);
				var select = "#validate_"+obj.attr("id");
				$(select+"") ? $(select+"").remove() : null;
				if(obj.attr("required") == "required"){
					var message = obj.parent().find('label').text()+" 는(은) 반드시 입력해주세요."
					obj.validate( obj.val(), message);
				}
			});
			if(submitPermission )
				this[0].submit();
		},
		serializeObject : function(){
		   var o = {};
		   var a = this.serializeArray();
		   $.each(a, function() {
		       if (o[this.name]) {
		           if (!o[this.name].push) {
		               o[this.name] = [o[this.name]];
		           }
		           o[this.name].push(this.value || '');
		       } else {
		           o[this.name] = this.value || '';
		       }
		   });
		   return o;
		},
	});

})(jQuery);