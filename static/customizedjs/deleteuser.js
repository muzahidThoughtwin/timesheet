 $(document).ready(function() {
          $("#deletenow").click(function(event) {
                event.preventDefault();
                var id = $("#inputid").val();
                var token = getCookie("Authorization");
                var url = baseUrl+"user/";
                $.ajax({
                     headers: {
                        'Authorization':token,
                     },
                      url: url + id,
                      type: "delete",
                      dataType: "json",
                      success: function(response) {
                            if (response) {
                                 console.log(response);
                                 $('.alert').show();
                                 window.setTimeout(function() {
                                 $(".alert").fadeTo(500, 0).slideUp(500, function(){
                                 $(this).remove(); 
                                 });
                                 location.reload()
                                 }, 2000);
                            }
                      },
                      error: function(err) {
                            // alert("Error");
                            return false;
                      }

                });

          });
    });

