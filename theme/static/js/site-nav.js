// import houdini from "houdinijs"

export default function initSiteNav(selector, activeClass) {
  const siteNav = document.querySelector(selector)
  const toggle = document.querySelector(`[data-toggle="#${siteNav.id}"]`)


  // Close the drawer when ESC is pressed and no submenu is open
  document.addEventListener("keydown", event => {
    // Bail if key is not ESC
    if (event.key !== "Escape") return

    // Bail if menu is closed
    if (!siteNav.classList.contains(activeClass)) return

    siteNav.classList.remove(activeClass);
  })

  toggle.addEventListener("click", function() {

    if (siteNav.classList.contains(activeClass)) {
        siteNav.classList.remove(activeClass);
    } else {
        siteNav.classList.add(activeClass);
    }
  });

  // Update the [aria-expanded] attribute on the toggle
//   siteNav.addEventListener("open.houdini", () => {
//     toggle.setAttribute("aria-expanded", true)
//   })
//   siteNav.addEventListener("close.houdini", () => {
//     toggle.setAttribute("aria-expanded", false)
//   })
}
