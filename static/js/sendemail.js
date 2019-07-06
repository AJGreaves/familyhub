$(document).ready(function () {

    const contactForm = document.querySelector('#contact-form');

    contactForm.addEventListener('submit', (event) => {
        event.preventDefault();
        const data = {
            service_id: "gmail",
            template_id: "familyhub_contact_form",
            user_id: "user_CQSk7h9Wyuw2xLhYG0hBX",
            template_params: {
                "from_name": contactForm.contactName.value,
                "from_email": contactForm.contactEmail.value,
                "subject": contactForm.contactSubject.value,
                "contact_form_message": contactForm.contactMessage.value,
            }
        };
    
        $.ajax('https://api.emailjs.com/api/v1.0/email/send', {
            type: 'POST',
            data: JSON.stringify(data),
            contentType: 'application/json'
        }).done(function () {
            $('input').val('');
            $('textarea').val('');
            alertModal('email sent');
        }).fail(function (error) {
            console.log('Oops... ' + JSON.stringify(error));
        });
    })
})