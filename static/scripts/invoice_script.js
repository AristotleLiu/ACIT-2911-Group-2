
// To add more Fields to the Invoice Creation page
// ------------------------------------------------------------------leave for now 
// var animalCount = 1;
  
$(document).ready(function() {
    //   $('.extra_animal_field').click(function() {
    
    //     var newAnimal = $('.create_invoice_animal').last().clone();
     
    //     var newClass = 'create_invoice_animal_' + animalCount;
    //     newAnimal.removeClass().addClass(newClass);
      
    //     newAnimal.find('input').val('');
     
    //     newAnimal.find('.extra_animal_field').remove();
    
    //     var deleteButton = $('<a class="delete_animal_field" href="#">Delete Animal</a>');
    //     deleteButton.data('target', '.' + newClass);
    //     newAnimal.append(deleteButton);
      
    //     $('.add_invoice_animal').append(newAnimal);
    //     animalCount++;
    //   });
    // ----------------------------------------------------------------------------------------------------
    
    //   Change color of status Highlight in the View Invoice
      $(document).on('click', '.delete_animal_field', function(e) {
        var targetClass = $(this).data('target');
        $(targetClass).remove();
        e.preventDefault();
      });
    
    if ($('#invoice_status').text().toLowerCase() === 'paid') {
        $('#invoice_status').addClass('green-text');
        } 
        else if ($('#invoice_status').text().toLowerCase() === 'unpaid') {
            $('#invoice_status').addClass('yellow-text');
            } 
        else {
            $('#invoice_status').addClass('red-text');
        }
    });
    
    
    filter.addEventListener("input", filterTable);
    