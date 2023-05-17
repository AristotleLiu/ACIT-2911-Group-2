const createSummary = async () => {
  try {
    const response = await fetch("/invoice/all")
    if (!response.ok) {
      throw new Error('Failed to fetch invoice data');
    }
    // data is a list of all invoices
    const data = await response.json
  }
  catch (error) {
    console.log(error)
  }
}

const renderModal = async (element) => {
  try {
      const modalTarget = element.getAttribute("data-target");
      // Get the invoice ID
      const thread = element.parentNode.parentNode;
      const invoiceId = thread.querySelector(".invoiceID").innerText;

      // Make a GET request to the server to fetch the invoice data
      const response = await fetch(`/invoice/${invoiceId}`);
      if (!response.ok) {
          throw new Error('Failed to fetch invoice data');
      }

      // Parse the response JSON data and populate the modal form fields
      const invoiceData = await response.json();
      if (modalTarget == "#view-invoice-modal") {
          document.querySelector(modalTarget + ' #invoice_name').innerHTML = `To: <span id="invoice_customer">${invoiceData["name"]}</span>`;
          document.querySelector(modalTarget + ' #invoice_address').innerHTML = `${invoiceData["street"]}, ${invoiceData["city"]}`;
          document.querySelector(modalTarget + ' #invoice_location').innerHTML = `${invoiceData["province"]}`;
          document.querySelector(modalTarget + ' #invoice_postal_code').innerHTML = `${invoiceData["postal_code"]}`;
          document.querySelector(modalTarget + ' #invoice_phone').innerHTML = `${invoiceData["phone"]}`;
          document.querySelector(modalTarget + ' #invoice_status').innerHTML = `${invoiceData["status"]}`; 
          // hehe... this is the color change for now----------------------------------------------------------------------------------------------
          var color_change = document.querySelector(modalTarget + ' #invoice_status');
          if(color_change.textContent.toLowerCase()===("paid")){
            document.getElementById("invoice_status").classList.remove("red-text");
            document.getElementById("invoice_status").classList.remove("yellow-text");
              document.getElementById("invoice_status").classList.add("green-text");
          }
          else if (color_change.textContent.toLowerCase()===("unpaid")){
            document.getElementById("invoice_status").classList.remove("red-text");
              document.getElementById("invoice_status").classList.remove("green-text");
              document.getElementById("invoice_status").classList.add("yellow-text");
          }
          else{
            document.getElementById("invoice_status").classList.remove("yellow-text");
            document.getElementById("invoice_status").classList.remove("green-text");
              document.getElementById("invoice_status").classList.add("red-text");
          }
          // ----------------------------------------------------------------------------------------------------------------------------------------
          document.querySelector(modalTarget + ' #invoice_number').innerHTML = `Invoice >> <strong>${invoiceData["id"]}</strong>`; 
          document.querySelector(modalTarget + ' #invoice_list_id').innerHTML = `<i class="fas fa-circle invoice_list"></i> <span class="fw-bold">ID:</span>#${invoiceData["id"]}`;
          document.querySelector(modalTarget + ' #invoice_list_date').innerHTML = `<i class="fas fa-circle invoice_list"></i> <span class="fw-bold">Date: </span>${(new Date(invoiceData["date"])).toISOString().split('T')[0]}`;

          while (document.querySelector(modalTarget + " tbody").hasChildNodes()) {
            document.querySelector(modalTarget + " tbody").removeChild(document.querySelector(modalTarget + " tbody").firstChild)
          }

          var sub_total = 0

          for (animal of invoiceData["animals"]) {
            sub_total += animal["animal_price"]

            var row = document.createElement("tr")
            var row_id = document.createElement("td")
            var row_name = document.createElement("td")
            var row_species = document.createElement("td")
            var row_price = document.createElement("td")

            var row_id_text = document.createTextNode(animal["animal_id"])
            var row_name_text = document.createTextNode(animal["animal_name"])
            var row_species_text = document.createTextNode(animal["animal_price"])
            var row_price_text = document.createTextNode(animal["animal_species"])

            row_id.appendChild(row_id_text)
            row_name.appendChild(row_name_text)
            row_species.appendChild(row_species_text)
            row_price.appendChild(row_price_text)

            row.appendChild(row_id)
            row.appendChild(row_name)
            row.appendChild(row_species)
            row.appendChild(row_price)

            document.querySelector(modalTarget + " tbody").appendChild(row)
          }

          document.querySelector(modalTarget + " #invoice_sub_total").innerHTML = `<span class="text-black me-4">Sub Total:</span> $${sub_total.toFixed(2)}`
          document.querySelector(modalTarget + " #invoice_tax").innerHTML = `<span class="text-black me-4">Tax(5%):</span> $${(sub_total * 0.05).toFixed(2)}`
          document.querySelector(modalTarget + " #invoice_total_amount").innerHTML = `<span class="text-black me-3"> Total Amount</span><span style="font-size: 25px;"> $${(sub_total * 1.05).toFixed(2)}</span>`
      }
      else if (modalTarget == "#edit-invoice-modal") {
          document.querySelector(modalTarget + ' #modal-form').action = `/invoice/${invoiceData.id}`;
          document.querySelector(modalTarget + ' .invoice_id').value = invoiceData.id
          document.querySelector(modalTarget + ' #status').value = invoiceData.status
          document.querySelector(modalTarget + ' .invoice_date').value = (new Date(invoiceData.date)).toISOString().split('T')[0]
          document.querySelector(modalTarget + ' .invoice_customer').value = invoiceData.name
          document.querySelector(modalTarget + ' .invoice_street').value = invoiceData.street
          document.querySelector(modalTarget + ' .invoice_city').value = invoiceData.city
          document.querySelector(modalTarget + ' .invoice_province').value = invoiceData.province
          document.querySelector(modalTarget + ' .invoice_postal_code').value = invoiceData.postal_code

          var sub_total = 0

          for (animal of invoiceData["animals"]) {
            sub_total += animal["animal_price"]
          }

          document.querySelector(modalTarget + ' .invoice_price').value = sub_total
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

// $(document).ready(function () {
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