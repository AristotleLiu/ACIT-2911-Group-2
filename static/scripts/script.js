const https = require("https");


const deleteButton = document.querySelector(".delete");
deleteButton.addEventListener("click",clickOnDeleteButton);

function clickOnDeleteButton(ev) {
    if (ev.target.tagName === "BUTTON") {
        alert("you clicked!")
    }
}