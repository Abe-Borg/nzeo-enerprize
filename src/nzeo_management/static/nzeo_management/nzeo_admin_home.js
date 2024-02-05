function setupTable(tableId, itemsPerPage) {
  var $tableBody = $('#' + tableId + ' tbody');
  var $pagination = $('#' + tableId.replace('table', 'pagination-table'));

  // Generate 20 items for the table
  for (var i = 1; i <= 20; i++) {
    $tableBody.append('<tr><th scope="row">' + i + '</th><td>Item ' + i + '</td></tr>');
  }

  var $items = $('#' + tableId + ' tbody tr');
  var numPages = Math.ceil($items.length / itemsPerPage);

  // Initial page setup
  $items.slice(itemsPerPage).hide();
  $pagination.append('<li class="page-item disabled"><a class="page-link" href="#">Previous</a></li>');
  for (var i = 1; i <= numPages; i++) {
    $pagination.append('<li class="page-item ' + (i === 1 ? 'active' : '') + '"><a class="page-link" href="#">' + i + '</a></li>');
  }
  $pagination.append('<li class="page-item ' + (numPages === 1 ? 'disabled' : '') + '"><a class="page-link" href="#">Next</a></li>');

  // Pagination click event
  $pagination.on('click', 'a.page-link', function(e) {
    e.preventDefault();
    var $this = $(this);
    var currentPage = $pagination.find('.active a').text();
    var newPage = $this.text();

    // Determine new page number and range of items to show
    if ($this.parent().hasClass('disabled')) {
      return false;
    } else if (newPage === 'Previous') {
      newPage = parseInt(currentPage, 10) - 1;
    } else if (newPage === 'Next') {
      newPage = parseInt(currentPage, 10) + 1;
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
    if(newPage === 1) {
      $pagination.find('li:first-child').addClass('disabled');
    } else if(newPage === numPages) {
      $pagination.find('li:last-child').addClass('disabled');
    }
  });
}


$(document).ready(function() {
  setupTable('table1', 10); // Setup first table with pagination
  setupTable('table2', 10); // Setup second table with pagination

  var lastTab = null;
  $('[data-custom-toggle="tab"]').click(function(e) {
      e.preventDefault();
      var currentAttrValue = $(this).attr('href');

      // Check if the current tab content is already shown
      if ($(currentAttrValue).hasClass('show')) {
          $(currentAttrValue).collapse('hide');
          $(this).attr('aria-selected', 'false');
          lastTab = null;
      } else {
          // Hide the previous tab content
          if (lastTab) {
              $(lastTab).collapse('hide');
              $('[href="' + lastTab + '"]').attr('aria-selected', 'false');
          }
          // Show the current tab content
          $(currentAttrValue).collapse('show');
          $(this).attr('aria-selected', 'true');
          lastTab = currentAttrValue;
      }

      // Toggle the 'active' class regardless of the collapse state
      $(this).toggleClass('active');
      if(lastTab) {
          $('[href="' + lastTab + '"]').toggleClass('active');
      }
  });
});

