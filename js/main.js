"use strict"

const productBuy = document.querySelectorAll(".product__buy");
const modalWindow = document.querySelector(".modal-window");
const modalWindowClose = document.querySelector(".modal-window__close");
const inputId = document.querySelector("input[name=\"id_product\"")


productBuy.forEach(item => {
    item.addEventListener("click", () => {
        modalWindow.classList.toggle("active");
        inputId.value = item.dataset.id;
    });
});

modalWindowClose.addEventListener("click", () => {
    modalWindow.classList.toggle("active");
    inputId.value = null;
});