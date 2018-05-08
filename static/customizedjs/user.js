$(document).ready(function(){
     $("#adduserform").submit(function(event){
      event.preventDefault();
       alert(baseUrl);
       console.log(baseUrl)
        var url = baseUrl+"admin/";
         $.ajax({
          url: url,
          type:"POST",
             data: {
             'first_name': $("#first_name").val(),
             'last_name': $("#last_name").val(),
              'dob': $("#dob").val(),
              'gender': $("#gender:checked").val(), 
              'email': $("#email").val(), 
              'password': $("#password").val(), 
              'designation': $("#designation").val(),
              'role': $("#role:checked").val(),  
              
             },
             dataType: "json",
             success: function(response){
             if(response){
               console.log(response);
               $('.alert').show();

          
                   window.setTimeout(function() {
                   $(".alert").fadeTo(500, 0).slideUp(500, function(){
                   $(this).remove(); 
                   });
                   location.reload()
                   }, 2000);
               if(response.status==201){
                alert("User Created Successfully!");
                window.location = "admindashboard"; 
               }
               if(response.status==404){
                console.log("Error in creating user")
                 alert("Error in creating user")
               };
               
             }
         },
         error: function (err) {
      
           return false;
         }
 
       });
 
     });
 });