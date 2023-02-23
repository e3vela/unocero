import '../scss/index.scss'
import initSearchForm from "./search-form"
import initSiteNav from "./site-nav"
import initDarkThemeToggle from './dark-theme'

const activeClass = '-active';
const darkThemeClass = 'dark-theme';

// Initialize the main navigation toggle
initSiteNav("#site-nav", activeClass)

// Search form
initSearchForm('.site-search:visible', 'button', '.form-wrapper', activeClass);

// Dark theme
initDarkThemeToggle('.dark-theme-toggle', darkThemeClass);
