$(document).ready(function(){
    var perPage = 8;
    var page = 1;

    function load_last_offers(){
        var startIndex = (page -1) * perPage;
        var endIndex = startIndex + perPage;
        $.getJSON(`/UNIQUEAPI174/pages/?type=product.InventoryItem`, function(data){
            let product_item = data.items;
            if (product_item.length > 0){
                totalPages = Math.ceil(product_item.length / perPage);
                for (let i = startIndex; i < endIndex; i++){
                    if (i >= product_item.length){
                        break;
                    }
                    let productPage = product_item[i];
                    let productPageId = productPage.id;
                    let productPageSlug = productPage.meta.slug;
                    let productPageAPI = `/UNIQUEAPI174/pages/${productPageId}`;
                    $.getJSON(productPageAPI, function(productDATA){
                        let product = productDATA;
                        if (product.PRODUCT_OFFER.length > 0){
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
                        }//end if
                    });// end getJSON
                } //End for
                if (page >= totalPages){
                    $('#load-more').hide();
                }else{
                    $('load-more').show();
                } //end for
                page++;
            }// endProduct_item_length if
        });//End getJSON
    };// end function
    $('load-more').click(function(){
        load_last_offers();
    });
    load_last_offers();
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