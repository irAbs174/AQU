$(document).ready(function() {
    var perPage = 10;
    var page = 1;
    function loadBlogPages() {
      var startIndex = (page - 1) * perPage;
      var endIndex = startIndex + perPage;
  
      $.getJSON(`/UNIQUEAPI174/pages/?type=blog.BlogPage`, function(data) {
        var blogPages = data.items;
        if (blogPages.length > 0) {
          totalPages = Math.ceil(blogPages.length / perPage);
  
          for (var i = startIndex; i < endIndex; i++) {
            if (i >= blogPages.length) {
              break;
            }
  
            var blogPage = blogPages[i];
            var blogPageId = blogPage.id;
            var blogPageSlug = blogPage.meta.slug;
            var blogPostsUrl = `/UNIQUEAPI174/pages/${blogPageId}`;
  
            $.getJSON(blogPostsUrl, function(postsData) {
              var post = postsData;
              var postHTML = `
                  <div class="card" style="width: 18rem">
                  <img
                    id="PostImage"
                    src="${post.image.url}"
                    class="card-img-top"
                    alt="${post.image.alt}"/>
                  <div class="card-body">
                    <h3 id="PostTitle" class="card-title h3">${post.title}</h3>
  
                    <span id="PostAuthor" class="bi bi-person">kik pick</span><br>
                    <span id="PostPublish" class="bi bi-calendar3">${post.jpub}</span>
  
                    <p id="PostIntro" class="card-text">
                      ${post.intro}
                    </p><br>
                    <a id="PostSingle" href="${blogPageSlug}">مشاهده بیشتر</a>
                  </div>
                </div>
              `;
  
              $('#blog_posts_archive').append(postHTML);
            });
          }
  
          if (page >= totalPages) {
            $('#load-more').hide();
          } else {
            $('#load-more').show();
          }
  
          page++;
        } 
      });
    }
    $('#load-more').click(function() {
        loadBlogPages();
      });
  
      loadBlogPages();
  });