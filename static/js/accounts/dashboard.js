function add_favourite(product_id, product_slug, product_title, product_image, product_quantity, product_color, product_add_cart_date){
    // Data to be sent with the POST request
    let token = $('input[name=csrfmiddlewaretoken]').val();
    let data = {
      'product_id': product_id,
      'product_slug':product_slug,
      'product_title': product_title,
      'product_image': product_image,
      'quantity':product_quantity,
      'selected_color_text':product_color,
      'add_cart_date':product_add_cart_date,
      csrfmiddlewaretoken: token,
    };
    // Send request to server
    $.ajax({
      url: '/cart/favourite/add',
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
  // add comparison
  function add_comparison(product_id, product_slug, product_title, product_image, product_quantity, product_color, product_color_quantity, product_add_cart_date){
    let token = $('input[name=csrfmiddlewaretoken]').val();
    // Data to be sent with the POST request
    let data = {
      'product_id':product_id,
      'product_slug':product_slug,
      'product_title': product_title,
      'product_image': product_image,
      'quantity':product_quantity,
      'selected_color_text':product_color,
      'product_color_quantity':product_color_quantity,
      'add_cart_date':product_add_cart_date,
      csrfmiddlewaretoken: token,
    };
    // Send request to server
    $.ajax({
      url: '/cart/comparison/add',
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
function update_user(){
  let frist_name = document.getElementById('validationCustom01').value;
  let last_name = document.getElementById('validationCustom02').value;
  let email = document.getElementById('validationCustom04').value;
  let oldPass = document.getElementById('validationCustom07').value;
  let newPass1 = document.getElementById('validationCustom08').value;
  let newPass2 = document.getElementById('validationCustom09').value;
  let token = $('input[name=csrfmiddlewaretoken]').val();
  var data = {
    'frist_name': frist_name,
    'last_name': last_name,
    'email':email,
    'old_password': oldPass,
    'new_password': newPass1,
    'confirm_password': newPass2,
    csrfmiddlewaretoken: token,
  }; 
  $.ajax({
    url: '/accounts/update_detail',
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
        location.reload(true)
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
function get_address(){
  let frist_name = document.getElementById('firstName').value;
  let last_name = document.getElementById('lastName').value;
  let address = document.getElementById('address').value;
  let pelak = document.getElementById('address2').value;
  let ostan = document.getElementById('ostan').value;
  let city = document.getElementById('shahr').value;
  let zip_code = document.getElementById('zip').value;
  let token = $('input[name=csrfmiddlewaretoken]').val();
  var data = {
    'first_name': frist_name,
    'last_name': last_name,
    'address': address,
    'pelak': pelak,
    'ostan': ostan,
    'city': city,
    'zip_code': zip_code,
    csrfmiddlewaretoken: token,
  }; 
  $.ajax({
    url: '/accounts/address',
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
        location.reload(true)
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