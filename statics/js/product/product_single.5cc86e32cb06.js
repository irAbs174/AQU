// set Variable
var product
var productPages
let count = 1;
let color_quantity_dict = {};
let countSpan = document.querySelector(".count");
let decrementBtn = document.querySelector(".decrement");
let incrementBtn = document.querySelector(".increment");
var cart_create_date = '0'
var product_slug;
$(document).ready(function() {
  $(".pcontent").magicTabs({
    headingTag: "h4",
  });
  // load page
  function loadPages() {
    var currentPath = window.location.pathname;
    var slug = currentPath.split('/').filter(Boolean).pop();
    $.getJSON(`/UNIQUEAPI174/pages/?slug=${slug}`, function(data) {
      productPages = data.items[0];
      // set product id to input
      let get_add_product_id = `<input id="add_to_cart_product" type="hidden" name="product_id" value="${productPages.id}"></input>`;
      $('input[name=product_id').text(get_add_product_id);
      // get product detail
      $.getJSON(`/UNIQUEAPI174/pages/${productPages.id}`, function(Data) {
        product = Data;
        // set page title
        document.title = product.title;
        // set product name to input
        let get_add_product_title = `<input id="add_to_cart_product_title" type="hidden" name="product_title" value="${product.product_title}">`;
        $('input[name=product_title]').html(get_add_product_title);
        // set cart image to input
        let get_add_cart_image = `<input id="add_to_cart_image" type="hidden" class="color-input" name="product_image_url" value="${product.image.full_url}">`;
        $('input[name=product_image_url]').html(get_add_cart_image);
        // Define variables
        let get_product_title = `<h1 class="blogh1 white-color">${product.title}</h1>`;
        let get_product_head = `<li>
        <a href="https://www.kikpick.com" class="text-light-emphasis">کیک پیک</a>
      </li>
      <li><a href="/category/brands/${product.brand.id}" class="text-light-emphasis">${product.brand.title}</a></li>
      <li>
        <a href="${product.meta.html_url}" class="text-light-emphasis">${product.product_title}</a>
      </li>`;
        let get_product_model_title = `<h1 id="product_model_title" class="blog-post-title h2">${product.product_title}</h1>`;
        let get_product_model_cat = `<a id="product_model_cat" href="/category/brands/${product.brand.id}">${product.brand.title}</a>`;
        let get_old_product_price = `<span id="old_product_price" class="h4 text-decoration-line-through icon2">${separateDigitsWithComma(product.price)} تومان</span>`;
        let get_product_price = `<span id="product_price" class="h1">${separateDigitsWithComma(product.price)} تومان</span>`;
        let get_product_short_desc = `<p id="product_short_desc">${product.short_description}</p>`;
        let get_product_desc = `<p id="product_short_desc">${product.description}</p>`;
        product_slug = slug;
        let get_product_table = `<tr class="trtd-a">
        <td>نوع محصول:</td>
        <td>${product.product_type}</td>
      </tr>
      <tr>
      <td>برند محصول:</td>
      <td>${product.brand.title}</td>
    </tr>
      <tr class="trtd-a">
      <td>جنس محصول:</td>
      <td>${product.product_jense}</td>
    </tr>
      <tr>
        <td>جنس محصول:</td>
        <td>${product.product_jense}</td>
      </tr>
      <tr class="trtd-a">
        <td>وزن محصول:</td>
        <td>${product.product_wight}</td>
      </tr>
      <tr>
        <td>ابعاد خارجی محصول:</td>
        <td>${product.product_abad}</td>
      </tr>
      <tr class="trtd-a">
        <td>سایز محصول:</td>
        <td>${product.product_size}</td>
      </tr>
      <tr>
        <td>گارانتی محصول:</td>
        <td>${product.product_garr}</td>
      </tr>`;
        let slideimg=[
          product.image.url,
        ];
        let colorOptions = '';
        if(product.PRODUCT_OFFER.length > 0){
          cart_create_date = product.PRODUCT_OFFER[0].value;
        }
        if (product.PRODUCT_COLORS.length > 0) {
          for (let j = 0; j < product.PRODUCT_COLORS.length; j++) {
            colorOptions += `<option value="${product.PRODUCT_COLORS[j].color}"selected>${product.PRODUCT_COLORS[j].color_title}</option>`;
            color_quantity_dict[product.PRODUCT_COLORS[j].color] = product.PRODUCT_COLORS[j].pquantity;
            if(j < product.PRODUCT_COLORS.length){
              let selectedValue = product.PRODUCT_COLORS[j].color
              let selectedColorDiv = document.querySelector('.selected-color');
              let colorSelect = document.getElementById('color-select');
              let selectedOption = colorSelect.options[colorSelect.selectedIndex];
              let optionText = product.PRODUCT_COLORS[j].color
              let color_quantity = color_quantity_dict[optionText];
              let get_add_to_cart_color_text = `<input id="add_to_cart_color_text" type="hidden" class="color-input" name="selected_color_text" value="${optionText}"></input>`;
              $('#add_to_cart_color_text').html(get_add_to_cart_color_text);
              $('input[name=product_color_quantity]').val(optionText);
              selectedColorDiv.style.backgroundColor = selectedValue;

            }
          }
        }
        let colorSelect = `
          <select id="color-select" class="color-select">
            ${colorOptions}
          </select>
        `;
        if (product.PRODUCT_SLIDE.length > 0) {
          for (var k = 0; k < product.PRODUCT_SLIDE.length; k++) {
            slideimg.push(product.PRODUCT_SLIDE[k].image.url);
          }}
        $("#gpro").zoomy(slideimg, {
          height: 368,
        });
        // Start send context to html page
        if(product.is_active && product.is_available){
          if(cart_create_date != '0'){
            $('#product_title').html(get_product_title);
            $('#product_head').append(get_product_head);
            $('#product_model_title').html(get_product_model_title);
            $('#product_model_cat').html(get_product_model_cat);
            $('#product_short_desc').html(get_product_short_desc);
            $('#old_product_price').html(get_old_product_price);
            $('#product_price').html(`<span id="product_price" class="h1">${separateDigitsWithComma(product.PRODUCT_OFFER[0].value)} تومان</span>`);
            $('#color-select').html(colorSelect);
            $('#product_desc').html(get_product_desc);
            $('#product_table').html(get_product_table);
            $('#product_is_available').html(`<h4 id="product_is_available" class="h4 mt-2 text-center">محصول در انبار موجود میباشد</h4>`);
          }else{
            $('#product_title').html(get_product_title);
            $('#product_head').append(get_product_head);
            $('#product_model_title').html(get_product_model_title);
            $('#product_model_cat').html(get_product_model_cat);
            $('#product_short_desc').html(get_product_short_desc);
            $('#old_product_price').html(``);
            $('#product_price').html(get_product_price);
            $('#color-select').html(colorSelect);
            $('#product_desc').html(get_product_desc);
            $('#product_table').html(get_product_table);
            $('#product_is_available').html(`<h4 id="product_is_available" class="h4 mt-2 text-center">محصول در انبار موجود میباشد</h4>`);
          }
        }else{
          if(cart_create_date != '0'){
            $('#product_title').html(get_product_title);
            $('#product_head').append(get_product_head);
            $('#product_model_title').html(get_product_model_title);
            $('#product_model_cat').html(get_product_model_cat);
            $('#product_short_desc').html(get_product_short_desc);
            $('#old_product_price').html(get_old_product_price);
            $('#product_price').html(`<span id="product_price" class="h1">${separateDigitsWithComma(product.PRODUCT_OFFER[0].value)} تومان</span>`);
            $('#color-select').html(colorSelect);
            $('#product_desc').html(get_product_desc);
            $('#product_table').html(get_product_table);
            $('#product_is_available').html(`<h4 id="product_is_available" class="h4 mt-2 text-center">محصول در انبار موجود نیست</h4>`);
          }else{
            $('#product_title').html(get_product_title);
            $('#product_head').append(get_product_head);
            $('#product_model_title').html(get_product_model_title);
            $('#product_model_cat').html(get_product_model_cat);
            $('#product_short_desc').html(get_product_short_desc);
            $('#old_product_price').html(``);
            $('#product_price').html(get_product_price);
            $('#color-select').html(colorSelect);
            $('#product_desc').html(get_product_desc);
            $('#product_table').html(get_product_table);
            $('#product_is_available').html(`<h4 id="product_is_available" class="h4 mt-2 text-center">محصول در انبار موجود نیست</h4>`);
          }
        }
      });
    });
  }
  // Add to cart button
  $('#add_cart_btn').click(function(e) {
    e.preventDefault();
    // Select product values from html document
    let product_title = $('#add_to_cart_product_title').val();
    let product_quantity = $('#count').text();
    let product_color = $('#color-select').val();
    let product_color_quantity = color_quantity_dict[product_color];
    let product_add_cart_date = cart_create_date;
    let token = $('input[name=csrfmiddlewaretoken]').val();
    // Data to be sent with the POST request
    let data = {
      'product_id':productPages.id,
      'product_title': product_title,
      'product_collection': product.collection.id,
      'quantity':product_quantity,
      'selected_color_text':product_color,
      'product_color_quantity':product_color_quantity,
      'product_image_url':product.image.url,
      'add_cart_date':product_add_cart_date,
      csrfmiddlewaretoken: token,
    };
    // Send request to server
    $.ajax({
      url: '/cart/add',
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
  });
// add to favourite
$('#add_favourite').click(function(e) {
  e.preventDefault();
  // Select product values from html document
  let product_title = $('#add_to_cart_product_title').val();
  let product_quantity = $('#count').text();
  let product_color = $('#color-select').val();
  let product_color_quantity = color_quantity_dict[product_color];
  let product_add_cart_date = cart_create_date;
  let token = $('input[name=csrfmiddlewaretoken]').val();
  // Data to be sent with the POST request
  let data = {
    'product_id':productPages.id,
    'product_title': product_title,
    'product_collection': product.collection.id,
    'quantity':product_quantity,
    'selected_color_text':product_color,
    'product_color_quantity':product_color_quantity,
    'product_image_url':product.image.url,
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
});
  let selectElement = document.getElementById('color-select');
  selectElement.addEventListener('change', (event) => {
    // Color Select
    let selectedValue = event.target.value;
    let selectedColorDiv = document.querySelector('.selected-color');
    let colorSelect = document.getElementById('color-select');
    let selectedOption = colorSelect.options[colorSelect.selectedIndex];
    let optionText = event.target.value;
    let color_quantity = color_quantity_dict[optionText];
    let get_add_to_cart_color_text = `<input id="add_to_cart_color_text" type="hidden" class="color-input" name="selected_color_text" value="${optionText}"></input>`;
    let get_add_to_cart_color_quantity = `<input id="add_to_cart_color_quantity" type="hidden" class="color-input" name="product_color_quantity" value="${color_quantity}">`;
    $('#add_to_cart_color_text').html(get_add_to_cart_color_text);
    $('input[name=product_color_quantity]').html(get_add_to_cart_color_quantity);
    selectedColorDiv.style.backgroundColor = selectedValue;
  });
  
  // Count Select
  decrementBtn.addEventListener("click", () => {
    if (count > 1) {
      count--;
      countSpan.textContent = count;
      let get_add_to_cart_quantity = `<input id="add_to_cart_quantity" type="hidden" name="quantity" value="${count}" min="1"></input>`;
      $('#add_to_cart_quantity').html(get_add_to_cart_quantity);
    }
  });
  incrementBtn.addEventListener("click", () => {
    count++;
    console.log(count);
    countSpan.textContent = count;
    let get_add_to_cart_quantity = `<input id="add_to_cart_quantity" type="hidden" name="quantity" value="${count}" min="1"></input>`;
    $('#add_to_cart_quantity').html(get_add_to_cart_quantity);
  });
  //SOME LOADS
  loadPages();
});
// Add to comparison
function add_comparison(){
  let product_title = $('#add_to_cart_product_title').val();
  let product_quantity = $('#count').text();
  let product_color = $('#color-select').val();
  let product_color_quantity = color_quantity_dict[product_color];
  let product_add_cart_date = cart_create_date;
  let token = $('input[name=csrfmiddlewaretoken]').val();
  // Data to be sent with the POST request
  let data = {
    'product_id':productPages.id,
    'product_slug':product_slug,
    'product_title': product_title,
    'product_image': product.image.url,
    'product_collection': product.collection.id,
    'quantity':product_quantity,
    'selected_color_text':product_color,
    'product_color_quantity':product_color_quantity,
    'product_image_url':product.image.url,
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
// Add to comparison
function add_favourite(){
  let product_title = $('#add_to_cart_product_title').val();
  let product_quantity = $('#count').text();
  let product_color = $('#color-select').val();
  let product_color_quantity = color_quantity_dict[product_color];
  let product_add_cart_date = cart_create_date;
  let token = $('input[name=csrfmiddlewaretoken]').val();
  // Data to be sent with the POST request
  let data = {
    'product_id':productPages.id,
    'product_slug':product_slug,
    'product_title': product_title,
    'product_image': product.image.url,
    'product_collection': product.collection.id,
    'quantity':product_quantity,
    'selected_color_text':product_color,
    'product_color_quantity':product_color_quantity,
    'product_image_url':product.image.url,
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
function separateDigitsWithComma(number) {
  // Convert the number to a string
  var numberString = String(number);

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

  return result;
}