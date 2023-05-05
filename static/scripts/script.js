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