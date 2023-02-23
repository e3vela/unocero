export default function initDarkThemeToggle(darkThemeToggle) {
    const toggles = document.querySelectorAll(darkThemeToggle);

    toggles.forEach((toggle) => {
        toggle.addEventListener("click", function() {
            document.body.classList.toggle('dark-theme');

            // Change the active class for all toggles
            toggles.forEach((toggle) => {toggle.classList.toggle("-active")});

        });
    });
}
