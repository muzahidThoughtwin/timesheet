var baseUrl = "http://127.0.0.1:8000/";

var role = getCookie("role");
var urlchecker = $(location).attr('pathname');
urlchecker.indexOf(1);
urlchecker.toLowerCase();
urlchecker = urlchecker.split("/")[1];

if(role == 1 && urlchecker != 'admin' ){
	location.replace("user/login");
}
if(role == 3 && urlchecker != 'user' ){
	location.replace("../../user/login");
}
// if(!role){
// 	location.replace("../../user/login");
// }

