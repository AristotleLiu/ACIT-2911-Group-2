const filter = document.querySelector("#animalNameSearch");
const animalList = document.querySelector("tbody");

/**
 * Deletes an animal from the list based on the provided ID.
 * If the animal is in an invoice, a warning alert is shown.
 * Otherwise, a DELETE request is sent to the server to delete the animal,
 * and the animal is removed from the list. The page is then reloaded after a delay.
 * @param {number} id - The ID of the animal to be deleted.
 */
const deleteAnimal = (id) => {
    const list = document.querySelectorAll("tr")
    const newList = Array.prototype.slice.call(list, 1)

    for (const item of newList) {
        if (item.firstElementChild.textContent == id) {
            if (item.getAttribute("in_invoice") == "True") {
                alert("WARNING: Animal is in an invoice")
            } else {
                fetch(`http://127.0.0.1:5000/animal/${id}`, {
                    method: 'DELETE'
                }).then(response => console.log(response));

                item.remove()
                setTimeout(() => location.reload(), 100)
            }
        }
    }
}

/**
 * Converts a date to a string representation in ISO format (YYYY-MM-DD).
 * @param {Date|null} date - The date object to be converted.
 * @returns {string|null} The string representation of the date in ISO format, or null if the date is null.
 */
const dateToString = (date) => {
    if (date != null && date != "None") {
        return (new Date(date)).toISOString().split('T')[0]
    }
    else {
        return "None"
    }
}

/**
 * Renders the modal and populates the form fields with the animal data.
 * @param {HTMLElement} element - The HTML element triggering the modal rendering.
 * @returns {Promise} A Promise that resolves when the modal rendering is completed.
 */
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
            document.querySelector(modalTarget + ' #purchase_date').value = dateToString(animalData.purchase_date);
            document.querySelector(modalTarget + ' #weight').value = animalData.weight;
            document.querySelector(modalTarget + ' #height').value = animalData.height;
            document.querySelector(modalTarget + ' #health').value = animalData.health;
            document.querySelector(modalTarget + ' #color').value = animalData.color;
            document.querySelector(modalTarget + ' #supplier').value = animalData.supplier;
            document.querySelector(modalTarget + ' #diet').value = animalData.diet;
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
            document.querySelector(modalTarget + ' #ul_animal_page_diet').innerHTML = "<b>Diet: </b> " + animalData.diet;
            document.querySelector(modalTarget + ' #ul_animal_page_purchase_date').innerHTML = "<b>Purchase Date: </b> " + dateToString(animalData.purchase_date);
            document.querySelector(modalTarget + ' #ul_animal_page_purchase_price').innerHTML = "<b>Purchase Price($): </b> " + animalData.purchase_price;
            document.querySelector(modalTarget + ' #ul_animal_page_sold_date').innerHTML = "<b>Sold Date: </b> " + dateToString(animalData.sold_date);
            document.querySelector(modalTarget + ' #ul_animal_page_supplier').innerHTML = "<b>Supplier: </b> " + animalData.supplier;
            document.querySelector(modalTarget + ' textarea').textContent = animalData.notes;
            document.querySelector(modalTarget + ' #animal-page-img').src = animalData.image_url;
        }
        else if (modalTarget == "#delete_modal") {
            document.querySelector(modalTarget + ' #delete_button').attributes.onclick.value = `deleteAnimal(${animalData.id})`
            document.querySelector(modalTarget + ' #del_modal_message').textContent = `Do you really want to delete [animal id: ${animalData.id}] This process cannot be undone`
        }
    } catch (error) {
        console.error(error);
    }
}

/**
 * Filters the table based on the input value of the search field.
 * @param {Event} event - The input event triggered by the search field.
 */
const filterTable = (event) => {
    animals = animalList.children;
    if (event.target.value != '') {
        for (animal of animals) {
            if (animal.querySelector(".animalName").innerText.toLowerCase().includes(event.target.value.toLowerCase()) || animal.querySelector(".animalID").innerText.includes(event.target.value)) {
                animal.classList.remove("hidden");
            } else {
                animal.classList.add("hidden");
            }
        }
    } else {
        for (animal of animals) {
            animal.classList.remove("hidden");
        }
    }
}

/**
 * Filters the table based on the values of the filter form fields.
 * @param {Event} event - The submit event triggered by the filter form.
 */
const filterForm = (event) => {
 
    const formEl = document.forms.filterForm;
    const animalFormData = new FormData(formEl);
    const filter_age = animalFormData.get('age');
    const filter_gender = animalFormData.get('gender');
    const filter_species = animalFormData.get('species');
    const filter_price_max = animalFormData.get('maxPrice');
    const filter_price_min = animalFormData.get('minPrice');
    const filter_health = animalFormData.get('health');
    const filter_color = animalFormData.get('color');
    const filter_supplier = animalFormData.get('supplier');
    const filter_is_sold = animalFormData.get('is_sold');

    const animals = animalList.children;
    for (animal of animals) {
        animal.classList.remove("hidden2");
    }

    if (filter_is_sold != '') {
        for (const animal of animals) {
            if (!(animal.getAttribute("in_invoice").toLowerCase().includes(filter_is_sold.toLowerCase()))) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_age != '') {
        for (const animal of animals) {
            if (!(animal.querySelector(".animalAge").innerText == filter_age)) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_gender != '') {
        for (const animal of animals) {
            if (!(animal.querySelector(".animalGender").innerText.toLowerCase() === filter_gender.toLowerCase())) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_species != '') {
        for (const animal of animals) {
            if (!(animal.querySelector(".animalSpecies").innerText.toLowerCase() === filter_species.toLowerCase())) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_price_min != '') {
        for (const animal of animals) {
            if (!(parseInt(animal.querySelector(".animalPrice").innerText) >= parseInt(filter_price_min))) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_price_max != '') {
        for (const animal of animals) {
            if (!(parseInt(animal.querySelector(".animalPrice").innerText) <= parseInt(filter_price_max))) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_health != '') {
        for (const animal of animals) {
            if (!(animal.getAttribute("animalhealth").toLowerCase() === filter_health.toLowerCase())) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_color != '') {
        for (const animal of animals) {
            if (!(animal.getAttribute("animalcolor").toLowerCase().includes(filter_color.toLowerCase()))) {
                animal.classList.add("hidden2");
            }
        }
    }

    if (filter_supplier != '') {
        for (const animal of animals) {
            if (!(animal.getAttribute("animalsupplier").toLowerCase() === filter_supplier.toLowerCase())) {
                animal.classList.add("hidden2");
            }
        }
    }
}

filter.addEventListener("input", filterTable);