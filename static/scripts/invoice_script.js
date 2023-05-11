const renderModal = async (element) => {
  try {
      const modalTarget = element.getAttribute("data-target");
      // Get the invoice ID
      const thread = element.parentNode.parentNode;
      const invoiceId = thread.querySelector(".invoiceID").innerText;

      // Make a GET request to the server to fetch the animal data
      const response = await fetch(`/invoice/${invoiceId}`);
      if (!response.ok) {
          throw new Error('Failed to fetch invoice data');
      }

      // Parse the response JSON data and populate the modal form fields
      const invoiceData = await response.json();
      if (modalTarget == "#view-invoice-modal") {
          document.querySelector(modalTarget + ' #invoice_name').innerHTML = `To: <span id="invoice_customer">${invoiceData["name"]}</span>`;
          document.querySelector(modalTarget + ' #invoice_address').innerHTML = `${invoiceData["city"]}`;
          document.querySelector(modalTarget + ' #invoice_location').innerHTML = `${invoiceData["province"]}`;
          document.querySelector(modalTarget + ' #invoice_postal_code').innerHTML = `${invoiceData["postal_code"]}`;
          document.querySelector(modalTarget + ' #invoice_phone').innerHTML = `${invoiceData["phone"]}`;
      }
      else if (modalTarget == "#edit-invoice-modal") {
          document.querySelector(modalTarget + ' #modal-form').action = `/invoice/${invoiceData.id}`;
          document.querySelector(modalTarget + ' #status').value = invoiceData.status
      }
  } catch (error) {
      console.error(error);
  }
}

const filterInvoice = document.querySelector("#searchInv")
const itemList = document.querySelector("tbody");
const animalIDs = document.querySelector("#animals_id");

// To add more Fields to the Invoice Creation page
// ------------------------------------------------------------------leave for now 
// var animalCount = 1;

$(document).ready(function () {
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
  $(document).on('click', '.delete_animal_field', function (e) {
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

const checkAnimalIDs = async (event) => {
  const animalIdArray = animalIDs.value.split(" ");
  const testIDs = [];
  for (const item of animalIdArray) {
    testID = parseFloat(item)
    if (!isNaN(testID)) {
      testIDs.push(parseFloat(item));
    }
  }

  try {
    for (const ID of testIDs) {
      // First, check if the ID exists
      const response = await fetch(`/animal/${ID}`);
      if (!response.ok) {
        throw new Error(`Failed to fetch animal data from ID ${ID}.`);
      }
      // Then, check if the animal is not apart of another invoice
      const animalData = await response.json();
      if (animalData.is_in_invoice) {
        throw new Error(`Cannot add animal: ID ${ID} already exists in another invoice.`);
      }
      document.querySelector("#submitbutton").classList.remove("disabled");
      document.querySelector("#submitbutton").removeAttribute("disabled")

      document.querySelector("#animalIdError").classList.add("hidden")
    }
  } catch (error) {
    console.error(error);
    document.querySelector("#submitbutton").classList.add("disabled");
    document.querySelector("#submitbutton").setAttribute("disabled", "")

    document.querySelector("#animalIdError").classList.remove("hidden");
    document.querySelector("#animalIdError").innerHTML = error
  }

  console.log(testIDs)
}


const filterTableInvoice = (event) => {
  const invoices = itemList.children;
  console.log(invoices)
  if (event.target.value != '') {
    for (invoice of invoices) {
      if (invoice.querySelector(".invoiceName").innerText.toLowerCase().includes(event.target.value.toLowerCase()) || invoice.querySelector(".invoiceID").innerText.includes(event.target.value)) {
        invoice.classList.remove("hidden");
      } else {
        invoice.className = "hidden";
      }
    }
  } else {
    for (invoice of invoices) {
      invoice.classList.remove("hidden");
    }
  }
}

filterInvoice.addEventListener("input", filterTableInvoice);
animalIDs.addEventListener("blur", checkAnimalIDs)