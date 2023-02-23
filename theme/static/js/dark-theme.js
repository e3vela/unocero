export default function initDarkThemeToggle(darkThemeToggle, darkThemeClass) {
    const toggles = document.querySelectorAll(darkThemeToggle);

    toggles.forEach((toggle) => {
        toggle.addEventListener('click', function() {
            // Add active class to the body
            document.body.classList.toggle(darkThemeClass);

            // Change the active class for all toggles
            toggles.forEach((toggle) => {toggle.classList.toggle('-active')});

            // Save current selected theme
            localStorage.setItem('isDarkThemeSelected', document.body.classList.contains(darkThemeClass));
        });
    });
}
