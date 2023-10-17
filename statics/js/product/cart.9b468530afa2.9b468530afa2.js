$(document).ready(function(){
  function separateDigitsWithComma() {
    let total = $('input[name=TOTAL_CART_NAME]').val();
    var numberString = String(total);
    // Split the string into an array of characters
    var digitsArray = numberString.split('');
  
    // Reverse the array to process digits from right to left
    digitsArray.reverse();
  
    // Iterate over the array and insert commas after every third digit
    for (var i = 3; i < digitsArray.length; i += 4) {
      digitsArray.splice(i, 0, ',');
    }
  
    // Reverse the array again to get the original order
    digitsArray.reverse();
  
    // Join the array into a string
    var result = digitsArray.join('');
  
    $('#CART_P_TOTAL').html(`<td id="CART_P_TOTAL">${result}</td>`);
  }
  separateDigitsWithComma();
});
// end readfy
function updateCart(productTitle, productId, productColorQuantity){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let quantity = document.getElementById(productId).value;
  let data = {
    'product_title': productTitle,
    'quantity':quantity,
    'product_color_quantity': productColorQuantity,
    csrfmiddlewaretoken: token,
  }
  $.ajax({
    url: '/cart/update',
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
// remove cart item
function removeItem(productTitle){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let data = {
      'product_title': productTitle,
      csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/remove',
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
function clearCart(){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let productID = $('.quantity').val();
  let data = {
      'product_id': productID,
      csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/clear',
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
function checkout(){
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let data = {
      csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/Get_checkout',
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
        window.location.href = "/cart/checkout";
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