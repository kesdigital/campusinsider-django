import "../scss/base.scss";

const burger: HTMLElement = document.querySelector("#burger");
const nav: HTMLElement = document.querySelector("#nav")

burger.addEventListener("click", () => {
  nav.classList.toggle("active");
  burger.classList.toggle("active");
})


const setActive = () => {
  const nav_links = document.getElementById("nav").getElementsByTagName("a")
  const current_path = window.location.href

  for (let i = 0; i < nav_links.length; i++) {
    console.log(nav_links[i].href)
    console.log(current_path)
    if (nav_links[i].href === current_path) {
      nav_links[i].classList.add("current")
    }
  }
}

window.onload = setActive;
