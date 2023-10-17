$(document).ready(function(){
    var page = 1;
    function load_brands(){
        var perPage = 10;
        var startIndex = (page - 1) * perPage;
        var endIndex = startIndex + perPage;
        $.getJSON(`/UNIQUEAPI174/pages/?type=brand.BrandPage`, function(data){
            let brand_item = data.items;
            totalPages = Math.ceil(brand_item.length / perPage);
            for (var i = startIndex; i < endIndex; i++) {
              if (i >= brand_item.length) {
                break;
              }
              let brand_page = brand_item[i];
              let brands_API = `/UNIQUEAPI174/pages/${brand_page.id}`;
              $.getJSON(brands_API, function(brandData){
                brand = brandData;
                var postHTML = `
                <div class="cardpro border d-inline-block">
                <img src="${brand.image.url}" class="card-img-top" alt="${brand.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${brand.title}</a>
                  </h3>
                  <hr />
                <div class="tolspro">
                <a href="/category/brands/${brand_page.id}"><button type="submit" class="btn btn-danger addtocard">
                        مشاهده محصولات
                    </button></a>
                </div>
                </div>
              </div>
                `;
                $('#BRAND').append(postHTML);
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
        load_brands();
      });
    load_brands();
});//endReady