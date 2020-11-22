function ReloadModules(){
	var XHR = ("onload" in new XMLHttpRequest()) ? XMLHttpRequest : XDomainRequest;
	var xhr = new XHR();
	xhr.open('GET', "http://127.0.0.1:5000/reload_modules", true);
	xhr.onload = function() {
	  alert( this.responseText );
	}
	xhr.onerror = function() {
	  alert( 'Ошибка ' + this.status );
	}
	xhr.send();
}
function ConfirmStopWen(){
	var res=confirm("Вы уверены что хотите остановить веб панель?");
	if(res){
		var XHR = ("onload" in new XMLHttpRequest()) ? XMLHttpRequest : XDomainRequest;
		var xhr = new XHR();
		xhr.open('GET', "http://127.0.0.1:5000/stop_bot", true);
		xhr.send();
	} 
}