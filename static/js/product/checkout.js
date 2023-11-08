$(document).ready(function () {
  function separateDigitsWithComma() {
    // Convert the number to a string
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
function order() {
  let token = $('input[name=csrfmiddlewaretoken]').val();
  firstName = document.getElementById('firstName').value;
  lastName = document.getElementById('lastName').value;
  tel = document.getElementById('tel').value;
  email = document.getElementById('email').value;
  State = document.getElementById('State').value;
  City = document.getElementById('City').value;
  nationalcode = document.getElementById('nationalcode').value;
  postalcode = document.getElementById('postalcode').value;
  tel2 = document.getElementById('tel2').value;
  address = document.getElementById('address').value;
  address2 = document.getElementById('address2').value;
  send_method = document.getElementById('validationCustom04').value;
  let data = {
    csrfmiddlewaretoken: token,
    'firstName': firstName,
    'lastName': lastName,
    'tel': tel,
    'email': email,
    'State': State,
    'City': City,
    'nationalcode': nationalcode,
    'postalcode': postalcode,
    'tel2': tel2,
    'address': address,
    'address2': address2,
    'SEND_METHOD': send_method,
  };
  // Send request to server
  $.ajax({
    url: '/get_order/',
    type: 'POST',
    data: data,
    success: function (response) {
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
          timer: 3000,
        });
        window.location.href = "/get_bank";
      }
    },
    error: function (xhr, status, error) {
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
$('.click_fadax_btn').click(function (e) {
  e.preventDefault();
  data = {
    'task': 'recive_payment_token',
  }
  $.ajax({
    url: 'fadax/',
    type: 'POST',
    data: data,
    success: function (response) {
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
          title: 'در حال انتقال به درگاخ فدکس',
          showConfirmButton: false,
          timer: 2000,
        });
        window.location.href = response.status;
      }
    },
    error: function (xhr, status, error) {
      console.log(status);
      Swal.fire({
        icon: "error",
        title: status,
        showConfirmButton: false,
        timer: 3000,
      });
    }
  });
});