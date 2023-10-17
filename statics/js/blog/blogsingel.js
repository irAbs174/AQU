// تابع برای باز کردن لینک‌ها در پنجره جدید
function openLink(url) {
  window.open(url, "_blank");
}

// افزودن رویداد کلیک به دکمه‌ها
var buttons = document
  .getElementsByClassName("share-buttons")[0]
  .getElementsByTagName("a");
for (var i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener("click", function (event) {
    event.preventDefault(); // جلوگیری از بارگیری لینک در هنگام کلیک
    var serviceName = this.classList[0]; // نام شبکه اجتماعی
    var url = ""; // لینک به اشتراک‌گذاری

    // تنظیم لینک مربوط به هر شبکه اجتماعی
    switch (serviceName) {
      case "telegram":
        url =
          "https://t.me/share?url=" + encodeURIComponent(window.location.href);
        break;
      case "instagram":
        url =
          "https://www.instagram.com/share?url=" +
          encodeURIComponent(window.location.href);
        break;
      case "whatsapp":
        url = "https://wa.me/?text=" + encodeURIComponent(window.location.href);
        break;
      case "email":
        url = "mailto:?body=" + encodeURIComponent(window.location.href);
        break;
      case "linkedin":
        url =
          "https://www.linkedin.com/shareArticle?url=" +
          encodeURIComponent(window.location.href);
        break;
      case "facebook":
        url =
          "https://www.facebook.com/sharer.php?u=" +
          encodeURIComponent(window.location.href);
        break;
    }

    openLink(url);
  });
}
