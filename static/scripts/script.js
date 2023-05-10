const deleteItem = (element) => {
    const thread = element.parentNode.parentNode;
    const animalId = thread.querySelector(".animalID").innerText;
    
    fetch(`http://127.0.0.1:5000/animal/${animalId}`, {
        method: 'DELETE'
    }).then(response => console.log(response));

    thread.remove()
}

const addItem = (element) => {
    setTimeout(() => location.reload(), 100)
}

const renderModal = async (element) => {
    try {
        const modalTarget = element.getAttribute("data-target");
        // Get the animal ID
        const thread = element.parentNode.parentNode;
        const animalId = thread.querySelector(".animalID").innerText;
    
        // Make a GET request to the server to fetch the animal data
        const response = await fetch(`/animal/${animalId}`);
        if (!response.ok) {
          throw new Error('Failed to fetch animal data');
        }
    
        // Parse the response JSON data and populate the modal form fields
        const animalData = await response.json();
        if (modalTarget == "#edit-animal-modal") {
            document.querySelector(modalTarget + ' #modal-form').action = `/animal/${animalData.id}`;
            document.querySelector(modalTarget + ' #name').value = animalData.name;
            document.querySelector(modalTarget + ' #age').value = animalData.age;
            document.querySelector(modalTarget + ' #gender').value = animalData.gender;
            document.querySelector(modalTarget + ' #species').value = animalData.species;
            document.querySelector(modalTarget + ' #price').value = animalData.price;
            document.querySelector(modalTarget + ' #purchase_price').value = animalData.purchase_price; 
            document.querySelector(modalTarget + ' #purchase_date').value = (new Date(animalData.purchase_date)).toISOString().split('T')[0]
            document.querySelector(modalTarget + ' #sold_date').value = (new Date(animalData.sold_date)).toISOString().split('T')[0];
            document.querySelector(modalTarget + ' #weight').value = animalData.weight;
            document.querySelector(modalTarget + ' #height').value = animalData.height;
            document.querySelector(modalTarget + ' #health').value = animalData.health;
            document.querySelector(modalTarget + ' #color').value = animalData.color;
            document.querySelector(modalTarget + ' #supplier').value = animalData.supplier;
            document.querySelector(modalTarget + ' #diet').value = JSON.stringify(animalData.diet);
            document.querySelector(modalTarget + ' #notes').value = animalData.notes;
            document.querySelector(modalTarget + ' #image_url').value = animalData.image_url;
        }
        else if (modalTarget == "#view-animal-modal") {
            document.querySelector(modalTarget + ' .modal-title').innerHTML = animalData.name;
            document.querySelector(modalTarget + ' #ul_animal_page_id').innerHTML = "<b>ID: </b> " + animalData.id;
            document.querySelector(modalTarget + ' #ul_animal_page_species').innerHTML = "<b>Species: </b> " + animalData.species;
            document.querySelector(modalTarget + ' #ul_animal_page_age').innerHTML = "<b>Age: </b> " + animalData.age;
            document.querySelector(modalTarget + ' #ul_animal_page_gender').innerHTML = "<b>Gender: </b> " + animalData.gender;
            document.querySelector(modalTarget + ' #ul_animal_page_price').innerHTML = "<b>Price($): </b> " + animalData.price;
            document.querySelector(modalTarget + ' #ul_animal_page_weight').innerHTML = "<b>Weight(g): </b> " + animalData.weight;
            document.querySelector(modalTarget + ' #ul_animal_page_height').innerHTML = "<b>Height(cm): </b> " + animalData.height;
            document.querySelector(modalTarget + ' #ul_animal_page_health').innerHTML = "<b>Health: </b> " + animalData.health;
            document.querySelector(modalTarget + ' #ul_animal_page_color').innerHTML = "<b>Color: </b> " + animalData.color;
            document.querySelector(modalTarget + ' #ul_animal_page_diet').innerHTML = "<b>Diet: </b> " + JSON.stringify(animalData.diet);
            document.querySelector(modalTarget + ' #ul_animal_page_purchase_date').innerHTML = "<b>Purchase Date (YYYY-MM-DD): </b> " + (new Date(animalData.purchase_date)).toISOString().split('T')[0];
            document.querySelector(modalTarget + ' #ul_animal_page_purchase_price').innerHTML = "<b>Purchase Price($): </b> " + animalData.purchase_price;
            document.querySelector(modalTarget + ' #ul_animal_page_sold_date').innerHTML = "<b>Sold Date (YYYY-MM-DD): </b> " + (new Date(animalData.sold_date)).toISOString().split('T')[0];
            document.querySelector(modalTarget + ' #ul_animal_page_supplier').innerHTML = "<b>Supplier: </b> " + animalData.supplier;
            document.querySelector(modalTarget + ' textarea').textContent = animalData.notes;
            document.querySelector(modalTarget + ' #animal-page-img').src = animalData.image_url;
        }
    } catch (error) {
        console.error(error);
    }
}

const filter = document.querySelector("#animalNameSearch");
const animalList = document.querySelector("tbody");

const filterTable = (event) => {
    animals = animalList.children;
    console.log(animals)
    if (event.target.value != '') {
        for (animal of animals) {
            if (animal.querySelector(".animalName").innerText.toLowerCase().includes(event.target.value.toLowerCase()) || animal.querySelector(".animalID").innerText.includes(event.target.value)) {
                animal.classList.remove("hidden");
            } else {
                animal.className = "hidden";
            }
        }
    } else {
        for (animal of animals) {
            animal.classList.remove("hidden");
        }
    }
}

// To add more Fields to the Invoice Creation page
var animalCount = 1;
  
$(document).ready(function() {
  $('.extra_animal_field').click(function() {

    var newAnimal = $('.create_invoice_animal').last().clone();
 
    var newClass = 'create_invoice_animal_' + animalCount;
    newAnimal.removeClass().addClass(newClass);
  
    newAnimal.find('input').val('');
 
    newAnimal.find('.extra_animal_field').remove();

    var deleteButton = $('<a class="delete_animal_field" href="#">Delete Animal</a>');
    deleteButton.data('target', '.' + newClass);
    newAnimal.append(deleteButton);
  
    $('.add_invoice_animal').append(newAnimal);
    animalCount++;
  });
  

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




