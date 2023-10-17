$(document).ready(function () {
  function loadProducts() {
    let page_number = $('input[name=page_number]').val();
    let pagintage_key = $('input[name=pagintage_key]').val();
    data = {
      'page_number': page_number,
      'load_filter': pagintage_key,
    };
    set_page_data('/shop_api/shop_data', data);
    window.scrollTo(0, 0);
  };// end function loadProducts

  function brand_count() {
    $.ajax({
      url: '/shop_api/shop_data',
      type: 'POST',
      data: {
        'page_number': '1',
        'load_filter': 'brand_count_list',
      },
      success: function (response) {
        if (response.success != false) {
          brand = response.context;
          for (let c = 0; c < brand.length; c++) {
            let brand_to_pages = `<ul class="navliststyle asidecat">
            <li class="bbs1px">
              <a href="/category/brands/${brand[c].id}" class="black-color ahover">${brand[c].title}</a>
              <span>${brand[c].count}</span>
            </li>
          </ul>`;
            $('#setBrand').append(brand_to_pages);
          };// end for
        };// end if
      }
    }); // end AJAX
  };// End function

  function cat_count() {
    $.ajax({
      url: '/shop_api/shop_data',
      type: 'POST',
      data: {
        'page_number': '1',
        'load_filter': 'category_count_list',
      },
      success: function (response) {
        if (response.success != false) {
          category = response.context;
          for (let c = 0; c < category.length; c++) {
            let category_to_pages = `<ul class="navliststyle asidecat">
            <li class="bbs1px">
              <a href="/category/products/${category[c].id}" class="black-color ahover">${category[c].title}</a>
              <span>${category[c].count}</span>
            </li>
          </ul>`;
            $('#setCat').append(category_to_pages);
          };// end for
        };// end if
      }
    }); // end AJAX
  };// End function

  loadProducts();
  brand_count();
  cat_count();

});//end ready

function set_page_data(url, data) {
  $('.load-more').show();
  $.ajax({
    url: url,
    type: 'POST',
    data: data,
    success: function (response) {
      if (response.success === false) {
        Swal.fire({
          title: response.status,
          showConfirmButton: false,
          timer: 3000,
        });
      } else {
        $('input[name=page_number]').val(response.next_pagintage);
        $('input[name=pagintage_key]').val(response.pagintage_key);
        let products = response.context;
        for (let i = 0; i < products.length; i++) {
          if (products === 'end'){
            $('.load-more').hide();
            break;
          };//endif
          if (i >= products.length) {
            break;
          };// end if
          let product = products[i];
          if (product.offer > 0) {
            let postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image}" class="card-img-top" alt="${product.title}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="text-decoration-line-through icon2">${separateDigitsWithComma(product.price)}</span>
                  <span class="red-color">${separateDigitsWithComma(product.offer)}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','slug','${product.product_title}','${product.image}','FV','SV','0')"></span>
                    <span class="price"></span></a>
                    <a href="/shop/${product.slug}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','slug','${product.product_title}','${product.image}','FV','SV','1','0')"></span>
                  </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          } else {
            let postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image}" class="card-img-top" alt="${product.title}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${separateDigitsWithComma(product.price)}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', 'slug', '${product.product_title}','${product.image}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.slug}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','slug','${product.product_title}','${product.image}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
            $('#PRODUCT').append(postHTML);
          };
        };
      };
    },
  });
};// end function set_page_data

// Start filters :
$('.default_filter').click(function (e) {
  e.preventDefault();
  $('#PRODUCT').html("");
  data = {
    'page_number': 1,
  };
  set_page_data('/shop_api/shop_data', data);
  window.scrollTo(0, 0);
}); //end default filter

$('.old_filter').click(function (e) {
  e.preventDefault();
  $('#PRODUCT').html("");
  data = {
    'page_number': 1,
    'load_filter': 'old_filter',
  };
  set_page_data('/shop_api/shop_data', data);
  window.scrollTo(0, 0);
}); //end expensive filter

$('.expensive_filter').click(function (e) {
  e.preventDefault();
  $('#PRODUCT').html("");
  data = {
    'page_number': 1,
    'load_filter': 'expensive_filter',
  };
  set_page_data('/shop_api/shop_data', data);
  window.scrollTo(0, 0);
}); //end expensive filter

