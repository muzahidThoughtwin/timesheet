$(document).ready(function(event) {      
    var el = document.getElementsByName("csrfmiddlewaretoken");
     // csrf_value = el[0].getAttribute("value");
    var url = "http://127.0.0.1:8000/admin/viewuserprojects";
    var token = getCookie("Authorization");
    console.log(token)
    $.ajax({
        headers: {
                  'Authorization':token,
                  
                  },
        url: url,
        type: "POST",
        data:{
           // 'csrfmiddlewaretoken':csrf_value
        },
        dataType: "json",
        success: function(resp) {
            if (resp) {
                console.log(resp);
                var len=resp.length;
                var trHTML = '';
                console.log(len)
                for(i=0;i<len;i++){

                  trHTML +=
                            '<tr><td>'
                            + resp[i].id
                            + '</td><td>'
                            + resp[i].name
                            + '</td><td>'
                            + resp[i].description 
                            + '</td><td>'
                            + resp[i].created_at
                            + '</td></tr>';
           
                }
                $('#tBody').append(trHTML);
                



                if (resp.status == 200) {
                    alert("Got details!");
                    console.log("response 200 coming");
                }
                

            }
        },
        error: function(err) {
            // alert("Error");
            return false;
        }

    });
});
