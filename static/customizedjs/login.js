$(document).ready(function(){
     $("#Button2").click(function(event){
      event.preventDefault();
      var url = baseUrl+"login";
   
         $.ajax({
          url:url,
          type:"POST",
             data: {
 
              'inputEmail': $("#Username").val(),
              'inputPassword': $("#Password").val(), 
              
             },
             dataType: "json",
             success: function(response){
             if(response){
               console.log(response);
               setCookie("Authorization", "Token "+response.token);
               setCookie("id", response.id);
               setCookie("role", response.role);
               setCookie("user", response.user);
 
               if(response.role==3){
                 $("#alertmesg").hide();
                 $("#alertsuccess").show();
                 $("#alertsuccess").html("Login Successfully");
                 window.location = "dashboard";
               }
               if(response.role==2){
                 $("#alertmesg").hide();
                 $("#alertsuccess").show();
                 $("#alertsuccess").html("Login Successfully");
               }
               if(response.role==1){
                 $("#alertmesg").hide();
                 $("#alertsuccess").show();
                 $("#alertsuccess").html("Login Successfully");
                 window.location = "../admin/dashboard";
               }
               if(response.status=="404"){
                 $("#alertsuccess")  .hide();
                 $("#alertmesg").show();
                 $("#alertmesg").html("Username or password does not exist");
                 return false;
               };
               if(response.status=="500"){
                 $("#alertsuccess").hide();
                 $("#alertmesg").show();
                 $("#alertmesg").html("Error while login");
                 return false;
               };
 
             } 
             // $("#alertsuccess").hide();
             // $("#alertmesg").show();
             // $("#alertmesg").html("Error while login");
             // return false;
         },
         error: function (err) {
           $("#alertsuccess").hide();
           $("#alertmesg").show();
           $("#alertmesg").html("Something went wrong. Please try again later. ");
           return false;
         }
 
       });
 
     });
 });
 