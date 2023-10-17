$(document).ready(function(){
    function load_blog_posts(){
        let currentPath = window.location.pathname;
        let slug = currentPath.split('/').filter(Boolean).pop();
        $.getJSON(`/UNIQUEAPI174/pages/?type=category.CategoryBlog&id=${slug}`,function(tstData){
          console.log(tstData);
          if(tstData.items.length > 0){
            document.title = `مقالات ${tstData.items[0].title}`;
            $('.blogh1').html(`<h1 class="blogh1 white-color">مقالات ${tstData.items[0].title}</h1>`);
          }else{
            Swal.fire({
              icon: "error",
              title: 'مقاله ای با این دسته بندی یافت نشد',
              showConfirmButton: false,
              timer: 2000,
            });
            window.open('/category/products');
            window.close();
            return;
          }
        })
        var perPage = 10;
        var page = 1;
        var startIndex = (page - 1) * perPage;
        var endIndex = startIndex + perPage;
        $.getJSON(`/UNIQUEAPI174/pages/?type=blog.BlogPage`, function(data){
            let item = data.items;
            totalPages = Math.ceil(item.length / perPage);
            for (var i = startIndex; i < endIndex; i++) {
              if (i >= item.length) {
                break;
              }
              let brand_page = item[i];
              let brands_API = `/UNIQUEAPI174/pages/${brand_page.id}`;
              $.getJSON(brands_API, function(brandData){
                blog = brandData;
                if (blog.collection.id == slug){
                    var postHTML = `
                    <div id="PRODUCT_BODY" class="cardpro" style="width: 18rem">
                      <img src="${blog.image.url}" class="card-img-top" alt="${blog.image.alt}" />
                      <div class="card-body">
                        <h3 class="card-title h4">
                          <a href="" class="black-color">${blog.title}</a>
                        </h3>
                        <hr />
                        <div id="TOOLS" class="tolspro">
                          <span class="price"></span></a>
                          <a href="${blog.meta.html_url}"><button class="btn btn-danger addtocard" type="submit">مشاهده بیشتر</button></a>
                        </div>
                      </div>
                    </div>
                  `;
                    $('#BLOG_CATEGORY_LIST').append(postHTML);
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
        load_blog_posts();
      });
    load_blog_posts();
});//endReady