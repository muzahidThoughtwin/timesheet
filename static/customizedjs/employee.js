
  $(document).ready(function() {

	var role = getCookie("role");
	if (role != 3) {
		alert("U r not emplyee")
		// setCookie("Authorization", "");
		// setCookie("id", "");
		// setCookie("role", "");
		// setCookie("user", "");
		// location.replace("login");
	}
});