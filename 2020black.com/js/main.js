const decrementBtn = document.querySelector(".decrement");
const incrementBtn = document.querySelector(".increment");
const countSpan = document.querySelector(".count");
const addToCartBtn = document.querySelector(".add-to-cart");
let count = 1;
decrementBtn.addEventListener("click", () => {
  if (count > 1) {
    count--;
    countSpan.textContent = count;
  }
});
incrementBtn.addEventListener("click", () => {
  count++;
  countSpan.textContent = count;
});
window.addEventListener("DOMContentLoaded", (event) => {
  const colorOptions = document.querySelectorAll(".color-option");

  colorOptions.forEach((option) => {
    option.addEventListener("click", () => {
      const color = option.style.backgroundColor;
      document.body.style.backgroundColor = color;
    });
  });
});
// =========================
$(document).ready(function () {
  $("#color-select").change(function () {
    var selectedColor = $(this).val();
    $(".selected-color").css("background-color", selectedColor);
  });
});
