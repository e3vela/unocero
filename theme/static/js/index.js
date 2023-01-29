import '../scss/index.scss'
import initSearchForm from "./search-form"
import initSiteNav from "./site-nav"

const activeClass = '-active';

// Initialize the main navigation toggle
initSiteNav("#site-nav", activeClass)

// Search form
initSearchForm('.site-search:visible', 'button', '.form-wrapper', activeClass);
