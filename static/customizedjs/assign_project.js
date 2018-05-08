$(document).ready(function() {
    $("#Button2").click(function(event) {
        event.preventDefault();
        var nn = $('#test').val();
        alert(nn);
        var url = baseUrl+"admin/assignproject";
        $.ajax({
            url: url,
            type: "POST",
            data: {
                'project': $("#select1").val(),
                'user': $("#select2").val(),
            },
            dataType: "json",
            success: function(response) {

                console.log(response);

                // $("#alertsuccess").hide();
                // $("#alertmesg").show();
                // $("#alertmesg").html("Error while login");
                // return false;
            },
            error: function(err) {
                $("#alertsuccess").hide();
                $("#alertmesg").show();
                $("#alertmesg").html("Something went wrong. Please try again later. ");
                return false;
            }

        });

    });
});