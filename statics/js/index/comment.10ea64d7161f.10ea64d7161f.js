var comments = [];

function addComment(event) {
  event.preventDefault();

  var username = document.getElementById("usernameInput").value;
  var comment = document.getElementById("commentInput").value;

  var newComment = {
    username: username,
    comment: comment,
    likes: 0,
    dislikes: 0,
  };

  comments.push(newComment);

  renderComments();

  document.getElementById("usernameInput").value = "";
  document.getElementById("commentInput").value = "";
}

function renderComments() {
  var commentList = document.getElementById("commentList");
  commentList.innerHTML = "";

  comments.forEach(function (comment, index) {
    var commentElement = document.createElement("li");
    commentElement.className = "comment";

    var commentContent =
      "<span class='user'>" +
      comment.username +
      ":<br></span> <span class='content'>" +
      comment.comment +
      "</span>";

    var commentActions = document.createElement("div");
    commentActions.className = "actions";

    var likeButton = document.createElement("button");
    likeButton.innerHTML = "&#128077;";
    likeButton.className = "like";
    likeButton.onclick = function () {
      likeComment(index);
    };

    var dislikeButton = document.createElement("button");
    dislikeButton.innerHTML = "&#128078;";
    dislikeButton.className = "dislike";
    dislikeButton.onclick = function () {
      dislikeComment(index);
    };

    commentActions.appendChild(likeButton);
    commentActions.appendChild(dislikeButton);

    commentElement.innerHTML = commentContent;
    commentElement.appendChild(commentActions);

    commentList.appendChild(commentElement);
  });
}

function likeComment(index) {
  comments[index].likes++;
  renderComments();
}

function dislikeComment(index) {
  comments[index].dislikes++;
  renderComments();
}



// نمایش کامنت‌ها هنگام بارگذاری صفحه
window.onload = renderComments;