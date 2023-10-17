$(document).ready(function() {
  function load_products(){
      var perPage = 10;
      var page = 1;
      var startIndex = (page - 1) * perPage;
      var endIndex = startIndex + perPage;
      $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data) {
        var product_item = data.items;
        var totalChild = data.meta.total_count;
        totalPages = Math.ceil(product_item.length / perPage);
        for (var i = startIndex; i < endIndex; i++) {
          if (i >= product_item.length) {
            break;
          }
          var productPage = product_item[i];
          var productPageId = productPage.id;
          var productPageSlug = productPage.meta.slug;
          var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
          $.getJSON(productPostsAPIURL, function(productsData) {
            var product = productsData
            if (product.PRODUCT_OFFER.length > 0) {
              var postHTML = `
              <div class="cardpro border d-inline-block">
              <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
              <div class="card-body">
                <h3 class="card-title h4">
                  <a href="" class="black-color">${product.title}</a>
                </h3>
                <span class="text-decoration-line-through icon2"
                  >${separateDigitsWithComma(product.price)}</span
                >
                <span class="red-color">${separateDigitsWithComma(product.PRODUCT_OFFER[0].value)}<span>تومان</span></span>
                <hr />
              <div class="tolspro">
              <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','0')"></span>
              <a href="${product.meta.html_url}"><button type="submit" class="btn btn-danger addtocard">
                      مشاهده و خرید
                  </button></a>
                  <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
              </div>
              </div>
            </div>
              `;
              $('#PRODUCT').append(postHTML);
            }else{
              var postHTML = `
              <div class="cardpro border d-inline-block">
              <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
              <div class="card-body">
                <h3 class="card-title h4">
                  <a href="" class="black-color">${product.title}</a>
                </h3>
                <span class="red-color">${separateDigitsWithComma(product.price)} <span>تومان</span></span>
                <hr />
              <div class="tolspro">
              <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','0')"></span>
              <a href="${product.meta.html_url}"><button type="submit" class="btn btn-danger addtocard">
                      مشاهده و خرید
                  </button></a>
                  <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
              </div>
              </div>
            </div>
              `;
              $('#PRODUCT').append(postHTML);
            }
          });
  }
    page++;
});
}
function load_products_offer(){
  var perPage = 10;
  var page = 1;
  var startIndex = (page - 1) * perPage;
  var endIndex = startIndex + perPage;
  $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data) {
    var product_item = data.items;
    var totalChild = data.meta.total_count;
    totalPages = Math.ceil(product_item.length / perPage);
    for (var i = startIndex; i < endIndex; i++) {
      if (i >= product_item.length) {
        break;
      }
      var productPage = product_item[i];
      var productPageId = productPage.id;
      var productPageSlug = productPage.meta.slug;
      var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
      $.getJSON(productPostsAPIURL, function(productsData) {
        var product = productsData
        if (product.PRODUCT_OFFER.length > 0) {
          var postHTML = `
          <div class="cardpro border d-inline-block">
          <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
          <div class="card-body">
            <h3 class="card-title h4">
              <a href="" class="black-color">${product.title}</a>
            </h3>
            <span class="text-decoration-line-through icon2"
              >${separateDigitsWithComma(product.price)}</span
            >
            <span class="red-color">${separateDigitsWithComma(product.PRODUCT_OFFER[0].value)}<span>تومان</span></span>
            <hr />
          <div class="tolspro">
          <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','0')"></span>
          <a href="${product.meta.html_url}"><button type="submit" class="btn btn-danger addtocard">
                  مشاهده و خرید
              </button></a>
              <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
          </div>
          </div>
        </div>
          `;
          $('#PRODUCT_OFFER').append(postHTML);
        }
      });
}
page++;
});
}
  function load_blog(){
    var perPage = 8;
    var page = 1;
    var startIndex = (page - 1) * perPage;
    var endIndex = startIndex + perPage;
    $.getJSON(`/UNIQUEAPI174/pages/?type=blog.BlogPage`, function(data) {
      var product_item = data.items;
      var totalChild = data.meta.total_count;
      totalPages = Math.ceil(product_item.length / perPage);
      for (var i = startIndex; i < endIndex; i++) {
        if (i >= product_item.length) {
          break;
        }
        var productPage = product_item[i];
        var productPageId = productPage.id;
        var productPageSlug = productPage.meta.slug;
        var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
        $.getJSON(productPostsAPIURL, function(productsData) {
          var blog = productsData
          var postHTML = `
          <div class="card m-1" style="width: 18rem">
          <img src="${blog.image.url}" class="card-img-top" alt="${blog.title}" />
          <div class="card-body">
              <h3 class="card-title h3">${blog.title}</h3>
              <p class="card-text">${blog.description}</p>
              <a href="${blog.meta.html_url}">مشاهده بیشتر</a>
          </div>
      </div>
          `;
          $('#BLOG_CONTENT').append(postHTML);
        });
}
  page++;
})}
//Doc Ready
load_products();
load_blog();
load_products_offer();
});
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
// seprate digits with comma function
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