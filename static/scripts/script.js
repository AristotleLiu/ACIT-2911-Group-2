
const deleteItem = (element) => {
    const thread = element.parentNode.parentNode
    animalId = thread.querySelector(".animalID").innerText
    
    fetch(`http://127.0.0.1:5000/animal/${animalId}`, {
        method: 'DELETE'
    }).then(response => console.log(response))
}