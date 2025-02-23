const form = document.querySelector('form'); // Get form element

form.addEventListener("submit", function(event) { // Event listener for form submission
  event.preventDefault(); // Prevent default form submission before JS logic runs

  //Custom validation
  const email = document.getElementById("email").value; //.value is for getting the value of the input
  const msg = document.getElementById("Message").value;

  // Email validation
  if (!emailIsValid(email)) {
    Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Your email is invalid!",
    });
    return;
  }

  if (msg.length < 10) {
    Swal.fire({
        icon: "error",
        title: "Oops...",
        text: "Your message must be at least 10 characters long!",
    });
    return;
  }

  // Submit the form after message pop up
  Swal.fire({ 
    title: "Success!",
    text: "Your message has been sent!",
    icon: "success",
  }).then(() => {
    form.submit();
  });
});

// Regular expression for email validation
function emailIsValid(input) {
    return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input);
}