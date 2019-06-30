function sendMail(contactForm) {
    emailjs.send("gmail", "familyhub_contact_form", {
        "from_name": contactForm.contactName.value,
        "from_email": contactForm.contactEmail.value,
        "subject": contactForm.contactSubject.value,
        "contact_form_message": contactForm.contactMessage.value,
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error);
        }
    );
}
