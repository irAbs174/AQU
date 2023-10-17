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