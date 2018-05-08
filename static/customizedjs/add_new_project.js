$(document).ready(function() {
	$("#createprojectform").submit(function(event) {
			event.preventDefault();
			var token = getCookie("Authorization");
			var url = baseUrl+"project/";
			$.ajax({
					headers: {
                  			'Authorization':token,
                  	},
					url: url,
					type: "POST",
					data: {
							'name': $("#projectname").val(),
							'description': $("#projectdescription").val(),
					},
					dataType: "json",
					success: function(response) {
							if (response) {
									console.log(response);
									$('.alert').show();
									// alert("Details updated  ")
									window.setTimeout(function() {
											$(".alert").fadeTo(500, 0).slideUp(500, function() {
													$(this).remove();
											});
											location.reload()
									}, 2000);
									if (response.status == 201) {
											alert("Project Created Successfully!");
											window.location = "admindashboard";
									}
									if (response.status == 404) {
											console.log("Error in creating user")
											alert("Error in creating user")
									};
							}
					},
					error: function(err) {
							// alert("Error");
							return false;
					}
			});
	});
});