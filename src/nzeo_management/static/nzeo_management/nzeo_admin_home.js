function setupPagination(tableId, itemsPerPage) {
  var $tableBody = $('#' + tableId + ' tbody');
  var $items = $tableBody.find('tr');
  var numPages = Math.ceil($items.length / itemsPerPage);

  // Clear existing pagination if it exists
  var $existingPagination = $('#' + tableId + '-pagination');
  if ($existingPagination.length) {
    $existingPagination.remove();
  }

  // Create and insert pagination only if we have more than one page
  if (numPages > 1) {
    var $pagination = $('<nav aria-label="Page navigation" id="' + tableId + '-pagination"><ul class="pagination"></ul></nav>').insertAfter($tableBody.parent());

    // Initial page setup
    $items.hide().slice(0, itemsPerPage).show(); // Only show the first page items
    $pagination.find('.pagination').append('<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>');
    for (var i = 1; i <= numPages; i++) {
        $pagination.find('.pagination').append('<li class="page-item ' + (i === 1 ? 'active' : '') + '"><a class="page-link" href="#">' + i + '</a></li>');
    }
    $pagination.find('.pagination').append('<li class="page-item ' + (numPages === 1 ? 'disabled' : '') + '"><a class="page-link" href="#">Next</a></li>');

    // Pagination click event
    $pagination.on('click', 'a.page-link', function(e) {
        e.preventDefault();
        var $this = $(this);
        var $pagination = $this.closest('nav').find('.pagination');
        var currentPage = parseInt($pagination.find('.active a').text(), 10);
        var newPage = $this.text();

        // Determine new page number and range of items to show
        if ($this.parent().hasClass('disabled')) {
            return false;
        } else if (newPage === 'Previous') {
            newPage = currentPage - 1;
        } else if (newPage === 'Next') {
            newPage = currentPage + 1;
        } else {
            newPage = parseInt(newPage, 10);
        }

        var startItem = (newPage - 1) * itemsPerPage;
        var endItem = startItem + itemsPerPage;

        // Show the proper items
        $items.hide().slice(startItem, endItem).show();

        // Update the active state of the pagination links
        $pagination.find('.page-item').removeClass('active').removeClass('disabled');
        $pagination.find('a.page-link').filter(function() {
            return $(this).text() === newPage.toString();
        }).parent().addClass('active');

        // Optionally, disable the Previous/Next buttons
        $pagination.find('li:first-child a').parent().toggleClass('disabled', newPage === 1);
        $pagination.find('li:last-child a').parent().toggleClass('disabled', newPage === numPages);
    });
  }
}

$(document).ready(function() {
  setupPagination('table1', 10); // Setup pagination for the first table
  setupPagination('table2', 10); // Setup pagination for the second table
});
