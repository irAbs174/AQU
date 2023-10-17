function support(user){
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let support_status = 'active';
    let data = {
      'support_room': user,
      'support_status': support_status,
      csrfmiddlewaretoken: token,
    }
    $.ajax({
      url: '/support/add',
      type: 'POST',
      data: data,
      success: function(response) {
        if (response.success === false) {
          Swal.fire({
            icon: "error",
            title: response.status,
            showConfirmButton: false,
            timer: 3000,
          });
        } else {
          Swal.fire({
            icon: "success",
            title: response.status,
            showConfirmButton: false,
            timer: 2000,
          });
          window.open('/support/' + user + '/', '_blank');
        }
      },
      error: function(xhr, status, error) {
        console.log(status);
        Swal.fire({
          icon: "error",
          title: status,
          showConfirmButton: false,
          timer: 3000,
        });
      }
    });
}