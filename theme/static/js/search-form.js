export default function initSearchForm(searchSelector, toggleSelector, formWrapperSelector, activeClass) {
    const toggleElement = $(searchSelector + ' ' + toggleSelector)[0];
    const searchWrapper = $(searchSelector + ' ' + formWrapperSelector)[0];
    const searchForm = searchWrapper.querySelector('form')
    const searchInput = searchWrapper.querySelector('input');

    // Open search form if the user has made a search
    document.addEventListener("DOMContentLoaded", function() {
        if (searchInput && searchInput.value) {
            searchWrapper.classList.add(activeClass);
        }
      });

    // Open form when user clicks on button
    toggleElement.addEventListener('click', function() {

        if (searchWrapper.classList.contains(activeClass)) {
            searchWrapper.classList.remove(activeClass);
        } else {
            searchWrapper.classList.add(activeClass);

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
        if (!toggleElement.classList.contains(activeClass)) {
            toggleElement.classList.add(activeClass);
        }
    });

}
