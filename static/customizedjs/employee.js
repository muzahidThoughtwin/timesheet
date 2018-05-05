
  $(document).ready(function() {

	var role = getCookie("role");
	if (role != 3) {
		setCookie("Authorization", "");
		setCookie("id", "");
		setCookie("role", "");
		setCookie("user", "");
		location.replace("login");
	}
});