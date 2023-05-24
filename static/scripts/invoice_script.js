const filterInvoice = document.querySelector("#searchInv")
const itemList = document.querySelector("tbody");
const animalIDs = document.querySelector("#animals_id");

/**
 * Filters sales data based on a specified date range.
 *
 * @param {Array} invoiceData - An array of invoice data.
 * @param {string} startDate - The start date of the range to filter by.
 * @param {string} endDate - The end date of the range to filter by.
 * @returns {Array} - Filtered sales data within the specified date range.
 */
function filterSalesByDate(invoiceData, startDate, endDate) {
  const filteredSales = invoiceData.filter(data => {
    const saleDate = new Date(data.date);
    return saleDate >= new Date(startDate) && saleDate <= new Date(endDate);
  });
  return filteredSales
}

/**
 * Calculates monthly sales based on the invoice data.
 *
 * @param {Array} invoiceData - An array of invoice data.
 * @returns {Object} - Monthly sales data, where keys are in the format 'YYYY-MM' and values represent the total sales for each month.
 */
function calcMonthlySales(invoiceData) {
  const monthlySales = {};
  invoiceData.forEach(invoice => {
    const saleDate = new Date(invoice.date);
    const year = saleDate.getFullYear();
    const month = saleDate.getMonth() + 1;
    const key = `${year}-${month.toString().padStart(2, '0')}`;

    if (monthlySales[key]) {
      monthlySales[key] += invoice.price;
    } else {
      monthlySales[key] = invoice.price;
    }
  });
  return monthlySales;
}

/**
 * Calculates annual sales based on the invoice data.
 *
 * @param {Array} invoiceData - An array of invoice data.
 * @returns {Object} - Annual sales data, where keys are years and values represent the total sales for each year.
 */
function calcAnnualSales(invoiceData) {
  const annualSales = {};
  invoiceData.forEach(invoice => {
    const saleDate = new Date(invoice.date);
    const year = saleDate.getFullYear();

    if (annualSales[year]) {
      annualSales[year] += invoice.price;
    } else {
      annualSales[year] = invoice.price;
    }
  });

  return annualSales;
}

/**
 * Finds the popular animal species based on the invoice data.
 *
 * @param {Array} invoiceData - An array of invoice data.
 * @returns {Object} - Animal species dictionary, where keys are animal species and values represent the count of occurrences.
 */
function findPopularAnimal(invoiceData) {
  animalDict = {}
  for (invoice of invoiceData) {
    for (animal of invoice.animals) {
      if (animalDict[animal.animal_species]) {
        animalDict[animal.animal_species] += 1
      } else {
        animalDict[animal.animal_species] = 1
      }
    }
  }

  return animalDict
}

/**
 * Calculates the total profit for each animal species based on the invoice data.
 *
 * @param {Array} invoiceData - An array of invoice data.
 * @returns {Object} - Animal species dictionary, where keys are animal species and values represent the total profit.
 */
function mostProfitableAnimals(invoiceData) {
  profitAnimalsDict = {}
  for (invoice of invoiceData) {
    for (animal of invoice.animals) {
      if (profitAnimalsDict[animal.animal_species]) {
        profitAnimalsDict[animal.animal_species] += animal.animal_price
      } else {
        profitAnimalsDict[animal.animal_species] = animal.animal_price
      }
    }
  }
  return profitAnimalsDict
}

/**
 * Sorts a dictionary by value in descending order.
 *
 * @param {Object} dict - The dictionary to be sorted.
 * @param {number} num - Optional. The number of top entries to return.
 * @returns {Array} - Sorted list of dictionary entries as objects, sorted by value in descending order.
 */
function sortDict(dict, num) {
  const sortedEntries = Object.entries(dict).sort((a, b) => b[1] - a[1]);
  const sortedList = sortedEntries.map(([key, value]) => ({ key, value }));
  
  if (num) {
    return sortedList.slice(0, num);
  } else {
    return sortedList;
  }
}

/**
 * Creates an excel summary report based on the invoice data and form input values.
 *
 * @param {Event} event - The event object triggered by the create summary action.
 */
