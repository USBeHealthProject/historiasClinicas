$("#show-view-role").click(function(){
	$('.show-view-role').css('display','block');
});

function show_add_role(){
  hide_modify_role();
  hide_error_role();
  $('.show-add-role').css('display','block');
}

function hide_add_role(){
    $('.show-add-role').hide();
}

function show_error_role(){
  $('.error-role').css('display','block');
}

function hide_error_role(){
    $('.error-role').hide();
}

function show_modify_role(id,name){
  hide_add_role();
  hide_error_role();

  switch (id) {
    case 1:
    case 2:
    case 3:
      console.log(id);
      hide_modify_role();
      $("#error-role-span").html("Este rol no puede ser modificado.");
      show_error_role();
      break;
    default:
      $('.show-modify-role').css('display','block');
      $('#modify-role-input').val(name);
      $('#modify-role-form').val(id);
  }
};

function hide_modify_role(){
    $('.show-modify-role').hide();
}



function delete_role(id){
  hide_add_role();
  hide_modify_role();
  hide_error_role();
  switch (id) {
    case 1:
    case 2:
    case 3:
      console.log(id);
      $("#error-role-span").html("Este rol no puede ser eliminado.");
      show_error_role();
      break;
    default:
      delete_role_ajax(id);
  }
};

function handleData(response){
  k = response.status;
  if (k == "ERROR"){
      $("#error-role").html("Este rol no puede ser eliminado.");
      $('#error-role').css('display','block');
  }
  else{
     $('#show-roles').load(document.URL +  ' #show-roles');
  }
  console.log(k);
}

function delete_role_ajax(id){
      $.ajax({
            type: 'GET',
            url: '/eliminar_rol/' + id,
            data: JSON.stringify(id),
            //async: false,
            contentType:'application/json; charset=utf-8',

            success: function(response) {
              console.log(response);
              var d = response;
              //console.log(d);
              var status = d.status;
              //console.log(status);

              if (status == "ERROR"){
                  $("#error-role-span").html("Este rol no puede ser eliminado.");
                  show_error_role();
                  //console.log(status);
              }
              else{
                 $('#show-roles').load(document.URL +  ' #show-roles');
              }
              //window.location.reload(true);
              //$('#show-roles').load(document.URL +  ' #show-roles');
            },
            error: function(error) {
              console.log(error);
            }
        });
}