$('.cheapest_filter').click(function (e) {
  e.preventDefault();
  $('#PRODUCT').html("");
  data = {
    'page_number': 1,
    'load_filter': 'cheapest_filter',
  };
  set_page_data('/shop_api/shop_data', data);
  window.scrollTo(0, 0);
}); //end cheapest_filter filter

$('#rangePriceFilter').click(function (e) {
  e.preventDefault();
  let minPrice = document.getElementById("min-price").value;
  let maxPrice = document.getElementById("max-price").value;
  if(minPrice != ''){
    if(maxPrice != ''){
      $('#PRODUCT').html("");
      data = {
        'page_number': 1,
        'minPrice': minPrice,
        'maxPrice': maxPrice,
        'load_filter': 'price_filter',
      };
      set_page_data('/shop_api/shop_data', data);
      $('#min-price').val(minPrice);
      $('#max-price').val(maxPrice);
      window.scrollTo(0, 0);
    }
  }else{
    Swal.fire({
      title: 'ابتدا مقادیر بیشترین و کمترین قیمت را وارد نمایید',
      showConfirmButton: false,
      timer: 3000,
    });
  };;//ENDIF
}); //end expensive filter

$('.load-more').click(function (e) {
  e.preventDefault();
  let page_number = $('input[name=page_number]').val();
  let pagintage_key = $('input[name=pagintage_key]').val();
  let minPrice = document.getElementById("min-price").value;
  let maxPrice = document.getElementById("max-price").value;
  data = {
    'page_number': page_number,
    'load_filter': pagintage_key,
    'minPrice': minPrice,
    'maxPrice': maxPrice,
  };
  set_page_data('/shop_api/shop_data', data);
}); //end cheapest_filter filter

