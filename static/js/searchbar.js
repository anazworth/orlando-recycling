document.addEventListener('keydown', function(event) {
    // Check if the user is pressing Command (Mac) or Control (Windows/Linux)
    var isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    var commandKey = isMac ? event.metaKey : event.ctrlKey;

    // Check if the key pressed is 'k' and the Command (or Control) key is pressed simultaneously
    if (event.key === 'k' && commandKey) {
        // Prevent the default action of the keypress event
        event.preventDefault();

        // Focus on the search bar
        document.getElementById('searchBar').focus();
    }
});
document.addEventListener('DOMContentLoaded', function() {
    var isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
    var searchKBD = document.getElementById('searchKBD');
    var isMobile = window.matchMedia('(max-width: 768px)').matches;

    if (isMobile) {
        return;
    }

    if (isMac) {
        searchKBD.textContent = '⌘ K'; // Unicode symbol for Command (⌘)
    } else {
        searchKBD.textContent = 'Ctrl K';
    }
});
document.addEventListener('DOMContentLoaded', function() {
    var searchBar = document.getElementById('searchBar');

    // Add event listener for keydown event
    searchBar.addEventListener('keydown', function(event) {
        // Check if the "Escape" key is pressed
        if (event.key === 'Escape') {
            // Unfocus the search bar
            searchBar.blur();
        }
    });
});