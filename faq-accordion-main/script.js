// Get all element with class of "collapsible"
let collapsible = document.getElementsByClassName("collapsible");

// Loop through all collapsible elements
for (let i = 0; i < collapsible.length; i++) {
    // event listener is basically for click, mouseover, mouseout, etc. let's add them to the collapsible elements
    collapsible[i].addEventListener("click", function() {
        // Toggle the "active" class to change button style
        this.classList.toggle("active");

        // Find the closest parent 'block' div and then get its .content div
        let content = this.closest("div[class^='block']").querySelector(".content");

        // Find the image inside the button
        let img = this.querySelector("img");

        // If the content is visible, hide it, else show it
        if (content.style.display === "block") {
            content.style.display = "none";
            img.src = "./assets/images/icon-plus.svg";  // Change back to plus icon
        } else {
            content.style.display = "block";
            img.src = "./assets/images/icon-minus.svg"; // Change to minus icon
        }
    });
}