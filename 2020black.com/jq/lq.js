$(".addtocard").click(function () {
  Swal.fire({
    icon: "success",
    title: "با موفقیت انجام شد",
    showConfirmButton: false,
    timer: 2000,
  });
});

$(document).ready(function () {
  $(".pcontent").magicTabs({
    headingTag: "h4",
  });
});
