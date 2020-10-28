this.addEventListener('install', function(event) {
    event.waitUntil(
      caches.open('v1').then(function(cache) {
        return cache.addAll([
            '/Service-workers/',
            '/css/materialize.min.css',
            '/js/materialize.min.js'
        ]);
      })
    );
  });