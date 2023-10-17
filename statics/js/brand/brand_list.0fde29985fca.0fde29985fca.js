$(document).ready(function(){
  var page = 1;
    function load_products(){
        let currentPath = window.location.pathname;
        let slug = currentPath.split('/').filter(Boolean).pop();
        $.getJSON(`/UNIQUEAPI174/pages/?type=brand.BrandPage&id=${slug}`,function(tstData){
          console.log(tstData);
          if(tstData.items.length > 0){
            document.title = `محصولات ${tstData.items[0].title}`;
            $('.blogh1').html(`<h1 class="blogh1 white-color">محصولات ${tstData.items[0].title}</h1>`);
          }else{
            Swal.fire({
              icon: "error",
              title: 'محصولی با این برند یافت نشد',
              showConfirmButton: false,
              timer: 2000,
            });
            window.open('/brand');
            window.close();
            return;
          }
        })
        var perPage = 10;
        var startIndex = (page - 1) * perPage;
        var endIndex = startIndex + perPage;
        $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data){
            let item = data.items;
            totalPages = Math.ceil(item.length / perPage);
            for (var i = startIndex; i < endIndex; i++) {
              if (i >= item.length) {
                break;
              }
              let brand_page = item[i];
              let brands_API = `/UNIQUEAPI174/pages/${brand_page.id}`;
              $.getJSON(brands_API, function(brandData){
                product = brandData;
                if (product.brand.id == slug){
                  if (product.PRODUCT_OFFER.length > 0) {
                    var postHTML = `
                    <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                      <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                      <div class="card-body">
                        <h3 class="card-title h4">
                          <a href="" class="black-color">${product.title}</a>
                        </h3>
                        <span class="text-decoration-line-through icon2">${separateDigitsWithComma(product.price)}</span>
                        <span class="red-color">${separateDigitsWithComma(product.PRODUCT_OFFER[0].value)}<span>تومان</span></span>
                        <hr />
                        <div id="TOOLS" class="tolspro">
                        <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${slug}','${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                          <span class="price"></span></a>
                          <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                          <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${slug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                        </div>
                      </div>
                    </div>
                  `;
                    $('#BRAND_LIST').append(postHTML);
                }else{
                    var postHTML = `
                    <div class="cardpro border d-inline-block">
                    <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                    <div class="card-body">
                      <h3 class="card-title h4">
                        <a href="" class="black-color">${product.title}</a>
                      </h3>
                      <span class="red-color">${separateDigitsWithComma(product.price)}<span>تومان</span></span>
                      <hr />
                    <div class="tolspro">
                    <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${slug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                    <a href="${product.meta.html_url}"><button type="submit" class="btn btn-danger addtocard">
                            مشاهده و خرید
                        </button></a>
                        <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${slug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                    </div>
                  </div>
                    `;
                    $('#BRAND_LIST').append(postHTML);
                }
                }
              })//getJson:brands_API
            }// endFor
            if (page >= totalPages) {
                $('#load-more').hide();
              } else {
                $('#load-more').show();
              }
            page++;
        })//getJSON:brand_page
    }
    //.ready
    $('#load-more').click(function() {
        load_products();
      });
    load_products();
});//endReady
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