function add_favourite(product_id, product_slug, product_title, product_image, product_quantity, product_color, product_add_cart_date) {
  // Data to be sent with the POST request
  let token = $('input[name=csrfmiddlewaretoken]').val();
  let data = {
    'product_id': product_id,
    'product_slug': product_slug,
    'product_title': product_title,
    'product_image': product_image,
    'quantity': product_quantity,
    'selected_color_text': product_color,
    'add_cart_date': product_add_cart_date,
    csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/favourite/add',
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
          timer: 2000,
        });
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
// add comparison
function add_comparison(product_id, product_slug, product_title, product_image, product_quantity, product_color, product_color_quantity, product_add_cart_date) {
  let token = $('input[name=csrfmiddlewaretoken]').val();
  // Data to be sent with the POST request
  let data = {
    'product_id': product_id,
    'product_slug': product_slug,
    'product_title': product_title,
    'product_image': product_image,
    'quantity': product_quantity,
    'selected_color_text': product_color,
    'product_color_quantity': product_color_quantity,
    'add_cart_date': product_add_cart_date,
    csrfmiddlewaretoken: token,
  };
  // Send request to server
  $.ajax({
    url: '/cart/comparison/add',
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
          timer: 2000,
        });
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

// فیلتر - چک باکس
var specialDiscountCheckbox = document.getElementById("specialdiscount");
// Offer CheckBox ! =>CHANGE<=
specialdiscount.addEventListener("change", function () {
  window.scrollTo(0, 0);
  if (specialdiscount.checked) {
    $.ajax({
      url: '/shop_api/shop_data',
      type: 'POST',
      data: {'page_number': 1, 'load_filter': 'offer_products_list'},
      success: function (response) {
        if (response.success === false) {
          Swal.fire({
            title: response.status,
            showConfirmButton: false,
            timer: 3000,
          });
        } else {
          $('input[name=page_number]').val(response.next_pagintage);
          $('input[name=pagintage_key]').val(response.pagintage_key);
          let products = response.context;
          for (let i = 0; i < products.length; i++) {
            if (i >= products.length) {
              break;
            };// end if
            let product = products[i];
              let postHTML = `
            <div class="cardpro border d-inline-block">
            <img src="${product.image}" class="card-img-top" alt="${product.title}" />
            <div class="card-body">
              <h3 class="card-title h4">
                <a href="" class="black-color">${product.title}</a>
              </h3>
              <span class="text-decoration-line-through icon2"
                >${separateDigitsWithComma(product.price)}</span
              >
              <span class="red-color">${separateDigitsWithComma(product.offer)}<span>تومان</span></span>
              <hr />
            <div class="tolspro">
            <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','','${product.product_title}','${product.image}','FV','SV','0')"></span>
            <a href="/shop/${product.slug}"><button type="submit" class="btn btn-danger addtocard">
                    مشاهده و خرید
                </button></a>
                <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
            </div>
            </div>
          </div>
              `;
              $('#PRODUCT').append(postHTML);
          };
        };
      },
    });
  } else {
    let page_number = $('input[name=page_number]').val();
    let pagintage_key = $('input[name=pagintage_key]').val();
    data = {
      'page_number': page_number,
      'pagintage_key': pagintage_key,
    };
    set_page_data('/shop_api/shop_data', data);
    window.scrollTo(0, 0);
  }
});


var pageXZ = 1;
specialDiscountCheckbox.addEventListener("change", function () {
  var perPage = 8;
  var startIndex = (pageXZ - 1) * perPage;
  var endIndex = startIndex + perPage;
  if (specialDiscountCheckbox.checked) {
    $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&is_available=true&limit=${perPage}&offset=${startIndex}`, function (data) {
      var product_item = data.items;
      if (product_item.length > 0) {
        totalPages = Math.ceil(data.meta.total_count / perPage);
        $('#PRODUCT').html("");
        for (var i = 0; i < product_item.length; i++) {
          if (i >= product_item.length) {
            break;
          }
          var productPage = product_item[i];
          var productPageId = productPage.id;
          var productPageSlug = productPage.meta.slug;
          var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
          $.getJSON(productPostsAPIURL, function (productsData) {
            var product = productsData;
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
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                    <span class="price"></span></a>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                  </div>
                </div>
              </div>
            `;
              $('#PRODUCT').append(postHTML);
            } else {
              var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${separateDigitsWithComma(product.price)}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
              $('#PRODUCT').append(postHTML);
            }

          });
        }
        if (pageXZ >= totalPages) {
          $('#load-more').hide();
        } else {
          $('#load-more').show();
        }

        pageXZ++;
      }
    });
  } else {
    $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem&limit=${perPage}&offset=${startIndex}`, function (data) {
      var product_item = data.items;
      if (product_item.length > 0) {
        totalPages = Math.ceil(data.meta.total_count / perPage);
        $('#PRODUCT').html("");
        for (var i = 0; i < product_item.length; i++) {
          if (i >= product_item.length) {
            break;
          }
          var productPage = product_item[i];
          var productPageId = productPage.id;
          var productPageSlug = productPage.meta.slug;
          var productPostsAPIURL = `/UNIQUEAPI174/pages/${productPageId}`;
          $.getJSON(productPostsAPIURL, function (productsData) {
            var product = productsData;
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
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                    <span class="price"></span></a>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                  </div>
                </div>
              </div>
            `;
              $('#PRODUCT').append(postHTML);
            } else {
              var postHTML = `
              <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                <img src="${product.image.url}" class="card-img-top" alt="${product.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${product.title}</a>
                  </h3>
                  <span class="red-color">${separateDigitsWithComma(product.price)}<span>تومان</span></span>
                  <hr />
                  <div id="TOOLS" class="tolspro">
                  <span class="bi bi-heart black-color"onclick="add_favourite('${product.id}', '${productPageSlug}', '${product.product_title}','${product.image.url}','FV','SV','0')"></span>
                  <span class="price"></span>
                    <a href="${product.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده و خرید</button></a>
                    <span class="bi bi-arrow-left-right" onclick="add_comparison('${product.id}','${productPageSlug}','${product.product_title}','${product.image.url}','FV','SV','1','0')"></span>
                    </div>
                </div>
              </div>
            `;
              $('#PRODUCT').append(postHTML);
            }

          });
        }
        if (pageXZ >= totalPages) {
          $('#load-more').hide();
        } else {
          $('#load-more').show();
        }

        pageXZ++;
      } else {
        Swal.fire({
          title: "محصولی برای نمایش با این فیلتر وجود ندارد",
          showConfirmButton: false,
          timer: 2000,
        });
      }
    });
  }
});
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