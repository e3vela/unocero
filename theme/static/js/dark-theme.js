export default function initDarkThemeToggle(darkThemeToggle) {
    const toggle = document.querySelector(darkThemeToggle);

    toggle.addEventListener("click", function() {
        document.body.classList.toggle('dark-theme');
    });
}
