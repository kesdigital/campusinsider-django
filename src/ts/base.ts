import "../scss/base.scss";

const burger: HTMLElement | null = document.querySelector("#burger");
const nav: HTMLElement | null = document.querySelector("#nav");

if (burger !== null && nav !== null) {
  burger.addEventListener("click", () => {
    nav.classList.toggle("active");
    burger.classList.toggle("active");
  })
}