const createSummary = async (event) => {
  try {
    const response = await fetch("/invoice/all")
    if (!response.ok) {
      throw new Error('Failed to fetch invoice data');
    }
    // data is a list of all invoices
    const data = await response.json()

    // Retrieve form input values from the modal
    const formEl = document.forms.summaryForm;
    const formData = new FormData(formEl);
    const startDate = formData.get('start_date');
    const endDate = formData.get('end_date');
    const quickSelect = formData.get('quick_select');
    const topSaleAnimals = formData.get('top_sale_animals');
    const mostProfitable = formData.get('most_profitable');

    // Filter invoice data based on selected date range, only invoices between start and end date are selected
    const filterSales = filterSalesByDate(data, startDate, endDate);
    // Calculate monthly or yearly sales
    var salesData;
    if (quickSelect === 'Monthly') {
      salesData = sortDict(calcMonthlySales(filterSales)); 
    } else {
      salesData = sortDict(calcAnnualSales(filterSales));
    }
    
    // Find popular animals and most profitable animals
    const popularAnimals = findPopularAnimal(filterSales);
    const profitableAnimals = mostProfitableAnimals(filterSales);
    
    // Sort animal dictionaries to get top sale animals and most profitable animals
    const topSaleAnimalsList = sortDict(popularAnimals, topSaleAnimals);
    const mostProfitableAnimalsList = sortDict(profitableAnimals, mostProfitable);

    const workbook = XLSX.utils.book_new();

    const salesDataWorkSheetData = []
    for (item of salesData) {
      if (quickSelect === "Monthly") {
        salesDataWorkSheetData.push({"Year-Month": item["key"], "Sub Total": item["value"]})
      } else {
        salesDataWorkSheetData.push({"Year": item["key"], "Sub Total": item["value"]})
      }
    }

    const topSaleAnimalsWorkSheetData = []
    for (item of topSaleAnimalsList) {
      topSaleAnimalsWorkSheetData.push({"Animal": item["key"], "Sold": item["value"]})
    }

    const mostProfitableAnimalsWorkSheetData = []
    for (item of mostProfitableAnimalsList) {
      mostProfitableAnimalsWorkSheetData.push({"Animal": item["key"], "Sub Total": item["value"]})
    }

    const salesDataWorkSheet = XLSX.utils.json_to_sheet(salesDataWorkSheetData);
    const topSaleAnimalsWorkSheet = XLSX.utils.json_to_sheet(topSaleAnimalsWorkSheetData);
    const mostProfitableAnimalsWorkSheet = XLSX.utils.json_to_sheet(mostProfitableAnimalsWorkSheetData);

    XLSX.utils.book_append_sheet(workbook, salesDataWorkSheet, 'Sales Data');
    XLSX.utils.book_append_sheet(workbook, topSaleAnimalsWorkSheet, 'Popular Animals');
    XLSX.utils.book_append_sheet(workbook, mostProfitableAnimalsWorkSheet, 'Most Profitable Animals');

    XLSX.writeFile(workbook, "summary.xlsx")
  }
  catch (error) {
    console.log(error)
  }
} 

/**
 * Renders the modal and populates its content with invoice data.
 *
 * @param {HTMLElement} element - The element that triggered the modal rendering.
 */
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
            var row_species_text = document.createTextNode(animal["animal_species"])
            var row_price_text = document.createTextNode(animal["animal_price"])

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

/**
 * Checks if the entered animal IDs are valid and available for inclusion in the invoice.
 *
 * @param {Event} event - The event object triggered by the animal ID input.
 */
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

/**
 * Filters the invoice list based on the search input value.
 *
 * @param {Event} event - The event object triggered by the search input.
 */
const filterTableInvoice = (event) => {
  const invoices = itemList.children;
  console.log(invoices)
  if (event.target.value != '') {
    for (invoice of invoices) {
      if (invoice.querySelector(".invoiceName").innerText.toLowerCase().includes(event.target.value.toLowerCase()) || invoice.querySelector(".invoiceID").innerText.includes(event.target.value)) {
        invoice.classList.remove("hidden");
      } else {
        invoice.classList.add("hidden");
      }
    }
  } else {
    for (invoice of invoices) {
      invoice.classList.remove("hidden");
    }
  }
}

/**
 * Filters the invoice list based on the form input values.
 *
 * @param {Event} event - The event object triggered by the filter form submission.
 */
const filterForm = (event) => {
 
  const formEl = document.forms.filterForm;
  const animalFormData = new FormData(formEl);
  const filter_province = animalFormData.get('invoice_province');
  const filter_city = animalFormData.get('invoice_city');
  const filter_status = animalFormData.get('status');

  console.log(filter_city)

  const invoices = document.querySelector("#invoiceList").children;
  for (invoice of invoices) {
    invoice.classList.remove("hidden2");
  }

  if (filter_province != '') {
    for (const invoice of invoices) {
        if (!(invoice.querySelector(".invoiceProvince").innerText == filter_province)) {
            invoice.classList.add("hidden2");
        }
    }
  }

  if (filter_city != '') {
    for (const invoice of invoices) {
        if (!(invoice.querySelector(".invoiceCity").innerText == filter_city)) {
            invoice.classList.add("hidden2");
        }
    }
  }

  if (filter_status != '') {
    for (const invoice of invoices) {
        console.log(filter_status)
        if (!(invoice.querySelector(".invoiceStatus").innerText == filter_status)) {
            invoice.classList.add("hidden2");
        }
    }
  }
}

filterInvoice.addEventListener("input", filterTableInvoice);
animalIDs.addEventListener("blur", checkAnimalIDs)