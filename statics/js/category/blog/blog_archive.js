$(document).ready(function(){
    function load_blog_category(){
        var perPage = 10;
        var page = 1;
        var startIndex = (page - 1) * perPage;
        var endIndex = startIndex + perPage;
        $.getJSON(`/UNIQUEAPI174/pages/?type=category.CategoryBlog`, function(data){
            let blog_item = data.items;
            totalPages = Math.ceil(blog_item.length / perPage);
            for (var i = startIndex; i < endIndex; i++) {
              if (i >= blog_item.length) {
                break;
              }
              let category_page = blog_item[i];
              let brands_API = `/UNIQUEAPI174/pages/${category_page.id}`;
              $.getJSON(brands_API, function(categoryData){
                category = categoryData;
                var postHTML = `
                <div class="cardpro border d-inline-block">
                <img src="${category.image.url}" class="card-img-top" alt="${category.image.alt}" />
                <div class="card-body">
                  <h3 class="card-title h4">
                    <a href="" class="black-color">${category.title}</a>
                  </h3>
                  <hr />
                <div class="tolspro">
                <a href="/category/posts/${category_page.id}"><button type="submit" class="btn btn-danger addtocard">
                        مشاهده مقالات
                    </button></a>
                </div>
                </div>
              </div>
                `;
                $('#BLOG_CATEGORY').append(postHTML);
              })//getJson:category_API
            }// endFor
            if (page >= totalPages) {
                $('#load-more').hide();
              } else {
                $('#load-more').show();
              }
            page++;
        })//getJSON:category_page
    }
    //.ready
    $('#load-more').click(function() {
        load_blog_category();
      });
    load_blog_category();
});//endReady