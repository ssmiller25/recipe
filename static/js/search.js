// search.js - Fuzzy search logic for Hugo site
// Uses Fuse.js for fuzzy searching

// Load Fuse.js from CDN
(function loadFuseJs() {
  if (!window.Fuse) {
    var script = document.createElement('script');
    script.src = 'https://cdn.jsdelivr.net/npm/fuse.js@7.1.0/dist/fuse.min.js';
    script.onload = initSearch;
    document.head.appendChild(script);
  } else {
    initSearch();
  }
})();

function initSearch() {
  var searchInput = document.getElementById('searchBox');
  var resultsDiv = document.getElementById('searchResults');
  if (!searchInput || !resultsDiv) return;
  // Hide results box initially
  resultsDiv.style.display = 'none';

  fetch('/search.json')
    .then(response => response.json())
    .then(data => {
      var fuse = new Fuse(data, {
        keys: ['title', 'summary'],
        threshold: 0.4,
        ignoreLocation: true,
        minMatchCharLength: 2
      });

      searchInput.addEventListener('input', function() {
        var query = searchInput.value.trim();
        if (!query) {
          resultsDiv.innerHTML = '';
          resultsDiv.style.display = 'none';
          return;
        }
        var results = fuse.search(query);
        resultsDiv.style.display = 'block';
        if (results.length === 0) {
          resultsDiv.innerHTML = '<p>No results found.</p>';
          return;
        }
        resultsDiv.innerHTML = results.map(function(result) {
          var item = result.item;
          return '<div class="search-result">' +
            '<a href="' + item.url + '"><strong>' + item.title + '</strong></a><br>' +
            '<span>' + item.summary + '</span>' +
            '</div>';
        }).join('');
      });
    })
    .catch(function(err) {
      resultsDiv.style.display = 'block';
      resultsDiv.innerHTML = '<p>Error loading search index.</p>';
    });
}
