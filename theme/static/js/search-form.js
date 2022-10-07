export default function initSearchForm(searchToggleSelector, formWrapperSelector, activeClass) {
    const searchToggle = document.querySelector(searchToggleSelector);
    const searchWrapper = document.querySelector(formWrapperSelector);
    const searchForm = searchWrapper.querySelector('form')
    const searchInput = searchWrapper.querySelector('input');

    // Open search form if the user has made a search
    document.addEventListener("DOMContentLoaded", function() {
        if (searchInput && searchInput.value) {
            searchWrapper.classList.add(activeClass);
        }
      });

    // Open form when user clicks on button
    searchToggle.addEventListener('click', function() {

        if (searchWrapper.classList.contains(activeClass)) {
            searchWrapper.classList.remove(activeClass);
        } else {
            searchWrapper.classList.add(activeClass);

            console.log(window.innerWidth);

            // Only focus when the site nav is not a side bar anymore
            if (window.innerWidth > 992) {
                searchInput.focus();

            // Trigger search on mobile
            } else {
                searchForm.submit();
            }
        }
    });

    // Close form when user clicks outside of form
    window.addEventListener('click', function () {
        if (document.activeElement === document.body) {
            if (searchWrapper.classList.contains(activeClass)) {
                searchWrapper.classList.remove(activeClass);
            }
        }
    });

    // Close form when user press ESC
    document.addEventListener('keydown', function(event){
        if(event.key === "Escape"){
            if (searchWrapper.classList.contains(activeClass)) {
                searchWrapper.classList.remove(activeClass);
            }
        }
    });

    // Change icon when form has been submitted
    searchForm.addEventListener('submit', function() {
        // Add class to button so icon can be changed
        if (!searchToggle.classList.contains(activeClass)) {
            searchToggle.classList.add(activeClass);
        }
    });

}
